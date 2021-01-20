from State import State
import random


class Agent:

    def __init__(self, startState, epsilon, epsilonDecayRate, learningRate, discountRate, name):
        self._epsilon = epsilon
        self._epsilonDecay = epsilonDecayRate
        self._learningRate = learningRate
        self._discountRate = discountRate
        self._QTable = []
        self._currentState = startState
        self._QTable.append(startState)
        self._name = name
    @property
    def getCurrentState(self):
        return self._currentState

    def setCurrentState(self, state):
        self._currentState = state

    def addNewState(self, nextStateParameters):
        self._QTable.append(State(nextStateParameters[0], nextStateParameters[1], nextStateParameters[2], nextStateParameters[3], nextStateParameters[4], nextStateParameters[5], 5))

    def isItANewState(self, nextStateParameters):
        length = len(self._QTable)
        for i in range(length):
            a = self._QTable[i].getForComp()
            if nextStateParameters == self._QTable[i].getForComp():
                return False, self._QTable[i]
        return True, None

    def calcQValue(self, reward, action, nextState):
        val = reward + self._discountRate * nextState.getMaxQValue() - self._currentState.getQValue(action)
        val = self._currentState.getQValue(action) + self._learningRate * val
        nextState.updateQValue(val, action)

    def stateUpdate(self, nextStateParameters, reward, action):
        isItNew, nextState = self.isItANewState(nextStateParameters)
        if isItNew:
            self.addNewState(nextStateParameters)
            nextState = self._QTable[len(self._QTable) - 1]

        self.calcQValue(reward, action, nextState)
        self._currentState = nextState
        #self._epsilon -= self._epsilonDecay

    def actionChooser(self):
        if random.randint(1, 100000) <= self._epsilon * 100000:
            return random.randint(0, 4)
        else:
            return self._currentState.getMaxQIndex()
