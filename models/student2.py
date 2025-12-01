from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .project2 import Project2

class Student2:
    def __init__(self, code:str, prefList:list[Project2], grade:int):
        self.code: str = code
        # preference in order of priority given by data.txt
        self.prefList: list[Project2] = prefList 
        self.project: Project2 = None
        self.grade: int = grade
      
    def projectPreference(self, currProject: Project2):
        for i, project in enumerate(self.prefList):
            if currProject.code == project.code:
                return i
