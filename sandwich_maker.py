import pyinputplus as pyip
# A program that asks users for their sandwich preferences.

# Dictionary of ingredients:prices
prices = {'Wheat': 1.50, 'White': 1.00,'Sourdough': 2.00,
          'Black Bean': 1.00,'Tofu': 2.50, 'Chicken': 3.50, 'Turkey': 3.50,
          'Cheddar': 1.50, 'Swiss': 2.00, 'Mozzarella': 2.50, 'no': 0.0,
          'add mayo': 0.50, 'add mustard': 0.50, 'add lettuce': 0.50, 'add tomato': 0.50,
          'no mayo': 0.0 , 'no mustard':0.0, 'no lettuce':0.0, 'no tomato':0.0 }
# Choose bread and protein
bread = pyip.inputMenu(['Wheat', 'White', 'Sourdough'],
                       prompt='Please choose your preferred bread:\n', numbered=True)

protein = pyip.inputMenu(['Black Bean', 'Tofu', 'Chicken', 'Turkey'],
                       prompt='Please choose your preferred protein:\n', numbered=True)

# Check for cheese, if so, what type.
cheese_yn = pyip.inputYesNo("Would you like cheese? ")
if cheese_yn == 'yes':
    cheese_type = pyip.inputMenu(['Cheddar','Swiss','Mozzarella'], prompt='What type of cheese would you like?\n', numbered=True)
else:
    cheese_type = 'no'

# Check for condiments, if so 'add', else 'no'   
mayo_yn = pyip.inputYesNo('Would you like mayo? ')
if mayo_yn == 'yes':
    mayo = 'add mayo'
else:
    mayo = 'no mayo'
mustard_yn = pyip.inputYesNo('Would you like mustard? ')
if mustard_yn == 'yes':
    mustard = 'add mustard'
else:
    mustard = 'no mustard'
lettuce_yn = pyip.inputYesNo('Would you like lettuce? ')
if lettuce_yn == 'yes':
    lettuce = 'add lettuce'
else:
    lettuce = 'no lettuce'
tomato_yn = pyip.inputYesNo('Would you like tomato? ')
if tomato_yn == 'yes':
    tomato = 'add tomato'
else:
    tomato = 'no tomato'
    
# Number of sandwiches.
how_many = pyip.inputInt('How many sandwiches would you like? ', min=1)

# Access dictionary at given key, get price, add together all chosen ingredients = price per sandwich.
price_of_sandwich = (prices[protein]+prices[bread]+prices[cheese_type] +
                     prices[mayo]+prices[mustard]+prices[lettuce]+prices[tomato])
# Price * number of sandwiches gives grand total.
grand_total = how_many * price_of_sandwich

# Tell user what they got, at what cost!
print(f'{how_many} {protein} on {bread} with {cheese_type} cheese, {mayo}, {mustard}, {lettuce}, {tomato}.')
print(f'At ${price_of_sandwich:,.2f} each, your grand total is ${grand_total:,.2f}')
