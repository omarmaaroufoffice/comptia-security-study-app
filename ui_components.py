import tkinter as tk
from tkinter import ttk
from datetime import datetime
from difficulty_manager import DifficultyLevel

class ProgressTracker(tk.Frame):
    def __init__(self, master, domains):
        super().__init__(master)
        self.domain_progress = {}
        
        # Add header with larger font
        header = tk.Label(self, text="Domain Progress:", font=('Arial', 12, 'bold'))
        header.pack(fill='x', pady=(5, 10))
        
        for domain_id, domain in domains.items():
            frame = tk.Frame(self)
            frame.pack(fill='x', pady=5)
            
            # Create domain label with name (wider)
            label_text = f"{domain_id}: {domain['name']}"
            label = tk.Label(frame, text=label_text, width=45, anchor='w', font=('Arial', 10))
            label.pack(side='left')
            
            # Progress bar (longer)
            progress = ttk.Progressbar(frame, length=300, mode='determinate')
            progress.pack(side='left', padx=10)
            
            # Stats frame for both percentages
            stats_frame = tk.Frame(frame)
            stats_frame.pack(side='left', padx=5)
            
            # Current session percentage (larger font)
            current_label = tk.Label(stats_frame, text="0%", width=10, anchor='w', 
                                   font=('Arial', 10, 'bold'))
            current_label.pack(side='top', pady=2)
            
            # All-time percentage
            alltime_label = tk.Label(stats_frame, text="(0%)", width=10, anchor='w',
                                   font=('Arial', 9))
            alltime_label.pack(side='bottom')
            
            self.domain_progress[domain_id] = {
                'bar': progress,
                'current_label': current_label,
                'alltime_label': alltime_label
            }
    
    def update_progress(self, domain_id, all_time_percentage, current_percentage=None):
        """Update progress display for a domain."""
        if domain_id in self.domain_progress:
            print(f"\nUpdating progress for domain {domain_id}:")  # Debug
            print(f"All-time: {all_time_percentage}%")
            print(f"Current session: {current_percentage}%")
            
            # Update progress bar
            self.domain_progress[domain_id]['bar']['value'] = all_time_percentage
            
            # Update all-time percentage
            all_time_color = "green" if all_time_percentage >= 70 else "orange" if all_time_percentage >= 50 else "red"
            self.domain_progress[domain_id]['alltime_label'].config(
                text=f"({all_time_percentage:.1f}%)",
                fg=all_time_color
            )
            
            # Update current session percentage
            if current_percentage is not None:
                current_color = "green" if current_percentage >= 70 else "orange" if current_percentage >= 50 else "red"
                self.domain_progress[domain_id]['current_label'].config(
                    text=f"{current_percentage:.1f}%",
                    fg=current_color
                )

class SessionTimer(tk.Label):
    def __init__(self, master):
        super().__init__(master, text="Session Time: 00:00:00")
        self.start_time = datetime.now()
    
    def update(self):
        elapsed = datetime.now() - self.start_time
        hours, remainder = divmod(elapsed.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.config(text=f"Session Time: {hours:02d}:{minutes:02d}:{seconds:02d}")
        self.after(1000, self.update)

class DifficultyControls(tk.Frame):
    def __init__(self, master, callback):
        super().__init__(master)
        self.callback = callback
        
        tk.Button(
            self,
            text="↓",
            command=lambda: self.callback('decrease'),
            width=2
        ).pack(side='left', padx=2)
        
        tk.Button(
            self,
            text="↑",
            command=lambda: self.callback('increase'),
            width=2
        ).pack(side='left', padx=2) 