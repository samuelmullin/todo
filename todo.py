from classes import ToDoSession


def main():
    # Create empty ToDoList
    session = ToDoSession()
    selection = ''

    while selection != 'Q':
        selection = session.get_user_input()

if __name__ == "__main__":
    main()
