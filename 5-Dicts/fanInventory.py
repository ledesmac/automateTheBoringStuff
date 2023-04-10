#! python3
# fanInventory.py - program to store and display characters inventory for RPGs
#

def displayInventory(inv: dict):
    count = 0
    print("Inventory: ")
    for key in inv.keys():
        count += int(inv[key])
        print(f'{inv[key]} {key}')
    
    print(f'Total number of items: {count}')

# Test Inventory
#stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#displayInventory(stuff)

def addToInventory(inv: dict, newItems):
    for i in newItems:
        if i in inv.keys():
            inv[i] += 1
        else:
            inv[i] = 1

    return inv

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)