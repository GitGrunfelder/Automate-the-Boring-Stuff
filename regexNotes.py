import re

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


message = 'Call me at 555-555-5555 tomorrow. 565-565-5656 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

# Above is how to find a specific phone number format
# without Regex.

# Below, by importing re at start, can create regex object.
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# The regex object has a .search() method, which searches any string it is passed
# It will return None if it isn't found
# Returns a 'match object' which has a 'group()' method, which returns actual matched text
mo = phoneNumRegex.search('My number is 555-590-5555.')
print('Phone number found: ' + mo.group())

'''The process is as follows:
1) import re
2) reObj = re.compile() create a regex object , feeding it the pattern you want found.
3) match_object = reObj.search('string') pass the string you want to search into the objects search method
4) call match_object.group() to return found values that match pattern'''

# Grouping via parenthesis - call # of group to return matched data, or groups() for all
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 555-590-5555.')
print('Area code: ' + mo.group(1) + ' Number: ' + mo.group(2))
print(mo.groups())

# Unpacking + grouping
areaCode, mainNum = mo.groups()
print(areaCode)
print(mainNum)

# Escaping chars within regex search
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (843) 590-5555.')
print('Area code: ' + mo.group(1) + ' Number: ' + mo.group(2))
print(mo.groups())

# The | symbol matches any one of the options it separates.
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

# By using parenthesis, you can search for parts of variances of words.
batRegex = re.compile(r'Bat(man|mobile|signal|copter)')
mo3 = batRegex.search('Batmobile lost a wheel')
print(mo3.group(1))

# Optional matching with ?
bat1Regex = re.compile(r'Bat(wo)?man')
mo4 = bat1Regex.search('The adventures of Batwoman')
print(mo4.group())

# Match zero or one of the group preceding question mark.
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo5 = phoneRegex.search('My number is 555-590-9050')
print(mo5.group())
mo6 = phoneRegex.search('My number is 590-9050')
print(mo6.group())

# Match zero or more with *
bat2Regex = re.compile(r'Bat(wo)*man')
mo7 = bat2Regex.search('The adventures of Batwowowowowowowoman')
print(mo7.group())

# Matching specific repetitions with Braces (the number in braces is how many in a row. HaHaHa or Ha x 3)
# Can use range such as (Ha){3,} - three or more
haRegex = re.compile(r'(Ha){3}')
mo8 = haRegex.search('HaHaHa')
print(mo8.group())

# Greedy and nongreedy matching
# Reg Expressions are Greedy by default - match longest string possible
# Non-Greedy or Lazy matches shortest (word){,3}?
haRegex = re.compile(r'(Ha){3,5}')
mo9 = haRegex.search('HaHaHaHaHa')
print(mo9.group())

haRegex = re.compile(r'(Ha){3,5}?')
mo10 = haRegex.search('HaHaHaHaHa')
print(mo10.group())

# search() finds first instance of matched text
# findall() finds strings of every matched text
phone2Regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # Notice NO groups
mo11 = phone2Regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo11) # The matched object is a list of all items that match string pattern. (NO GROUPS)

phone2Regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # With groups - it returns tuples
mo12 = phone2Regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo12) # More specifically, a list of tuples of strings - one string for each group


# Character Classes
# \d - digits 0-9
# \D - Anything other than 0-9
# \w - any letter, digit, or underscore ('word')
# \W - Anything NOT a letter, digit, or underscore
# \s - Any space, tab, or newline char ("space" characters)
# \S - anything not a space char.

xmasRegex = re.compile(r'\d+\s\w+') # 1 OR MORE digit, space char, 1 or more word char
mo13 = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo13)

# Making your own character classes
vowelRegex = re.compile(r'[aeiouAEIOU]') # Using square brackets allows use of your own specific patterns (here all vowels)
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')) # Items in brackets will not be treated like normal symbols, 
# don't need to escape them. Also [^text...] will find everything BUT the item. Adding a ^ to the above example finds all consonants.

# ^ and $ are used to denote find at beginning or end. 
startsRegex = re.compile(r'with')
mo14 = startsRegex.search('This starts with this.')
print(mo14)

startsRegex = re.compile(r'^with')
mo14 = startsRegex.search('This starts with this.')
print(mo14)

startsRegex = re.compile(r'this$')
mo14 = startsRegex.search('This starts with this.')
print(mo14)

startsRegex = re.compile(r'this.$')
mo14 = startsRegex.search('This starts with this.')
print(mo14)

# If both are used, the entirety of the pattern within the symbols must match, and begin and end with correct things.

# Wildcard Character
# The . or dot matches any char except newline.
atRegex = re.compile(r'.at') # The . represents any single character besides \n - finds any 1 letter + at.
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

# Match any and everything with (.*)
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo15 = nameRegex.search('First Name: George Last Name: Grunfelder')
print(mo15.group(1))

nonGreedyRegex = re.compile(r'<.*?>') # Finds shortest instance
mo = nonGreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
GreedyRegex = re.compile(r'<.*>') # Without ?, finds longest string that matches pattern.
mo = GreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

# How to match newlines! Pass second argument of re.DOTALL
noNewLineRegex = re.compile(r'.*')
print(noNewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

newLineRegex = re.compile(r'.*', re.DOTALL)
print(newLineRegex.search(
    'Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

'''Recap:
? matches zero or one
* matches zero or more
+ matches 1 or more
{n} matches exactly n
{n,} matches n or more
{,m} matches up to m
{n,m} matches from n to m number of pattern
{}? *? +? NONGREEDY - matches smallest amount it can
^spam means str must begin with spam
spam? means str must end with spam
. matches any char except newline
\d \w \s ---digit, word, or space char
\D \W \S ---NONdigit NONword NONspace chars
[abcABC] matches any between brackets
[^abc] matches any not in brackets'''

# Ignoring case with re.I
robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man').group())
print(robocop.search('ROBOCOP is part robot').group())
print(robocop.search('roboCop is all Cop').group())
# Since re.compile is passed re.I (or re.IGNORECASE) it returns all matches to the text, regardless of caps.

# Sub()
namesRegex = re.compile(r'Agent \w+') # Regex finds any instances of Agent (1 or more word chars)
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret docs to Agent George')) # Find namesRegex, 
# sub first parameter in regEx matches in second parameter wherever there is a match.

# You can sub in part of the found reg ex into all instances of regex
agentNamesRegex = re.compile(r'Agent (\w)\w*') # Search for all instances of Agent (group1 (any word char))any word chars til space
print(agentNamesRegex.sub(r'\1****', "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent."))
# Sub in group 1, which is the first letter of last name, any time the regex is found.

# To combine re.IGNORECASE, re.DOTALL, and re.VERBOSE
someRegexValue = re.compile(r'foo', re.IGNORECASE | re.DOTALL | re.VERBOSE) 
# This would return any instances of foo, regardless of capitalization,
# including any newlines, and ignoring any extraspace /comments in the regex compiler.