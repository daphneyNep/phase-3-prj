from __init__ import CONN, CURSOR
from teacher import Teacher
from student import Student


class Cli:
    def start(self):
        print("Welcome to the classroom Lister App")
        print("")
        self.menu()

    def menu(self):
        print('Please choose from this selection')
        print("-----------------------------------")
        print("Press '1' to list out all of the teachers")
        print("Press '2' to select a teacher")
        print("Press '3' to create a teacher")
        print("Press '4' to delete a teacher")
        print("Press '5' to list out all of the students")
        print("Press '6' to select a student")
        print("Press '7' to create a student")
        print("Press '8' to delete a student")
        print("")
        print("Press '9' to view students by teacher's name")
        print("Press '10' to exit")
        self.selection()
    
    def selection(self):
        user_input = input("Input Here:")
        if user_input == "1":
            self.print_all_teacher_names()
        elif user_input == "2":
            self.select_teacher()
        elif user_input == "3":
            self.create_teacher()
        elif user_input == "4":
            self.delete_teacher()
        elif user_input == "5":
            self.print_all_student_names()
        elif user_input == "6":
            self.select_student()
        elif user_input == "7":
            self.create_student()
        elif user_input == "8":
            self.delete_student()
        elif user_input == "9":
            self.view_students_by_teacher()
        elif user_input == "10":
            print("Exiting the application. Goodbye!")
            exit()
        else:
            print("Invalid selection. Please try again.")
        input("Press Enter to continue...")
        print("")

    def print_all_teacher_names(self):
        try:
            teachers = Teacher.all()
            if teachers:
                for teacher in teachers:
                    self.print_teacher(teacher)
            else:
                print("No teachers found.")
        except ValueError as e:
            print(f"Error: {e}")

    def print_teacher(self, teacher):
        print("")
        print("==========")
        print(f"ID: {teacher.id}")
        print(f"Name: {teacher.name}")
        print("==========")

    def select_teacher(self):
        teacher_name = input("Enter the teacher's NAME: ")
        teacher = Teacher.find_by_name(teacher_name)
        if teacher:
            self.print_teacher(teacher)
        else:
            print("Teacher not found.")

    def create_teacher(self):
        name = input("Enter the teacher's NAME: ")
        if name.strip() == "":
            print("Error: Teacher name cannot be empty.")
            return
        try:
            Teacher.create(name)
            print(f"Teacher {name} created successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def delete_teacher(self):
        teacher_id = input("Enter the teacher's ID to delete: ")
        if not teacher_id.isdigit():
            print("Error: Teacher ID must be a number.")
            return
        
        teacher = Teacher.find_by_id(teacher_id)
        if teacher:
            print(f"Teacher {teacher.name} deleted successfully.")
        else:
            print("Teacher not found.")

    def print_all_student_names(self):
        students = Student.all()
        if students:
            for student in students:
                self.print_student(student)
        else:
            print("No students found.")

    def print_student(self, student):
        print("")
        print("==========")
        print(f"ID: {student.student_id}")
        print(f"Name: {student.name}")
        print(f"Grade: {student.grade}")
        print(f"Teacher: {student.teacher_name}")
        print("==========")

    def select_student(self):
        student_id = input("Enter the student's ID: ")
        if not student_id.isdigit():
            print("Error: Student ID must be a number.")
            return
        
        student = Student.find_by_id(student_id)
        if student:
            self.print_student(student)
        else:
            print("Student not found.")

    def create_student(self):
        name = input("Enter the student's name: ")
        if name.strip() == "":
            print("Error: Student name cannot be empty.")
            return
        
        try:
            grade = int(input("Enter the student's grade: "))
            student_id = int(input("Enter the student's ID: "))
        except ValueError:
            print("Error: Grade and Student ID must be integers.")
            return
        
        teacher_name = input("Enter the teacher's name:")
        Student.create(name, grade, student_id, teacher_name)
        print(f"Student {name} created successfully.")

    def delete_student(self):
        student_id = input("Enter the student's ID to delete: ")
        if not student_id.isdigit():
            print("Error: Student ID must be a number.")
            return
        
        student = Student.find_by_id(student_id)
        if student:
            Student.delete(student_id)
            print(f"Student {student.name} deleted successfully.")
        else:
            print("Student not found.")
    
    def view_students_by_teacher(self):
        teacher_name = input("Enter the teacher's name: ")
        teacher = Teacher.find_by_name(teacher_name)
        if teacher:
            students = Student.find_by_teacher(teacher_name)
            if students:
                for student in students:
                    self.print_student(student)
            else:
                print(f"No students found for teacher {teacher_name}.")
        else:
            print("Teacher not found.")

    def __repr__(self):
        cli = Cli()
        cli().start()

    