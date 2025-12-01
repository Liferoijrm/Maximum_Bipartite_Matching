import os
from models.project import Project
from models.student import Student
from src.preprocessing import preprocessing
from src.SPAallocation import SPAallocation
from src.SPAallocation2 import SPAallocation2

def main():
    # Obtém o diretório do projeto automaticamente
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)  # sobe um nível para project-root
    data_path = os.path.join(project_root, "data", "data.txt")

    projects, students, projects2, students2 = preprocessing(data_path)
    # SPAallocation will generate a maximum matching
    # for every iteration in SPAallocation, display graph information
    SPAallocation(projects, students)
    SPAallocation2(projects2, students2)

    for project in projects:
        student_codes = " ".join(student.code for student in project.students)
        print(f"{project.code}: {student_codes}")

    print("\n============\n")

    for project in projects2:
        student_codes = " ".join(student.code for student in project.students)
        print(f"{project.code}: {student_codes}")


if __name__ == "__main__":
    main()