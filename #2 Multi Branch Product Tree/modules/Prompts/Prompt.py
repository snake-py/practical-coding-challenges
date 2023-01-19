import re
import inquirer
from .Command import Command

from modules.Product import Catalog, Kit, Product

class Prompt:
    def execute_command(self, catalog: Catalog, command: str):
        print(Command.CREATE_PRODUCT.value)
        if command == Command.CREATE_PRODUCT.value:
            self.inquirer_create_product(catalog)
        elif command == Command.CREATE_KIT.value:
            self.inquirer_create_kit(catalog)
        elif command == Command.PRINT_KIT.value:
            self.inquirer_print_kit(catalog)
        elif command == Command.PRINT_CATALOG.value:
            catalog.print_catalog()
        
    def should_quit(self, command: str) -> bool:
        return command == Command.QUIT.value

    def inquirer_print_kit(self, catalog: Catalog):
        questions = [inquirer.List('commands', message="What Kit do you want to print?", 
            choices=catalog.get_kit_names())] 
        answer = inquirer.prompt(questions=questions)
        id = re.search('\w{8}-\w{4}-\w{4}-\w{4}-\w{12}', answer['commands']).group()
        kit = catalog.get_by_id(id)
        if kit:
            kit.print_self()
        else:
            print("Invalid input")


    def inquirer_create_kit(self, catalog: Catalog) -> Kit:
        questions = [
            inquirer.Text('name', message="What is the Kit Name?"),
        ]
        name = inquirer.prompt(questions=questions)
        questions = [
            inquirer.Checkbox('children',
                        message="What are you interested in?",
                        choices=catalog.get_product_names() + catalog.get_kit_names()
                        ),
        ]
        answers = inquirer.prompt(questions=questions)
        children = []
        for child_string in answers['children']:
            id = re.search('\w{8}-\w{4}-\w{4}-\w{4}-\w{12}', child_string).group()
            entry = catalog.get_by_id(id)
            if entry:
                children.append(entry)
            else:
                print("Invalid input")
        catalog.create_kit(name['name'], children)



    def inquirer_create_product(self, catalog) -> Product:
        questions = [
            inquirer.Text('name', message="What is the product name?"),
            inquirer.Text('price', message="What is the product price?")
        ]
        answers = inquirer.prompt(questions=questions)
        print(answers)
        valid = self.should_not_be_empty(answers)
        if valid:
            return catalog.create_product(answers['name'], float(answers['price']))
        print("Invalid input")
        return None

    def should_not_be_empty(self, answers):
        for answer_key in answers:
            if answers[answer_key] == '':
                return False
        return True

    def inquirer_current_options(self, catalog: Catalog) -> list:
        if catalog.has_products():
            return [
                Command.CREATE_PRODUCT.value,
                Command.CREATE_KIT.value,
                Command.PRINT_KIT.value,
                Command.PRINT_CATALOG.value,
                Command.QUIT.value
                ]
        else:
            return [
                Command.CREATE_PRODUCT.value,
                Command.QUIT.value
                ]
        
