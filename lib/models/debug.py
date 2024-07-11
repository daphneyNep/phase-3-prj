from __init__ import CONN, CURSOR

from teacher import Teacher
from student import Student

import ipdb

Teacher.create_table()
Student.create_table()

ipdb.set_trace()
