from classes import ToDoList
from functions import get_user_input


def main():
    # Create empty ToDoList
    todolist = ToDoList()
    selection = ''

    while selection != 'Q':
        selection, user_input = get_user_input(todolist)

        # Add or remove items as necessary
        if selection == 'A':
            todolist.add_item(user_input)
        elif selection == 'R':
            todolist.remove_item(user_input)


if __name__ == "__main__":
    main()
