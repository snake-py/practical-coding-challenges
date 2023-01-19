from modules.Employee import AccountManager, BackOfficeEmployee, Director


def make_dummy_back_office_employees(n):
    employees = set()
    for n in range(n):
        emp = BackOfficeEmployee(f'BackOfficeEmployee {n}', 1000, 'BackOfficeEmployee', 10)
        employees.add(emp)
    return employees

def make_dummy_account_managers(n):
    employees = set()
    for n in range(n):
        emp = AccountManager(f'AccountManager {n}', 1000, 'AccountManager', 5)
        employees.add(emp)
    return employees

def make_dummy_directors(n):
    employees = set()
    for n in range(n):
        emp = Director(f'Director {n}', 1000, 'Director', 10)
        employees.add(emp)
    return employees
