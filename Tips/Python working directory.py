# This one is so helpful when needed. Sometimes you may need to identify 
# or double check where your Python is working.

# get working directory with getcwd() method of os library:
import os
dirPath = os.getcwd()
print(dirPath)


# And if you want to change directory:
import os
os.chdir(r'C:\Users\rbuzzini\Documents\Personale\Git\Python\Fun Projects')
print(os.getcwd())


# printing libraries directory
import pandas
print(pandas)
