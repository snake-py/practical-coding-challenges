import json


class Storage:

    def __init__(self, storage_path: str = 'catalog.json'):
        self.storage_path = storage_path
        self.in_memory_storage = {}
        self.load_from_json()   

    def load_from_json(self):
        with open(self.storage_path, 'r') as file:
            self.in_memory_storage = json.load(file)

    def save_to_json(self):
        with open(self.storage_path, 'w') as file:
            json.dump(self.in_memory_storage, file, indent=4)
