#! python3
# bullet_point_adder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste() # Pastes from clipboard.

lines = text.split('\n') # Grabs a chunk of lines, splits them
for i, val in enumerate(lines): # I use enumerate(), can use range(len())
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines) # Rejoins

pyperclip.copy(text) # Sticks back on clipboard.