from uuid import uuid4
from typing import List, Set


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.id = uuid4()
        self.price = price


class Kit:
    def __init__(self, name: str, children: List['Kit' or Product] = None):
        self.name = name
        self.id = uuid4()
        self.children = children

    def is_kit_valid(self, IDS_IN_KIT: Set[str]) -> bool:
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

    def print_self(self, level: int = 0):
        print(f'{"  " * level}{self.name} - {round(self.calculate_price(), 2)}')
        for child in self.children:
            if isinstance(child, Kit):
                child.print_self(level + 1)
            else:
                print(f'{"  " * (level + 1)}{child.name} - {round(child.price, 2)}')


class Catalog:
    products = []
    kits = []
    IDS_IN_KIT = set()

    def add_product(self, product: Product):  
        self.products.append(product)
    
    def create_product(self, name: str, price: float):
        product = Product(name, price)
        self.add_product(product)
        return product
    
    def add_kit(self, kit: Kit):
        self.kits.append(kit)

    def create_kit(self, name: str, children: List[Product or Kit]):
        self.IDS_IN_KIT = set()
        kit = Kit(name, children)
        self.IDS_IN_KIT.add(kit.id)
        if kit.is_kit_valid(self.IDS_IN_KIT):
            self.add_kit(kit)
            return kit
        else:
            del kit
            return None

    def print_kit(self, kit: Kit):
        kit.print_self()
    
    def print_catalog(self):
        for kit in self.kits:
            print(f"Kit - {kit.name}")
            self.print_kit(kit)
            print("-----------------------")

# Created the Catalog instance
catalog = Catalog()

# Create the products
# p1 = catalog.create_product('product1', 10)
# p2 = catalog.create_product('product2', 20)
# p3 = catalog.create_product('product3', 30)
# p4 = catalog.create_product('product4', 40)
# p5 = catalog.create_product('product5', 50)

# # Create the kits
# kit1 = catalog.create_kit('kit1', [p1, p2])
# kit2 = catalog.create_kit('kit2', [p3, p4, p5])
# kit3 = catalog.create_kit('kit3', [kit2, kit1])

# # Should not work:
# kit4 = catalog.create_kit('kit3', [kit2, kit3])
# kit5 = catalog.create_kit('kit3', [kit2, p3])

# Print the catalog
# print(kit2)
# print(kit3)
# print(kit4)
# print(kit5)


# # Print Tree Structure 


# catalog.print_kit(kit3)
# kit3.print_self()
product_c = catalog.create_product('Product C', 10)
product_g = catalog.create_product('Product G', 15)
product_f = catalog.create_product('Product F', 5)
product_k = catalog.create_product('Product K', 20)
product_h = catalog.create_product('Product H', 50)


kit_d = catalog.create_kit('kit D', [product_h, product_k])
kit_b = catalog.create_kit('kit B', [kit_d, product_f, product_g])
kit_a = catalog.create_kit('kit A', [kit_b, product_c])



catalog.print_catalog()