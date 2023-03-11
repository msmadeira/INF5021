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
# greater value (used to save time iterating over whole array)
greater_value_action = []
greater_value = 0

# training variables
num_training_episodes = 500

env = gym.make("BipedalWalker-v3")

# create lists to keep track of reward and epsilon
training_rewards = []
epsilons = []

def find_closest(arr, val):
    idx = np.abs(arr - val).argmin()
    return arr[idx]


def stringify_action(action):
    return str(action[0]) + ';' + str(action[1]) + ';' + str(action[2]) + ';' + str(action[3])


def parse_action(string_action):
    return np.array([float(x) for x in string_action.split(';')])


def get_action_with_highest_reward_from_state(st):
    return max(Q[st], key=Q[st].get)


def get_random_action():
    global action_space
    return np.array([random.choice(action_space), random.choice(action_space), random.choice(action_space), random.choice(action_space)])


# discretization: action space
action_space = np.around(np.arange(start=env.action_space.low[0], stop=env.action_space.high[0], step=0.1), 1)
action_space_dictionary = {}
for i in range(action_space.size):
    key1 = str(action_space[i])
    for j in range(action_space.size):
        key2 = key1 + ';' + str(action_space[j])
        for k in range(action_space.size):
            key3 = key2 + ';' + str(action_space[k])
            for m in range(action_space.size):
                key4 = key3 + ';' + str(action_space[m])
                action_space_dictionary[key4] = 0


# discretization: observation space
number_of_observation_parameters = 1
hull_angle_speed_parameters = []

for i in range(number_of_observation_parameters):
    low = env.observation_space.low[i]
    high = env.observation_space.high[i]
    hull_angle_speed_parameters = np.around(np.arange(start=low, stop=high, step=0.1), 2)


# initialize Q-table
Q = {}
for i in range(hull_angle_speed_parameters.size):
    Q[hull_angle_speed_parameters[i]] = action_space_dictionary.copy()

# Each of this episode is its own game.
action_size = env.action_space.shape[0]
for episode in range(num_training_episodes):
    state, info = env.reset()

    # print(find_closest(hull_angle_speed_parameters, state[0]))
    # print(hull_angle_speed_parameters)
    # print(state[0])

    total_training_rewards = 0

    while True:
        # choose action given the states based on a random number
        exp_exp_tradeoff = random.uniform(0, 1)

        # if rng larger than epsilon: exploitation
        if exp_exp_tradeoff > epsilon:
            # get action in dictionary with the highest reward and parse it
            action = greater_value_action
        # else exploration
        else:
            action = get_random_action()

        # perform action and get reward and next state
        new_state, reward, done, truncated, info = env.step(action)

        q_state_representation = find_closest(hull_angle_speed_parameters, state[0])
        q_new_state_representation = find_closest(hull_angle_speed_parameters, new_state[0])
        highest_value_new_state = Q[q_new_state_representation][get_action_with_highest_reward_from_state(q_new_state_representation)]
        stringified_action = stringify_action(action)

        q_state_new_value = Q[q_state_representation][stringified_action] + alpha * (float(reward) + discount_factor - highest_value_new_state - Q[q_state_representation][stringified_action])

        if q_state_new_value > greater_value:
            greater_value = q_state_new_value
            greater_value_action = action

        Q[q_state_representation][stringified_action] = q_state_new_value

        total_training_rewards += reward
        state = new_state

        if done or truncated:
            break

    #cutting down exploration by reducing epsilon
    epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay * episode)

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