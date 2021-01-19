from State import State
from numpy import argmax
from random import randint

a = State(0, 0, 'holding', 0, 0, 'holding', 5)
b = State(0, 0, 'holding', 0, 0, 'holding', 5)
QTable = [a, b]
print(a.getForComp() == b.getForComp())


def isItANewState(nextStateParameters):
    length = len(QTable)
    for i in range(length):
        if nextStateParameters == QTable[i].getForComp():
            return False
    return True


print(isItANewState([0, 0, 'holding', 0, 0, 'holding']))
print(isItANewState([0, 0, 'holding', 0, 1, 'holding']))
print(argmax([1, 3, 10, 8, 7]))

print('aaba' != 'aaa')
