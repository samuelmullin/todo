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
            key = int(key)
        except ValueError:
            return

        if key < len(self.items):
            del(self.items[key])

    def print_list(self):
        print('~~ ToDo List ~~')
        print('---------------')
        if self.items:
            for index, item in enumerate(self.items):
                print('{}: {}'.format(index, item))
        else:
            print('Your list is empty!')
        print('---------------\n')
