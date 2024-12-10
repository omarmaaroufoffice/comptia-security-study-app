from enum import Enum
import json

class DifficultyLevel(Enum):
    """Enumeration of difficulty levels."""
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3

class DifficultyManager:
    """Manages difficulty levels and user performance tracking for quiz topics."""
    
    def __init__(self):
        """Initialize the difficulty manager."""
        self.topic_difficulties = {}  # Stores difficulty level for each topic
        self.user_performance = {}    # Stores performance metrics for each topic
        
    def set_topic_difficulty(self, topic_path, difficulty):
        """Set difficulty for a specific topic.
        
        Args:
            topic_path (str): The full path of the topic
            difficulty (DifficultyLevel): The difficulty level to set
        """
        self.topic_difficulties[topic_path] = difficulty
        
    def get_topic_difficulty(self, topic_path):
        """Get difficulty for a specific topic.
        
        Args:
            topic_path (str): The full path of the topic
            
        Returns:
            DifficultyLevel: The difficulty level (defaults to INTERMEDIATE)
        """
        return self.topic_difficulties.get(topic_path, DifficultyLevel.INTERMEDIATE)
        
    def update_user_performance(self, topic_path, is_correct):
        """Update user performance for a topic.
        
        Args:
            topic_path (str): The full path of the topic
            is_correct (bool): Whether the user answered correctly
        """
        if topic_path not in self.user_performance:
            self.user_performance[topic_path] = {
                'attempts': 0,
                'correct': 0,
                'current_streak': 0
            }
            
        perf = self.user_performance[topic_path]
        perf['attempts'] += 1
        if is_correct:
            perf['correct'] += 1
            perf['current_streak'] += 1
        else:
            perf['current_streak'] = 0
            
    def get_success_rate(self, topic_path):
        """Get success rate for a topic.
        
        Args:
            topic_path (str): The full path of the topic
            
        Returns:
            float: Success rate as a percentage
        """
        if topic_path not in self.user_performance:
            return 0.0
        
        perf = self.user_performance[topic_path]
        if perf['attempts'] == 0:
            return 0.0
        return (perf['correct'] / perf['attempts']) * 100
        
    def suggest_difficulty_adjustment(self, topic_path):
        """Suggest if difficulty should be adjusted based on performance.
        
        Args:
            topic_path (str): The full path of the topic
            
        Returns:
            str or None: 'increase', 'decrease', or None if no adjustment needed
        """
        if topic_path not in self.user_performance:
            return None
            
        perf = self.user_performance[topic_path]
        current_difficulty = self.get_topic_difficulty(topic_path)
        
        # Need at least 3 attempts before suggesting changes
        if perf['attempts'] < 3:
            return None
        
        # Calculate success rate
        success_rate = self.get_success_rate(topic_path)
        
        # If success rate > 80% and current streak >= 3, suggest increasing difficulty
        if (success_rate > 80 and 
            perf['current_streak'] >= 3 and 
            current_difficulty != DifficultyLevel.ADVANCED):
            return 'increase'
            
        # If success rate < 40%, suggest decreasing difficulty
        if (success_rate < 40 and 
            current_difficulty != DifficultyLevel.BEGINNER):
            return 'decrease'
            
        return None

    def get_performance_summary(self, topic_path):
        """Get a summary of performance for a topic.
        
        Args:
            topic_path (str): The full path of the topic
            
        Returns:
            dict: Performance summary including attempts, success rate, and current streak
        """
        if topic_path not in self.user_performance:
            return {
                'attempts': 0,
                'success_rate': 0.0,
                'current_streak': 0,
                'difficulty': self.get_topic_difficulty(topic_path).name
            }
            
        perf = self.user_performance[topic_path]
        return {
            'attempts': perf['attempts'],
            'success_rate': self.get_success_rate(topic_path),
            'current_streak': perf['current_streak'],
            'difficulty': self.get_topic_difficulty(topic_path).name
        } 

    def save_stats(self):
        """Save difficulty settings and performance data."""
        try:
            stats_data = {
                'topic_difficulties': {k: v.value for k, v in self.topic_difficulties.items()},
                'user_performance': self.user_performance
            }
            with open('difficulty_settings.json', 'w') as f:
                json.dump(stats_data, f, indent=2)
        except Exception as e:
            print(f"Error saving difficulty stats: {str(e)}")

    def load_stats(self):
        """Load saved difficulty settings and performance data."""
        try:
            with open('difficulty_settings.json', 'r') as f:
                stats_data = json.load(f)
                self.topic_difficulties = {k: DifficultyLevel(v) for k, v in stats_data['topic_difficulties'].items()}
                self.user_performance = stats_data['user_performance']
        except (FileNotFoundError, json.JSONDecodeError):
            # No saved stats or invalid file - use defaults
            self.topic_difficulties = {}
            self.user_performance = {} 