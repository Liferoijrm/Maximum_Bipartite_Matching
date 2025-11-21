from ..models.project import Project
from ..models.student import Student

def preprocessing(data_path: str):

    raw_project_data, raw_student_data = extractData(data_path)
    project_data, student_data = formatData(raw_project_data, raw_student_data)
    # TODO: colocar os dados formatados com parse() em arrays Student[] e Project[]
    # return students, projects
    

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
        

