def display_inventory(inventory):
    totalItems = 0
    print("Inventory:")
    for key,value in inventory.items():
        totalItems += value
        print(value,key)
    print("Total number of items: {}".format(totalItems))


def add_to_inventory(inventory,items):
    tempValue = 0
    for item in items:
        if item in inventory:
            tempValue = inventory.get(item)
            tempValue += 1
            inventory[item] = int(tempValue)
        else:
            inventory[item] = 1
    display_inventory(inventory)


def sortInventory(inventory,order):
    order = order.lower()
    if order == "count,desc":
        sortedInv = [v[0] for v in sorted(inventory.items(), key=lambda kv: (-kv[1], kv[0]))]
        return sortedInv
    elif order == "count,asc":
        sortedInv = [v[0] for v in sorted(inventory.items(), key=lambda kv: (-kv[1], kv[0]))]
        sortedInv = sortedInv[::-1]
        return sortedInv


def print_table(inventory,order):
    max_lenKey = 0
    max_lenVal = 0
    #maximum_key = max(len(x) for x in inventory)
    for key,value in inventory.items():
        if len(key) > max_lenKey:
            max_lenKey = len(key)
        elif len(str(value)) > max_lenVal:
            max_lenVal = len(str(value))
    STRINGLENGHT = max_lenVal + max_lenKey + 10
    if order:
        if order == "count,desc":
            items = sortInventory(inventory,"count,desc")
            print(items)
            print("Inventory: ")
            print('{text1:>{len1}}{text2:>{len2}}'.format(text1='count ',
                text2='item name', len1=max_lenKey, len2=STRINGLENGHT))
            print('-'*(STRINGLENGHT+10))
            for element in items:
                    print('{cnt:>{len1}}{item:>{len2}}'.format(cnt=inventory[element]
                    ,len1 = max_lenKey, item=element, len2=STRINGLENGHT))




###TEST ENVIROMENT###
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#   add_to_inventory(inv,loot)
print_table(inv,"count,desc")
###END OF TESTING ###
