shopping_list = []

while True:
    command = input("please enter your commmand: ")

    if command == 'exit':
        exit(0)

    if command == 'add-item':
        item = input("please enter the item: ")
        shopping_list.append(item)

    if command == 'list-items':
        for i, item in enumerate(shopping_list):
            print(f'{i}: {item}')

    if command == 'remove-item':
        index = int(input("please enter the item index: "))
        deleted_item = shopping_list.pop(index)
        print(f"successfully deleted '{deleted_item}' ")