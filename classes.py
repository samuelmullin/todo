import os


class ToDoSession():

    def __init__(self):
        self.lists = []
        self.active_list = None
        self.parent_menu_options = {
            'C': {
                'text': 'Create a List',
                'action': self.create_list,
                'input_text': 'Enter new List Title: '
            },
            'D': {
                'text': 'Delete a List',
                'action': self.delete_list,
                'input_text': 'Enter List # to Delete: '
            },
            'S': {
                'text': 'Select a List',
                'action': self.set_active_list,
                'input_text': 'Enter List # to View: '
            },
            'Q': {
                'text': 'Quit',
                'action': None,
                'input_text': None
            }
        }

        self.child_menu_options = {
            'A': {
                'text': 'Add an Item',
                'action': self.add_item,
                'input_text': 'Enter new Item Text: '
            },
            'R': {
                'text': 'Remove an Item',
                'action': self.remove_item,
                'input_text': 'Enter Item # to Delete: '
            },
            'B': {
                'text': 'Return to All List View',
                'action': self.unset_active_list,
                'input_text': None

            },
            'Q': {
                'text': 'Quit',
                'action': None,
                'input_text': None
            }
        }

    def create_list(self, input):
        self.lists.append(ToDoList(title=input))

    def input_to_index(self, input):
        try:
            index = int(input) - 1
        except ValueError:
            index = None

        return index

    def delete_list(self, input):
        index = self.input_to_index(input)

        if index is None:
            return

        if -1 < index < len(self.lists):
            del(self.lists[int(index)])

    def set_active_list(self, input):
        index = self.input_to_index(input)

        if index is None:
            return

        if -1 < index < len(self.lists):
            self.active_list = self.lists[index]

    def unset_active_list(self):
        self.active_list = None

    def print_lists(self):
        print('~~ All Lists ~~')
        print('---------------')
        if self.lists:
            for index, todolist in enumerate(self.lists):
                print('{}: {}'.format(index + 1, todolist.title if todolist.title else 'No Title'))
        else:
            print('You Have no Lists!')
        print('---------------\n')

    def print_menu(self, blank=False):
        clear = os.system('clear')  # Dump in a var so it doesn't print a 0.

        if self.active_list:
            self.active_list.print_list()
        else:
            self.print_lists()

        active_menu = self.child_menu_options if self.active_list else self.parent_menu_options

        if blank:
            print('\n' * len(active_menu))
        else:
            for key, option in active_menu.items():
                print('{}: {}'.format(key, option['text']))

    def get_user_input(self):
        # Clear the screen and print the updated list
        self.print_menu()

        # Get menu selection from user
        selection = input('\nPlease select an option: ').upper()

        active_menu = self.child_menu_options if self.active_list else self.parent_menu_options

        if selection in active_menu and active_menu[selection]['action']:
            self.print_menu(blank=True)
            if active_menu[selection]['input_text']:
                active_menu[selection]['action'](input(active_menu[selection]['input_text']))
            else:
                active_menu[selection]['action']()

        return selection

    def add_item(self, input):
        self.active_list.add_item(input)

    def remove_item(self, input):
        self.active_list.remove_item(input)


class ToDoList():
    """ A simple class to hold a collection of items that you need ToDo.
    """
    def __init__(self, title=None):
        self.items = []
        self.title = title or ''

    def add_item(self, text):
        self.items.append(text)

    def remove_item(self, key):
        # Cast key to int as input comes as str
        try:
            key = int(key) - 1
        except ValueError:
            return

        # Make sure it's larger than -1 so you don't accidentally delete the last
        # item in the list.
        if -1 < key < len(self.items):
            del(self.items[key])

    def print_list(self):
        print('~~ {} ~~'.format(self.title if self.title else 'ToDo List'))
        print('---------------')
        if self.items:
            for index, item in enumerate(self.items):
                print('{}: {}'.format(index + 1, item))
        else:
            print('Your list is empty!')
        print('---------------\n')
