def set_inventory(inventory, fruit, quantity=0):
        inventory[fruit] = quantity

def main():
    new_inventory = {}
    set_inventory(new_inventory, 'strawberries', 10)
#testEqual('strawberries' in new_inventory, True)
    print(new_inventory["strawberries"])
#testEqual(new_inventory['strawberries'], 10)
    set_inventory(new_inventory['strawberries'], 10)
    set_inventory(new_inventory, 'strawberries', 25)
#testEqual(new_inventory['strawberries'] , 25)
    print(new_inventory["strawberries"])

if __name__ == '__main__':
    main()