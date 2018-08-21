import os


class ToDoSession():

    def __init__(self):
        self.todolist = ToDoList()
        self.menu_options = {
            'A': {
                'text': 'Add an Item',
                'action': self.add_item,
                'input_text': 'Enter Item Priority(>0): '
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
        clear = os.system('clear')  # NOQA - Du
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

    def add_item(self, priority):
        input_error = True

        while input_error:
            try:
                priority = int(priority)
            except ValueError:
                priority = -1

            if priority < 0:
                priority = input('\r' + self.menu_options['A']['input_text'])
            else:
                input_error = False

        text = input("Please Enter the Item Text: ")
        self.todolist.add_item(priority, text)

    def remove_item(self, input):
        self.todolist.remove_item(input)


class ToDoList():
    """ A simple class to hold a collection of items that you need ToDo.
    """
    def __init__(self, title=None):
        self.items = []
        self.priorities = {}
        self.title = title or ''
        self.max_priority = 0

    def add_item(self, priority, text):
        self.items.append({
            'text': text,
            'priority': priority
        })
        if priority in self.priorities:
            self.priorities[priority] += 1
        else:
            self.priorities[priority] = 1

        if priority > self.max_priority:
            for index in range(self.max_priority + 1, priority):
                self.priorities[index] = 0
            self.max_priority = priority

    def remove_item(self, key):
        # Cast key to int as input comes as str
        try:
            key = int(key) - 1
        except ValueError:
            return

        # Make sure it's larger than -1 so you don't accidentally delete the last
        # item in the list.
        if -1 < key < len(self.items):
            priority = self.items[key]['priority']
            self.priorities[priority] -= 1
            del(self.items[key])

    def print_list(self):
        print('~~ {} ~~'.format(self.title if self.title else 'ToDo List'))
        print('---------------')
        missing_priorities = []
        for key, value in self.priorities.items():
            if value > 1:
                print('{} - {} '.format(key, value))
            elif value == 0:
                missing_priorities.append(str(key))
        if missing_priorities:
            print('(Missing Priorities: {})'.format(', '.join(missing_priorities)))
        print('---------------')
        if self.items:
            for index, item in enumerate(self.items):
                print('{index}: {priority} - {text}'.format(
                    index=index + 1,
                    priority=item['priority'],
                    text=item['text']
                ))
        else:
            print('Your list is empty!')
        print('---------------\n')
