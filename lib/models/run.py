from teacher import Teacher
from student import Student

from cli import Cli

Teacher.create_table()
Student.create_table()

Cli().start()

