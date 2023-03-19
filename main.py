inventories = []


def search_inventory():
    if not inventories:
        print('\nInventory empty\n')
        return

    item_search = input('\nSearch by item name or description\nEnter: ')
    if not item_search:
        print('\nPlease enter a search term\n')
        return

    search_results = []
    for my_dict in inventories:
        if item_search.lower() in my_dict['Item name'].lower() \
                or item_search.lower() in my_dict['Description'].lower():
            search_results.append(my_dict)

    if not search_results:
        print('\nThis item or description does not exist\n')
    else:
        for result in search_results:
            for key, value in result.items():
                print(f'{key}: {value}')
            print('-' * 15)


def update_quantity():
    if not inventories:
        print('\nInventory empty\n')
        return

    item_for_update = input('Enter the name of the item to update: ')
    if not item_for_update:
        print('\nItem name cannot be empty\n')
        return

    for item in inventories:
        if item['Item name'] == item_for_update:
            try:
                new_quantity = int(input('Enter new quantity: '))
                item['Quantity'] = new_quantity
                print('\nSuccessful update\n')
                break
            except ValueError as e:
                print("Value Error occurred: ", e)
    else:
        print('\nThis item does not exist\n')


def remove_inventory():
    if not inventories:
        print('\nInventory empty\n')
        return

    item_name = input('Enter the name of the item to remove: ')
    try:
        item_to_remove = list(filter(lambda x: x['Item name'] == item_name, inventories))[0]
        inventories.remove(item_to_remove)
        print('\nSuccessful removal\n')
    except IndexError:
        print('\nThis item does not exist\n')


def view_inventory():
    if not inventories:
        print('\nInventory empty\n')
        return

    for item in inventories:
        print('-' * 15)
        print('\n'.join([f'{key}: {value}' for key, value in item.items()]))


def add_item():
    item_name = input('Name of item: ')
    description = input('Description of item: ')

    try:
        quantity = int(input('Quantity of item: '))
        new_item = {
            'Item name': item_name,
            'Description': description,
            'Quantity': quantity
        }
        inventories.append(new_item)
        print('\nSuccessfully added to inventory\n')
    except ValueError as e:
        print("Value Error occurred: ", e)


def menu():
    print('1. View Inventory')
    print('2. Add Item')
    print('3. Remove Item')
    print('4. Update Quantity')
    print('5. Search Inventory')
    print('q/Q for Quit')

    choice = input('\nEnter your choice: ')
    if not choice:
        print('\nPlease enter a search term\n')
        return None
    return choice


def main():
    print('---Inventory System---\n')
    while True:
        choice = menu()

        if choice == '1':
            view_inventory()
        elif choice == '2':
            add_item()
        elif choice == '3':
            remove_inventory()
        elif choice == '4':
            update_quantity()
        elif choice == '5':
            search_inventory()
        elif choice and choice in 'qQ':
            print('Quitting the program')
            break
        else:
            print('\nInvalid choice. Try again.\n')


if __name__ == '__main__':
    main()
