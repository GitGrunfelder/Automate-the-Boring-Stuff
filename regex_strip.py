import re
# This function replicates the strip() function, using Regex.
my_str = '     banana     '
my_str_2 = 'aaaa.....bb.....banana....bbb....bbb'
def stripRegex(string, target): # Feed it string to strip and a target to retrieve.
    stringRegex = re.compile(rf'{target}') # This retrieve targeted word, leaving all else behind.
    mo = stringRegex.search(string)
    print(mo.group())
    

stripRegex(my_str, 'banana')
