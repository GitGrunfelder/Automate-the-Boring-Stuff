#! python3
# phoneAndEmail.py - Finds phone numbers and emails on the clipboard.

import pyperclip
import re

'''Get text off clipboard.
Find all numbers and email addresses in text
Paste them onto clipboard.

Can use pyperclip to copy and paste
Need two regex objects, one for numbers, one for emails
find all matches, not just first
neatly format into a single str for pasting
display a message if none found'''

numberRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # Area code as 555 or (555) (matches zero or one) GROUP 1
    (\s|-|\.)?                      # separator as space, -, . matches zero or one
    (\d{3})                         # First 3 digits                                  GROUP 3
    (\s|-|\.)                       # separator, at least one
    (\d{4})                         # Last 4 digits                                   GROUP 5
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension (zero or more spaces, extension abrv. zero or more spaces, 2-5 digits) matches zero or one
    )''', re.VERBOSE) #<-- This allows for weird spacing and comments in regex object
    
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # Username, any char, upper or lower, any digit, underscore, %, +,-, one or more
    @                       # at symbol
    [a-zA-Z0-9.-]+          # Domain name, any char, digits, . and -, one or more
    (\.[a-zA-Z]{2,4})       #.something 2-4 length
    )''', re.VERBOSE)
                        
# I have defined the email pattern and the number patterns to match.
# Now copy these to a new list for editing
pastedText = str(pyperclip.paste())

matches = []
for groups in numberRegex.findall(pastedText): # Loops through matched groups in copied text
    phoneNum = '-'.join([groups[1], groups[3], groups[5]]) # Joins area code and main numbers
    if groups[8] != '': # If there is ext, add that
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum) # Put combined string into list
for groups in emailRegex.findall(pastedText): # Append all matching emails
    matches.append(groups[0])
  
# Emails and numbers have been taken out of text. Now to copy onto clipboard.
if len(matches) > 0: # If emails or numbers exist
    pyperclip.copy('\n'.join(matches)) # Join all items in matches list, via newlines
    print('Copied to clipboard: ')
    print('\n'.join(matches)) # Show copied text
else:
    print('No matches.')


