

def read_inventory():
    inventory = []
    with open('item.txt', 'r') as file:
        for line in file:
            sn, name, description, price, quantity = line.strip().split(',')
            price = int(price[1:].strip())
            quantity = int(quantity.strip())
            inventory.append([int(sn), name, description, price, quantity])
    return inventory