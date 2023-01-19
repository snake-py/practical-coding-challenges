from threading import Thread, Event
from flask import Flask, render_template, request
from modules.Tickets import Ticket, TicketSystem
from utils import make_dummy_back_office_employees, make_dummy_account_managers, make_dummy_directors


app = Flask(__name__)

ticketSystem = TicketSystem(make_dummy_back_office_employees(6), make_dummy_account_managers(2), make_dummy_directors(1))
Thread(target=ticketSystem.work).start()

@app.route("/", methods=['GET', 'POST'])
def ticketApi():
    if request.method == "POST":
        return add_ticket(), 201
    elif request.method == "GET":
        return get_ticket(), 200
    return "Wrong HTTP method"


@app.route('/ticket/<ticket_id>', methods=['GET'])
def ticket(ticket_id):
    if request.method == "GET":
        return get_ticket_by_id(ticket_id), 200
    return "Wrong HTTP method"

def get_ticket_by_id(ticket_id):
    all_tickets = ticketSystem.history
    for ticket in all_tickets:
        if str(ticket.id) == ticket_id:
            return render_template('ticket.html', ticket=ticket.to_dict(True))
    return "Ticket not found", 404


def add_ticket():
    ticket_input = request.get_json()
    try:
        ticket = Ticket(ticket_input['title'], ticket_input['description'], ticket_input.get('difficulty', 1))
        ticketSystem.dispatch_case(ticket)
    except ValueError as e:
        return str(e), 400
    return {"id": ticket.id, "title": ticket.title, "description": ticket.description, "target_difficulty": ticket.target_difficulty}


def get_ticket():
    all_tickets = ticketSystem.history
    tickets = []
    for ticket in all_tickets:
        tickets.append(ticket.to_dict())
    return render_template('all_tickets.html', tickets=tickets)


if __name__ == '__main__':
    app.run(debug=True)
