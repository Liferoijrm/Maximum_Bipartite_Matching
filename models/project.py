from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .student import Student

class Project:
    def __init__(self, code:str, vacancies:int, minGrade:int):
        self.code: str = code
        self.vacancies: int = vacancies
        self.minGrade: int = minGrade
        # order of priority: (student grades) max first
        self.students: list[Student] = []

    def hasVacancies(self):
        return self.vacancies > len(self.students)
    
    def studentToBeMogged(self):
        moggedStudent: Student = self.students[0]
        for student in self.students:
            if student.grade < moggedStudent.grade:
                moggedStudent = student
            elif student.grade == moggedStudent.grade and student.projectPreference(self) > moggedStudent.projectPreference(self):
                moggedStudent = student
        
        return moggedStudent

    