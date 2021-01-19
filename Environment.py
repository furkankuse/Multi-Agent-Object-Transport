class Environment:
    def __init__(self, maxReward, minReward, env):
        self._maxReward = maxReward
        self._minReward = minReward
        self.env = env

    def nextState(self, state, agent1action, agent2action):
        # Input : Current state of the game, actions chosen by the agents
        # Output : Next state of the game and reward for given actions

        currentStateAgent1 = state.getAgent1
        nextStateAgent1 = self.nextIndexes([currentStateAgent1[0], currentStateAgent1[1]], agent1action)
        currentStateAgent2 = state.getAgent2
        nextStateAgent2 = self.nextIndexes([currentStateAgent2[0], currentStateAgent2[1]], agent2action)
        agent1IsItOkay, agent2IsItOkay = self.canItBeThere(nextStateAgent1, nextStateAgent2)

        # Holding object from both sides
        if (currentStateAgent1[2] == 'holdingLeft' and currentStateAgent2[2] == 'holdingRight') or (
                currentStateAgent2[2] == 'holdingLeft' and currentStateAgent1[2] == 'holdingRight'):
            # Check if both of them try to go same direction
            if agent1action == agent2action:
                #   Check if one of them go in to wall
                if not (agent1IsItOkay and agent2IsItOkay):
                    return self.nextStateFormater(currentStateAgent1, currentStateAgent2, 0)
                #   Check if they reach the
            # Check if they try to go different direction
            else:
                return self.nextStateFormater(currentStateAgent1, currentStateAgent2, 0)
        # Holding object from one side
        elif currentStateAgent1[2] == 'holdingLeft' or currentStateAgent1[2] == 'holdingRight' or currentStateAgent2[
            2] == 'holdingLeft' or currentStateAgent2[2] == 'holdingRight':
            # Check if the moving one goes into wall
            if not (agent1IsItOkay and agent2IsItOkay):
                return self.nextStateFormater(currentStateAgent1, currentStateAgent2, 0)
            # Check if the moving one grabs the object

        # None of them holding
        else:
            pass


    def canItBeThere(self, indexOfAgent1, indexOfAgent2):
        # This one will check if the agents will be able to move that indexes
        pass

    def nextCond(self, nextIndexes):
        pass

    def nextStateFormater(self, agent1, agent2, reward):
        return [agent1[0], agent1[1], agent1[2], agent2[0], agent2[1], agent2[2]], reward

    def nextState(self, currentIndex, action):
        # Input : Current indexes, and the action taken by the agent
        # Output : Next state of the agent, which includes next indexes and condition of the agent,
        if action == 0:
            nextIndexes = [currentIndex[0], currentIndex[1] - 1]
        elif action == 1:
            [currentIndex[0] + 1, currentIndex[1]]
        elif action == 2:
            [currentIndex[0], currentIndex[1] + 1]
        elif action == 3:
            [currentIndex[0] - 1, currentIndex[1]]
        else:
            [currentIndex[0], currentIndex[1]]

        nextIndexes.append(self.nextCond())
        return nextIndexes
