import os


def get_user_input(todolist):
    # Clear the screen and print the updated list
    print_menu(todolist)

    # Get menu selection from user
    selection = input('\n Please select an option: ').upper()
    user_input = ''

    # If the option requires further input, get it
    if selection == 'A':
        print_menu(todolist, blank=True)
        message = 'Enter New Item Text: '
    elif selection == 'R':
        print_menu(todolist, blank=True)
        message = 'Enter Item # to Delete: '
    else:
        message = None

    user_input = input(message) if message else ''

    return (selection, user_input,)


def print_menu(todolist, blank=False):
    clear = os.system('clear')  # Dump in a var so it doesn't print a 0.
    todolist.print_list()

    base_options = {
        'A': 'Add an Item',
        'R': 'Remove an Item',
        'Q': 'Quit'
    }

    if blank:
        print('\n' * len(base_options))
    else:
        for key, option in base_options.items():
            print('{}: {}'.format(key, option))
