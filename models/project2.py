from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .student2 import Student2

class Project2:
    def __init__(self, code:str, vacancies:int, minGrade:int):
        self.code: str = code
        self.vacancies: int = vacancies
        self.minGrade: int = minGrade
        # order of priority: (student grades) max first, already ordered
        self.prefList: list[Student2] = []
        self.students: list[Student2] = []
        self.proposals: list[Student2] = []

    def hasVacancies(self):
        return self.vacancies > len(self.students)
    
    def didNotProposeToAll(self):
        return len(self.prefList) > len(self.proposals)
    
    def preferredStudentToBeProposed(self):
        proposed_codes = {p.code for p in self.proposals}   
        for student in self.prefList:
            if student.code not in proposed_codes:
                return student

    