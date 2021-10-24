from item import Item
from phone import Phone
from keyboard import Keyboard
import csv
import os

os.getcwd()
items_path = r'C:\Users\rbuzzini\Documents\Personale\Git\Python\Fun Projects\datasets'
os.chdir(items_path)

Item.instantiate_from_csv()

print(Item.all)


item1 = Keyboard('MyItem', 500, 6 )
print(item1.name, type(item1)) 
item1.name = 'OtherItem'
item1.apply_increment(0.2)
item1.price
