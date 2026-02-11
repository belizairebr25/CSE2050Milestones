import csv
from pathlib import Path

COURSE_CATALOG_PATH:Path = Path(__file__).resolve().parent.parent / 'MilestoneMaterials/course_catalog.csv'

UNIV_DATA_PATH:Path = Path(__file__).resolve().parent.parent / 'MilestoneMaterials/university_data.csv'





def get_course_data() -> list[dict]:
    with COURSE_CATALOG_PATH.open('r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        courses:list[dict] = []
        for row in reader:
            course:dict = {
                'course_code': None,
                'credits': None
            }
            for key in row:
                value = row[key]
                course[key] = value
            courses.append(course)

    return courses


def get_student_data() -> list[dict]:
    with UNIV_DATA_PATH.open('r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        students:list[dict] = []

        for row in reader:
            student:dict = {
                'student_id': None,
                'name': None,
                'courses': None
            }
            for key in row:
                value = row[key]
                student[key] = value
            students.append(student)
    return students

