import re

# A lot of times, the sales and marketing teams might require finding/extracting 
# emails and other contact information from large text documents.

# insert your text here:
text = """This is a simple text example in order to see how to extract 
    (abcde@gmail.com fghijk@gmail.com lmnop@gmail.com) all mails from a txt file 
    in Python (1viksoa@outlook.com w_fvwjdwiq9@libero.com) with 're' module"""

re.findall(r"[\w.-]+@[\w.-]+", text)

# You can directly read a file and process it, use the following code:
with open("filename.txt", "r") as fp:
    text = fp.read()
re.findall(r"[\w.-]+@[\w.-]+", text)


# References: 
# https://www.analyticsvidhya.com/blog/2020/01/4-applications-of-regular-expressions-that-every-data-scientist-should-know-with-python-code/