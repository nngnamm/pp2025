class Student:
    def __init__(self, sid, name, dob):
        self.id = sid
        self.name = name
        self.dob = dob

    def show(self):
        print(f"ID: {self.id}, Name: {self.name}, DoB: {self.dob}")


class Course:
    def __init__(self, cid, name):
        self.id = cid
        self.name = name

    def show(self):
        print(f"ID: {self.id}, Name: {self.name}")


class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_number(self, msg):
        while True:
            try:
                n = int(input(msg))
                if n > 0:
                    return n
                print("Positive number pls?")
            except:
                print("Error. Integer pls?")

    def input_students(self):
        n = self.input_number("Number of students pls? ")
        for _ in range(n):
            sid = input("ID: ").strip()
            name = input("Name: ").strip()
            dob = input("DoB (YYYY-MM-DD): ").strip()
            self.students.append(Student(sid, name, dob))

    def list_students(self):
        if not self.students:
            print("No students rn.")
            return
        print("\nStudents:")
        for s in self.students:
            s.show()

    def input_courses(self):
        n = self.input_number("Number of courses pls? ")
        for _ in range(n):
            cid = input("ID: ").strip()
            name = input("Name: ").strip()
            self.courses.append(Course(cid, name))

    def list_courses(self):
        if not self.courses:
            print("No courses rn.")
            return
        print("\nCourses:")
        for c in self.courses:
            c.show()

    def input_marks(self):
        if not self.courses:
            print("No courses rn.")
            return
        if not self.students:
            print("No students rn.")
            return

        print("Available courses:")
        for i, c in enumerate(self.courses, 1):
            print(f"{i}. {c.name} ({c.id})")

        while True:
            try:
                ch = int(input("Course number: "))
                if 1 <= ch <= len(self.courses):
                    break
                print("Invalid.")
            except:
                print("Error. Valid number pls.")

        course = self.courses[ch - 1]

        if course.id not in self.marks:
            self.marks[course.id] = {}

        for s in self.students:
            while True:
                try:
                    m = float(input(f"Mark for {s.name} ({s.id}): "))
                    if 0 <= m <= 100:
                        break
                    print("Mark between 0 and 100.")
                except:
                    print("Error. Number pls.")
            self.marks[course.id][s.id] = m

    def show_marks(self):
        if not self.courses:
            print("No courses rn.")
            return

        print("Available courses:")
        for i, c in enumerate(self.courses, 1):
            print(f"{i}. {c.name} ({c.id})")

        while True:
            try:
                ch = int(input("Course number: "))
                if 1 <= ch <= len(self.courses):
                    break
                print("Error.")
            except:
                print("Valid number pls.")

        course = self.courses[ch - 1]

        print(f"\nMarks for {course.name}:")
        if course.id not in self.marks:
            print("No marks for this course.")
            return

        for s in self.students:
            mark = self.marks[course.id].get(s.id, "N/A")
            print(f"{s.name} ({s.id}): {mark}")


def main():
    school = School()

    while True:
        print("\n1. Input Students")
        print("2. Input Courses")
        print("3. Input Marks")
        print("4. Students List")
        print("5. Courses List")
        print("6. Show marks for course")
        print("7. Exit")

        choice = input("Choose pls: ").strip()

        if choice == "1":
            school.input_students()
        elif choice == "2":
            school.input_courses()
        elif choice == "3":
            school.input_marks()
        elif choice == "4":
            school.list_students()
        elif choice == "5":
            school.list_courses()
        elif choice == "6":
            school.show_marks()
        elif choice == "7":
            print("Bye")
            break
        else:
            print("Choose the right option pls.")


if __name__ == "__main__":
    main()
