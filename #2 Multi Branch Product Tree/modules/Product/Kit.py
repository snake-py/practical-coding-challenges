from uuid import uuid4
from typing import List, Set

from .Product import Product


class Kit:
    def __init__(self, name: str, children: List['Kit' or Product or dict] = None):
        self.IDS_IN_KIT = set()
        self.id = uuid4()
        self.IDS_IN_KIT.add(self.id)
        self.name = name
        self.children = children
        if not self.is_kit_valid(self.IDS_IN_KIT):
            raise ValueError('Circular reference')

    def load_children(self, children: List[dict]):
        for child in children:
            if child.get('children') is not None:
                kit = Kit(child['name'], [])
                kit.load_children(child['children'])
                if not kit.is_kit_valid(set()):
                    del kit
                    raise ValueError('Circular reference')
                self.children.append(kit)
            else:
                self.children.append(Product(child['name'], child['price']))

    def is_kit_valid(self, IDS_IN_KIT: Set[str]) -> bool:
        ## TODO - This will currently prevent even if there is no circular reference in place, just check branch by branch
        """Prevents circular references"""
        for child in self.children:
            if child.id in IDS_IN_KIT:
                return False
            IDS_IN_KIT.add(child.id)
            if isinstance(child, Kit):
                if not child.is_kit_valid(IDS_IN_KIT):
                    return False
        return True
    
    def get_children(self) -> List['Kit' or Product]:
        return self.children

    def calculate_price(self, price: float = 0) -> float:
        """Sum of all leafs and plus 10% on every leaf"""
        for child in self.children:
            if isinstance(child, Kit):
                price_without = child.calculate_price()
                price += price_without * 1.1
            else:
                price += child.price * 1.1
        return price

    def __str__(self):
        return f'Kit: {self.name} - {self.id}'

    def get_all_children_names(self) -> List[str]:
        names = []
        for child in self.children:
            if isinstance(child, Kit):
                names.extend(child.get_all_children_names())
            else:
                names.append(child.name)
        return names

    def print_self(self, level: int = 0):
        print(f'{"  " * level}{self.name} - {round(self.calculate_price(), 2)}')
        for child in self.children:
            if isinstance(child, Kit):
                child.print_self(level + 1)
            else:
                print(f'{"  " * (level + 1)}{child.name} - {round(child.price, 2)}')