from numpy import argmax


class State:

    def __init__(self, agent1X, agent1Y, agent1Con, agent2X, agent2Y, agent2Con, actionSize):
        self._agent1X = agent1X
        self._agent1Y = agent1Y
        self._agent1Con = agent1Con
        self._agent2X = agent2X
        self._agent2Y = agent2Y
        self._agent2Con = agent2Con
        self._actionSize = actionSize
        self._QValues = []
        for i in range(actionSize):
            self._QValues.append(0)

    @property
    def getAgent1(self):
        return [self._agent1X, self._agent1Y, self._agent1Con]

    @property
    def getAgent2(self):
        return [self._agent2X, self._agent2Y, self._agent2Con]

    def updateQValue(self, newValue, action):
        self._QValues[action] = newValue

    def getForComp(self):
        return [self._agent1X, self._agent1Y, self._agent1Con, self._agent2X, self._agent2Y, self._agent2Con]

    @property
    def getQValue(self, action):
        return self._QValues[action]

    def getMaxQValue(self):
        return max(self._QValues)

    def getMaxQIndex(self):
        return argmax(self._QValues)