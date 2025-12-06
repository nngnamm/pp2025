import math
import numpy as np


class School:
    """Manages students, courses, and marks"""
    
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def calculate_gpa(self, student_id):
        """Calculate GPA for a student using numpy arrays for weighted sum"""
        if not self.courses or not self.marks:
            return 0.0
        
        credits_list = []
        marks_list = []
        
        for course in self.courses:
            if course.id in self.marks and student_id in self.marks[course.id]:
                credits_list.append(course.credits)
                marks_list.append(self.marks[course.id][student_id])
        
        if not credits_list:
            return 0.0
        
        credits_array = np.array(credits_list)
        marks_array = np.array(marks_list)
        
        weighted_sum = np.sum(credits_array * marks_array)
        total_credits = np.sum(credits_array)
        
        gpa = weighted_sum / total_credits if total_credits > 0 else 0.0
        return math.floor(gpa * 10) / 10
