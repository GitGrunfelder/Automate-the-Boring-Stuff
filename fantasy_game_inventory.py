# Takes a given inventory and returns a message
# of # of each and total items in inventory.

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

'''This is a function that tracks items in inventory, and shows type and count for each
For each item and count, increase count by count. '''
def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        item_total += v
    print(f'Total number of items: {item_total}')

'''This function takes a given inventory and loot,
and returns an updated inventory with loot added to current inventory.'''
def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1
    return inventory
    
displayInventory(inv)
inv = addToInventory(inv, dragonLoot)
print('\nAnd below we find the updated inventory!\n')
displayInventory(inv)