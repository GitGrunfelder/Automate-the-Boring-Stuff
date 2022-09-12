import pyperclip

'''Ch 6 - String Manipulation'''


# spam = 'helLo'
# print(spam.upper())
# print(spam.lower())
# print(spam)
# '''These methods do not change the string, just modify and return a new one.
# In order to change, assign to spam = spam.upper() ...'''

# '''These methods are useful for validating user input.'''
# print('123'.isalpha())
# print('Hello'.isalpha())
# print('Hello123'.isalnum())
# print('123'.isdecimal())
# print(' '.isspace())
# print('This Is A Title'.istitle())
# print('This is not'.istitle())

# Example
# def validateInput():
#     while True:
#         age = input('Enter your age: ')
#         if age.isdecimal():
#             break
#         print('Try again.')
    
#     while True:
#         password = input('Choose a password (letters and numbers only): ')
#         if password.isalnum():
#             break
#         print('Only numbers and letters please.')
        
# validateInput()

# '''startwith() and endswith() are useful for checking if start
# or end of string match given entry.'''
# print('Hello'.startswith('Hel'))

# '''.join() is called on a string, this string "whatever you want between items in list",
# is stuck between the passed list. It then returns a string.'''

# exlist = ['This', 'is', 'how', 'join()', 'works.']
# print(exlist)
# print(' '.join(exlist))

# '''split() is the opposite, it is called on your str/variable, and split at whitespaces by default.
# Add parameters to split at whatever delimiter you want.'''
# my_str = 'Hello and welcome to Burger King.'
# print(my_str)
# print(my_str.split())
# '''A usecase would be split(\n) on a chunks of sentences/paragraphs.
# This returns a list of each line in the writing.'''

# '''You can .partition(separator) a string, which returns a tuple with before, partition, after as the results.'''
# print('This is a sentence.'.partition(' is')) #<-- Finds the first instance of separator.

# print('Hello'.ljust(30))
# print('Hello'.rjust(30))
# print('Hello'.center(30, '*'))        

# Example
# def printPicnic(itemsDict, leftWidth, rightWidth):
#     print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
#     for k, v in itemsDict.items():
#         print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
        
# picnic = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
# printPicnic(picnic, 20, 7)

'''strip() removes left(lstrip) right (rstrip) or both sides extra whitespaces. If you
pass an argument, it will remove that from the outer ends of string.'''
# spam = 'SpamSpamBaconSpamEggsSpamSpam'
# print(spam.strip('Spam'))


#Unicode
# '''ord() returns the code point of any one character string,
# while chr() gives the one character string of an integer code point.
# Useful for math or ordering using letters.'''
# print(ord('B'))

# pyperclip module
'''This module can copy and paste into other locations from clipboard.'''
pyperclip.copy('Hello, world!')
print(pyperclip.paste())