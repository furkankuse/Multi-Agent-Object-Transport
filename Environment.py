class Environment:
    def __init__(self, maxReward, minReward, env, IndexOfTheObject):
        self._maxReward = maxReward
        self._minReward = minReward
        self._env = env
        self._IndexOfTheObject = IndexOfTheObject
        # will be array of integers
        # zeros will represent empty areas
        # ones will be target area
        # twos will be walls
        # three will be the object

    @property
    def getEnv(self):
        return self._env

    def setIndexOfTheObject(self, indexes):
        self._IndexOfTheObject = indexes

    def setEnv(self, env):
        self._env = env

    def nextState(self, state, agent1action, agent2action):
        # Input : Current state of the game, actions chosen by the agents
        # Output : Next state of the game and reward for given actions

        currentStateAgent1 = state.getAgent1
        nextStateAgent1 = self.generateNextState(currentStateAgent1, agent1action)
        currentStateAgent2 = state.getAgent2
        nextStateAgent2 = self.generateNextState(currentStateAgent2, agent2action)
        agent1IsItOkay, agent2IsItOkay = self.canItBeThere(nextStateAgent1, nextStateAgent2)
        # initial value of reward is 0
        # if one of the agents or both of them grab the object it becomes 1
        # if object carried to the target area it becomes 10
        reward = 0

        # Holding object from both sides
        # Which means, they are moving together
        if (currentStateAgent1[2] == 'holdingLeft' and currentStateAgent2[2] == 'holdingRight') or (
                currentStateAgent2[2] == 'holdingLeft' and currentStateAgent1[2] == 'holdingRight'):
            # Check if both of them try to go same direction
            if agent1action == agent2action:
                #   Check if one of them go in to wall
                if not (agent1IsItOkay and agent2IsItOkay):
                    nextStateAgent1 = currentStateAgent1
                    nextStateAgent2 = currentStateAgent2
                #   if they move
                else:
                    reward = self.moveTheObject(agent2action)

            # Check if they try to go different direction
            else:
                nextStateAgent1 = currentStateAgent1
                nextStateAgent2 = currentStateAgent2

        # **************************************************************************************** #
        # This part might be unnecessary
        # Holding object from one side
        # elif currentStateAgent1[2] == 'holdingLeft' or currentStateAgent1[2] == 'holdingRight' or currentStateAgent2[
        #    2] == 'holdingLeft' or currentStateAgent2[2] == 'holdingRight':
        # Check if the moving one goes into wall
        #    if not (agent1IsItOkay and agent2IsItOkay):
        #        return self.nextStateFormatter(currentStateAgent1, currentStateAgent2, 0)
        # Check if the moving one grabs the object

        # **************************************************************************************** #

        # Case which they move separately
        else:
            # check if agent fail to move
            if not agent1IsItOkay or currentStateAgent1[2] == "holdingLeft" or currentStateAgent1[2] == "holdingRight":
                nextStateAgent1 = currentStateAgent1
            if not agent2IsItOkay or currentStateAgent2[2] == "holdingLeft" or currentStateAgent2[2] == "holdingRight":
                nextStateAgent2 = currentStateAgent2

            if nextStateAgent1[2] != currentStateAgent1[2] or nextStateAgent2[2] != currentStateAgent2[2]:
                reward = self._minReward

        return self.nextStateFormatter(nextStateAgent1, nextStateAgent2, reward)

    def moveTheObject(self, action):
        # This function moves the object to the given direction,
        # and returns the reward for it
        nextIndexes = self.generateNextState([self._IndexOfTheObject[0],self._IndexOfTheObject[1],"free"], action)
        self._env[self._IndexOfTheObject[0]][self._IndexOfTheObject[1]] = 0
        self._IndexOfTheObject = [nextIndexes[0], nextIndexes[1]]
        if self._env[nextIndexes[0]][nextIndexes[1]] == 1:
            return self._maxReward
        else:
            self._env[nextIndexes[0]][nextIndexes[1]] = 3
            return 0

    def canItBeThere(self, indexOfAgent1, indexOfAgent2):
        # This one will check if the agents will be able to move that indexes
        agent1, agent2 = True, True

        # For checking if the agents get on the same index
        if indexOfAgent1[0] == indexOfAgent2[0] and indexOfAgent1[1] == indexOfAgent2[1]:
            agent1, agent2 = False, False

        if indexOfAgent2[2] == indexOfAgent1[2] and indexOfAgent1[2] != "free":
            agent1, agent2 = False, False

        # For checking if the agents go out of the index
        #if 0 > indexOfAgent1[0] or indexOfAgent1[0] >= len(self._env) or 0 > indexOfAgent1[1] or indexOfAgent1[1] >= len(self._env[0]):
        #    agent1 = False

        #if 0 > indexOfAgent2[0] or indexOfAgent2[0] >= len(self._env) or 0 > indexOfAgent2[1] or indexOfAgent2[1] >= len(self._env[0]):
        #    agent2 = False

        # For checking if the agents go into the object or a wall
        if self._env[indexOfAgent1[0]][indexOfAgent1[1]] > 1:
            agent1 = False

        if self._env[indexOfAgent2[0]][indexOfAgent2[1]] > 1:
            agent2 = False

        return agent1, agent2

    def nextCond(self, nextIndexes, currentCond):
        if currentCond != "free":
            return currentCond

        if nextIndexes[1] + 1 < len(self._env) and self._env[nextIndexes[0]][nextIndexes[1] + 1] == 3:
            return "holdingLeft"
        if nextIndexes[1] - 1 >= 0 and self._env[nextIndexes[0]][nextIndexes[1] - 1] == 3:
            return "holdingRight"

        return "free"

    def nextStateFormatter(self, agent1, agent2, reward):
        return [agent1[0], agent1[1], agent1[2], agent2[0], agent2[1], agent2[2]], reward

    def generateNextState(self, currentState, action):
        # Input : Current indexes, and the action taken by the agent
        # Output : Next state of the agent, which includes next indexes and condition of the agent,
        nextState = [currentState[0], currentState[1]]
        if action == 0 and currentState[0] - 1 >= 0:
            nextState[0] = nextState[0] - 1
        elif action == 1 and currentState[1] + 1 < len(self._env[0]):
            nextState[1] = currentState[1] + 1
        elif action == 2 and currentState[0] + 1 < len(self._env):
            nextState[0] = currentState[0] + 1
        elif action == 3 and currentState[1] - 1 >= 0:
            nextState[1] = currentState[1] - 1
        else:
            nextState = [currentState[0], currentState[1]]

        nextState.append(self.nextCond(nextState, currentState[2]))
        return nextState
