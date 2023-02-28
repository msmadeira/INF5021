import gymnasium as gym
import numpy as np
import random
import matplotlib.pyplot as plt
import sys

# get debug argument
debug = sys.argv[1] == 'True'

# Setting hyperparameters
alpha = 0.7
discount_factor = 0.618
epsilon = 1
max_epsilon = 1
min_epsilon = 0.01
decay = 0.01

# training variables
num_training_episodes = 100

env = gym.make("BipedalWalker-v3")

# create lists to keep track of reward and epsilon
training_rewards = []
epsilons = []

# Each of this episode is its own game.
action_size = env.action_space.shape[0]
for episode in range(num_training_episodes):
    state, info = env.reset()

    total_training_rewards = 0

    while True:
        action = np.random.uniform(-1.0, 1.0, size=action_size)

        # perform action and get reward and next state
        new_state, reward, done, truncated, info = env.step(action)


        total_training_rewards += reward
        state = new_state

        if done or truncated:
            break

    # add total reward and reduced epsilon values
    training_rewards.append(total_training_rewards)
    epsilons.append(epsilon)

print("Training score over time: " + str(sum(training_rewards) / num_training_episodes))

# plot graphs
if debug:
    # Visualizing results and total reward over all episodes
    x = range(num_training_episodes)
    plt.plot(x, training_rewards)
    plt.xlabel('Episode')
    plt.ylabel('Training total reward')
    plt.title('Total rewards over all episodes in training')
    plt.show()