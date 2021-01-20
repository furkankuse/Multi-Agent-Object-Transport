from State import State
from Agent import Agent
from Environment import Environment
startState = State(5, 0, "free", 5, 4, "free", 5)
env = [[0, 0, 1, 1, 1, 0, 0],
       [0, 0, 0, 2, 0, 0, 0],
       [0, 0, 0, 3, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0],
       [2, 2, 0, 2, 2, 2, 2],
       [0, 0, 0, 0, 0, 0, 2]]
environment = Environment(10, 1, env, [2, 3])
epsilon = .3
epsilonDecay = .001
learningRate = .4
discountRate = .95
agent1 = Agent(startState, epsilon, epsilonDecay, learningRate, discountRate, "bir")
agent2 = Agent(startState, epsilon, epsilonDecay, learningRate, discountRate, "iki")

for i in range(15):
    agent1.setCurrentState(startState)
    agent2.setCurrentState(startState)
    environment.setEnv(env)
    j = 0
    while True:
        action1 = agent1.actionChooser()
        action2 = agent2.actionChooser()
        nextStateParameters, reward = environment.nextState(agent1.getCurrentState, action1, action2)
        agent1.stateUpdate(nextStateParameters, reward, action1)
        agent2.stateUpdate(nextStateParameters, reward, action2)
        print(action1, end=" ")
        print(action2)
        print(nextStateParameters, end=" ")
        print(reward)
        j += 1
        if j == 100:
            print("*")
            break
        if reward == 10:
            print("One episode is finished")
            break
