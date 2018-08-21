import os


class ToDoSession():

    def __init__(self):
        self.todolist = ToDoList()
        self.menu_options = {
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
            'Q': {
                'text': 'Quit',
                'action': None,
                'input_text': None
            }
        }

    def print_menu(self, blank=False):
        clear = os.system('clear')  # NOQA
        self.todolist.print_list()

        if blank:
            print('\n' * len(self.menu_options))
        else:
            for key, option in self.menu_options.items():
                print('{}: {}'.format(key, option['text']))

    def get_user_input(self):
        # Clear the screen and print the updated list
        self.print_menu()

        # Get menu selection from user
        selection = input('\nPlease select an option: ').upper()

        if selection in self.menu_options and self.menu_options[selection]['input_text']:
            self.print_menu(blank=True)
            self.menu_options[selection]['action'](
                input(
                    self.menu_options[selection]['input_text']
                )
            )
        return selection

    def add_item(self, input):
        self.todolist.add_item(input)

    def remove_item(self, input):
        self.todolist.remove_item(input)


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
