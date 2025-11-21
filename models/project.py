from student import Student

class Project:
    def __init__(self, code:str, minGrade:int, edges:list[Student], vacancies:int):
        self.code: str = code
        self.minGrade: int = minGrade
        # order of priority: (student grades) max first
        self.edges: list[Student] = edges
        self.vacancies: int = vacancies

    