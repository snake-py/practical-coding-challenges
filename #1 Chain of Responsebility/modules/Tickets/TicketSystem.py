from re import A
from typing import Set
from modules.Employee.Employee import Employee
from .Ticket import Ticket

class TicketSystem: 
    def __init__(self, back_office_employees: Set[Employee], account_managers: Set[Employee], directors: Set[Employee]):
        self.tickets = []
        self.history = []
        self.back_office_employees = back_office_employees
        self.account_managers = account_managers
        self.directors = directors
        print(self.back_office_employees)

    def work(self):
        try:
            while True:
                if len(self.tickets) > 0:
                    ticket = self.tickets.pop(0)
                    self.assign_case(ticket)
        except KeyboardInterrupt:
            print("Keyboard interrupt")
            exit(0)
        
    def dispatch_case(self, ticket: Ticket):
        self.tickets.append(ticket)
        self.history.append(ticket)

    def assign_case(self, ticket: Ticket):
        employee = self.get_employee(ticket)
        if employee is None:
            return
        employee.assign_case(ticket, callback=self.handle_employee_response)

    def get_employee(self, ticket: Ticket):
        if ticket.difficulty == 1:
            return self.get_free_back_office_employee()
        elif ticket.difficulty in (1, 2):
            return self.get_free_account_manager_or_director()
        elif ticket.difficulty in (1, 2, 3):
            return self.get_free_director()

    def get_free_back_office_employee(self):
        for employee in self.back_office_employees:
            if employee.is_free:
                return employee
        return None

    def get_free_account_manager_or_director(self):
        for employee in self.account_managers:
            if employee.is_free:
                return employee
        for employee in self.directors:
            if employee.is_free:
                return employee
        return None

    def get_free_director(self):
        for employee in self.directors:
            if employee.is_free:
                return employee
        return None

    def handle_employee_response(self, status: bool, employee, ticket: Ticket):
        print("Ticket", ticket.title, "was handled by", employee.name, "with status", status)
        if not status:
            self.tickets.append(ticket)
