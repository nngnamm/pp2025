class Course:
    """Represents a course with ID, name, and credits"""
    
    def __init__(self, cid, name, credits=3):
        self.id = cid
        self.name = name
        self.credits = credits

    def show(self):
        """Return string representation of course"""
        return f"ID: {self.id}, Name: {self.name}, Credits: {self.credits}"
