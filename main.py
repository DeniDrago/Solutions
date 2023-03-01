inventories = []


def search_inventory():
    if not inventories:
        print('\nInventory empty\n')
        return

    item_search = input('\nSearch by item name or description\nEnter: ')
    found = False   # Флаг для отслеживания, были ли найдены результаты
    for my_dict in inventories:
        if item_search in my_dict['Item name'] or item_search in my_dict['Description']:
            for key, value in my_dict.items():
                print(f'{key}: {value}')
            print('-' * 15)
            found = True    # Установка флага, если результат найден
    if not found:   # Проверка флага после цикла
        print('\nThis item or description does not exist\n')


def update_quantity():
    if not inventories:
        print('\nInventory empty\n')
        return

    item_for_update = input('Enter name of item to update quantity: ')
    found = False
    for my_dict in inventories:
        if my_dict['Item name'] == item_for_update:
            new_quantity = int(input('Enter new quantity: '))
            my_dict['Quantity'] = new_quantity
            print('\nSuccessful update\n')
            found = True
    if not found:
        print('\nThis item does not exist\n')


def remove_inventory():
    if not inventories:
        print('\nInventory empty\n')
        return

    remove = input('Enter name of item to remove: ')
    found = False
    for my_dict in inventories:
        if my_dict['Item name'] == remove:
            inventories.remove(my_dict)
            print('\nSuccessful removal\n')
            found = True
    if not found:
        print('\nThis item does not exist\n')


def view_inventory():
    if not inventories:
        print('\nInventory empty\n')
        return
    for my_dict in inventories:
        for key, value in my_dict.items():
            print(f'{key}: {value}')
        print('-' * 15)


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
