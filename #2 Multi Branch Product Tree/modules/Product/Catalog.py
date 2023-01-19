from .Product import Product
from .Kit import Kit
from typing import List, Set
from modules.Storage import Storage

class Catalog:
    products = []
    kits = []

    def __init__(self, path: str =  'catalog.json', storage: Storage = None, interactive: bool = False):
        self.storage = storage or Storage(path)
        if not interactive:
            self.load()

    def load(self):
        if self.is_kit(self.storage.in_memory_storage):
            kit = Kit(self.storage.in_memory_storage['name'], [])
            kit.load_children(self.storage.in_memory_storage['children'])
            print(kit)
            if not kit.is_kit_valid(set()):
                del kit
                raise ValueError('Circular reference')
            self.add_kit(kit)
    
    def is_kit(self, dic: dict) -> bool:
        return dic.get('children') is not None

    def add_product(self, product: Product):  
        self.products.append(product)
    
    def has_products(self) -> bool:
        return len(self.products) > 0

    def create_product(self, name: str, price: float):
        product = Product(name, price)
        self.add_product(product)
        return product
    
    def add_kit(self, kit: Kit):
        self.kits.append(kit)

    def create_kit(self, name: str, children: List[Product or Kit]):
        try: 
            kit = Kit(name, children)
            self.add_kit(kit)
            return kit
        except ValueError as exception:
            print(exception)
            return None

    def print_kit(self, kit: Kit):
        kit.print_self()
    
    def print_catalog(self):
        for kit in self.kits:
            print("-----------------------")
            print(f"{kit.name}")
            print("-----------------------")
            self.print_kit(kit)
            print("-----------------------")

    def get_product_names(self) -> List[str]:
        return [f"Name: {product.name} - price: {product.price} - {product.id} " for product in self.products]

    def get_kit_names(self) -> List[str]:
        return [f"Name: {kit.name} - price: {kit.calculate_price()} - Children {kit.get_all_children_names()} - {kit.id}" for kit in self.kits]

    def get_by_id(self, id: str) -> Product or Kit:
        for product in self.products:
            if str(product.id) == id:
                return product
        for kit in self.kits:
            if str(kit.id) == id:
                return kit
        return None