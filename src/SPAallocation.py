# variation on the SPA algorithm to produce the MEM, original algorithm available on (Abraham, Irving & Manlove, 2007)
from models.project import Project
from models.student import Student

def SPAallocation(projects: list[Project], students: list[Student]) -> dict:
    while any(student.project is None and student.didNotProposeToAll() for student in students):
        for student in students:
            if student.project is None and student.didNotProposeToAll():
                proposedProject = student.preferredProjectToBeProposed()
                student.proposals.append(proposedProject)
        
                if  student.grade >= proposedProject.minGrade:
                    if proposedProject.hasVacancies():
                        student.project = proposedProject
                        proposedProject.students.append(student)
                    elif studentMeetsMoggingCriteria(student, proposedProject):
                        moggedStudent = proposedProject.studentToBeMogged()
                        moggedStudent.project = None
                        proposedProject.students.remove(moggedStudent)
                        student.project = proposedProject
                        proposedProject.students.append(student)
                break
                        
def studentMeetsMoggingCriteria(student: Student, proposedProject: Project):
    """Criteria for mogging: 1. have a better grade; 2. if grades are equal, have better project preference (the lower the index, the bigger the preference)"""
    if student.grade > proposedProject.studentToBeMogged().grade:
        return True
    elif student.grade == proposedProject.studentToBeMogged().grade and student.projectPreference(proposedProject) < proposedProject.studentToBeMogged().projectPreference(proposedProject):
        return True
    return False

def calculateProjectPreference(projects: list[Project], students: list[Student]) -> dict:
    # Com base na alocação final, calcular a preferência de cada projeto pelos estudantes alocados
    project_preference = {}
    for project in projects:
        preference_list = []
        for student in students:
            if student.project == project:
                preference_list.append(student)
        # Ordenar a lista de preferência com base na nota dos estudantes (maior nota primeiro)
        preference_list.sort(key=lambda s: s.grade, reverse=True)
        project_preference[project.code] = preference_list
    return project_preference
