from .Employee import Employee

class Director(Employee):
    def __init__(self, name: str, experience: int, salary: float, position: str):
        self.handle_difficulty = (1, 2, 3)
        super().__init__(name, experience, salary, position)
