import re
# commaReg = re.compile(r'^\d{1,3}(,\d{3})*$')
# mo = commaReg.search('1,234,555')
# print(mo)

# nameReg = re.compile(r'(^[A-Z]\w+) Watanabe')
# print(nameReg.search("Haruto watanabe").group())

wordMixReg = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.I)
print(wordMixReg.search("Carol eats 7 cats.").group())
