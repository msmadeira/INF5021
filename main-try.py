import gymnasium as gym
import numpy as np
import random
import matplotlib.pyplot as plt
import sys
import time

start_time = time.time()

# get debug argument
debug = sys.argv[1] == 'True'

# Setting hyperparameters
alpha = 0.99
discount_factor = 0.618
epsilon = 1
max_epsilon = 1
min_epsilon = 0.01
decay = 0.01

# training variables
num_training_episodes = 5000

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
    # TODO: use numpy
    return np.array([float(x) for x in string_action.split(';')])


def get_action_with_highest_reward_from_state(st):
    # TODO: use numpy
    return max(Q[st], key=Q[st].get)


def get_state_representation(st):
    global hull_angle_speed_parameters, hip1_angle_parameters, knee1_angle_parameters, hip2_angle_parameters
    global knee2_angle_parameters
    # return find_closest(hull_angle_speed_parameters, st[0])
    # return f'{find_closest(hull_angle_speed_parameters, st[0])};{st[8]};{st[13]};{st[4]};{st[6]};{st[9]};{st[11]}'
    return f'{find_closest(hull_angle_speed_parameters, st[0])};{st[8]};{st[13]};{find_closest(knee1_angle_parameters, st[6])};{find_closest(knee2_angle_parameters, st[11])}'


# discretization: action space
action_space = np.around(np.arange(start=env.action_space.low[0], stop=env.action_space.high[0], step=0.5), 1)
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
# -----------------------------------
# hull angle speed
step = 0.7
low = env.observation_space.low[0]
high = env.observation_space.high[0]
hull_angle_speed_parameters = np.append(np.around(np.arange(start=low, stop=high, step=step), 2), [3.14])
# legs ground contact
leg1_ground_contact_parameters = np.array([0.0, 1.0])
leg2_ground_contact_parameters = np.array([0.0, 1.0])
# leg1 angles
step = 0.7
low = env.observation_space.low[4]
high = env.observation_space.high[4]
hip1_angle_parameters = np.append(np.around(np.arange(start=low, stop=high, step=step), 2), [3.14])
low = env.observation_space.low[6]
high = env.observation_space.high[6]
knee1_angle_parameters = np.append(np.around(np.arange(start=low, stop=high, step=step), 2), [3.14])
# leg2 angles
low = env.observation_space.low[9]
high = env.observation_space.high[9]
hip2_angle_parameters = np.append(np.around(np.arange(start=low, stop=high, step=step), 2), [3.14])
low = env.observation_space.low[11]
high = env.observation_space.high[11]
knee2_angle_parameters = np.append(np.around(np.arange(start=low, stop=high, step=step), 2), [3.14])

# initialize Q-table
Q = {}
for i in range(hull_angle_speed_parameters.size):
    # TEMP: for testing
    # Q[hull_angle_speed_parameters[i]] = action_space_dictionary.copy()

    key1 = str(hull_angle_speed_parameters[i])
    for j in range(leg1_ground_contact_parameters.size):
        key2 = key1 + ';' + str(leg1_ground_contact_parameters[j])
        for k in range(leg2_ground_contact_parameters.size):
            key3 = key2 + ';' + str(leg2_ground_contact_parameters[k])
            # for l in range(hip1_angle_parameters.size):
            #     key4 = key3 + ';' + str(hip1_angle_parameters[l])
            for m in range(knee1_angle_parameters.size):
                key5 = key3 + ';' + str(knee1_angle_parameters[m])
                # for n in range(hip1_angle_parameters.size):
                #     key6 = key5 + ';' + str(hip2_angle_parameters[n])
                for o in range(knee2_angle_parameters.size):
                    # key7 = key6 + ';' + str(knee2_angle_parameters[o])
                    key7 = key5 + ';' + str(knee2_angle_parameters[o])
                    #     Q[key7] = action_space_dictionary.copy()
                    Q[key7] = action_space_dictionary.copy()

# Each of this episode is its own game.
action_size = env.action_space.shape[0]
for episode in range(num_training_episodes):
    state, info = env.reset()

    total_training_rewards = 0

    while True:
        # q_state_representation = find_closest(hull_angle_speed_parameters, state[0])
        q_state_representation = get_state_representation(state)

        # print(f'{state[8] == leg1_ground_contact_parameters[1]};{state[8] == leg1_ground_contact_parameters[0]}')

        # choose action given the states based on a random number
        exp_exp_tradeoff = random.uniform(0, 1)

        # if rng larger than epsilon: exploitation
        if exp_exp_tradeoff > epsilon:
            # get action in dictionary with the highest reward and parse it
            action = parse_action(get_action_with_highest_reward_from_state(q_state_representation))
        # else exploration
        else:
            action = np.random.choice(action_space, size=action_size)

        # perform action and get reward and next state
        new_state, reward, done, truncated, info = env.step(action)

        q_new_state_representation = get_state_representation(new_state)
        highest_value_new_state = Q[q_new_state_representation][get_action_with_highest_reward_from_state(q_new_state_representation)]
        stringified_action = stringify_action(action)

        q_state_new_value = Q[q_state_representation][stringified_action] + alpha * (
                float(reward) + discount_factor * highest_value_new_state - Q[q_state_representation][
            stringified_action])

        Q[q_state_representation][stringified_action] = q_state_new_value

        total_training_rewards += reward
        state = new_state

        if done or truncated:
            break

    # cutting down exploration by reducing epsilon
    epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay * episode)

    # add total reward and reduced epsilon values
    training_rewards.append(total_training_rewards)
    epsilons.append(epsilon)

print("Training score over time: " + str(sum(training_rewards) / num_training_episodes))
print("\n--- %s seconds ---" % (time.time() - start_time))

# plot graphs
if debug:
    # Visualizing results and total reward over all episodes
    x = range(num_training_episodes)
    plt.plot(x, training_rewards)
    plt.xlabel('Episódio')
    plt.ylabel('Recompensa total de treinamento')
    plt.title('Recompensa total em todos episódios de treinamento')
    plt.show()
