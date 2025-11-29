from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .project import Project

class Student:
    def __init__(self, code:str, prefList:list[Project], grade:int):
        self.code: str = code
        # preference in order of priority given by data.txt
        self.prefList: list[Project] = prefList 
        self.proposals: list[Project] = []
        self.project: Project = None
        self.grade: int = grade

    def didNotProposeToAll(self):
        return len(self.prefList) > len(self.proposals)
    
    def preferredProjectToBeProposed(self):
        proposed_codes = {p.code for p in self.proposals}   
        for project in self.prefList:
            if project.code not in proposed_codes:
                return project

            
            
    def projectPreference(self, currProject: Project):
        for i, project in enumerate(self.prefList):
            if currProject.code == project.code:
                return i
