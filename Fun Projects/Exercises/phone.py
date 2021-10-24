import csv
import os
from item import Item

os.getcwd()
items_path = r'C:\Users\rbuzzini\Documents\Personale\Git\Python\Fun Projects\datasets'
#items_path = r'Fun Projects\datasets'
os.chdir(items_path)

# create Phone class
class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int=0, broken_phones: int=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than or equal to 0"
        
        # Assign to self object
        self.broken_phones = broken_phones

