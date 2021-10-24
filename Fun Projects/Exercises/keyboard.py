import csv
import os
from item import Item

os.getcwd()
items_path = r'C:\Users\rbuzzini\Documents\Personale\Git\Python\Fun Projects\datasets'
#items_path = r'Fun Projects\datasets'
os.chdir(items_path)

# create Phone class
class Keyboard(Item):
    def __init__(self, name: str, price: float, quantity: int=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )
        
    

