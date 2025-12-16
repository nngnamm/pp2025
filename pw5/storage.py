import os
import pickle
import gzip


def save_students(students):
    """Save students to students.txt"""
    with open('students.txt', 'w', encoding='utf-8') as f:
        for s in students:
            f.write(f"{s.id}|{s.name}|{s.dob}\n")


def save_courses(courses):
    """Save courses to courses.txt"""
    with open('courses.txt', 'w', encoding='utf-8') as f:
        for c in courses:
            f.write(f"{c.id}|{c.name}|{c.credits}\n")


def save_marks(marks):
    """Save marks to marks.txt"""
    with open('marks.txt', 'w', encoding='utf-8') as f:
        for course_id, student_marks in marks.items():
            for student_id, mark in student_marks.items():
                f.write(f"{course_id}|{student_id}|{mark}\n")


def compress_data():
    """Compress all text files into students.dat using gzip"""
    data = {
        'students': None,
        'courses': None,
        'marks': None
    }
    
    # Read students.txt if exists
    if os.path.exists('students.txt'):
        with open('students.txt', 'r', encoding='utf-8') as f:
            data['students'] = f.read()
    
    # Read courses.txt if exists
    if os.path.exists('courses.txt'):
        with open('courses.txt', 'r', encoding='utf-8') as f:
            data['courses'] = f.read()
    
    # Read marks.txt if exists
    if os.path.exists('marks.txt'):
        with open('marks.txt', 'r', encoding='utf-8') as f:
            data['marks'] = f.read()
    
    # Compress and save to students.dat
    with gzip.open('students.dat', 'wb') as f:
        pickle.dump(data, f)
    
    # Clean up text files
    for filename in ['students.txt', 'courses.txt', 'marks.txt']:
        if os.path.exists(filename):
            os.remove(filename)


def load_data():
    """Decompress and load data from students.dat"""
    if not os.path.exists('students.dat'):
        return None, None, None
    
    try:
        with gzip.open('students.dat', 'rb') as f:
            data = pickle.load(f)
        
        students_data = data.get('students', '')
        courses_data = data.get('courses', '')
        marks_data = data.get('marks', '')
        
        return students_data, courses_data, marks_data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None, None


def parse_students(data):
    """Parse students data from string"""
    from domains.student import Student
    
    students = []
    if data:
        for line in data.strip().split('\n'):
            if line:
                parts = line.split('|')
                if len(parts) == 3:
                    students.append(Student(parts[0], parts[1], parts[2]))
    return students


def parse_courses(data):
    """Parse courses data from string"""
    from domains.course import Course
    
    courses = []
    if data:
        for line in data.strip().split('\n'):
            if line:
                parts = line.split('|')
                if len(parts) == 3:
                    courses.append(Course(parts[0], parts[1], int(parts[2])))
    return courses


def parse_marks(data):
    """Parse marks data from string"""
    marks = {}
    if data:
        for line in data.strip().split('\n'):
            if line:
                parts = line.split('|')
                if len(parts) == 3:
                    course_id, student_id, mark = parts
                    if course_id not in marks:
                        marks[course_id] = {}
                    marks[course_id][student_id] = float(mark)
    return marks
