parkA = []  # Can Park
parkB = []  # Cannot Park


def isAvailable():
    if 0 <= len(parkA) < 4:
        return True
    else:
        return False


def status():
    s = 'Park : '
    for i in range(len(parkA)):
        s = s + parkA[i] + ' '
    return s


def park(name):
    if isAvailable():
        parkA.append(name)
        print(name + ' Parked (' + str(4 - len(parkA)) + ' Available)')
    else:
        print(name + ' Cannot Park Here')


def moveBack():
    q = ''
    if len(parkB) == 0:
        return q
    else:
        for i in range(len(parkB)):
            tmp = parkB.pop()
            q = q + 'push ' + tmp + ' '
            parkA.append(tmp)
        return q


def depart(name):
    q = ''
    c = parkA[::-1]
    if len(parkA) == 0:
        print('No Car Parked Here')
    elif name in c:
        for i, s in enumerate(c):
            if s == name:
                parkA.pop()
                print(name + ' Departed!')
                print('How to depart >> ' + q + 'pop ' + name  + ' ' + moveBack())
                break
            else:
                tmp = parkA.pop()
                q = q + 'pop ' + tmp + ' '
                parkB.append(tmp)
    else:
        print('No ' + name + ' Here')


depart('A')
park('A')
park('B')
park('C')
park('D')
park('E')
print(status())
depart('A')
print(status())
depart('B')
print(status())
park('A')
print(status())
