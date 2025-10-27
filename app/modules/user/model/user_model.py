from datetime import datetime

class User:
    """User model"""

    def __init__(self, email, name, password_hash=None, id=None, created_at=None):
        self.id = id
        self.email = email
        self.name = name
        self.password_hash = password_hash
        self.created_at = created_at or datetime.now().isoformat()

    def to_dict(self):
        """Convert to dictionary (includes password hash)"""
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'password_hash': self.password_hash,
            'created_at': self.created_at
        }

    def to_safe_dict(self):
        """Convert to dictionary without password"""
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'created_at': self.created_at
        }

    @staticmethod
    def from_dict(data):
        """Create a User from a dictionary"""
        return User(
            email=data['email'],
            name=data.get('name', ''),
            password_hash=data.get('password_hash'),
            id=data.get('id'),
            created_at=data.get('created_at')
        )
