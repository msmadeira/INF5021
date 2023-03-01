---
theme: "purplin"
---

# Gymnasium Bipedal Walker Reinforcement Learning

INF5021 - Matheus Madeira

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>

---
layout: image-right
image: './img/slide2.gif'
---

# Descrição do Problema

Lorem ipsum, a ideia é reinforcement learning do ambiente Bipedal Walker.

### O que é Gymnasium?

```py
import gymnasium as gym
env = gym.make("LunarLander-v2", render_mode="human")
observation, info = env.reset(seed=42)
for _ in range(1000):
   action = env.action_space.sample()  # this is where you would insert your policy
   observation, reward, terminated, truncated, info = env.step(action)

   if terminated or truncated:
      observation, info = env.reset()
env.close()
```

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>

---
layout: image-x
image: './img/slide4.gif'
imageOrder: 1
---

# Reinforcement Learning

descrição de como funciona, espaços, diferentes técnicas, explicar on-policy off-policy, aproximacao de funçÕes etc

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>

---
layout: intro
---

## Bipedal Walker

<br>

<div class="grid grid-cols-2 gap-x-4">
<div>
Descrição mais detalhada do que é o problema, espaço de ações, observação, observation high, low
Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum


</div>
<div>

### tabela do espaço com todas as informações numéricas
| Action Space  |   |
|---|---|
| Observation Shape  |  [.., 3.14] |
| ...  |   |
|  ... |   |
|  ... |   |


</div>
</div>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>

---

# Solução/Formulação do problema

<br>

Devido a contínuo a possível solução era mais restrita, com possibilidade de x, y e z.
Explicação do processo até chegar a solução final.
### Possivelmente mais de 1 slide, explicando cada formulação e o que é

<br>

$$
\begin{array}{c}

\nabla \times \vec{\mathbf{B}} -\, \frac1c\, \frac{\partial\vec{\mathbf{E}}}{\partial t} &
= \frac{4\pi}{c}\vec{\mathbf{j}}    \nabla \cdot \vec{\mathbf{E}} & = 4 \pi \rho \\

\nabla \times \vec{\mathbf{E}}\, +\, \frac1c\, \frac{\partial\vec{\mathbf{B}}}{\partial t} & = \vec{\mathbf{0}} \\

\nabla \cdot \vec{\mathbf{B}} & = 0

\end{array}
$$

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>

---

# Implementação

Lorem ipsum neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit (Possivelmente + slides)

### Função lorem()

```py
        Q[state, action] = Q[state, action]+alpha*(reward+discount_factor*
        np.max(Q[new_state, :])-Q[state, action]) 
        total_training_rewards += reward      
        state = new_state         
        
        if done == True:
            break
    
    epsilon = min_epsilon+(max_epsilon-min_epsilon)*np.exp(-decay*episode)
    
    training_rewards.append(total_training_rewards)
    epsilons.append(epsilon)
```

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>

---
layout: image-right
image: './img/slide2.gif'
---

# Resultados

Descrição dos resultados, com alguns gráficos nos próximos slides ou removendo o gif da lateral

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>

---
layout: quote
position: center
---

# DEMO

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>

---
layout: center
class: "text-center"
---

# Obrigado!

### Link Apresentação: [mathsmadeira.com/INF5021/](https://mathsmadeira.com/INF5021/)

[GitHub Repo](https://github.com/msmadeira/INF5021)

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>