import tkinter as tk
from tkinter import messagebox
import random
import json
from openai import OpenAI
from topics import EXAM_TOPICS
from question_history import QuestionHistory
from datetime import datetime
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from difficulty_manager import DifficultyManager, DifficultyLevel
from session_stats import SessionStats
from ui_components import ProgressTracker, SessionTimer, DifficultyControls
from loading_screen import LoadingScreen
import threading
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

class CompTIAQuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("CompTIA Quiz")
        
        # Larger window size
        window_width = 1200
        window_height = 900
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)
        master.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
        # Initial focus attempt
        self.force_focus()
        
        # Schedule additional focus attempts
        self.master.after(5000, self.force_focus)  # Try again after 5 seconds
        self.master.after(10000, self.force_focus) # Try again after 10 seconds
        
        # Initialize managers first
        self.history = QuestionHistory()
        self.difficulty_manager = DifficultyManager()
        self.session_stats_manager = SessionStats()
        
        # Main container
        self.main_container = tk.Frame(master)
        self.main_container.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Add difficulty indicator to UI
        self.difficulty_frame = tk.Frame(self.main_container)
        self.difficulty_frame.pack(fill='x', pady=5)
        
        self.difficulty_label = tk.Label(self.difficulty_frame, text="Difficulty: ")
        self.difficulty_label.pack(side='left')
        
        self.current_difficulty = tk.Label(self.difficulty_frame, text="", fg="blue")
        self.current_difficulty.pack(side='left')
        
        # Question frame
        self.question_frame = tk.Frame(self.main_container)
        self.question_frame.pack(fill='both', expand=True)
        
        self.question_label = tk.Label(
            self.question_frame, 
            text="", 
            wraplength=700,
            font=('Arial', 24)
        )
        self.question_label.pack(pady=20)

        # Options frame
        self.options_frame = tk.Frame(self.main_container)
        self.options_frame.pack(fill='x', pady=20)

        self.var = tk.StringVar()
        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(
                self.options_frame, 
                text="", 
                variable=self.var, 
                value=i,
                font=('Arial', 20)
            )
            btn.pack(anchor='w', pady=5)
            self.option_buttons.append(btn)

        # Buttons frame
        self.buttons_frame = tk.Frame(self.main_container)
        self.buttons_frame.pack(fill='x', pady=20)

        self.submit_button = tk.Button(self.buttons_frame, text="Submit", command=self.check_answer)
        self.submit_button.pack(side='left', padx=10)

        self.next_button = tk.Button(self.buttons_frame, text="Next Question", command=self.next_question)
        self.next_button.pack(side='left')
        self.next_button.config(state=tk.DISABLED)

        # Add Stats button
        self.stats_button = tk.Button(self.buttons_frame, text="Show Coverage", command=self.show_coverage_stats)
        self.stats_button.pack(side='right', padx=10)

        # Add shutdown button to buttons frame
        self.shutdown_button = tk.Button(
            self.buttons_frame, 
            text="Exit", 
            command=self.shutdown,
            bg='red',
            fg='black',
            font=('Arial', 15, 'bold')
        )
        self.shutdown_button.pack(side='right', padx=10)

        # Objective label
        self.objective_label = tk.Label(self.main_container, text="", wraplength=700, fg="gray")
        self.objective_label.pack(pady=10)

        # Add session stats frame at bottom right
        self.stats_frame = tk.Frame(self.main_container)
        self.stats_frame.pack(side='right', anchor='se', padx=10, pady=5)
        
        self.session_stats_label = tk.Label(self.stats_frame, text="Session: 0/0 (0%)", fg="blue")
        self.session_stats_label.pack()
        
        # Initialize session tracking
        self.session_stats = {
            'correct': 0,
            'total': 0
        }

        # Initialize attributes
        self.current_question = None
        self.correct_answer = None
        self.explanation = None
        self.objective = None
        self.current_topic = None
        
        # Load the first question
        self.load_question()

        # Add menu bar
        self.create_menu()
        
        # Add progress tracker
        self.progress_tracker = ProgressTracker(self.main_container, EXAM_TOPICS)
        self.progress_tracker.pack(fill='x', pady=5)
        
        # Add session timer
        self.timer = SessionTimer(self.main_container)
        self.timer.pack(side='top', pady=5)
        self.timer.update()
        
        # Update difficulty frame with controls
        self.difficulty_controls = DifficultyControls(
            self.difficulty_frame,
            self.adjust_difficulty
        )
        self.difficulty_controls.pack(side='right')

    def select_random_topic(self):
        """Randomly select a topic based on weights and recent history."""
        # Initialize topic history if not exists
        if not hasattr(self, 'topic_history'):
            self.topic_history = {
                'covered_topics': [],  # List of all covered topics
                'domain_coverage': {},  # Domain coverage tracking
                'last_topics': []      # Changed back to list for ordered history
            }
        
        # Get all possible topics
        all_topics = []
        for domain_id, domain in EXAM_TOPICS.items():
            for subtopic_id, subtopic in domain['subtopics'].items():
                for topic in self._get_leaf_topics(subtopic['topics']):
                    full_path = f"{domain_id} > {subtopic_id} > {topic}"
                    if full_path not in self.topic_history['last_topics']:  # Only add if not recently used
                        all_topics.append({
                            "domain": {
                                "id": domain_id,
                                "name": domain["name"],
                                "weight": domain["weight"]
                            },
                            "subtopic": {
                                "id": subtopic_id,
                                "name": subtopic["name"]
                            },
                            "specific_topic": topic,
                            "full_path": full_path
                        })
        
        # If all topics have been used recently, clear history
        if not all_topics:
            self.topic_history['last_topics'].clear()
            return self.select_random_topic()
        
        # Weight topics by domain weight and coverage
        weights = []
        for topic in all_topics:
            domain_id = topic['domain']['id']
            base_weight = topic['domain']['weight']
            
            # Reduce weight if domain has been covered a lot
            domain_count = self.topic_history['domain_coverage'].get(domain_id, {'count': 0})['count']
            coverage_factor = 1.0 / (1.0 + domain_count * 0.1)  # Reduce weight as coverage increases
            
            weights.append(base_weight * coverage_factor)
        
        # Select topic
        selected_topic = random.choices(all_topics, weights=weights)[0]
        
        # Update history
        self.topic_history['last_topics'].append(selected_topic['full_path'])
        if len(self.topic_history['last_topics']) > 20:  # Keep last 20 topics
            self.topic_history['last_topics'].pop(0)
        
        return selected_topic

    def _get_leaf_topics(self, topics_dict):
        """Helper method to get all leaf topics from a topic dictionary."""
        leaf_topics = []
        
        def traverse(d, current_path=""):
            if isinstance(d, str):
                leaf_topics.append(d if not current_path else f"{current_path} - {d}")
                return
            if isinstance(d, dict):
                for k, v in d.items():
                    if k != "name":
                        new_path = k if not current_path else f"{current_path} - {k}"
                        traverse(v, new_path)
        
        traverse(topics_dict)
        return leaf_topics

    def update_topic_history(self, topic_info):
        """Track which topics have been covered."""
        if not hasattr(self, 'topic_history'):
            self.topic_history = {
                'covered_topics': [],
                'domain_coverage': {},
                'last_topics': []
            }
        
        # Add timestamp to topic info
        topic_entry = {
            'timestamp': datetime.now().isoformat(),
            'topic_info': topic_info
        }
        
        # Add to covered topics
        self.topic_history['covered_topics'].append(topic_entry)
        
        # Update domain coverage
        domain_id = topic_info['domain']['id']
        if domain_id not in self.topic_history['domain_coverage']:
            self.topic_history['domain_coverage'][domain_id] = {
                'count': 0,
                'last_accessed': None
            }
        
        self.topic_history['domain_coverage'][domain_id]['count'] += 1
        self.topic_history['domain_coverage'][domain_id]['last_accessed'] = datetime.now().isoformat()
        
        # Keep track of last N topics to avoid repetition
        MAX_RECENT_TOPICS = 10
        self.topic_history['last_topics'].append(topic_info['full_path'])
        if len(self.topic_history['last_topics']) > MAX_RECENT_TOPICS:
            self.topic_history['last_topics'].pop(0)

    def get_topic_coverage_stats(self):
        """Get statistics about topic coverage."""
        if not hasattr(self, 'topic_history'):
            return None
        
        stats = {
            'total_questions': len(self.topic_history['covered_topics']),
            'domain_coverage': {},
            'recent_topics': self.topic_history['last_topics'][-5:]  # Last 5 topics
        }
        
        # Calculate domain coverage percentages
        total_questions = stats['total_questions']
        if total_questions > 0:
            for domain_id, coverage in self.topic_history['domain_coverage'].items():
                stats['domain_coverage'][domain_id] = {
                    'count': coverage['count'],
                    'percentage': (coverage['count'] / total_questions) * 100,
                    'last_accessed': coverage['last_accessed']
                }
        
        return stats

    def format_question_prompt(self):
        """Create a standardized prompt for the OpenAI API."""
        selected_topic = self.select_random_topic()
        difficulty = self.difficulty_manager.get_topic_difficulty(selected_topic['full_path'])
        
        return [
            {
                "role": "system",
                "content": f"""You are a CompTIA exam question generator. Generate a question following this EXACT format (including the prefixes):

Question on its own line
CORRECT: The correct answer
OPTION: First incorrect option
OPTION: Second incorrect option
OPTION: Third incorrect option
OPTION: The exact same text as the correct answer

Important rules for generating questions:
1. Vary question types - use different formats such as (disregard the order):
   - Scenario-based questions 
   - Implementation questions 
   - Troubleshooting questions 
   - Configuration questions 
   - Comparison questions 
2. Avoid overusing "What is the primary purpose of..."
3. Make questions practical and situation-based when possible
4. Match CompTIA's cognitive complexity levels

Important rules for generating options:
1. Each incorrect option must be plausible within the security context
2. Incorrect options should use proper security terminology
3. Options should be similar in length and style to the correct answer
4. Incorrect options should represent common misconceptions or partial understandings
5. Each option should be unique and clearly different from others
6. Avoid obviously wrong or nonsensical options
7. All options should be complete, grammatically correct sentences
8. Options should match the question's grammatical structure

EXPLANATION: A detailed explanation of why the correct answer is right and why others are wrong
OBJECTIVE: {selected_topic['full_path']}

Additional guidelines:
1. Include ALL prefixes exactly as shown
2. One option MUST be exactly identical to the correct answer
3. The explanation should be detailed and educational
4. Do not include any empty lines
5. Do not include any additional text or formatting"""
            },
            {
                "role": "user",
                "content": "Generate a CompTIA-style question following the exact format specified."
            }
        ]

    def save_question_data(self, question_data):
        """Save question data to history."""
        self.history.add_question(question_data)

    def update_session_stats(self, is_correct):
        """Update and display session statistics."""
        self.session_stats['total'] += 1
        if is_correct:
            self.session_stats['correct'] += 1
        
        # Calculate percentage
        percentage = (self.session_stats['correct'] / self.session_stats['total']) * 100 if self.session_stats['total'] > 0 else 0
        
        # Update display with color based on performance
        color = "green" if percentage >= 70 else "orange" if percentage >= 50 else "red"
        stats_text = f"Session: {self.session_stats['correct']}/{self.session_stats['total']} ({percentage:.1f}%)"
        self.session_stats_label.config(text=stats_text, fg=color)

    def check_answer(self):
        """Check the selected answer."""
        selected_option = self.var.get()
        if selected_option:
            is_correct = selected_option == self.correct_answer
            
            # Create and center feedback window
            feedback_window = tk.Toplevel(self.master)
            feedback_window.title("Question Result")
            
            # Set size and center position
            width = 1050  # Increased from 700 by 50%
            height = 900  # Increased from 600 by 50%
            screen_width = self.master.winfo_screenwidth()
            screen_height = self.master.winfo_screenheight()
            x = (screen_width - width) // 2
            y = (screen_height - height) // 2
            feedback_window.geometry(f"{width}x{height}+{x}+{y}")
            
            # Make modal and stay on top
            feedback_window.transient(self.master)
            feedback_window.grab_set()
            feedback_window.focus_force()
            
            # Create main content frame with padding
            content_frame = tk.Frame(feedback_window, padx=40, pady=20)  # Increased padding
            content_frame.pack(fill='both', expand=True)
            
            # Result header
            result_text = "✓ Correct!" if is_correct else "✗ Incorrect"
            result_color = 'green' if is_correct else 'red'
            tk.Label(
                content_frame,
                text=result_text,
                font=('Arial', 36, 'bold'),  # Changed from 48 to 36 (1.5x original 24)
                fg=result_color
            ).pack(pady=(0, 20))
            
            # Show correct answer if wrong
            if not is_correct:
                tk.Label(
                    content_frame,
                    text="Correct Answer:",
                    font=('Arial', 21, 'bold')  # Changed from 28 to 21 (1.5x original 14)
                ).pack(pady=(0, 5))
                tk.Label(
                    content_frame,
                    text=self.correct_answer,
                    font=('Arial', 20),  # Changed from 26 to 20 (1.5x original 13)
                    wraplength=900  # Increased from 600 to match wider window
                ).pack(pady=(0, 20))
            
            # Explanation
            tk.Label(
                content_frame,
                text="Explanation:",
                font=('Arial', 21, 'bold')  # Changed from 28 to 21 (1.5x original 14)
            ).pack(pady=(0, 5))
            tk.Label(
                content_frame,
                text=self.explanation,
                font=('Arial', 20),  # Changed from 26 to 20 (1.5x original 13)
                wraplength=900,  # Increased from 600 to match wider window
                justify='left'
            ).pack(pady=(0, 20))
            
            # Performance stats
            stats_frame = tk.Frame(content_frame)
            stats_frame.pack(fill='x', pady=10)
            
            topic_stats = self.session_stats_manager.get_topic_stats(self.current_topic['full_path'])
            domain_stats = self.session_stats_manager.get_domain_stats(self.current_topic['domain']['id'])
            
            # Topic performance
            tk.Label(
                stats_frame,
                text=f"Topic Performance - Session: {topic_stats['current_session']['percentage']:.1f}% | "
                     f"All-time: {topic_stats['all_time']['percentage']:.1f}%",
                font=('Arial', 18)  # Changed from 24 to 18 (1.5x original 12)
            ).pack()
            
            # Domain performance
            tk.Label(
                stats_frame,
                text=f"Domain Performance - Session: {domain_stats['current_session']['percentage']:.1f}% | "
                     f"All-time: {domain_stats['all_time']['percentage']:.1f}%",
                font=('Arial', 18)  # Changed from 24 to 18 (1.5x original 12)
            ).pack()
            
            # Next Question button
            tk.Button(
                content_frame,
                text="Next Question",
                command=lambda: [feedback_window.destroy(), self.next_question()],
                font=('Arial', 18, 'bold'),  # Increased from 12 to 18 (1.5x)
                width=15,
                height=2
            ).pack(pady=20)
            
            # Update stats
            self.session_stats_manager.update_stats(
                is_correct, 
                self.current_topic['full_path'],
                self.current_topic['domain']['id']
            )
            self.update_stats_display()
            
            # Disable submit button
            self.submit_button.config(state=tk.DISABLED)

    def load_question(self):
        """Load a new question from OpenAI API."""
        loading_screen = LoadingScreen(self.master)
        
        def load_question_thread():
            try:
                # Topic selection (5%)
                loading_screen.update_progress('topic_selection')
                self.current_topic = self.select_random_topic()
                
                # Store the selected topic in history
                self.update_topic_history(self.current_topic)
                
                # Difficulty adjustment (5%)
                loading_screen.update_progress('difficulty_adjustment')
                current_difficulty = self.difficulty_manager.get_topic_difficulty(self.current_topic['full_path'])
                
                # Question generation (70%)
                loading_screen.update_progress('question_generation')
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=self.format_question_prompt(),
                    temperature=0.7
                )
                
                # Response processing (15%)
                loading_screen.update_progress('response_processing')
                response_content = response.choices[0].message.content
                question, correct_answer, options, explanation, objective = self.parse_response(response_content)
                
                # UI update (3%)
                loading_screen.update_progress('ui_update')
                self.master.after(0, lambda: self.update_ui_with_question(
                    question, correct_answer, options, explanation, objective, current_difficulty
                ))
                
                # Completion (2%)
                loading_screen.update_progress('completion')
                self.master.after(500, loading_screen.destroy)
                
            except Exception as e:
                print(f"Error loading question: {str(e)}")
                loading_screen.destroy()
                messagebox.showerror("Error", f"Failed to load question: {str(e)}")
                self.master.after(1000, self.load_question)
        
        # Start loading in separate thread
        thread = threading.Thread(target=load_question_thread)
        thread.daemon = True
        thread.start()
    
    def update_ui_with_question(self, question, correct_answer, options, explanation, objective, difficulty):
        """Update UI with new question data."""
        self.current_question = question
        self.correct_answer = correct_answer
        self.explanation = explanation
        self.objective = objective
        
        # Update difficulty display
        self.current_difficulty.config(
            text=difficulty.name,
            fg={"BEGINNER": "green", "INTERMEDIATE": "blue", "ADVANCED": "red"}[difficulty.name]
        )
        
        # Update question display
        self.question_label.config(text=question)
        self.objective_label.config(text=f"Exam Objective: {objective}")
        
        # Update options
        random.shuffle(options)
        for i in range(4):
            self.option_buttons[i].config(text=options[i])
            self.option_buttons[i].config(value=options[i])
        
        # Reset UI state
        self.var.set(None)
        self.submit_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)

    def next_question(self):
        """Load the next question."""
        self.load_question()

    def parse_response(self, response_content):
        """Parse and validate the API response to ensure correct formatting."""
        lines = [line.strip() for line in response_content.split('\n') if line.strip()]
        
        try:
            question = lines[0]
            
            # Extract correct answer
            correct_line = next((line for line in lines if line.startswith('CORRECT: ')), None)
            if not correct_line:
                raise ValueError("No correct answer marked")
            correct_answer = correct_line.replace('CORRECT: ', '').strip()

            # Extract options
            options = [line.replace('OPTION: ', '').strip() 
                      for line in lines if line.startswith('OPTION: ')]
            
            # If we don't have enough options, generate plausible alternatives
            if len(options) < 4 or len(set(options)) < 4:
                existing_options = set(options)
                existing_options.add(correct_answer)
                
                # Extract key terms from question and correct answer
                question_terms = set(question.lower().split())
                answer_terms = set(correct_answer.lower().split())
                
                # Generate contextual alternatives based on question type
                if "which of the following" in question.lower():
                    key_terms = [term for term in answer_terms if term not in {'the', 'a', 'an', 'and', 'or', 'but'}]
                    if key_terms:
                        alternatives = [
                            f"Using {key_terms[0]} with additional security controls",
                            f"Implementing {key_terms[-1]} without other measures",
                            f"Combining multiple approaches except {key_terms[0]}",
                            f"Only using automated {key_terms[-1]} solutions"
                        ]
                    else:
                        alternatives = self.generate_generic_alternatives(question, correct_answer)
                        
                elif any(word in question.lower() for word in ["primary", "main", "most"]):
                    key_terms = [term for term in answer_terms if term not in {'the', 'a', 'an', 'and', 'or', 'but'}]
                    if key_terms:
                        alternatives = [
                            f"Regular monitoring of {key_terms[0]} activities",
                            f"Periodic review of {key_terms[-1]} implementation",
                            f"Automated {key_terms[0]} management",
                            f"Delegated {key_terms[-1]} oversight"
                        ]
                    else:
                        alternatives = self.generate_generic_alternatives(question, correct_answer)
                        
                elif "how" in question.lower():
                    alternatives = [
                        "Through manual intervention and monitoring",
                        "Using automated tools exclusively",
                        "By implementing third-party solutions",
                        "Through periodic assessments and reviews"
                    ]
                    
                elif "why" in question.lower():
                    alternatives = [
                        "To reduce operational costs",
                        "To simplify system management",
                        "To meet minimum compliance requirements",
                        "To streamline existing processes"
                    ]
                    
                else:
                    alternatives = self.generate_generic_alternatives(question, correct_answer)
                
                # Add alternatives until we have 4 unique options
                for alt in alternatives:
                    if len(existing_options) >= 4:
                        break
                    if alt not in existing_options and alt != correct_answer:
                        options.append(alt)
                        existing_options.add(alt)
            
            # Trim to exactly 4 options while keeping correct answer
            if len(options) > 4:
                if correct_answer in options:
                    options.remove(correct_answer)
                    options = options[:3]
                    options.append(correct_answer)
                else:
                    options = options[:4]
                    options[0] = correct_answer

            # Extract explanation and objective
            explanation = next((line.replace('EXPLANATION: ', '').strip() 
                              for line in lines if line.startswith('EXPLANATION: ')), 
                             "No explanation provided.")
            
            objective = next((line.replace('OBJECTIVE: ', '').strip() 
                             for line in lines if line.startswith('OBJECTIVE: ')), 
                            self.current_topic['full_path'])

            return question, correct_answer, options, explanation, objective

        except Exception as e:
            print(f"Error parsing response: {str(e)}")
            print("Raw response:")
            print(response_content)
            raise ValueError(f"Failed to parse response: {str(e)}")

    def generate_generic_alternatives(self, question, correct_answer):
        """Generate context-aware generic alternatives."""
        security_terms = {
            'encryption': ['hashing', 'encoding', 'obfuscation'],
            'authentication': ['authorization', 'accounting', 'auditing'],
            'monitoring': ['logging', 'tracking', 'surveillance'],
            'policy': ['procedure', 'guideline', 'standard'],
            'control': ['measure', 'safeguard', 'protection']
        }
        
        # Find relevant security terms
        question_terms = question.lower().split()
        for term, alternatives in security_terms.items():
            if term in question_terms:
                return [
                    f"Using {alt} instead of {term}" for alt in alternatives
                ] + [f"Combining {term} with {alternatives[0]}"]
        
        # Default alternatives if no specific terms found
        return [
            "Implementing a multi-layered approach",
            "Using risk-based assessment methods",
            "Applying defense-in-depth strategies",
            "Following industry best practices"
        ]

    def show_coverage_stats(self):
        """Display a window showing topic coverage statistics."""
        stats_window = tk.Toplevel(self.master)
        stats_window.title("Topic Coverage Statistics")
        stats_window.geometry("800x600")
        
        # Center the window
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width - 800) // 2
        y = (screen_height - 600) // 2
        stats_window.geometry(f"+{x}+{y}")
        
        # Force focus with multiple attempts
        self.force_window_focus(stats_window)
        
        # Get current stats
        stats = self.get_topic_coverage_stats()
        if not stats:
            tk.Label(stats_window, text="No questions attempted yet").pack(pady=20)
            return

        # Create notebook for tabbed interface
        notebook = ttk.Notebook(stats_window)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Add tabs and their content
        self._add_summary_tab(notebook, stats)
        self._add_recent_topics_tab(notebook)
        self._add_domain_details_tab(notebook, stats)
        self._add_difficulty_tab(notebook)
        self._add_domain_coverage_tab(notebook)

        # Add export button
        export_button = tk.Button(stats_window, text="Export Stats", command=lambda: self.export_stats(stats))
        export_button.pack(pady=10)

    def _add_summary_tab(self, notebook, stats):
        """Add summary tab to the stats window."""
        summary_frame = ttk.Frame(notebook)
        notebook.add(summary_frame, text='Summary')

        # Add total questions count
        tk.Label(summary_frame, 
                text=f"Total Questions Attempted: {stats['total_questions']}", 
                font=('Arial', 12, 'bold')).pack(pady=10)

        # Create pie chart of domain coverage
        fig, ax = plt.subplots(figsize=(6, 4))
        domain_names = []
        domain_counts = []
        for domain_id, coverage in stats['domain_coverage'].items():
            domain_names.append(f"{domain_id}\n{EXAM_TOPICS[domain_id]['name']}")
            domain_counts.append(coverage['count'])

        ax.pie(domain_counts, labels=domain_names, autopct='%1.1f%%')
        ax.set_title('Domain Coverage Distribution')

        canvas = FigureCanvasTkAgg(fig, master=summary_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=10)

    def _add_recent_topics_tab(self, notebook):
        """Add recent topics tab to the stats window."""
        recent_frame = ttk.Frame(notebook)
        notebook.add(recent_frame, text='Recent Topics')

        # Create treeview for recent topics
        tree = ttk.Treeview(recent_frame, columns=('Time', 'Topic'), show='headings')
        tree.heading('Time', text='Time')
        tree.heading('Topic', text='Topic')
        tree.pack(fill='both', expand=True, padx=5, pady=5)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(recent_frame, orient='vertical', command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scrollbar.set)

        # Add recent topics to treeview
        for topic in reversed(self.topic_history['covered_topics']):
            time = datetime.fromisoformat(topic['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
            tree.insert('', 'end', values=(time, topic['topic_info']['full_path']))

    def _add_domain_details_tab(self, notebook, stats):
        """Add domain details tab to the stats window."""
        details_frame = ttk.Frame(notebook)
        notebook.add(details_frame, text='Domain Details')

        # Create treeview for domain details
        detail_tree = ttk.Treeview(details_frame, columns=('Domain', 'Count', 'Percentage', 'Last Access'), show='headings')
        detail_tree.heading('Domain', text='Domain')
        detail_tree.heading('Count', text='Questions')
        detail_tree.heading('Percentage', text='Coverage %')
        detail_tree.heading('Last Access', text='Last Accessed')
        detail_tree.pack(fill='both', expand=True, padx=5, pady=5)

        # Add domain details to treeview
        for domain_id, coverage in stats['domain_coverage'].items():
            domain_name = EXAM_TOPICS[domain_id]['name']
            count = coverage['count']
            percentage = f"{coverage['percentage']:.1f}%"
            last_access = datetime.fromisoformat(coverage['last_accessed']).strftime('%Y-%m-%d %H:%M:%S')
            detail_tree.insert('', 'end', values=(domain_name, count, percentage, last_access))

    def _add_difficulty_tab(self, notebook):
        """Add difficulty tab to the stats window."""
        difficulty_frame = ttk.Frame(notebook)
        notebook.add(difficulty_frame, text='Difficulty Analysis')

        # Add domain performance over time graph
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        domains_performance = self.session_stats_manager.get_all_domains_performance()
        
        for domain_id, stats in domains_performance.items():
            history = stats['all_time']['history']
            if history:
                timestamps = [datetime.fromisoformat(entry['timestamp']) for entry in history]
                success_rates = [entry['cumulative_success_rate'] for entry in history]
                ax2.plot(timestamps, success_rates, label=f"Domain {domain_id}")
        
        ax2.set_title('Domain Performance Over Time')
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Success Rate (%)')
        ax2.legend()
        plt.xticks(rotation=45)
        
        canvas2 = FigureCanvasTkAgg(fig2, master=difficulty_frame)
        canvas2.draw()
        canvas2.get_tk_widget().pack(pady=10)

        # Create treeview for difficulty stats
        diff_tree = ttk.Treeview(
            difficulty_frame,
            columns=('Topic', 'Current Difficulty', 'Success Rate', 'Attempts', 'Streak'),
            show='headings'
        )
        diff_tree.heading('Topic', text='Topic')
        diff_tree.heading('Current Difficulty', text='Current Difficulty')
        diff_tree.heading('Success Rate', text='Success Rate')
        diff_tree.heading('Attempts', text='Total Attempts')
        diff_tree.heading('Streak', text='Current Streak')
        diff_tree.pack(fill='both', expand=True, padx=5, pady=5)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(difficulty_frame, orient='vertical', command=diff_tree.yview)
        scrollbar.pack(side='right', fill='y')
        diff_tree.configure(yscrollcommand=scrollbar.set)

        # Add difficulty data
        for topic_path in self.difficulty_manager.user_performance:
            perf = self.difficulty_manager.user_performance[topic_path]
            difficulty = self.difficulty_manager.get_topic_difficulty(topic_path)
            success_rate = self.difficulty_manager.get_success_rate(topic_path)
            
            diff_tree.insert('', 'end', values=(
                topic_path,
                difficulty.name,
                f"{success_rate:.1f}%",
                perf['attempts'],
                perf['current_streak']
            ))

    def _add_domain_coverage_tab(self, notebook):
        """Add domain coverage tab to the stats window."""
        domain_coverage_frame = ttk.Frame(notebook)
        notebook.add(domain_coverage_frame, text='Domain Coverage')

        # Create figure with two subplots
        fig3, (ax3, ax4) = plt.subplots(2, 1, figsize=(8, 8))

        # Get domain stats
        domains_performance = self.session_stats_manager.get_all_domains_performance()
        domain_names = []
        current_percentages = []
        all_time_percentages = []
        expected_percentages = []  # Based on exam weights

        for domain_id, stats in domains_performance.items():
            domain_names.append(f"{domain_id}\n{EXAM_TOPICS[domain_id]['name']}")
            current_percentages.append(stats['current_session']['percentage'])
            all_time_percentages.append(stats['all_time']['percentage'])
            # Calculate expected percentage based on exam weight
            weight = EXAM_TOPICS[domain_id]['weight']
            expected_percentages.append(weight)

        # Plot current vs all-time performance
        x = range(len(domain_names))
        width = 0.35

        ax3.bar([i - width/2 for i in x], current_percentages, width, label='Current Session', color='skyblue')
        ax3.bar([i + width/2 for i in x], all_time_percentages, width, label='All-time', color='lightgreen')
        ax3.set_ylabel('Success Rate (%)')
        ax3.set_title('Domain Performance Comparison')
        ax3.set_xticks(x)
        ax3.set_xticklabels(domain_names, rotation=45, ha='right')
        ax3.legend()

        # Plot coverage vs exam weights
        total_questions = sum(stats['all_time']['total'] for stats in domains_performance.values())
        actual_coverage = []
        
        for domain_id in domains_performance:
            questions = domains_performance[domain_id]['all_time']['total']
            coverage = (questions / total_questions * 100) if total_questions > 0 else 0
            actual_coverage.append(coverage)

        ax4.bar([i - width/2 for i in x], actual_coverage, width, label='Actual Coverage', color='lightcoral')
        ax4.bar([i + width/2 for i in x], expected_percentages, width, label='Exam Weight', color='lightblue')
        ax4.set_ylabel('Percentage (%)')
        ax4.set_title('Coverage vs Exam Weights')
        ax4.set_xticks(x)
        ax4.set_xticklabels(domain_names, rotation=45, ha='right')
        ax4.legend()

        ax4.tick_params(axis='x', rotation=45)
        ax4.set_ylim(0, 100)  # Set y-axis from 0 to 100%
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to prevent label cutoff

        plt.tight_layout()
        
        canvas3 = FigureCanvasTkAgg(fig3, master=domain_coverage_frame)
        canvas3.draw()
        canvas3.get_tk_widget().pack(pady=10)

        # Add coverage details in a treeview
        coverage_tree = ttk.Treeview(
            domain_coverage_frame,
            columns=('Domain', 'Questions', 'Coverage', 'Weight', 'Difference'),
            show='headings'
        )
        coverage_tree.heading('Domain', text='Domain')
        coverage_tree.heading('Questions', text='Questions')
        coverage_tree.heading('Coverage', text='Actual Coverage %')
        coverage_tree.heading('Weight', text='Exam Weight %')
        coverage_tree.heading('Difference', text='Difference')
        coverage_tree.pack(fill='both', expand=True, padx=5, pady=5)

        # Add coverage data
        for domain_id, stats in domains_performance.items():
            questions = stats['all_time']['total']
            coverage = (questions / total_questions * 100) if total_questions > 0 else 0
            weight = EXAM_TOPICS[domain_id]['weight']
            difference = coverage - weight
            
            coverage_tree.insert('', 'end', values=(
                EXAM_TOPICS[domain_id]['name'],
                questions,
                f"{coverage:.1f}%",
                f"{weight}%",
                f"{difference:+.1f}%"
            ))

    def export_stats(self, stats):
        """Export statistics to a JSON file."""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"topic_coverage_{timestamp}.json"
        
        try:
            with open(filename, 'w') as f:
                json.dump(stats, f, indent=2)
            messagebox.showinfo("Export Successful", f"Statistics exported to {filename}")
        except Exception as e:
            messagebox.showerror("Export Failed", f"Failed to export statistics: {str(e)}")

    def update_stats_display(self):
        """Update both current session and all-time stats displays."""
        # Update current session display
        current_stats = self.session_stats_manager.get_current_session_stats()
        current_color = "green" if current_stats['percentage'] >= 70 else "orange" if current_stats['percentage'] >= 50 else "red"
        current_text = f"Current Session: {current_stats['correct']}/{current_stats['total']} ({current_stats['percentage']:.1f}%)"
        self.session_stats_label.config(text=current_text, fg=current_color)
        
        # Update progress bars and domain stats
        domains_performance = self.session_stats_manager.get_all_domains_performance()
        for domain_id, stats in domains_performance.items():
            print(f"\nUpdating display for domain {domain_id}:")  # Debug
            print(f"Current session: {stats['current_session']}")
            print(f"All-time: {stats['all_time']}")
            
            self.progress_tracker.update_progress(
                domain_id,
                stats['all_time']['percentage'],
                stats['current_session']['percentage']
            )

    def shutdown(self):
        """Properly shut down the application."""
        try:
            # Save current session
            self.session_stats_manager.end_session()
            
            # Save difficulty stats
            if hasattr(self, 'difficulty_manager'):
                self.difficulty_manager.save_stats()
            
            # Show goodbye message
            messagebox.showinfo("Goodbye", "Session saved. Thank you for studying!")
            
            # Destroy the window and quit
            self.master.destroy()
            self.master.quit()
        except Exception as e:
            print(f"Error during shutdown: {str(e)}")
            # Force quit if error occurs during clean shutdown
            self.master.destroy()
            self.master.quit()

    def create_menu(self):
        """Create the application menu bar."""
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(
            label="Export Statistics",
            command=lambda: self.export_stats(self.get_topic_coverage_stats())
        )
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.shutdown)
        
        # View menu
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Coverage Statistics", command=self.show_coverage_stats)
        view_menu.add_command(label="Study Recommendations", command=self.show_recommendations)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def adjust_difficulty(self, direction):
        """Manually adjust difficulty level."""
        if not hasattr(self, 'current_topic') or not self.current_topic:
            return
            
        current = self.difficulty_manager.get_topic_difficulty(self.current_topic['full_path'])
        if direction == 'increase' and current != DifficultyLevel.ADVANCED:
            new_level = DifficultyLevel(current.value + 1)
            self.difficulty_manager.set_topic_difficulty(self.current_topic['full_path'], new_level)
            self.current_difficulty.config(
                text=new_level.name,
                fg={"BEGINNER": "green", "INTERMEDIATE": "blue", "ADVANCED": "red"}[new_level.name]
            )
        elif direction == 'decrease' and current != DifficultyLevel.BEGINNER:
            new_level = DifficultyLevel(current.value - 1)
            self.difficulty_manager.set_topic_difficulty(self.current_topic['full_path'], new_level)
            self.current_difficulty.config(
                text=new_level.name,
                fg={"BEGINNER": "green", "INTERMEDIATE": "blue", "ADVANCED": "red"}[new_level.name]
            )

    def show_recommendations(self):
        """Show study recommendations based on performance."""
        recommendations_window = tk.Toplevel(self.master)
        recommendations_window.title("Study Recommendations")
        recommendations_window.geometry("600x400")
        
        # Center the window
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width - 600) // 2
        y = (screen_height - 400) // 2
        recommendations_window.geometry(f"+{x}+{y}")
        
        # Force focus with multiple attempts
        self.force_window_focus(recommendations_window)
        
        # Add scrollable frame
        canvas = tk.Canvas(recommendations_window)
        scrollbar = ttk.Scrollbar(recommendations_window, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Get performance data
        domains_performance = self.session_stats_manager.get_all_domains_performance()
        
        # Add header
        tk.Label(
            scrollable_frame,
            text="Study Recommendations",
            font=('Arial', 14, 'bold')
        ).pack(pady=10)
        
        # Analyze and display recommendations
        weak_areas = []
        for domain_id, stats in domains_performance.items():
            performance = stats['all_time']['percentage']
            expected = EXAM_TOPICS[domain_id]['weight']
            total_questions = self.session_stats_manager.all_sessions['total_questions']
            coverage = (stats['all_time']['total'] / total_questions * 100) if total_questions > 0 else 0
            
            frame = tk.Frame(scrollable_frame)
            frame.pack(fill='x', pady=5, padx=10)
            
            domain_name = EXAM_TOPICS[domain_id]['name']
            status = "⚠️ Needs Focus" if performance < 70 else "✅ Good Progress"
            coverage_status = "📊 Under-covered" if coverage < expected else "📈 Well-covered"
            
            tk.Label(
                frame,
                text=f"{domain_id}: {domain_name}",
                font=('Arial', 11, 'bold')
            ).pack(anchor='w')
            
            tk.Label(
                frame,
                text=f"Performance: {performance:.1f}% ({status})",
                fg="red" if performance < 70 else "green"
            ).pack(anchor='w')
            
            tk.Label(
                frame,
                text=f"Coverage: {coverage:.1f}% vs {expected}% target ({coverage_status})",
                fg="red" if coverage < expected else "green"
            ).pack(anchor='w')
            
            if performance < 70 or coverage < expected:
                weak_areas.append(domain_id)
        
        # Pack scrollbar and canvas
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        
        # Add action buttons
        button_frame = ttk.Frame(recommendations_window)
        button_frame.pack(fill='x', pady=10)
        
        ttk.Button(
            button_frame,
            text="Focus on Weak Areas",
            command=lambda: self.focus_on_domains(weak_areas)
        ).pack(side='left', padx=5)
        
        ttk.Button(
            button_frame,
            text="Close",
            command=recommendations_window.destroy
        ).pack(side='right', padx=5)

    def show_about(self):
        """Show about dialog."""
        about_text = """
        CompTIA Security+ Study App
        Version 1.0
        
        A study tool for the CompTIA Security+ SY0-701 exam.
        
        Features:
        - Adaptive difficulty
        - Progress tracking
        - Performance analytics
        - Study recommendations
        
        Good luck with your studies!
        """
        
        messagebox.showinfo("About", about_text)

    def focus_on_domains(self, domain_ids):
        """Temporarily adjust topic selection to focus on specific domains."""
        # Implementation for focusing on specific domains
        pass

    def get_domain_coverage_stats(self):
        """Calculate domain coverage statistics."""
        coverage = {domain: 0 for domain in EXAM_TOPICS.keys()}
        total_questions = len(self.topic_history['covered_topics'])
        
        for topic in self.topic_history['covered_topics']:
            domain = topic['topic_info']['domain']['id']
            coverage[domain] += 1
        
        return {
            domain: {
                'count': count,
                'percentage': (count/total_questions*100) if total_questions > 0 else 0,
                'target': EXAM_TOPICS[domain]['weight'],
                'difference': ((count/total_questions*100) if total_questions > 0 else 0) - EXAM_TOPICS[domain]['weight']
            }
            for domain, count in coverage.items()
        }

    def force_window_focus(self, window):
        """Force a window to top and focus with multiple attempts."""
        def single_attempt():
            window.lift()
            window.focus_force()
            window.attributes('-topmost', True)
            window.after(100, lambda: window.attributes('-topmost', False))
        
        # Make three attempts, 5 seconds apart
        single_attempt()
        window.after(5000, single_attempt)
        window.after(10000, single_attempt)

    def force_focus(self):
        """Force window to top and focus."""
        self.master.lift()  # Bring window to top
        self.master.attributes('-topmost', True)  # Force window to stay on top temporarily
        self.master.focus_force()  # Force focus
        self.master.after(100, lambda: self.master.attributes('-topmost', False))  # Allow window to be lowered after gaining focus

if __name__ == "__main__":
    root = tk.Tk()
    app = CompTIAQuizApp(root)
    root.mainloop()