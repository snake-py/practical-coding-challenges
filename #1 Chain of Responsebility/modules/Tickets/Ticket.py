from datetime import datetime
from enum import Enum
from uuid import uuid4

class TicketStatus(Enum):
    OPEN = 1
    IN_PROGRESS = 2
    CLOSED = 3

class Ticket:
    def __init__(self, title: str, description: str, target_difficulty: int = 1):
        if target_difficulty < 1 or target_difficulty > 3:
            raise ValueError('Difficulty must be between 1 and 3')
        self.id = uuid4()
        self.title = title
        self.description = description
        self.difficulty = 1 # 1 = easy, 2 = medium, 3 = hard
        self.target_difficulty = target_difficulty # back office employee difficulty 
        self.status = TicketStatus.OPEN
        self.history = []
        self.current_employee = None
        self.start_time = None
        self.end_time = None

    def __str__(self):
        return f'{self.title} - {self.status} - {self.target_difficulty}'

    def to_dict(self, include_history=False):
        dic = {
            'id': str(self.id),
            'title': self.title,
            'description': self.description,
            'difficulty': self.difficulty,
            'target_difficulty': self.target_difficulty,
            'status': self.status,
            'start_time': str(self.start_time),
            'end_time': str(self.end_time),
        }
        if include_history:
            dic['history'] = self.history
        return dic


    def start(self, employee):
        self.current_employee = employee
        self.history.append(f'{employee.name} - with {employee.id} started working on {self.title}')
        self.start_time = datetime.now()
        self.status = TicketStatus.IN_PROGRESS.value

    def close(self, employee):
        self.end_time = datetime.now()
        self.history.append(f'{employee.name} - with {employee.id} closed {self.title}')
        self.status = TicketStatus.CLOSED.value

    def escalate(self):
        if self.difficulty == 3:
            raise ValueError('Ticket is already escalated')
        self.difficulty += 1
        print(f'Escalated {self.title} - {self.id} to difficulty {self.difficulty}')
