# r'' is a life saver. It stands for raw string, r in front of the string quotes
# ensure that file paths don't get confused between Python and system settings.
# Whenever you’re typing paths in your code, just by including that r in front of
#  the quotes you can avoid lots of errors that might occur due to conflicts and
#  confusions regarding path symbols like: /, //,  \. This problem occurs more 
# often than you’d imagine and it can be very frustrating to troubleshoot. 
# Just use r in front and path problems no more!

titanic_data = r'C:\Users\rbuzzini\Documents\Personale\Git\Python\Fun Projects\datasets\titanic\train.csv'

data=open(titanic_data, "r")
print(data.read())