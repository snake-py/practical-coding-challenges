from uuid import uuid4



class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.id = uuid4()
        self.price = price