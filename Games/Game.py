from Agents.State import State
from Agents.SingleQAgent import Agent
from Environment.Environment import Environment
import copy

startState = State(5, 0, "free", 5, 4, "free", 5)
env = [[0, 0, 1, 1, 1, 0, 0],
       [0, 0, 0, 2, 0, 0, 0],
       [0, 0, 0, 3, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0],
       [2, 2, 0, 2, 2, 2, 2],
       [0, 0, 0, 0, 0, 0, 2]]
environment = Environment(10, 1, copy.deepcopy(env), [2, 3])
epsilon = .8
epsilonDecay = .9
learningRate = .1
discountRate = .98
agent1 = Agent(startState, epsilon, epsilonDecay, learningRate, discountRate, "first")
agent2 = Agent(startState, epsilon, epsilonDecay, learningRate, discountRate, "second")

for i in range(100):
    agent1.setCurrentState(startState)
    agent2.setCurrentState(startState)
    environment.setEnv(copy.deepcopy(env))
    environment.setIndexOfTheObject([2, 3])
    k = 0
    filename = "Outputs/episode_" + str(i + 1) + ".txt"
    f = open(filename, "w")
    while True:
        action1 = agent1.actionChooser()
        action2 = agent2.actionChooser()
        nextStateParameters, rewards = environment.nextState(agent1.getCurrentState, action1, action2)
        agent1.stateUpdate(nextStateParameters, rewards[0], action1)
        agent2.stateUpdate(nextStateParameters, rewards[1], action2)
        out = "action of agent1 = " + str(action1) + ", action of agent2 = " + str(action2) + "\n"
        out += "next state = " + str(nextStateParameters) + ", reward of agent1 = " + str(rewards[0]) + ", reward of agent2 = " + str(rewards[1]) + "\n"
        f.write(out)
        k += 1
        if rewards[0] == 10:
            print("One episode is finished for i = " + str(i + 1))
            break
    f.close()
    agent1.epsilonDecay()
    agent2.epsilonDecay()
