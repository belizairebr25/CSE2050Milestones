import unittest
from university import *

class TestUniversity(unittest.TestCase):

   """Tests the university class for object creation, adding courses,
       duplicate course management, adding a student, duplicate student
       management, get student info, get nonexistent student info,
       get course, get nonexistent course"""
    
   def setUp(self):
      #define object data
      #course objects referenced by code
      self.test_course = ("CSE2301", 4)
      self.fake_course = ("FAK998", 8)
      self.course_object_return_format = f"Course Code: {self.test_course[0]}, credits: {self.test_course[1]}"
      #Student objects referenced by ID
      self.test_student = ("STU999", "Jimbob Laplant")
      self.fake_student = ("STU998", "Fruadathan McFakery")
      self.student_object_return_format = f"name: {self.test_student[1]}, id: {self.test_student[0]}"
      
      #create objects
      self.UCONN = University()
      #unpack test_course tuple to use as parameters
      self.UCONN.add_course(*self.test_course)
      #unpack test_student tuple to use as parameters
      self.UCONN.add_student(*self.test_student)

   def test_object_creation(self):   
      """test if university object created. The university constructor has no parameters"""
      #checks to see if the object uconn returns it's name. This should be handled with something like an __str__ method
      self.assertEqual(self.UCONN, "UCONN")

   def test_course_creation(self):
      """tests to see if courses can be added to object. Method add_course has parameters: self, course_code, credits """
      #assert course object created by name 
      self.assertIsInstance(self.test_course[0], Course)

   def test_duplicate_course_management(self):
      """test if duplicate course additions are rejected"""
      #assert creating another test_object of the course class raises a ValueError; implementation may include checking "in" courses dict
      with self.assertRaises(ValueError):
         self.uconn.add_course(*self.test_course)

   def test_student_creation(self):
      """test to se if students can be added to university object. Method add_student has parameters: self, student_id, name"""
      #assert student object created by name
      self.assertIsInstance(self.test_student[1], Student)

   def test_duplicate_student_management(self):
      """test if duplicate course additions are rejected"""
      #assert creating another test_object of the student class raises a ValueError; implementation may include checking "in" students dict
      with self.assertRaises(ValueError):
         self.UCONN.add_student(*self.test_student)

   def test_get_student(self):
      """tests get_student method which should return (formatted with __str__ ?) student object"""
      #assert get_student method returns (properly formatted?) student object
      self.assertEqual(self.UCONN.get_student(self.test_student[0]), self.student_object_return_format)
   
   def test_get_fake_student(self):
      """test if getting a fake student with get_student raises a value error"""
      #assert get_student method raises value error with erroneous input
      with self.assertRaises(ValueError):
         self.UCONN.get_student(self.fake_student[0])

   def test_get_course(self):
      """tests get_course method which should return (formatted with __str__ ?) course object"""
      #assert get_course method returns (properly formatted?) course object
      self.assertEqual(self.UCONN.get_course(self.test_course[0]), self.course_object_return_format)
   
   def test_get_fake_course(self):
      """test if getting a fake course with get_course raises a value error"""
      #assert get_course method raises value error with erroneous input
      with self.assertRaises(ValueError):
         self.UCONN.get_course(self.fake_course[0])

#TO DO:
"""test/verify university class tests"""
"""implement course class tests"""
"""implement student class tests"""
