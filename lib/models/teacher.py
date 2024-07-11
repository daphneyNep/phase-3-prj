from __init__ import CONN, CURSOR

class Teacher:

    def __init__(self, name, id=None):
        self.id = id
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must exist and be longer than 0 characters long")
        
    def student(self):
        sql = """ 
        SELECT * FROM students"""
        
        self.id = CURSOR.lastrowid
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS teachers ( 
            id INTEGER PRIMARY KEY,
            name TEXT
            );"""

        CURSOR.execute(sql)
        CONN.commit()
        
    def save(self):
        sql = """
            INSERT INTO teachers (NAME) VALUES (?);"""
        
        CURSOR.execute(sql, (self.name,))
        self.id = CURSOR.lastrownid
        CONN.commit()
    
    @classmethod
    def all(cls):
        sql = """SELECT * FROM teachers;"""

        data = CURSOR.execute(sql).fetchall()
        return [cls.instantiate_from_db(row) for row in data if row]
    
    @classmethod
    def instantiate_from_db(cls, row):
        id, name = row
        if not name or len(name) == 0:
            raise ValueError("Name must exist and be longer than 0 characters long")
        return cls(name, id)
    
    @classmethod
    def create(cls, name):
        sql = """
        INSERT INTO teachers (name) VALUES (?);"""

        CURSOR.execute(sql, (name,))
        CONN.commit()
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
        SELECT * FROM teachers WHERE id = (?);
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        if row:
            return cls.instantiate_from_db(row)
        return None
    
    def delete(cls, teacher_id):
        sql = """DELETE FROM teacher WHERE teacher_id = (?);"""

        CURSOR.execute(sql, (teacher_id,))
        CONN.commit()
    
    @classmethod
    def find_by_name(cls, teacher_name): 
        sql = """ 
            SELECT * FROM teachers WHERE NAME = (?);"""

        row = CURSOR.execute(sql, (teacher_name,)).fetchone()
        if row:
            return cls.instantiate_from_db(row)
        return None
    
    def update(self):
        sql = """
        UPDATE teachers SET name = ? WHERE id = (?);"""

        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()
    
    def __repr__(self):
        return f'<Teacher id={self.id} name={self.name}>'
    