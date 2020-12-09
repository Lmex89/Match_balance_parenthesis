
class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):

        if self.items:
            return self.items.pop()

    def size(self):

        if self.items:
            return len(self.items)

    def is_empty(self):

        if self.items == []:
            return True

        return False


def match_balance(string):

    closing_dict = {
        '(': 1,
        '[': 2,
        '{': 3,
        ')': -1,
        ']': -2,
        '}': -3,
    }

    total = 0
    mystack = Stack()
    for i in (string):
        mystack.push(closing_dict[i])

    while not mystack.is_empty():
        total += mystack.pop()

    if total == 0:
        return True

    return False


print(match_balance("({([[]])}"))
