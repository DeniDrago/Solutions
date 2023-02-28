inventories = []


def search_inventory():
    if inventories:
        search = input('1 - Search by item name\n2 - Search by description\nEnter: ')
        if search == '1':
            item_search = input('Enter name of item: ')
            for my_dict in inventories:
                if item_search in my_dict['Item name']:
                    for key, value in my_dict.items():
                        print(f'{key}: {value}')
                else:
                    print('\nThis item does not exist\n')
        elif search == '2':
            description_search = input('Enter description of item: ')
            for my_dict in inventories:
                if description_search in my_dict['Description']:
                    for key, value in my_dict.items():
                        print(f'{key}: {value}')
                else:
                    print('\nThis description does not exist\n')
        else:
            print('\nThis option does not exist, try again\n')
    else:
        print("\nInventory empty\n")


def update_quantity():
    if inventories:
        item_for_update = input('Enter name of item to update quantity: ')
        for my_dict in inventories:
            if my_dict['Item name'] == item_for_update:
                new_quantity = int(input('Enter new quantity: '))
                my_dict['Quantity'] = new_quantity
                print('\nSuccessful update\n')
            else:
                print('\nThis item does not exist\n')
    else:
        print("\nInventory empty\n")


def remove_inventory():
    if inventories:
        remove = input('Enter name of item to remove: ')
        for my_dict in inventories:
            if my_dict['Item name'] == remove:
                inventories.remove(my_dict)
                print('\nSuccessful removal\n')
            else:
                print('\nThis item does not exist\n')
    else:
        print("\nInventory empty\n")


def view_inventory():
    output = ""
    if inventories:
        for my_dict in inventories:
            for key, value in my_dict.items():
                output += f'{key}: {value}\n'
            output += ('-' * 15 + '\n')
    else:
        output = "\nInventory empty\n"
    print(output)


def add_item():
    item_name = input('Name of item: ')
    description = input('Description of item: ')
    quantity = int(input('Quantity of item: '))
    inventory = {
        'Item name': item_name,
        'Description': description,
        'Quantity': quantity
    }
    inventories.append(inventory)
    print('\nSuccessfully added to inventory\n')


def menu():
    print('1. View Inventory')
    print('2. Add Item')
    print('3. Remove Item')
    print('4. Update Quantity')
    print('5. Search Inventory')
    print('q/Q for Quit')

    choice = input('\nEnter your choice: ')
    return choice


if __name__ == '__main__':
    print('---Inventory System---\n')
    while True:
        choose_menu = menu()
        if choose_menu == '1':
            view_inventory()
        elif choose_menu == '2':
            add_item()
        elif choose_menu == '3':
            remove_inventory()
        elif choose_menu == '4':
            update_quantity()
        elif choose_menu == '5':
            search_inventory()
        elif choose_menu in 'qQ':
            break
        else:
            print('\nThis option does not exist, try again\n')
