In this milestone we will implement an object oriented interface for managing student and university data using python.

The program will read student and course data from CSV files and create the necessary objects
All classes and methods need docstring with author's name
All invalid lookups must be rejected. All duplicate enteries must be DRYed.
~Validate letter grades before using or storing(what does this mean?)


There will be a class "Course(University)":

  it will include object variables: 
  
    "course_code" ex: CSE2050
    
    "credits" ex: 4
    
    "students" list of student objects in course
    
  it will include methods: 
  
    "add_student(self, student)" which adds a student to the class roster
    "get_student_count(self)" returns the number of students in the class
    
  it must:
  
    When a student is added to a course it should be reflected in the student and course objects. The course class is responsible for maintaining this relationship
    
  it may:
  
    be nice to format object output with __str__

There will be a class "Student(University)":

  it will include object variables:
  
    "student_id" of type string
    
    "name" the student's name
    
    "courses" a dictionary of all the courses the student takes where the key is the course object and the value(str) is the grade in that course
    
  it will include methods:
  
    "enroll(self, course, grade)" that enrolls the student in a course. This should call the add_student() method from the course class which in turn edits the student object. This is to allow that method to be callable from outside of this method yet still update changes globally. ie: this method should NOT edit the Student object by itself other than the grade in the course which was not provided as a parameter for the add_student method above
    
    "update-grade(course, grade)" modifies grade of student object
    
    "calculate_gpa(self)" grade = [A=4.0, A-=3.7, B+=3.3, B=3.0, C=2.0, D=1.0, F=0] this number gets multiplied by credits in that course. This number gets added for all courses and then is divided by the number of credits. ex: points += (grade * credits) for grade, credits in courses_taking; gpa = points/sum(credits). Division by zero must be prevented
    
    "get_courses(self)" which returns a list of course objects
    
    "get_course_info(self)" returns a summary of all courses and information such as course code, grade, and credits

There will be a class "University":
"""likely a superclass that stores all students and courses and allows for queries"""

  it will include object variables:
  
    "students" dictionary of student_id s as keys and student objects as values
    
    "courses" dictionary of course codes as keys and course objects as values

  it will include methods:
  
    "add_course(self, course_code, credits)" iff course does not exist create it and return new course object
    
    "add_student(self, student_id, name)" iff student does not exist create it and return new student object
    
    "get_student(self, student_id)" returns student object (may want to use students dict)

    "get_course(self, course_code)" returns course object for given course code

    "get_course_enrollment(self, course_code)" returns the number of students enrolled in given course

    "get_students_in_course(self, course_code)" returns list of student objects enrolled in given course
    
Required test cases include:

  Course Class: 
  
    • Test object creation for course class 
    
    • Test adding student objects to the course roster 
    
    • Test that code prevents duplicate object entries in student roster 
    
    • Test student count 
    
  Student Class: 
  
    • Test object creation for student class 
    
    • Test enrolling to course 
    
    • Test GPA calculation 
    
    • Test getting student courses 
    
  University Class: 
  
    • Test object creation for university class 
    
    • Test adding a course to university object 
    
    • Test duplicate course objects 
    
    • Test adding a student 
    
    • Test adding duplicate student 
    
    • Test getting student info 
    
    • Test getting non-existent student info 
    
    • Test getting course 
    
    • Test getting non-existent course
    

Submission must include:

  Python source file(s)
  
  Python test file
  
  Readme file(NOT THIS ONE!) on how to run the program and the tests
  

  
    
    
