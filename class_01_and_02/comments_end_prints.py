# Here allow to write comments in the code
print("Hello World") # This is a comment after the code

"""
Docstrings

This is a multiline comment
"""

'''
Docstrings
This is also a multiline comment
'''

print("Hello World after the docstrings", 123, True) # This is a print without separator
print("Hello World after the docstrings", 123, True, sep=" - ") # This is a print with separator
print("Hello World after the docstrings", 123, True, sep=" - ", end=".") # This is a print with separator and end