from reader import get_course_data, get_student_data

class Course:
    def __init__(self, course_code:str, credits:int):
        self.course_code = course_code
        self.credits = credits
        self.students:list['Student'] = []

    def add_student(self, student: 'Student'):
        self.students.append(student)

    def get_student_count(self) -> int:
        return len(self.students)


class Student:
    def __init__(self, student_id:str, name:str, courses:list[dict]):
        self.student_id = student_id
        self.name = name
        self.courses = courses

    def enroll(self, course:Course, grade:str):
        self.courses.append({
            'course': course,
            'grade': grade
        })

    def update_grade(self, course:Course, new_grade:str):
        for entry in self.courses:
            if entry['course'] == course:
                entry['grade'] = new_grade

    def calculate_gpa(self) -> float:
        grade_points = 0
        all_credits = 0
        for entry in self.courses:
            points = GRADE_POINTS.get(entry['grade'])
            course_credits = entry['course'].credits
            all_credits += course_credits
            grade_points += points * course_credits

        gpa = round(grade_points / all_credits, 2)

        print(gpa)
        return gpa



    def get_courses(self) -> list[Course]:
        course_arr: list[Course] = []
        for entry in self.courses:
            course_arr.append(entry['course'])

        return course_arr

    def get_course_info(self) -> str:
        summary:str = 'Student Courses:\n\n'
        for c in self.courses:
            course = c['course']
            grade = c['grade']
            credits = course.credits

            summary += (f'Code: {course.course_code}\n'
                        f'Grade: {grade}\n'
                        f'Credits: {credits}\n\n')
        return summary


ALL_STUDENTS:list[Student] = []
ALL_COURSES:list[Course] = []

GRADE_POINTS = {
    'A' : 4.0, 'A-' : 3.7,
    'B+': 3.3, 'B' : 3.0, 'B-' : 2.7,
    'C+': 2.3, 'C' : 2.0, 'C-' : 1.7,
    'D' : 1.0,
    'F' : 0.0,
}


course_map:dict[str, Course] = {}
for c in get_course_data():
    code = c.get('course_code')
    credits = int(c.get('credits'))
    course_obj = Course(code, credits)
    ALL_COURSES.append(course_obj)
    course_map[code] = course_obj


def parse_student_course(raw:str, c_map:dict[str, Course], student: Student):
    courses:list[dict] = []

    if not raw:
        return courses

    for course_part in raw.split(';'):
        code_grade = course_part.split(':')
        if len(code_grade) != 2:
            continue

        course_code, course_grade = code_grade[0], code_grade[1]

        obj = c_map.get(course_code)
        if course_obj is None:
            continue


        obj.add_student(student)
        student.enroll(obj, course_grade)
    return None


for s in get_student_data():
    student_id = s.get('student_id')
    student_name = s.get('name')

    student = Student(student_id, student_name, courses=[])
    parse_student_course(s.get('courses'), course_map, student)

    ALL_STUDENTS.append(student)

