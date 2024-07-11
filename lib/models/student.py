from __init__ import CONN, CURSOR

class Student:

    def __init__(self, name, grade, student_id, teacher_name):
        self.name = name
        self.grade = grade
        self.student_id = student_id
        self.teacher_name = teacher_name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a string and be longer than 0 characters.")
        
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, grade):
        if isinstance(grade, int):
            self._grade = grade
        else:
            raise ValueError("Grade must be an integer.")
    
    @property
    def teacher_name(self):
        return self._teacher_name

    @teacher_name.setter
    def teacher_name(self, teacher_name):
        if isinstance(teacher_name, str) and len(teacher_name) > 0:
            self._teacher_name = teacher_name
        else:
            raise ValueError("Teacher name must be a string and be longer than 0 characters.")
        
    @property
    def student_id(self):
        return self._student_id
        
    @student_id.setter
    def student_id(self, student_id):
        if isinstance(student_id, int) and student_id > 0:
            self._student_id = student_id
        else:
            raise ValueError("Student ID must be an integer and greater than 0")

    def save(self):
        sql = """ INSERT INTO students (name, grade, student_id, teacher_name) VALUES (?,?,?,?)"""
        CURSOR.execute(sql, (self.name, self.grade, self.student_id, self.teacher_name))
        CONN.commit()
        self.student_id = CURSOR.lastrowid
    
    @classmethod
    def create_table(cls):
        sql = """ CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        grade INTEGER,
        student_id INTEGER,
        teacher_name TEXT
        );"""
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def all(cls):
        sql = """SELECT * FROM students;"""
        data = CURSOR.execute(sql).fetchall()
        return [cls.instantiate_from_db(row) for row in data if row]
    
    @classmethod
    def instantiate_from_db(cls, row):
        if len(row) < 5:
            raise ValueError("Row does not contain enough values to instantiate a Student.")
        return cls(
            name=row[1], 
            grade=row[2], 
            student_id=row[3], 
            teacher_name=row[4]
        )
    
    @classmethod
    def create(cls, name, grade, student_id, teacher_name):
        student = cls(name=name, grade=grade, student_id=student_id, teacher_name=teacher_name)
        student.save()
        return student
    
    @classmethod
    def find_by_id(cls, student_id):
        sql = """ SELECT * FROM students WHERE student_id = ?; """
        row = CURSOR.execute(sql, (student_id,)).fetchone()
        if row:
            return cls.instantiate_from_db(row)
        return None
    
    @classmethod
    def delete(cls, student_id):
        sql = """ DELETE FROM students WHERE student_id = ?; """
        CURSOR.execute(sql, (student_id,))
        CONN.commit()

    @classmethod
    def find_by_teacher(cls, teacher_name):
        sql = """ SELECT * FROM students WHERE teacher_name = ?; """
        rows = CURSOR.execute(sql, (teacher_name,)).fetchall()
        if rows:
            return [cls.instantiate_from_db(row) for row in rows]
        return []
    
    def __repr__(self):
        return f'<Student id={self.student_id} name={self.name} grade={self.grade} student_id={self.student_id} teacher_name={self.teacher_name}>'