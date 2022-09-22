import re

my_str = '     banana     '
my_str_2 = '...   ...tt...carrrs   tttttttt'
def stripRegex(string, target=' '):
    stringRegex = re.compile(rf'\w+[^{target}]')
    mo = stringRegex.search(string)
    print(mo.group())
    

stripRegex(my_str)
