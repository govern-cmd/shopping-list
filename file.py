shopping_list =[]
while True:
    add_item = input("Enter item: ")
    shopping_list.append(add_item)
    quit = input("Press Enter to continue or q to quit")

    if quit != '':
        break
    print("Final shopping List")

    print(shopping_list)


