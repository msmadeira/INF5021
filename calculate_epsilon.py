# Helper file to get an appropriate epsilon value
import matplotlib.pyplot as plt
import numpy as np

epsilon = 1
max_epsilon = 1
min_epsilon = 0.01
decay = 0.0007
episodes = 10000
epsilons = []

for episode in range(episodes):
    epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay * episode)
    epsilons.append(epsilon)

x = range(episodes)
plt.plot(x, epsilons)
plt.xlabel('Episódio')
plt.ylabel('Epsilon por treinamento')
plt.title('Decaimento do espsilon')
plt.show()