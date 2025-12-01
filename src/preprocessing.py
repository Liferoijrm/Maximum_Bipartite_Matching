from models.project import Project
from models.student import Student

from models.project2 import Project2
from models.student2 import Student2

def preprocessing(data_path: str):

    raw_project_data, raw_student_data = extractData(data_path)
    project_data, student_data = formatData(raw_project_data, raw_student_data)
    projects, students = instantiateObjectsFromData(project_data, student_data)

    projects2, students2 = instantiateObjectsFromData2(project_data, student_data)

    return projects, students, projects2, students2

def extractData(data_path: str):

    raw_project_data = []
    raw_student_data = []

    state = 0

    with open(data_path, 'r') as data:
        lines = data.readlines()

    for line in lines:
        if line[0] != '(' and state == 1:
            state = 2
        elif line[0] == '(' and state == 2:
            raw_student_data.append(line.strip())
        elif line[0] == '(':
            state = 1
            raw_project_data.append(line.strip())

    return raw_project_data, raw_student_data

def formatData(raw_project_data: list, raw_student_data: list):

    project_data = []
    student_data = []

    for data in raw_project_data:
        data = data.replace("(", "")
        data = data.replace(")", "")
        data = data.replace(" ", "")
        project_data.append(data)
    for data in raw_student_data:
        data = data = data.replace(") (",",")
        data = data = data.replace(":",",")
        data = data.replace("(", "")
        data = data.replace(")", "")
        data = data.replace(" ", "")
        student_data.append(data)
    
    return project_data, student_data
        
def instantiateObjectsFromData(project_data: list, student_data: list):
    projects: list[Project] = []
    students: list[Student] = []
    for data in project_data:
        code, vacancies, minGrade = data.split(",")
        vacancies = int(vacancies)
        minGrade = int(minGrade)
        projects.append(Project(code, vacancies, minGrade))
    for data in student_data:
        code, *StrPrefList, grade = data.split(",")
        grade = int(grade)
        projectPrefList: list[Project] = [] 
        for string in StrPrefList:
            for proj in projects:
                if string == proj.code and proj not in projectPrefList:
                    projectPrefList.append(proj)
                    break
        students.append(Student(code, projectPrefList, grade))
    return projects, students

def instantiateObjectsFromData2(project_data: list, student_data: list):
    projects2: list[Project2] = []
    students2: list[Student2] = []
    for data in project_data:
        code, vacancies, minGrade = data.split(",")
        vacancies = int(vacancies)
        minGrade = int(minGrade)
        projects2.append(Project2(code, vacancies, minGrade))
    for data in student_data:
        code, *StrPrefList, grade = data.split(",")
        grade = int(grade)
        projectPrefList: list[Project2] = [] 
        for string in StrPrefList:
            for proj in projects2:
                if string == proj.code and proj not in projectPrefList:
                    projectPrefList.append(proj)
                    break
        students2.append(Student2(code, projectPrefList, grade))
    for proj in projects2:
        studentPrefList: list[Student2] = [] 
        for student in students2:
            if student.grade >= proj.minGrade:
                studentPrefList.append(student)
        ordered = sorted(studentPrefList, key=lambda s: s.grade, reverse=True)
        proj.prefList = ordered
        
    return projects2, students2