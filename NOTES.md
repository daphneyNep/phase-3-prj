Overview of Project

Classroom lister app. Should be able to list out teachers and their students as well as their teachers.

The application must include a database created and modified with python ORM methods that you write.

-The data model must include at least 2 model classes.
	-teacher, student
-The data model must include at least 1 one-to-many relationship.
	-artist has many songs
	-a student belongs to an teacher (teacher_name foreign key)
-Property methods should be defined to add appropriate constraints to each model class.
	-teacher
		-name (should exist, should be type string)
	    -student
		-name (should exist, should be type string)
		-grade (should exist, should be type string)
		-student id (should exist, should be type string)
