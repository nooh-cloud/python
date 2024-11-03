
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.enrollments = []

class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id

class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student '{student.name}' added successfully.")

    def add_course(self, course):
        self.courses.append(course)
        print(f"Course '{course.course_name}' added successfully.")

    def enroll_student(self, student_id, course_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        course = next((c for c in self.courses if c.course_id == course_id), None)
        
        if student and course:
            enrollment = Enrollment(student, course)
            student.enrollments.append(enrollment)
            print(f"Student '{student.name}' enrolled in course '{course.course_name}'.")
        else:
            print("Enrollment failed. Student or course ID may be invalid.")

    def display_student_info(self, student_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            print(f"Student Name: {student.name}")
            print("Enrolled Courses:")
            for enrollment in student.enrollments:
                print(f"  - {enrollment.course.course_name}")
        else:
            print("Student not found.")

    def menu(self):
        while True:
            print("\nStudent Management Menu")
            print("1. Add a new student")
            print("2. Add a new course")
            print("3. Enroll a student in a course")
            print("4. Display student information")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                name = input("Enter student name: ")
                student_id = input("Enter student ID: ")
                self.add_student(Student(name, student_id))
            elif choice == '2':
                course_name = input("Enter course name: ")
                course_id = input("Enter course ID: ")
                self.add_course(Course(course_name, course_id))
            elif choice == '3':
                student_id = input("Enter student ID: ")
                course_id = input("Enter course ID: ")
                self.enroll_student(student_id, course_id)
            elif choice == '4':
                student_id = input("Enter student ID: ")
                self.display_student_info(student_id)
            elif choice == '5':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

sms = StudentManagementSystem()
sms.menu()
