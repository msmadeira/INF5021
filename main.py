import gymnasium as gym
import numpy as np
import random
import matplotlib.pyplot as plt
import sys

#get debug argument
debug = sys.argv[1] == 'True'

#Setting hyperparameters
alpha = 0.7
discount_factor = 0.618
epsilon = 1
max_epsilon = 1
min_epsilon = 0.01
decay = 0.01

#training variables
num_training_episodes = 2000

env = gym.make("Taxi-v3")
# env = gym.make("BipedalWalker-v3", render_mode="human")

#Initilize q-table
#TODO: Box has no attribute n
Q = np.zeros((env.observation_space.n, env.action_space.n))

#create lists to keep track of reward and epsilon
training_rewards = []
epsilons = []

#training
for episode in range(num_training_episodes):
    state, info = env.reset()
    #starting tracker for rewards
    total_training_rewards = 0
    
    for step in range(100):
        #choose action given the states based on a random number
        exp_exp_tradeoff = random.uniform(0, 1)
        
        #if rng larger than epsilon: exploitation
        if exp_exp_tradeoff > epsilon:
            action = np.argmax(Q[state,:])
        # else exploration
        else:
            action = env.action_space.sample()
            
        #perform action and get reward and next state
        new_state, reward, done, truncated, info = env.step(action)
        
        #update q-table
        Q[state, action] = Q[state, action] + alpha * (reward + discount_factor * np.max(Q[new_state, :]) - Q[state, action])
        total_training_rewards += reward
        state = new_state
        
        #ending episode
        if done or truncated:
            break
        
    #cutting down exploration by reducing epsilon
    epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay * episode)
    
    #add total reward and reduced epsilon values
    training_rewards.append(total_training_rewards)
    epsilons.append(epsilon)
    
print("Training score over time: " + str(sum(training_rewards) / num_training_episodes))

#plot graphs

if debug:
    #Visualizing results and total reward over all episodes
    x = range(num_training_episodes)
    plt.plot(x, training_rewards)
    plt.xlabel('Episode')
    plt.ylabel('Training total reward')
    plt.title('Total rewards over all episodes in training') 
    plt.show()

    #Visualizing the epsilons over all episodes
    plt.plot(epsilons)
    plt.xlabel('Episode')
    plt.ylabel('Epsilon')
    plt.title("Epsilon for episode")
    plt.show()