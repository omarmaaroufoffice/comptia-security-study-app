import json
from datetime import datetime

class SessionStats:
    def __init__(self):
        self.stats_file = "all_sessions_stats.json"
        self.current_session = {
            'correct': 0,
            'total': 0,
            'start_time': datetime.now().isoformat(),
            'topics': {},
            'domains': {}  # Add domain tracking
        }
        self.all_sessions = self.load_stats()

    def load_stats(self):
        """Load statistics from file."""
        try:
            with open(self.stats_file, 'r') as f:
                data = json.load(f)
                # Ensure topic stats exist in loaded data
                if 'topic_stats' not in data:
                    data['topic_stats'] = {}
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            return {
                'sessions': [],
                'total_correct': 0,
                'total_questions': 0,
                'topic_stats': {},  # Track topic performance across all sessions
                'domain_stats': {}  # Track domain performance across all sessions
            }

    def save_stats(self):
        """Save statistics to file."""
        try:
            with open(self.stats_file, 'w') as f:
                json.dump(self.all_sessions, f, indent=2)
        except Exception as e:
            print(f"Error saving session stats: {str(e)}")

    def update_stats(self, is_correct, topic_path, domain_id):
        """Update statistics for a question attempt."""
        print(f"\nBefore update - Domain {domain_id}:")  # Debug
        print(f"Current session: {self.current_session['domains']}")
        print(f"All-time: {self.all_sessions.get('domain_stats', {})}")

        # Update current session stats
        self.current_session['total'] += 1
        if is_correct:
            self.current_session['correct'] += 1

        # Update domain stats for current session
        if domain_id not in self.current_session['domains']:
            self.current_session['domains'][domain_id] = {'correct': 0, 'total': 0}
        
        domain_stats = self.current_session['domains'][domain_id]
        domain_stats['total'] += 1
        if is_correct:
            domain_stats['correct'] += 1

        # Update all-time domain stats
        if 'domain_stats' not in self.all_sessions:
            self.all_sessions['domain_stats'] = {}
        
        if domain_id not in self.all_sessions['domain_stats']:
            self.all_sessions['domain_stats'][domain_id] = {
                'correct': 0,
                'total': 0,
                'last_attempt': None,
                'history': []
            }
        
        all_time_stats = self.all_sessions['domain_stats'][domain_id]
        all_time_stats['total'] += 1
        if is_correct:
            all_time_stats['correct'] += 1
        all_time_stats['last_attempt'] = datetime.now().isoformat()

        print(f"\nAfter update - Domain {domain_id}:")  # Debug
        print(f"Current session: {self.current_session['domains']}")
        print(f"All-time: {self.all_sessions['domain_stats']}")

        # Save after each update
        self.save_stats()

    def get_current_session_stats(self):
        """Get current session statistics."""
        total = self.current_session['total']
        correct = self.current_session['correct']
        percentage = (correct / total * 100) if total > 0 else 0
        return {
            'correct': correct,
            'total': total,
            'percentage': percentage
        }

    def get_all_time_stats(self):
        """Get all-time statistics."""
        total = self.all_sessions['total_questions']
        correct = self.all_sessions['total_correct']
        percentage = (correct / total * 100) if total > 0 else 0
        return {
            'correct': correct,
            'total': total,
            'percentage': percentage
        }

    def end_session(self):
        """End the current session and save stats."""
        # Add session to history
        session_summary = {
            'start_time': self.current_session['start_time'],
            'end_time': datetime.now().isoformat(),
            'correct': self.current_session['correct'],
            'total': self.current_session['total'],
            'topics_covered': list(self.current_session['topics'].keys()),
            'domains_covered': list(self.current_session['domains'].keys())
        }
        self.all_sessions['sessions'].append(session_summary)
        
        # Update domain history before saving
        for domain_id, stats in self.current_session['domains'].items():
            if domain_id not in self.all_sessions['domain_stats']:
                self.all_sessions['domain_stats'][domain_id] = {
                    'correct': 0,
                    'total': 0,
                    'last_attempt': None,
                    'history': []
                }
            
            domain_stats = self.all_sessions['domain_stats'][domain_id]
            success_rate = (stats['correct'] / stats['total'] * 100) if stats['total'] > 0 else 0
            domain_stats['history'].append({
                'timestamp': datetime.now().isoformat(),
                'success_rate': success_rate,
                'cumulative_success_rate': (domain_stats['correct'] / domain_stats['total'] * 100) 
                    if domain_stats['total'] > 0 else 0
            })
        
        # Save all stats
        self.save_stats()

    def get_topic_stats(self, topic_path):
        """Get statistics for a specific topic."""
        all_time_stats = self.all_sessions['topic_stats'].get(topic_path, {
            'correct': 0,
            'total': 0,
            'last_attempt': None,
            'sessions_seen': 0
        })
        
        current_stats = self.current_session['topics'].get(topic_path, {
            'correct': 0,
            'total': 0
        })

        all_time_percentage = (
            (all_time_stats['correct'] / all_time_stats['total'] * 100)
            if all_time_stats['total'] > 0 else 0
        )
        
        current_percentage = (
            (current_stats['correct'] / current_stats['total'] * 100)
            if current_stats['total'] > 0 else 0
        )

        return {
            'all_time': {
                'correct': all_time_stats['correct'],
                'total': all_time_stats['total'],
                'percentage': all_time_percentage,
                'last_attempt': all_time_stats['last_attempt']
            },
            'current_session': {
                'correct': current_stats['correct'],
                'total': current_stats['total'],
                'percentage': current_percentage
            }
        }

    def get_all_topics_performance(self):
        """Get performance statistics for all topics."""
        topics_performance = {}
        for topic_path in self.all_sessions['topic_stats'].keys():
            topics_performance[topic_path] = self.get_topic_stats(topic_path)
        return topics_performance 

    def get_domain_stats(self, domain_id):
        """Get performance statistics for a specific domain."""
        print(f"\nGetting stats for domain {domain_id}:")  # Debug log
        
        all_time_stats = self.all_sessions.get('domain_stats', {}).get(domain_id, {
            'correct': 0,
            'total': 0,
            'last_attempt': None,
            'history': []
        })
        
        current_stats = self.current_session['domains'].get(domain_id, {
            'correct': 0,
            'total': 0
        })

        print(f"All-time stats: {all_time_stats}")
        print(f"Current session stats: {current_stats}")

        # Calculate percentages
        all_time_percentage = (
            (all_time_stats['correct'] / all_time_stats['total'] * 100)
            if all_time_stats['total'] > 0 else 0
        )
        
        current_percentage = (
            (current_stats['correct'] / current_stats['total'] * 100)
            if current_stats['total'] > 0 else 0
        )

        print(f"Calculated percentages:")
        print(f"All-time: {all_time_percentage}%")
        print(f"Current session: {current_percentage}%")

        return {
            'all_time': {
                'correct': all_time_stats['correct'],
                'total': all_time_stats['total'],
                'percentage': all_time_percentage,
                'last_attempt': all_time_stats['last_attempt'],
                'history': all_time_stats['history']
            },
            'current_session': {
                'correct': current_stats['correct'],
                'total': current_stats['total'],
                'percentage': current_percentage
            }
        }

    def get_all_domains_performance(self):
        """Get performance statistics for all domains."""
        domains_performance = {}
        for domain_id in self.all_sessions.get('domain_stats', {}).keys():
            domains_performance[domain_id] = self.get_domain_stats(domain_id)
        return domains_performance