
import re
# Strong pass is >= 8 chars, at least: 1 uppercase, 1 lower case, 1 digit

def passwordTester(password):
    
    if len(password) < 8:
        print('Password too short.')
        return
    digitRegex = re.compile(r'[0-9]+')
    upperRegex = re.compile(r'[A-Z]+')
    lowerRegex = re.compile(r'[a-z]+')
    mo1 = digitRegex.search(password)
    mo2 = upperRegex.search(password)
    mo3 = lowerRegex.search(password)
    if mo1 != None and mo2 != None and mo3 != None:
        print('Valid password.')
    else:
        print('Password is too weak, try again.')
    
weak_pass = 'weakweak'  
strong_pass = 'aG12345678'
short_pass = '123'

passwordTester(short_pass)
