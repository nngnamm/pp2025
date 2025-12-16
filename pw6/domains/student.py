class Student:
    """Represents a student with ID, name, and date of birth"""
    
    def __init__(self, sid, name, dob):
        self.id = sid
        self.name = name
        self.dob = dob

    def show(self):
        """Return string representation of student"""
        return f"ID: {self.id}, Name: {self.name}, DoB: {self.dob}"
