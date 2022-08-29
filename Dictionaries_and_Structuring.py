#This module makes dictionaries easier to read.
import pprint
spam = {'color': 'red', 'age':'30'}
print(list(spam.keys())) # You can turn a dictionary into a list by passing it to list function.

for k, v in spam.items(): # Multiple assignment method, to loop through dict items, and use each part of dict.
    print(f"Key:{k} | Value:{v}")

print('color' in spam)
print('color' in spam.keys())
print('30' in spam)

# get() method - checks if key is in dict, and falls back on second value if not.
picnicItems = {'apples':'2', 'bananas':'4'}
print(f"I am bringing {picnicItems.get('apples', 0)} apples, and {picnicItems.get('eggs', 0)} eggs.")

# setdefault('key', 'val') method checks for a key, and if it isn't present, sets key to default value,
# otherwise returns that keys value.

message = "The binding of isaac is a frustrating game."
count = {}

for char in message: # For each character in the str,
    count.setdefault(char, 0) # if char is not in count, set to 0.
    count[char] += 1 # Increase count of char. --> Loop

pprint.pprint(count)

