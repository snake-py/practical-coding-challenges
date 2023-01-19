# Core Libs
import click
import re
import inquirer
# Own Modules
from modules.Prompts import Prompt
from modules.Product import Catalog, Product, Kit



@click.group()
def cli():
    """"
    Following Commands are required to be implemented
    1. Create a product
    2. Create a kit
    3. Print a kit
    4. Print the catalog
    """
    pass
 

@cli.command()
def load():
    """Load a catalog from a json file"""
    catalog = Catalog() 
    catalog.print_catalog()



@cli.command()
def build():
    """Interactively build a catalog"""
    catalog = Catalog(interactive=True)
    prompt = Prompt()
    keep_running = True
    try:
        while keep_running:
            questions = [inquirer.List('commands', message="What do you want to do?", 
                choices=prompt.inquirer_current_options(catalog))]
            answer = inquirer.prompt(questions=questions)
            if  not answer or prompt.should_quit(answer.get('commands', 'Quit')):
                keep_running = False
                break
            else:
                prompt.execute_command(catalog, answer['commands'])
    except KeyboardInterrupt:
        print("KeyboardInterrupt")


if __name__ == '__main__':
    cli()