from State import State
import random


class Agent:

    def __init__(self, startState, epsilon, epsilonDecayRate, learningRate, discountRate):
        self._epsilon = epsilon
        self._epsilonDecay = epsilonDecayRate
        self._learningRate = learningRate
        self._discountRate = discountRate
        self._QTable = []
        self._currentState = startState

    def setCurrentState(self, state):
        self._currentState = state

    def addNewState(self, agent1X, agent1Y, agent1Con, agent2X, agent2Y, agent2Con):
        self._QTable.append(State(agent1X, agent1Y, agent1Con, agent2X, agent2Y, agent2Con, 5))

    def isItANewState(self, nextStateParameters):
        length = len(self._QTable)
        for i in range(length):
            if nextStateParameters == self._QTable[i].getForComp():
                return False, self._QTable[i]
        return True, None

    def updateQValue(self, reward, action, nextState):
        val = reward + self._discountRate * nextState.getMaxQValue - self._currentState.getQValue(action)
        val = self._currentState.getQValue(action) + self._learningRate * val
        nextState.updateQValue(val, action)

    def actionChooser(self, epsilon):
        if random.randint(1, 100000) <= epsilon * 100000:
            return random.randint(0, 4)
        else:
            return self._currentState.getMaxQIndex
