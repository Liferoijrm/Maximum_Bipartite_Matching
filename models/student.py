from project import Project

class Student:
    def __init__(self, code:str, prefList:list[tuple[str,bool,int]], edges:list[Project], grade:int):
        self.code: str = code
        # order of priority: (has proposed) (priority) min first
        self.prefList: list[tuple[str,bool,int]] = prefList 
        self.edges: list[Project] = edges
        self.grade: int = grade