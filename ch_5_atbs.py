
# An example of a nested dictionary. Each main item in the dict, \
# or the person, has a set of things and how many they are bringing.
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
            'Bob':{'ham sandwiches':3, 'apples':2},
            'Carol': {'cups': 3, 'apple pies': 1}}

# This function takes listed dictionary, and an item to search for.
# Set counter to 0
def totalBrought(guests, item):
    numBrought = 0
    # for k,v -- for key/value (because get() returns both key and value) in dictionary passed in.
    for k, v in guests.items():
        # searches for item passed in as parameter, and if not found, returns 0.
        numBrought = numBrought + v.get(item, 0)
    return numBrought


print('Number of things being brought')
print("Apples- " + str(totalBrought(allGuests, "apples")))
print("Cakes- " + str(totalBrought(allGuests, "cake"))) # <-- This prints 0 because it uses the fallback value you fed it.


# Empty Dictionary?
example_dictionary = {}
# 2
example_dictionary = {'foo':42}
# 3 Main difference between list and dictionary.
# Dictionaries consist of key:value pairs. Unlike lists, dictionaries are unordered (can't be sliced either.)
# 4 KeyError
# 5 
# There is no difference. If 'cat' is a value, it will print in both, otherwise, if it is a key, it will not be accessed on the \
# second call.
# 6 
# Basically same as answer above but sub out value for key.
# 7 
# spam.setdefault('color', 'black') - if color is not in spam as a key, create it, and give it value of black. If it exists \
# The color will remain as it is, not change due to this command.
# 8
#pprint


