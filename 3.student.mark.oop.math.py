import math
import numpy as np
import curses
from curses import wrapper


class Student:
    def __init__(self, sid, name, dob):
        self.id = sid
        self.name = name
        self.dob = dob

    def show(self):
        return f"ID: {self.id}, Name: {self.name}, DoB: {self.dob}"


class Course:
    def __init__(self, cid, name, credits=3):
        self.id = cid
        self.name = name
        self.credits = credits

    def show(self):
        return f"ID: {self.id}, Name: {self.name}, Credits: {self.credits}"


class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_number(self, stdscr, msg, y, x):
        while True:
            stdscr.addstr(y, x, msg + " " * 20)
            stdscr.refresh()
            curses.echo()
            try:
                n = int(stdscr.getstr(y, x + len(msg), 10).decode('utf-8'))
                curses.noecho()
                if n > 0:
                    return n
                stdscr.addstr(y + 1, x, "Positive number please!")
                stdscr.refresh()
                stdscr.getch()
            except:
                curses.noecho()
                stdscr.addstr(y + 1, x, "Error. Integer please!")
                stdscr.refresh()
                stdscr.getch()

    def input_students(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "=== INPUT STUDENTS ===", curses.A_BOLD)
        stdscr.refresh()
        
        n = self.input_number(stdscr, "Number of students:", 2, 0)
        
        for i in range(n):
            stdscr.clear()
            stdscr.addstr(0, 0, f"=== STUDENT {i+1}/{n} ===", curses.A_BOLD)
            
            stdscr.addstr(2, 0, "ID: ")
            stdscr.refresh()
            curses.echo()
            sid = stdscr.getstr(2, 4, 20).decode('utf-8').strip()
            
            stdscr.addstr(3, 0, "Name: ")
            stdscr.refresh()
            name = stdscr.getstr(3, 6, 30).decode('utf-8').strip()
            
            stdscr.addstr(4, 0, "DoB (YYYY-MM-DD): ")
            stdscr.refresh()
            dob = stdscr.getstr(4, 18, 15).decode('utf-8').strip()
            curses.noecho()
            
            self.students.append(Student(sid, name, dob))
        
        stdscr.addstr(6, 0, "Students added successfully! Press any key...", curses.A_REVERSE)
        stdscr.refresh()
        stdscr.getch()

    def list_students(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "=== STUDENTS LIST ===", curses.A_BOLD)
        
        if not self.students:
            stdscr.addstr(2, 0, "No students yet.", curses.A_DIM)
            stdscr.addstr(4, 0, "Press any key to return...", curses.A_REVERSE)
            stdscr.refresh()
            stdscr.getch()
            return
        
        for i, s in enumerate(self.students, 1):
            stdscr.addstr(i + 1, 0, f"{i}. {s.show()}")
        
        stdscr.addstr(len(self.students) + 3, 0, "Press any key to return...", curses.A_REVERSE)
        stdscr.refresh()
        stdscr.getch()

    def input_courses(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "=== INPUT COURSES ===", curses.A_BOLD)
        stdscr.refresh()
        
        n = self.input_number(stdscr, "Number of courses:", 2, 0)
        
        for i in range(n):
            stdscr.clear()
            stdscr.addstr(0, 0, f"=== COURSE {i+1}/{n} ===", curses.A_BOLD)
            
            stdscr.addstr(2, 0, "ID: ")
            stdscr.refresh()
            curses.echo()
            cid = stdscr.getstr(2, 4, 20).decode('utf-8').strip()
            
            stdscr.addstr(3, 0, "Name: ")
            stdscr.refresh()
            name = stdscr.getstr(3, 6, 30).decode('utf-8').strip()
            
            stdscr.addstr(4, 0, "Credits: ")
            stdscr.refresh()
            credits = int(stdscr.getstr(4, 9, 5).decode('utf-8').strip())
            curses.noecho()
            
            self.courses.append(Course(cid, name, credits))
        
        stdscr.addstr(6, 0, "Courses added successfully! Press any key...", curses.A_REVERSE)
        stdscr.refresh()
        stdscr.getch()

    def list_courses(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "=== COURSES LIST ===", curses.A_BOLD)
        
        if not self.courses:
            stdscr.addstr(2, 0, "No courses yet.", curses.A_DIM)
            stdscr.addstr(4, 0, "Press any key to return...", curses.A_REVERSE)
            stdscr.refresh()
            stdscr.getch()
            return
        
        for i, c in enumerate(self.courses, 1):
            stdscr.addstr(i + 1, 0, f"{i}. {c.show()}")
        
        stdscr.addstr(len(self.courses) + 3, 0, "Press any key to return...", curses.A_REVERSE)
        stdscr.refresh()
        stdscr.getch()

    def input_marks(self, stdscr):
        if not self.courses:
            stdscr.clear()
            stdscr.addstr(0, 0, "No courses yet.", curses.A_DIM)
            stdscr.addstr(2, 0, "Press any key...", curses.A_REVERSE)
            stdscr.refresh()
            stdscr.getch()
            return
        
        if not self.students:
            stdscr.clear()
            stdscr.addstr(0, 0, "No students yet.", curses.A_DIM)
            stdscr.addstr(2, 0, "Press any key...", curses.A_REVERSE)
            stdscr.refresh()
            stdscr.getch()
            return

        stdscr.clear()
        stdscr.addstr(0, 0, "=== INPUT MARKS ===", curses.A_BOLD)
        stdscr.addstr(2, 0, "Available courses:")
        
        for i, c in enumerate(self.courses, 1):
            stdscr.addstr(i + 2, 0, f"{i}. {c.name} ({c.id})")

        ch = self.input_number(stdscr, "Course number:", len(self.courses) + 4, 0)
        
        if ch < 1 or ch > len(self.courses):
            stdscr.addstr(len(self.courses) + 6, 0, "Invalid choice!", curses.A_REVERSE)
            stdscr.refresh()
            stdscr.getch()
            return

        course = self.courses[ch - 1]

        if course.id not in self.marks:
            self.marks[course.id] = {}

        stdscr.clear()
        stdscr.addstr(0, 0, f"=== MARKS FOR {course.name} ===", curses.A_BOLD)
        
        for i, s in enumerate(self.students):
            while True:
                try:
                    stdscr.addstr(i + 2, 0, f"Mark for {s.name} ({s.id}): " + " " * 20)
                    stdscr.refresh()
                    curses.echo()
                    m = float(stdscr.getstr(i + 2, len(f"Mark for {s.name} ({s.id}): "), 10).decode('utf-8'))
                    curses.noecho()
                    
                    if 0 <= m <= 100:

                        m_rounded = math.floor(m * 10) / 10
                        self.marks[course.id][s.id] = m_rounded
                        stdscr.addstr(i + 2, 50, f"Saved: {m_rounded}", curses.A_DIM)
                        break
                    stdscr.addstr(i + 3, 0, "Mark between 0 and 100!", curses.A_REVERSE)
                    stdscr.refresh()
                    stdscr.getch()
                except:
                    curses.noecho()
                    stdscr.addstr(i + 3, 0, "Error. Number please!", curses.A_REVERSE)
                    stdscr.refresh()
                    stdscr.getch()
        
        stdscr.addstr(len(self.students) + 4, 0, "Marks saved! Press any key...", curses.A_REVERSE)
        stdscr.refresh()
        stdscr.getch()

    def show_marks(self, stdscr):
        if not self.courses:
            stdscr.clear()
            stdscr.addstr(0, 0, "No courses yet.", curses.A_DIM)
            stdscr.addstr(2, 0, "Press any key...", curses.A_REVERSE)
            stdscr.refresh()
            stdscr.getch()
            return

        stdscr.clear()
        stdscr.addstr(0, 0, "=== SHOW MARKS ===", curses.A_BOLD)
        stdscr.addstr(2, 0, "Available courses:")
        
        for i, c in enumerate(self.courses, 1):
            stdscr.addstr(i + 2, 0, f"{i}. {c.name} ({c.id})")

        ch = self.input_number(stdscr, "Course number:", len(self.courses) + 4, 0)
        
        if ch < 1 or ch > len(self.courses):
            return

        course = self.courses[ch - 1]

        stdscr.clear()
        stdscr.addstr(0, 0, f"=== MARKS FOR {course.name} ===", curses.A_BOLD)
        
        if course.id not in self.marks:
            stdscr.addstr(2, 0, "No marks for this course.", curses.A_DIM)
            stdscr.addstr(4, 0, "Press any key...", curses.A_REVERSE)
            stdscr.refresh()
            stdscr.getch()
            return

        for i, s in enumerate(self.students):
            mark = self.marks[course.id].get(s.id, "N/A")
            stdscr.addstr(i + 2, 0, f"{s.name} ({s.id}): {mark}")
        
        stdscr.addstr(len(self.students) + 4, 0, "Press any key...", curses.A_REVERSE)
        stdscr.refresh()
        stdscr.getch()

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

    def show_student_gpa(self, stdscr):
        if not self.students:
            stdscr.clear()
            stdscr.addstr(0, 0, "No students yet.", curses.A_DIM)
            stdscr.addstr(2, 0, "Press any key...", curses.A_REVERSE)
            stdscr.refresh()
            stdscr.getch()
            return

        stdscr.clear()
        stdscr.addstr(0, 0, "=== STUDENT GPA ===", curses.A_BOLD)
        stdscr.addstr(2, 0, "Select student:")
        
        for i, s in enumerate(self.students, 1):
            stdscr.addstr(i + 2, 0, f"{i}. {s.name} ({s.id})")

        ch = self.input_number(stdscr, "Student number:", len(self.students) + 4, 0)
        
        if ch < 1 or ch > len(self.students):
            return

        student = self.students[ch - 1]
        gpa = self.calculate_gpa(student.id)

        stdscr.clear()
        stdscr.addstr(0, 0, f"=== GPA FOR {student.name} ===", curses.A_BOLD)
        stdscr.addstr(2, 0, f"Student: {student.name} ({student.id})")
        stdscr.addstr(3, 0, f"GPA: {gpa:.1f}", curses.A_REVERSE)
        stdscr.addstr(5, 0, "Press any key...", curses.A_REVERSE)
        stdscr.refresh()
        stdscr.getch()

    def sort_students_by_gpa(self, stdscr):
        if not self.students:
            stdscr.clear()
            stdscr.addstr(0, 0, "No students yet.", curses.A_DIM)
            stdscr.addstr(2, 0, "Press any key...", curses.A_REVERSE)
            stdscr.refresh()
            stdscr.getch()
            return

        student_gpas = [(s, self.calculate_gpa(s.id)) for s in self.students]
        
        student_gpas.sort(key=lambda x: x[1], reverse=True)

        stdscr.clear()
        stdscr.addstr(0, 0, "=== STUDENTS SORTED BY GPA (DESCENDING) ===", curses.A_BOLD)
        
        for i, (student, gpa) in enumerate(student_gpas, 1):
            stdscr.addstr(i + 1, 0, f"{i}. {student.name} ({student.id}) - GPA: {gpa:.1f}")
        
        stdscr.addstr(len(student_gpas) + 3, 0, "Press any key...", curses.A_REVERSE)
        stdscr.refresh()
        stdscr.getch()


def main_menu(stdscr, school):
    curses.curs_set(0)  
    stdscr.nodelay(0)
    
    menu_items = [
        "1. Input Students",
        "2. Input Courses",
        "3. Input Marks",
        "4. Students List",
        "5. Courses List",
        "6. Show marks for course",
        "7. Calculate Student GPA",
        "8. Sort Students by GPA",
        "9. Exit"
    ]
    
    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        
        title = "STUDENT MANAGEMENT SYSTEM"
        stdscr.addstr(1, (w - len(title)) // 2, title, curses.A_BOLD | curses.A_UNDERLINE)
        
        for i, item in enumerate(menu_items):
            stdscr.addstr(i + 4, (w - len(item)) // 2, item)
        
        stdscr.addstr(len(menu_items) + 5, (w - 20) // 2, "Choose an option: ", curses.A_REVERSE)
        stdscr.refresh()
        
        curses.echo()
        choice = stdscr.getstr(len(menu_items) + 5, (w - 20) // 2 + 18, 2).decode('utf-8').strip()
        curses.noecho()

        if choice == "1":
            school.input_students(stdscr)
        elif choice == "2":
            school.input_courses(stdscr)
        elif choice == "3":
            school.input_marks(stdscr)
        elif choice == "4":
            school.list_students(stdscr)
        elif choice == "5":
            school.list_courses(stdscr)
        elif choice == "6":
            school.show_marks(stdscr)
        elif choice == "7":
            school.show_student_gpa(stdscr)
        elif choice == "8":
            school.sort_students_by_gpa(stdscr)
        elif choice == "9":
            stdscr.clear()
            stdscr.addstr(h // 2, (w - 10) // 2, "Goodbye!", curses.A_BOLD)
            stdscr.refresh()
            curses.napms(1000)
            break
        else:
            stdscr.addstr(len(menu_items) + 6, (w - 30) // 2, "Invalid option! Press any key...", curses.A_REVERSE)
            stdscr.refresh()
            stdscr.getch()


def main(stdscr):
    school = School()
    main_menu(stdscr, school)


if __name__ == "__main__":
    wrapper(main)
