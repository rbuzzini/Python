# sep parameter
# if want to print multiple values with a user-defined separater, 
# you can use print’s sep parameter for that.
str1="mailname"
str2="geemayl.com"

print(str1, str2, sep="@")


# end parameter
# Python’s print function has a \n new line character at the end by default.
# But, sometimes, you just don’t want it to enter a new line after print or 
# better yet you might want to add a different character to the end of each print function.
# end parameter is perfect for that.
print("one", end=",")
print("two", end=",")
print("and so on", end="...")