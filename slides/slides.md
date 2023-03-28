---
theme: "purplin"
colorSchema: 'light'
---

# Aprendizado por Reforço em Simulação Física 2D

INF5021 - Matheus Madeira

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="">
    <SlideCurrentNo />
  </Item>
</BarBottom>

---
layout: image-right
image: './img/slide2.gif'
---

# Introdução

- Simulação física é uma área de extrema relevância para a computação.
- Esse trabalho busca servir como mais uma referência de aplicação de IA.
- Agente de aprendizado de reforço para um ambiente de simulação física em 2D (<span class="text-sm">Python, Gymnasium</span>).

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="">
    <SlideCurrentNo />
  </Item>
</BarBottom>
---

# Objetivos

<div class="flex items-center py-6">
<div class="flex flex-col mx-auto">
<div class="p-3 border border-purple-200 rounded-md shadow-md mb-8 w-150">
<span class="text-2xl font-semibold mb-2 border-b-2 border-purple inline-flex">Objetivo Geral</span> <br>
<span class="ml-2 text-xl leading-relaxed">Desenvolver um agente por aprendizado por reforço para o ambiente Box2D Bipedal Walker.</span>
</div>

<div class="p-3 border border-purple-200 rounded-md shadow-md w-150">
<span class="text-2xl font-semibold mb-2 border-b-2 border-purple inline-flex">Objetivos Específicos</span> <br>
<div class="ml-2 text-sm leading-relaxed">
<ul>
<li>Implementar um agente de aprendizado por reforço</li>
<li>Comparar o agente implementado com um agente aleatório do ambiente</li>
</ul>
</div>
</div>
</div>
</div>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="">
    <SlideCurrentNo />
  </Item>
</BarBottom>

---
layout: image-x
image: './img/slide4.gif'
imageOrder: 2
---

# <span class="absolute top-8 left-13">Fundamentação Teórica</span>

## Aprendizado por reforço

<div class="mt-6">

- Aprender através da interação buscando atingir um objetivo.
- Interações entre Agente e o Ambiente.
  - Espaço de ações, e espaço de observação (estado).
- Q-learning
</div>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="">
    <SlideCurrentNo />
  </Item>
</BarBottom>

---

# Fundamentação Teórica

<br><br><br>

$$ \begin{array}{c} \underbrace{Q(s,a)}_{\scriptstyle\text{Novo valor}}=\underbrace{Q(s,a)}_{\scriptstyle\text{Valor antigo}}+\mkern-34mu\underset{\text{Taxa de aprendizado}}{\underset{\Bigl|}{\alpha}}\mkern-30mu[\underbrace{R(s,a)}_{\scriptstyle\text{Recompensa}}+\mkern-30mu\underset{\text{Taxa de desconto}}{\underset{\Biggl|}{\gamma}}\mkern-75mu\overbrace{\max Q'(s',a')}^{\scriptstyle\substack{\text{Valor máximo esperado, dado o novo} \\ \text{estado e todas suas possíveis ações}}}\mkern-45mu-Q(s,a)]\end{array} $$

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="">
    <SlideCurrentNo />
  </Item>
</BarBottom>

---

# Fundamentação Teórica

## DDPG
- Deep Deterministic Policy Gradients
- Aprende uma Q-function e uma Policy
- Usado para espaços de ação e observação contínuos
- Actor, Critic, Target Actor, Target Critic


<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="">
    <SlideCurrentNo />
  </Item>
</BarBottom>

---

# Fundamentação Teórica

## DDPG

<div class="flex flex-col">
  <div class="mx-auto">
    <img src="/img/ddpg.png" class="w-130"/>
  </div>
</div>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="">
    <SlideCurrentNo />
  </Item>
</BarBottom>

---

# Trabalhos Relacionados

## <span class="text-2xl">Gambim (2021). _Aprendizado por Reforço em Jogos de Estratégia_</span>

<div class="grid grid-cols-5 gap-x-5 px-5 pt-5 items-center">
<div class="col-span-3">

- Agente por aprendizado por reforço para o jogo para o jogo de estratégia Battle for Wesnoth.
- Deep Q-learning.

</div>
<div class="col-span-2">
  <img src="/img/related-works-1.jpg" class="max-w-full"/>
</div>
</div>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="">
    <SlideCurrentNo />
  </Item>
</BarBottom>
---

# Trabalhos Relacionados

## <span class="text-2xl">Song et al (2018). _Recurrent Deterministic Policy Gradient Method for Bipedal Locomotion on Rough Terrain Challenge_</span>

<div class="grid grid-cols-5 gap-x-5 px-5 pt-5">
<div class="col-span-3">

- Deep Learning Framework capaz de resolver problemas de locomoção parcialmente observáveis. 
- Baseado em Recurrent Deterministic Policy Gradient (RDPG).

</div>
<div class="col-span-2">
  <img src="/img/related-works-2.png" class="max-w-full"/>
</div>
</div>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="">
    <SlideCurrentNo />
  </Item>
</BarBottom>

---

# Trabalhos Relacionados

## <span class="text-2xl">Mishra et al (2021). _Environment Interaction of a Bipedal Robot  using Model-Free Control Framework Hybrid  off-Policy and on-Policy Reinforcement  Learning Algorithm_</span>

<div class="grid grid-cols-5 gap-x-5">
<div class="col-span-3 pt-5">

- Algoritmo híbrido de DDPG e PPO.
- Off-policy (DDPG) e On-policy (PPO) trabalhando juntos.

</div>
<div class="col-span-2">
  <img src="/img/related-works-3.png" class="max-w-full"/>
</div>
</div>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="">
    <SlideCurrentNo />
  </Item>
</BarBottom>

---

# Metodologia

## Gymnasium

<div class="mt-4">

- Biblioteca ambientes para aprendizado por reforço.
</div>
 
<br>

```py
import gymnasium as gym
env = gym.make("LunarLander-v2", render_mode="human")
observation, info = env.reset(seed=42)
for _ in range(1000):
   action = env.action_space.sample()
   observation, reward, terminated, truncated, info = env.step(action)

   if terminated or truncated:
      observation, info = env.reset()
env.close()
```

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="">
    <SlideCurrentNo />
  </Item>
</BarBottom>

---
layout: image-x
image: './img/slide2.gif'
imageOrder: 2
---

# Metodologia

## Bipedal Walker
<div class="mt-8">

- Box2D Bipedal Walker
- Robô com 4 juntas que caminha num terreno levemente desigual.
- Objetivo de 300 pontos em 1600 passos.
  - Queda -> -100 pontos. 
  - Toque ao motor -> custa uma pequena quantia de pontos.
</div>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="">
    <SlideCurrentNo />
  </Item>
</BarBottom>

---

# Metodologia

## Bipedal Walker

<div class="mt-12">

| Espaço de ação  | Box(-1.0, 1.0, (4,), float32) |
|---|--|
| Forma do espaço de observação |  (24,) |
| Espaço de observação Máximo | [3.14, 5, 5, 5, 3.14, 5, 3.14, 5, 5, 3.14, 5, 3.14, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| Espaço de observação Mínimo | [-3.14, -5, -5, -5, -3.14, -5, -3.14, -5, 0, -3.14, -5, -3.14, -5, -0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1] |
</div>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="">
    <SlideCurrentNo />
  </Item>
</BarBottom>

---
layout: image-x
image: './img/flowchart.png'
imageOrder: 2
---

<div class="-mt-5">

# Metodologia

### Solução 1

- Discretização do espaço de observação e do espaço de ação.
- Divisão de ações em intervalos de 0.2 (10 partes).
- Divisão de variáveis de observação em intervalos de 0.7 (10 partes).
- Observação: velocidade angular do casco, contato de pernas com chão, posição das juntas.

</div>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="">
    <SlideCurrentNo />
  </Item>
</BarBottom>

---

# Metodologia

### Solução 1

<br>

- Não foi possível adicionar mais variáveis de observação devido a memória e tempo de execução
- Etapas:
  - Implementação do Agente (α = 0.7, γ = 0.618, ε descrescente (mínimo: 0.01))
  - Treinamento
  - Comparação
  

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="">
    <SlideCurrentNo />
  </Item>
</BarBottom>

---

# Solução 1: Resultados

<div class="grid grid-cols-2 gap-x-5 px-5">
<div class="flex flex-col">
  <img src="/img/resultado-solucao-1.jpg" class="max-w-full"/>
  <span class="mx-auto mt-3 text-center">Agente DDPG - Recompensa média -89.9</span>
</div>
<div class="flex flex-col">
  <img src="/img/resultado-random.jpg" class="max-w-full"/>
  <span class="mx-auto mt-3 text-center">Agente aleatório - Recompensa média -99.6</span>
</div>
</div>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="">
    <SlideCurrentNo />
  </Item>
</BarBottom>

---

# Metodologia

### Solução 2

- Utilização de uma rede neural codificada utilizando PyTorch, derivada a partir do paper original [2015].
- Etapas:
  - Implementação do código para fazer uso da rede neural (parâmetros XXXXX)
  - Treinamento
  - Comparação


<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="">
    <SlideCurrentNo />
  </Item>
</BarBottom>

---

# Solução 2: Resultados

<div class="grid grid-cols-2 gap-x-5 px-5">
<div class="flex flex-col">
  <img src="/img/resultado-solucao-2.png" class="max-w-full"/>
  <span class="mx-auto mt-3 text-center">Agente DDPG - Recompensa média XXXXX</span>
</div>
<div class="flex flex-col">
  <img src="/img/resultado-solucao-1.jpg" class="max-w-full"/>
  <span class="mx-auto mt-3 text-center">Agente Q-learning - Recompensa média -89.9</span>
</div>
</div>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="">
    <SlideCurrentNo />
  </Item>
</BarBottom>

---
layout: quote
position: center
---

# DEMO

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="">
    <SlideCurrentNo />
  </Item>
</BarBottom>

---

# Conclusão

<br>

- Maior aprofundamento na área de IA.
  - Desenvolvimento de habilidades práticas com ferramentas e formulação de soluções.
- Trabalho traz a contribuição de ser mais uma referência de desenvolvimento para a classe de problemas.
- Melhorias futuras:
  - Mais implementações para comparação (TP3, PPO, etc).
  - Implementação para ambientes mais complexos (Hardcore).

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="">
    <SlideCurrentNo />
  </Item>
</BarBottom>

---

# Referências

- Sutton, R.S. & Barto, A.G. (1998). _Reinforcement Learning: An Introduction._ <br> <span style="color: rgb(76, 29, 149, 0.4)">The MIT Press, Cambridge, MA.</span>
- Panin, A. (2020). _Introduction to Reinforcement Learning: On-policy vs off-policy._ <br>
- Tostaeva, G. (2020). _Introduction to Q-learning with OpenAI Gym._ <br>
- Huang, C. (2020).  _CleanRL (Clean Implementation of RL Algorithms)._ <br>
- Gambim, T.R. (2021). _Aprendizado por Reforço em Jogos de Estratégia._ <br> <span style="color: rgb(76, 29, 149, 0.4)">TCC (Graduação em Engenharia de Computação) - PUCRS.</span>
- Song, D.R. & Yang, C. & McGreavy, C. & Li, Z. (2018). _Recurrent Deterministic Policy Gradient Method for Bipedal Locomotion on Rough Terrain Challenge._ <br> <span style="color: rgb(76, 29, 149, 0.4)">15th International Conference on Control, Automation, Robotics and Vision (ICARCV), Singapore.</span>


<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="">
    <SlideCurrentNo />
  </Item>
</BarBottom>

---

# Referências

- Mishra, P.K. & Prakash, P. (2021). _Environment Interaction of a Bipedal Robot  using Model-Free Control Framework Hybrid  off-Policy and on-Policy Reinforcement  Learning Algorithm._ <br> <span style="color: rgb(76, 29, 149, 0.4)">International Journal of  Innovative Science and Research Technology.</span>
- Lillicrap, T.P. & Hunt, J.J. & Pritzel, A. & Heess, N. & Erez, T. & Tassa, Y. & Silver, D. & Wierstra, D. (2015). _Continuous control with deep reinforcement learning._ <br> <span style="color: rgb(76, 29, 149, 0.4)">International Conference on Learning Representations.</span>
- Tabor, P. (2019). _How to Implement Deep Learning Papers._ <br>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="">
    <SlideCurrentNo />
  </Item>
</BarBottom>

---
layout: center
class: "text-center"
---

# Obrigado!

## <span class="text-2xl">Link Apresentação: [mathsmadeira.com/ufrgs/INF5021/](https://mathsmadeira.com/INF5021/)</span>
## <span class="text-2xl">GitHub Repo: [https://github.com/msmadeira/INF5021](https://github.com/msmadeira/INF5021)</span>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="">
    <SlideCurrentNo />
  </Item>
</BarBottom>
