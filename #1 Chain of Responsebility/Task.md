# Case Routing

## Intro

Imagine you have a sales department with three levels of employees: backoffice, account manager, and director. Whenever a case is automatically created, it must be first allocated to a backoffice employee who is free. If the backoffice employee can't handle the case, he or she must escalate the case to an account manager. If the manager is not free or not able to handle it, then the case should be escalated to a director.

## Your Task

Design the classes and data structures for this problem. Implement a method dispatchCase() which assigns a case to the first available employee.

## Remarks

It is not important what the case looks like. The important part is the employee hierarchy and how cases are routed to employees.
