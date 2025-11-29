import os
from models.project import Project
from models.student import Student
from src.preprocessing import preprocessing
from src.SPAallocation import SPAallocation

def main():
    # Obtém o diretório do projeto automaticamente
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)  # sobe um nível para project-root
    data_path = os.path.join(project_root, "data", "data.txt")

    projects, students = preprocessing(data_path)
    # SPAallocation will generate a maximum matching
    # for every iteration in SPAallocation, display graph information
    SPAallocation(projects, students)

    for project in projects:
        student_codes = " ".join(student.code for student in project.students)
        print(f"{project.code}: {student_codes}")


if __name__ == "__main__":
    main()