import random, time
import pyinputplus as pyip

response = pyip.inputNum('Please enter a number greater than 68: ', greaterThan=68)
print(response)

'''
These automatically reprompt for input on incorrect input.

inputStr() - enter and validate strings
inputNum() - enter and validate ints/floats - returns ints/floats unlike input()
inputInt() / inputFloat() - can take 'prompt', min/max/greaterThan/lessThan
inputChoice() - ensures user picks one of provided choices
inputMenu() - provides menu with numbered or lettered options
inputDatetime() - ensures user inputs date and time
inputYesNo() - must be 'yes' or 'no'
inputBool() - takes "True" or "False" , returns boolean
inputEmail() - ensures valid email address is entered
inputFilePath() - ensures valid filepath and filename, and checks if it exists
inputPassword() - like input(), but displays * as characters entered.
(blank=True) for allowing no input ...optional input
limit=# of tries before error
timeout=# of seconds user has to enter input
(limit=3, default='N/A') passing default shows that message instead of error
'''

roman_response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero']) 
# Accepts uppercase roman nums, but order can be invalid

no_evens = pyip.inputNum('Enter an odd number: ',blockRegexes=[r'[02468]$'])
print(no_evens)

# allowRegex > blockRegex

'''Creating a custom function that can take input, and reprompt repeatedly
useful for when ReGex would be difficult. Such as only accepting ints that add to 10.'''
def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception(f'The digits must add up to 10, not {sum(numbersList)}.')
    return int(numbers) # returns int form of numbers.

response = pyip.inputCustom(addsUpToTen) # inputCustom also accepts general pyip methods (blank/limit/timeout...)
print(response)

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        print('Have a nice day!')
        break

numOfQuestions = 10
correctAnswers = 0
print('Welcome to the basic multiplication quiz game!')
time.sleep(2)
print('You have 3 attempts for each question and 8 seconds to answer!')
time.sleep(2)
print('Good Luck!')
for questionNumber in range(numOfQuestions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = f'{questionNumber+1}: {num1} x {num2} = '
    try:
        pyip.inputStr(prompt, allowRegexes=[f'{num1*num2}'], blockRegexes=['.*', 'Incorrect!'], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correctAnswers += 1
    time.sleep(1)
print(f"Score:{correctAnswers}/{numOfQuestions}")






