import curses
from input import input_number


def list_students(stdscr, school):
    """Display all students"""
    stdscr.clear()
    stdscr.addstr(0, 0, "=== STUDENTS LIST ===", curses.A_BOLD)
    
    if not school.students:
        stdscr.addstr(2, 0, "No students yet.", curses.A_DIM)
        stdscr.addstr(4, 0, "Press any key to return...", curses.A_REVERSE)
        stdscr.refresh()
        stdscr.getch()
        return
    
    for i, s in enumerate(school.students, 1):
        stdscr.addstr(i + 1, 0, f"{i}. {s.show()}")
    
    stdscr.addstr(len(school.students) + 3, 0, "Press any key to return...", curses.A_REVERSE)
    stdscr.refresh()
    stdscr.getch()


def list_courses(stdscr, school):
    """Display all courses"""
    stdscr.clear()
    stdscr.addstr(0, 0, "=== COURSES LIST ===", curses.A_BOLD)
    
    if not school.courses:
        stdscr.addstr(2, 0, "No courses yet.", curses.A_DIM)
        stdscr.addstr(4, 0, "Press any key to return...", curses.A_REVERSE)
        stdscr.refresh()
        stdscr.getch()
        return
    
    for i, c in enumerate(school.courses, 1):
        stdscr.addstr(i + 1, 0, f"{i}. {c.show()}")
    
    stdscr.addstr(len(school.courses) + 3, 0, "Press any key to return...", curses.A_REVERSE)
    stdscr.refresh()
    stdscr.getch()


def show_marks(stdscr, school):
    """Display marks for a selected course"""
    if not school.courses:
        stdscr.clear()
        stdscr.addstr(0, 0, "No courses yet.", curses.A_DIM)
        stdscr.addstr(2, 0, "Press any key...", curses.A_REVERSE)
        stdscr.refresh()
        stdscr.getch()
        return

    stdscr.clear()
    stdscr.addstr(0, 0, "=== SHOW MARKS ===", curses.A_BOLD)
    stdscr.addstr(2, 0, "Available courses:")
    
    for i, c in enumerate(school.courses, 1):
        stdscr.addstr(i + 2, 0, f"{i}. {c.name} ({c.id})")

    ch = input_number(stdscr, "Course number:", len(school.courses) + 4, 0)
    
    if ch < 1 or ch > len(school.courses):
        return

    course = school.courses[ch - 1]

    stdscr.clear()
    stdscr.addstr(0, 0, f"=== MARKS FOR {course.name} ===", curses.A_BOLD)
    
    if course.id not in school.marks:
        stdscr.addstr(2, 0, "No marks for this course.", curses.A_DIM)
        stdscr.addstr(4, 0, "Press any key...", curses.A_REVERSE)
        stdscr.refresh()
        stdscr.getch()
        return

    for i, s in enumerate(school.students):
        mark = school.marks[course.id].get(s.id, "N/A")
        stdscr.addstr(i + 2, 0, f"{s.name} ({s.id}): {mark}")
    
    stdscr.addstr(len(school.students) + 4, 0, "Press any key...", curses.A_REVERSE)
    stdscr.refresh()
    stdscr.getch()


def show_student_gpa(stdscr, school):
    """Display GPA for a selected student"""
    if not school.students:
        stdscr.clear()
        stdscr.addstr(0, 0, "No students yet.", curses.A_DIM)
        stdscr.addstr(2, 0, "Press any key...", curses.A_REVERSE)
        stdscr.refresh()
        stdscr.getch()
        return

    stdscr.clear()
    stdscr.addstr(0, 0, "=== STUDENT GPA ===", curses.A_BOLD)
    stdscr.addstr(2, 0, "Select student:")
    
    for i, s in enumerate(school.students, 1):
        stdscr.addstr(i + 2, 0, f"{i}. {s.name} ({s.id})")

    ch = input_number(stdscr, "Student number:", len(school.students) + 4, 0)
    
    if ch < 1 or ch > len(school.students):
        return

    student = school.students[ch - 1]
    gpa = school.calculate_gpa(student.id)

    stdscr.clear()
    stdscr.addstr(0, 0, f"=== GPA FOR {student.name} ===", curses.A_BOLD)
    stdscr.addstr(2, 0, f"Student: {student.name} ({student.id})")
    stdscr.addstr(3, 0, f"GPA: {gpa:.1f}", curses.A_REVERSE)
    stdscr.addstr(5, 0, "Press any key...", curses.A_REVERSE)
    stdscr.refresh()
    stdscr.getch()


def sort_students_by_gpa(stdscr, school):
    """Display students sorted by GPA in descending order"""
    if not school.students:
        stdscr.clear()
        stdscr.addstr(0, 0, "No students yet.", curses.A_DIM)
        stdscr.addstr(2, 0, "Press any key...", curses.A_REVERSE)
        stdscr.refresh()
        stdscr.getch()
        return

    student_gpas = [(s, school.calculate_gpa(s.id)) for s in school.students]
    student_gpas.sort(key=lambda x: x[1], reverse=True)

    stdscr.clear()
    stdscr.addstr(0, 0, "=== STUDENTS SORTED BY GPA (DESCENDING) ===", curses.A_BOLD)
    
    for i, (student, gpa) in enumerate(student_gpas, 1):
        stdscr.addstr(i + 1, 0, f"{i}. {student.name} ({student.id}) - GPA: {gpa:.1f}")
    
    stdscr.addstr(len(student_gpas) + 3, 0, "Press any key...", curses.A_REVERSE)
    stdscr.refresh()
    stdscr.getch()


def main_menu(stdscr, school):
    """Display main menu and handle user choices"""
    from input import input_students, input_courses, input_marks
    
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
            input_students(stdscr, school)
        elif choice == "2":
            input_courses(stdscr, school)
        elif choice == "3":
            input_marks(stdscr, school)
        elif choice == "4":
            list_students(stdscr, school)
        elif choice == "5":
            list_courses(stdscr, school)
        elif choice == "6":
            show_marks(stdscr, school)
        elif choice == "7":
            show_student_gpa(stdscr, school)
        elif choice == "8":
            sort_students_by_gpa(stdscr, school)
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
