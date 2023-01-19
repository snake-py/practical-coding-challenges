from datetime import datetime
from enum import Enum
from time import sleep
from typing import Set
from uuid import uuid4
import threading
from random import randrange


class TicketStatus(Enum):
    OPEN = 1
    IN_PROGRESS = 2
    CLOSED = 3

class Ticket:
    def __init__(self, title: str, description: str, target_difficulty: int = 1):
        self.id = uuid4()
        self.title = title
        self.description = description
        self.difficulty = 1 # 1 = easy, 2 = medium, 3 = hard
        self.target_difficulty = target_difficulty
        self.status = TicketStatus.OPEN
        self.history = []
        self.current_employee = None
        self.start_time = None
        self.end_time = None

    def __str__(self):
        return f'{self.title} - {self.status} - {self.target_difficulty}'

    def start(self, employee):
        self.current_employee = employee
        self.history.append(f'{employee.name} - with {employee.id} started working on {self.title}')
        self.start_time = datetime.now()
        self.status = TicketStatus.IN_PROGRESS

    def close(self):
        self.end_time = datetime.now()
        self.status = TicketStatus.CLOSED

    def escalate(self):
        if self.difficulty == 3:
            raise ValueError('Ticket is already escalated')
        self.difficulty += 1


class Employee:
    def __init__(self, name: str, salary: float, position: str, experience: int = 1):
        self.id = uuid4()
        self.name = name
        self.experience  = experience # 1 to 10
        self.salary = salary
        self.position = position
        self.is_busy = False

    def calculate_sleep_time(self, ticket: Ticket) -> int:
        base_time = 1
        return base_time * ticket.target_difficulty / self.experience

    def handle_ticket(self, ticket: Ticket):
        self.is_busy = True
        ticket.start(self)
        if not self.can_handle_task(ticket.difficulty):
            self.is_busy = False
            self.is_busy = False
            return False
        sleep(self.calculate_sleep_time(ticket))
        if self.can_handle_task(ticket.target_difficulty):
            self.is_busy = False
            ticket.close()
            self.is_busy = False
            return True
        else:
            ticket.escalate()
            self.is_busy = False
            return False

    def can_handle_task(self, difficulty) -> bool:
        if isinstance(self, BackOfficeEmployee) and difficulty == 1:
            return True
        elif isinstance(self, AccountManager) and difficulty in (1, 2):
            return True
        elif isinstance(self, Director) and difficulty in (1, 2, 3):
            return True
        return False
        


class BackOfficeEmployee(Employee):
    def __init__(self, name: str, experience: int, salary: float, position: str):
        super().__init__(name, experience, salary, position)

class AccountManager(Employee):
    def __init__(self, name: str, experience: int, salary: float, position: str):
        super().__init__(name, experience, salary, position)

class Director(Employee):
    def __init__(self, name: str, experience: int, salary: float, position: str):
        super().__init__(name, experience, salary, position)



class TicketSystem: 

    def __init__(self, employees: Set[Employee]):
        self.tickets = []
        self.employees = set(employees)
        self.active_employee = set()
        
    
    def start_worker(self):
        for employee in self.employees:
            employee_thread = threading.Thread(target=self.working, args=(employee,))
            employee_thread.start()
            self.active_employee.add(employee_thread)

    def working(self, employee: Employee):
        try:
            while True:
                if len(self.tickets) == 0:
                    print(f'{employee.name} - with {employee.id} is waiting for tickets')
                    sleep(2)
                    continue
                ticket = self.tickets.pop(0)
                is_done = employee.handle_ticket(ticket)
                if is_done:
                    print(f'{employee.name} - with {employee.id} closed {ticket.title}')
                else:
                    self.tickets.append(ticket)
                    print(f'{employee.name} - with {employee.id} escalated {ticket.title} with target_difficulty {ticket.target_difficulty}')
        except KeyboardInterrupt:
            self.close_working_day()

    def close_working_day(self):
        print('Closing working day')
        for employee in self.active_employee:
            employee.join()

    def add_ticket(self, ticket: Ticket):
        self.tickets.append(ticket)




def add_dummy_tickets(ticketSystem, n):
    for i in range(n):
        ticket = Ticket(f'Ticket {i}', f'Description {i}', randrange(1, 3))
        ticketSystem.add_ticket(ticket)
        

if __name__ == '__main__':
    employees = set()
    for n in range(3):
        emp = BackOfficeEmployee(f'BackOfficeEmployee {n}', 1000, 'BackOfficeEmployee', 1)
        employees.add(emp)
    for n in range(2):
        emp = AccountManager(f'AccountManager {n}', 1000, 'AccountManager', 1)
        employees.add(emp)
    for n in range(1):
        emp = Director(f'Director {n}', 1000, 'Director', 1)
        employees.add(emp)

    ticketSystem = TicketSystem(employees)
    threading.Thread(target=add_dummy_tickets, args=(ticketSystem, 20)).start()
    ticketSystem.start_worker()
    
    
    

