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



