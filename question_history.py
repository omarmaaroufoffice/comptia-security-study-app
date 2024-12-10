import json
import os
from datetime import datetime

class QuestionHistory:
    def __init__(self):
        self.history_file = "question_history.json"
        self.history = {
            'questions': [],
            'statistics': {
                'total_questions': 0,
                'correct_answers': 0,
                'topics_covered': [],
                'domains_covered': []
            }
        }
        self.load_history()

    def load_history(self):
        """Load question history from file."""
        try:
            with open(self.history_file, 'r') as f:
                loaded_history = json.load(f)
                # Ensure all required keys exist
                if not isinstance(loaded_history, dict):
                    loaded_history = {}
                self.history = {
                    'questions': loaded_history.get('questions', []),
                    'statistics': {
                        'total_questions': loaded_history.get('statistics', {}).get('total_questions', 0),
                        'correct_answers': loaded_history.get('statistics', {}).get('correct_answers', 0),
                        'topics_covered': loaded_history.get('statistics', {}).get('topics_covered', []),
                        'domains_covered': loaded_history.get('statistics', {}).get('domains_covered', [])
                    }
                }
        except (FileNotFoundError, json.JSONDecodeError):
            # Keep the default initialized structure
            pass

    def add_question(self, question_data):
        """Add a question attempt to history."""
        # Ensure history has the correct structure
        if not isinstance(self.history, dict):
            self.history = {
                'questions': [],
                'statistics': {
                    'total_questions': 0,
                    'correct_answers': 0,
                    'topics_covered': [],
                    'domains_covered': []
                }
            }
        
        # Add question to history
        self.history['questions'].append(question_data)
        
        # Update statistics
        stats = self.history['statistics']
        stats['total_questions'] += 1
        if question_data['is_correct']:
            stats['correct_answers'] += 1
        
        # Track unique topics and domains
        topic_path = question_data['topic_info']['full_path']
        domain_id = question_data['topic_info']['domain']['id']
        
        if topic_path not in stats['topics_covered']:
            stats['topics_covered'].append(topic_path)
        if domain_id not in stats['domains_covered']:
            stats['domains_covered'].append(domain_id)
        
        # Save to file
        self.save_history()

    def save_history(self):
        """Save question history to file."""
        try:
            with open(self.history_file, 'w') as f:
                json.dump(self.history, f, indent=2)
        except Exception as e:
            print(f"Error saving question history: {str(e)}")

    def get_statistics(self):
        """Get summary statistics of question history."""
        stats = self.history['statistics']
        return {
            'total_questions': stats['total_questions'],
            'correct_answers': stats['correct_answers'],
            'success_rate': (
                stats['correct_answers'] / stats['total_questions'] * 100
            ) if stats['total_questions'] > 0 else 0,
            'unique_topics': len(stats['topics_covered']),
            'unique_domains': len(stats['domains_covered'])
        } 