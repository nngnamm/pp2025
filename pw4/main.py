from curses import wrapper
from domains import School
from output import main_menu


def main(stdscr):
    """Main entry point for the application"""
    school = School()
    main_menu(stdscr, school)


if __name__ == "__main__":
    wrapper(main)
