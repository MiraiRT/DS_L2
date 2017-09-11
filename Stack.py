class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, i):
        self.items.append(i)


s = Stack()
print(s.items)
s1 = Stack(['A', 'B'])
print(s1.items)
s.push(1)
s1.push('C')
print(s.items)
print(s1.items)
