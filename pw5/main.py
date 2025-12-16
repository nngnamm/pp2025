from curses import wrapper
from domains import School
from output import main_menu
from storage import load_data, parse_students, parse_courses, parse_marks, compress_data


def main(stdscr):
    """Main entry point for the application"""
    school = School()
    
    # Load data from students.dat if it exists
    students_data, courses_data, marks_data = load_data()
    
    if students_data is not None:
        school.students = parse_students(students_data)
        school.courses = parse_courses(courses_data)
        school.marks = parse_marks(marks_data)
    
    # Run the main menu
    main_menu(stdscr, school)
    
    # Before exiting, compress all data
    from storage import save_students, save_courses, save_marks
    save_students(school.students)
    save_courses(school.courses)
    save_marks(school.marks)
    compress_data()


if __name__ == "__main__":
    wrapper(main)
