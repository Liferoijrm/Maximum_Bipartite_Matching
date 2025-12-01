# Modified SPA so that projects make the proposals
from models.project2 import Project2
from models.student2 import Student2

def SPAallocation2(projects: list[Project2], students: list[Student2]):
    while any(project.hasVacancies() and project.didNotProposeToAll() for project in projects):
        for project in projects:
            if project.hasVacancies() and project.didNotProposeToAll():
                candidate = project.preferredStudentToBeProposed()
                project.proposals.append(candidate)

                if candidate.project is None:
                    candidate.project = project
                    project.students.append(candidate)
                else:
                    current_project = candidate.project
                    if studentPrefersNewProject(candidate, project, current_project):
                        current_project.students.remove(candidate)

                        candidate.project = project
                        project.students.append(candidate)
                break  

def studentPrefersNewProject(student: Student2, newProject: Project2, oldProject: Project2):
    
    new_pref = student.projectPreference(newProject)
    old_pref = student.projectPreference(oldProject)

    if new_pref is None:
        return False
    if old_pref is None:
        return True

    return new_pref < old_pref

