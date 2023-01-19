# Basic Technical documentation

Read about the challenge [here](./Task.md)
if you are looking for the article, you can find it [here](Article.md) or on (dev.to)[https://dev.to/snakepy/1-code-challenge-chain-of-responsibility-python-376]

## What did I do

I wrote a concept and left it there for reference. From there I tackled the challenge with a flask application.
The app has 3 simple routes

GET: '/': The home page, which will display all tickets in memory<br/>
GET: '/ticket/<ticket_id>': The ticket page, which will display the ticket with the given id<br/>
POST: '/': The ticket creation page, which will create a new ticket with the given data and dispatch it to the TicketSystem<br/>

Tickets need the following data to be created:

```json
{
    "title": "test title",
    "description": "test description",
    "difficulty": 1
}
```

The `difficulty` is a number between 1 and 3, it is used to set the target difficulty

-   1 needs at least BackOfficeEmployee
-   2 needs at least AccountManage
-   3 needs at least Director

Curl example:

```bash
curl --location --request POST 'http://localhost:5000/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "test 6",
    "description": "test",
    "difficulty": 1
}'
```

## Start the app

create a virtual environment and install the requirements

```bash
python -m venv venv
source venv/bin/activate # or venv\Scripts\activate.bat on windows
```

install the requirements

```bash
pip install -r requirements.txt
```

start the app

```bash
python app.py
```

Completion in 5 hours
