class ToDoList():
    """ A simple class to hold a collection of items that you need ToDo.
    """
    def __init__(self):
        self.items = []

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
        print('~~ ToDo List ~~')
        print('---------------')
        if self.items:
            for index, item in enumerate(self.items):
                print('{}: {}'.format(index + 1, item))
        else:
            print('Your list is empty!')
        print('---------------\n')
