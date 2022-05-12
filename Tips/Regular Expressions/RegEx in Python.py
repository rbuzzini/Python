import re

# A Regular Expression (RegEx) is a sequence of characters that defines a search pattern.

# 1st example, Search the string to see if it starts with "The" and ends with "Italy":
txt = "The rain in Italy"
x = re.search("^The.*Italy$", txt)   # same result with re.match("^The.*Italy$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")


# The re module offers a set of functions that allows us to search a string for a match:
# `findall` returns a list containing all matches
# `search` or `match` return a Match object if there is a match anywhere in the string
# `split` returns a list where the string has been split at each match
# `sub`	replaces one or many matches with a string


# To specify regular expressions, metacharacters are used. In the above example, ^ and $ are metacharacters.



# Useful reference:
# https://www.programiz.com/python-programming/regex
