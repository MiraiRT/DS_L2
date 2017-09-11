class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, o):
        self.items.append(o)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]


s = Stack()
name = 'Rachata'
for i in range(0, len(name)):
    s.push(name[i])
print(s.items)
for i in range(0, len(s.items)):
    print(s.items[i], end='')
print()
print(s.size())
print(s.isEmpty())
print(s.peek())
for i in range(0, len(name)):
    s.pop()
    print(s.items)
