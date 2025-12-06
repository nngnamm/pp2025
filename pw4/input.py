import curses


def input_number(stdscr, msg, y, x):
    """Get a positive integer from user"""
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


def input_students(stdscr, school):
    """Input multiple students"""
    from domains.student import Student
    
    stdscr.clear()
    stdscr.addstr(0, 0, "=== INPUT STUDENTS ===", curses.A_BOLD)
    stdscr.refresh()
    
    n = input_number(stdscr, "Number of students:", 2, 0)
    
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
        
        school.students.append(Student(sid, name, dob))
    
    stdscr.addstr(6, 0, "Students added successfully! Press any key...", curses.A_REVERSE)
    stdscr.refresh()
    stdscr.getch()


def input_courses(stdscr, school):
    """Input multiple courses"""
    from domains.course import Course
    
    stdscr.clear()
    stdscr.addstr(0, 0, "=== INPUT COURSES ===", curses.A_BOLD)
    stdscr.refresh()
    
    n = input_number(stdscr, "Number of courses:", 2, 0)
    
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
        
        school.courses.append(Course(cid, name, credits))
    
    stdscr.addstr(6, 0, "Courses added successfully! Press any key...", curses.A_REVERSE)
    stdscr.refresh()
    stdscr.getch()


def input_marks(stdscr, school):
    """Input marks for a selected course"""
    import math
    
    if not school.courses:
        stdscr.clear()
        stdscr.addstr(0, 0, "No courses yet.", curses.A_DIM)
        stdscr.addstr(2, 0, "Press any key...", curses.A_REVERSE)
        stdscr.refresh()
        stdscr.getch()
        return
    
    if not school.students:
        stdscr.clear()
        stdscr.addstr(0, 0, "No students yet.", curses.A_DIM)
        stdscr.addstr(2, 0, "Press any key...", curses.A_REVERSE)
        stdscr.refresh()
        stdscr.getch()
        return

    stdscr.clear()
    stdscr.addstr(0, 0, "=== INPUT MARKS ===", curses.A_BOLD)
    stdscr.addstr(2, 0, "Available courses:")
    
    for i, c in enumerate(school.courses, 1):
        stdscr.addstr(i + 2, 0, f"{i}. {c.name} ({c.id})")

    ch = input_number(stdscr, "Course number:", len(school.courses) + 4, 0)
    
    if ch < 1 or ch > len(school.courses):
        stdscr.addstr(len(school.courses) + 6, 0, "Invalid choice!", curses.A_REVERSE)
        stdscr.refresh()
        stdscr.getch()
        return

    course = school.courses[ch - 1]

    if course.id not in school.marks:
        school.marks[course.id] = {}

    stdscr.clear()
    stdscr.addstr(0, 0, f"=== MARKS FOR {course.name} ===", curses.A_BOLD)
    
    for i, s in enumerate(school.students):
        while True:
            try:
                stdscr.addstr(i + 2, 0, f"Mark for {s.name} ({s.id}): " + " " * 20)
                stdscr.refresh()
                curses.echo()
                m = float(stdscr.getstr(i + 2, len(f"Mark for {s.name} ({s.id}): "), 10).decode('utf-8'))
                curses.noecho()
                
                if 0 <= m <= 100:
                    m_rounded = math.floor(m * 10) / 10
                    school.marks[course.id][s.id] = m_rounded
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
    
    stdscr.addstr(len(school.students) + 4, 0, "Marks saved! Press any key...", curses.A_REVERSE)
    stdscr.refresh()
    stdscr.getch()
