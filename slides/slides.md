---
theme: "purplin"
colorSchema: 'light'
---

# Aprendizado por Reforço em Simuladores de Física Bidimensionais

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

# Introdução

- Simulação física é uma área de extrema relevância para a computação, porém são problemas de grande complexidade.
- Esse trabalho busca servir como mais uma referência de como podemos usar inteligência artificial para resolver essa classe de problemas.
- Agente de aprendizado de reforço para um ambiente de simulação física em 2D (<span class="text-sm">Python, Gymnasium</span>).

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
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
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>

---

# Trabalhos Relacionados

## <span class="text-2xl">Gambim (2021). _Aprendizado por Reforço em Jogos de Estratégia_</span>

<div class="grid grid-cols-5 gap-x-5 px-5 pt-5">
<div class="col-span-3">

- Desenvolvimento de um agente por aprendizado por reforço para o jogo para o jogo de estratégia Battle for Wesnoth.
- Desenvolvimento de um ambiente para o jogo em OpenAI Gym.
- Espaço de ações discreto, espaço de observação contínuo.
- Implementação em Deep Q-learning.

</div>
<div class="col-span-2">
  <img src="/img/related-works-1.jpg" class="max-w-full"/>
</div>
</div>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>
---

# Trabalhos Relacionados

## <span class="text-2xl">Song et al (2018). _Recurrent Deterministic Policy Gradient Method for Bipedal Locomotion on Rough Terrain Challenge_</span>

<div class="grid grid-cols-5 gap-x-5 px-5 pt-5">
<div class="col-span-3">

- Desenvolvimento de um deep learning framework capaz de resolver problemas de locomoção parcialmente observáveis. Baseado em Recurrent Deterministic Policy Gradient (RDPG).
- Algumas melhorias: (i) tail-step boostrap da diferença temporal, injeção de experiências externas de outros agentes, entre outros.
- Utilização do ambiente Bipedal Walker do OpenAI Gym no modo Hardcore.

</div>
<div class="col-span-2">
  <img src="/img/related-works-2.png" class="max-w-full"/>
</div>
</div>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>
---

# Trabalhos Relacionados

## <span class="text-2xl">Mishra et al (2021). _Environment Interaction of a Bipedal Robot  using Model-Free Control Framework Hybrid  off-Policy and on-Policy Reinforcement  Learning Algorithm_</span>

<div class="grid grid-cols-5 gap-x-5">
<div class="col-span-3 pt-5">

- Desenvolvimento de um algoritmo híbrido de DDPG e PPO para resolver o problema BipedalWalker Hardcore.
- Um algoritmo off-policy (DDPG) e um on-policy (PPO) trabalhando juntos.
- Trazendo a eficiência de dados off-policy e usando o gradiente de alta variância de on-policy.

</div>
<div class="col-span-2">
  <img src="/img/related-works-3.png" class="max-w-full"/>
</div>
</div>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
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
- Interações entre Agente (tomador de decisões) e o Ambiente.
- Ambiente tem um espaço de ações, e um espaço de observação (estado).
- On-policy, Off-policy
- Q-learning
</div>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>

---

# Fundamentação Teórica

<br><br><br>

$$ \begin{array}{c} \underbrace{Q(s,a)}_{\scriptstyle\text{Novo valor}}=\underbrace{Q(s,a)}_{\scriptstyle\text{Valor antigo}}+\mkern-34mu\underset{\text{Taxa de aprendizado}}{\underset{\Bigl|}{\alpha}}\mkern-30mu[\underbrace{R(s,a)}_{\scriptstyle\text{Recompensa}}+\mkern-30mu\underset{\text{Taxa de desconto}}{\underset{\Biggl|}{\gamma}}\mkern-75mu\overbrace{\max Q'(s',a')}^{\scriptstyle\substack{\text{Valor máximo esperado, dado o novo} \\ \text{estado e todas suas possíveis ações}}}\mkern-45mu-Q(s,a)]\end{array} $$

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>

---

# Fundamentação Teórica

## DDPG
- Model-free learning

<div class="flex flex-col">
  <div class="mx-auto">
    <img src="/img/ddpg.png" class="w-130"/>
  </div>
</div>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>

---

# Metodologia

## Gymnasium

<div class="mt-4">

- Biblioteca contendo uma diversa coleção de diferentes ambientes para aprendizado por reforço.
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
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>

---
layout: image-x
image: './img/slide2.gif'
imageOrder: 2
---

# Metodologia

## Bipedal Walker
<div class="mt-4">

- Ambiente com um robô com 4 juntas que caminha num terreno levemente desigual.
- Para resolução é necessário 300 pontos em 1600 passos de tempo.
- Recompensas são obtidas por se mover para frente, totalizando 300 pontos ao final. 
  - Se o robô cair, -100 pontos. 
  - Aplicar torque ao motor custa uma pequena quantia de pontos.
</div>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>

---

# Metodologia

## Bipedal Walker

### Estado consiste de (i) velocidade do ângulo do casco, (ii) velocidade angular, (iii) velocidade horizontal, (iv) velocidade vertical, (v) posição das juntas, sua velocidade angular e se a perna está em contato com o chão, e (vii) 10 medições de telêmetro.

<div class="mt-4">

| Espaço de ação  | Box(-1.0, 1.0, (4,), float32) |
|---|--|
| Forma do espaço de observação |  (24,) |
| Espaço de observação Máximo | [3.14, 5, 5, 5, 3.14, 5, 3.14, 5, 5, 3.14, 5, 3.14, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| Espaço de observação Mínimo | [-3.14, -5, -5, -5, -3.14, -5, -3.14, -5, 0, -3.14, -5, -3.14, -5, -0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1] |
</div>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>

---
layout: image-x
image: './img/flowchart.png'
imageOrder: 2
---

<div class="-mt-5">

# Metodologia

## Solução 1

- Discretização do espaço de observação e do espaço de ação do ambiente.
- Divisão de variáveis do espaço de ação em intervalos de 0.2 (10 partes).
- Divisão de variáveis contínuas do espaço de observação em intervalos de 0.7 (10 partes).
- Variáveis de observação utilizadas: velocidade do ângulo do casco, pernas estão em contato com o chão, posição das juntas.

</div>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>

---

# Metodologia

## Solução 1

- Não foi possível adicionar mais variáveis de observação devido a memória e tempo de execução
- Etapas:
  - Implementação do Agente
    - α = 0.7
    - γ = 0.618
    - ε descrescente, decaimento de 1% por episódio, valor mínimo: 0.01
  - Treinamento
  - Comparação
  

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
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
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
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
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
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

# Conclusão

<br>

- Foi possível obter um maior aprofundamento na área de IA, desenvolvendo habilidades práticas tanto com ferramentas bem utilizadas na área, quanto com a formulação de soluções.
- O resultado do trabalho consegue trazer uma contribuição como mais uma referência de desenvolvimento para a classe de problemas escolhido.
- Melhorias futuras:
  - Mais implementações para comparação (TP3, PPO, etc)
  - Implementação para ambientes mais complexos

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
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
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>

---

# Referências

- Mishra, P.K. & Prakash, P. (2021). _Environment Interaction of a Bipedal Robot  using Model-Free Control Framework Hybrid  off-Policy and on-Policy Reinforcement  Learning Algorithm._ <br> <span style="color: rgb(76, 29, 149, 0.4)">International Journal of  Innovative Science and Research Technology.</span>
- Lillicrap, T.P. & Hunt, J.J. & Pritzel, A. & Heess, N. & Erez, T. & Tassa, Y. & Silver, D. & Wierstra, D. (2015). _Continuous control with deep reinforcement learning._ <br> <span style="color: rgb(76, 29, 149, 0.4)">International Conference on Learning Representations.</span>

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

## <span class="text-2xl">Link Apresentação: [mathsmadeira.com/ufrgs/INF5021/](https://mathsmadeira.com/INF5021/)</span>
## <span class="text-2xl">GitHub Repo: [https://github.com/msmadeira/INF5021](https://github.com/msmadeira/INF5021)</span>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>
