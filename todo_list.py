print("Hello and welcome to the todo list program!")

todo_list = {}


def add_things():
    name = input("Please enter your name:")
    things_to_do = input("Please enter a thing you want to do:")
    if things_to_do in todo_list:
        print("This thing to do is already here please enter another!")

    else:
        todo_list[name] = things_to_do
        print(f"{name} added a new thing to do.")


def search_for_a_name():
    name = input("Please enter your name to search:")

    if name not in todo_list:
        print("This thing is not in our todo list!")

    else:
        print(f"{name} has to {todo_list[name]}")


def change_things():
    old_name = input("Please enter the old name to change:")
    new_name = input("Please enter a new name you want to change:")
    new_things_todo = input("Please enter the new things todo:")

    if old_name in todo_list:
        todo_list[new_name] = new_things_todo
        todo_list.pop(old_name)
        print(f"Changed the {old_name} with {new_name} and new things todo")

    else:
        print("The old name is not in our list please enter a new name!")


def remove_names():
    name = input("Enter a name to remove:")

    if name in todo_list:
        todo_list.pop(name)
        print(f"Removed {name} from our list!")

    else:
        print("The name is not in our list!")


def see_everything_in_our_todo_list():
    if todo_list:
        for name, thing_to_do in todo_list.items():
            print(f"{name} has to {thing_to_do}")

    else:
        print("There is nothing in our list please go and add something!")


while True:
    print()
    print("1. Add things to do in our list")
    print("2. Search for a thing")
    print("3. Change things")
    print("4. Remove things from our list")
    print("5. See what is in our list")
    print("6. Exit our program")

    choice = int(input("Enter your choice(1, 2, 3, 4, 5, 6):"))

    if choice == 1:
        add_things()

    elif choice == 2:
        search_for_a_name()

    elif choice == 3:
        change_things()

    elif choice == 4:
        remove_names()

    elif choice == 5:
        see_everything_in_our_todo_list()

    elif choice == 6:
        print("Exiting goodbye................")
        break

    else:
        print("Please enter a number(1, 2, 3, 4, 5, 6)")
