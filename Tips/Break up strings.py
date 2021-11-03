# Split method

# Split function divides a string into a list in which every element is a part
# of the string, according to the separrator character.
# Here some examples:

str1 = "Hello World"
str2 = "Hello,World"

lst1 = str1.split(" ")
lst2 = str2.split(",")

print(lst1, lst2, sep='\n')