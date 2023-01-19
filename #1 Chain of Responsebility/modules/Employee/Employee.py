from time import sleep
from uuid import uuid4
from modules.Tickets.Ticket import Ticket

class Employee:
    def __init__(self, name: str, salary: float, position: str, experience: int = 1):
        self.id = uuid4()
        self.name = name
        self.experience  = experience # 1 to 10
        self.salary = salary
        self.position = position
        self.is_free = True

    def calculate_sleep_time(self, ticket: Ticket) -> int:
        base_time = 1
        return base_time * ticket.target_difficulty / self.experience

    def assign_case(self, ticket: Ticket, callback):
        self.is_free = False
        result = self.handle_ticket(ticket)
        callback(result, self, ticket)

    def handle_ticket(self, ticket: Ticket):
        ticket.start(self)
        if not self.can_handle_task(ticket.difficulty):
            self.is_free = True
            return False
        sleep(self.calculate_sleep_time(ticket))
        if self.can_handle_task(ticket.target_difficulty):
            ticket.close(self)
            self.is_free = True
            return True
        else:
            ticket.escalate()
            self.is_free = True
            return False

    def can_handle_task(self, difficulty) -> bool:
        if difficulty in self.handle_difficulty:
            return True
        return False
        



