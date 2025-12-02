students = []
courses = []
marks = {}


def input_number(number):
    while True:
        try:
            n = int(input(number))
            if n > 0:
                return n
            else:
                print("Positive number pls?")
        except ValueError:
            print("Error. Integer pls?")


def input_students():
    n = input_number("Number of students pls?")
    for _ in range(n):
        student_id = input("ID: ").strip()
        name = input("Name: ").strip()
        dob = input("DoB (YYYY-MM-DD): ").strip()
        students.append((student_id, name, dob))


def input_courses():
    n = input_number("Number of courses pls?")
    for _ in range(n):
        course_id = input("ID: ").strip()
        name = input("Name:").strip()
        courses.append((course_id, name))


def input_marks():
    if not courses:
        print("No courses rn.")
        return
    if not students:
        print("No students rn.")
        return

    print("Available Courses:")
    for i, (cid, cname) in enumerate(courses):
        print(f"{i + 1}. {cname} ({cid})")

    while True:
        try:
            choice = int(input("Course number: "))
            if 1 <= choice <= len(courses):
                break
            else:
                print("Invalid.")
        except ValueError:
            print("Error. Valid number pls.")

    course_id, course_name = courses[choice - 1]
    if course_id not in marks:
        marks[course_id] = {}

    for student_id, name, dob in students:
        while True:
            try:
                mark = float(input(f"Mark for {name} ({student_id}): "))
                if 0 <= mark <= 100:
                    break
                else:
                    print("Mark between 0 and 100.")
            except ValueError:
                print("Error. Number pls.")
        marks[course_id][student_id] = mark


def list_students():
    if not students:
        print("No students rn.")
        return
    print("\nStudents:")
    for student_id, name, dob in students:
        print(f"ID: {student_id}, Name: {name}, DoB: {dob}")


def list_courses():
    if not courses:
        print("No courses rn.")
        return
    print("\nCourses:")
    for course_id, name in courses:
        print(f"ID: {course_id}, Name: {name}")


def show_marks():
    if not courses:
        print("No courses rn.")
        return
    print("Available courses:")
    for i, (cid, cname) in enumerate(courses):
        print(f"{i + 1}. {cname} ({cid})")

    while True:
        try:
            choice = int(input("Course number: "))
            if 1 <= choice <= len(courses):
                break
            else:
                print("Error.")
        except ValueError:
            print("Valid number pls.")

    course_id, course_name = courses[choice - 1]
    print(f"\nMarks for course {course_name}:")
    if course_id in marks:
        for student_id, name, dob in students:
            mark = marks[course_id].get(student_id, "N/A")
            print(f"{name} ({student_id}): {mark}")
    else:
        print("No marks for this course.")


def main():
    while True:
        print("1. Input Students")
        print("2. Input Courses")
        print("3. Input Marks")
        print("4. Students List")
        print("5. Courses List")
        print("6. Show marks for course")
        print("7. Exit")

        choice = input("Choose pls").strip()
        if choice == "1":
            input_students()
        elif choice == "2":
            input_courses()
        elif choice == "3":
            input_marks()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            show_marks()
        elif choice == "7":
            print("Bye")
            break
        else:
            print("Choose the right option pls.")


if __name__ == "__main__":
    main()
