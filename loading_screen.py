import tkinter as tk
from tkinter import ttk
import time
import threading

class LoadingScreen(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Window setup
        self.title("Loading Next Question")
        width = 300
        height = 150
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f'{width}x{height}+{x}+{y}')
        
        # Remove window decorations
        self.overrideredirect(True)
        
        # Make window stay on top
        self.transient(parent)
        self.grab_set()
        
        # Configure style
        style = ttk.Style()
        style.configure("Loading.TProgressbar", 
                       troughcolor='lightgray',
                       background='green',
                       thickness=10)
        
        # Add loading message
        self.message = tk.Label(
            self,
            text="Preparing...",
            font=('Arial', 12, 'bold')
        )
        self.message.pack(pady=20)
        
        # Add detailed status
        self.status = tk.Label(
            self,
            text="",
            font=('Arial', 10),
            fg='gray'
        )
        self.status.pack(pady=5)
        
        # Add progress bar
        self.progress = ttk.Progressbar(
            self,
            style="Loading.TProgressbar",
            length=250,
            mode='determinate'
        )
        self.progress.pack(pady=10)
        
        # Add cancel button
        self.cancel_button = tk.Button(
            self,
            text="Cancel",
            command=self.cancel_loading,
            bg='#ff4444',
            fg='white'
        )
        self.cancel_button.pack(pady=10)
        
        self.cancelled = False
        self.start_time = time.time()
        
        # Define operation weights (total = 100)
        self.operations = {
            'topic_selection': {'weight': 5, 'message': 'Selecting topic...'},
            'difficulty_adjustment': {'weight': 5, 'message': 'Adjusting difficulty...'},
            'question_generation': {'weight': 70, 'message': 'Generating question (this may take a moment)...'},
            'response_processing': {'weight': 15, 'message': 'Processing response...'},
            'ui_update': {'weight': 3, 'message': 'Updating interface...'},
            'completion': {'weight': 2, 'message': 'Complete!'}
        }
        
        # Track progress
        self.current_progress = 0
        
    def update_progress(self, operation, message=None):
        """Update progress based on operation."""
        if operation not in self.operations:
            return
            
        # Calculate progress
        op_data = self.operations[operation]
        self.current_progress += op_data['weight']
        
        # Update UI
        self.progress['value'] = self.current_progress
        self.message['text'] = message or op_data['message']
        
        # Show elapsed time
        elapsed = time.time() - self.start_time
        self.status['text'] = f"Time elapsed: {elapsed:.1f}s"
        
        # If it's the question generation phase and taking long, show additional message
        if operation == 'question_generation' and elapsed > 5:
            self.status['text'] += "\nAPI request in progress..."
        
        self.update()
        
    def cancel_loading(self):
        """Cancel the loading operation."""
        self.cancelled = True
        self.message['text'] = "Cancelling..."
        self.status['text'] = "Please wait..."
        self.cancel_button['state'] = 'disabled'
        self.update()
        self.after(500, self.destroy)  # Give user visual feedback before closing 