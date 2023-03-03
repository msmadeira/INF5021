---
theme: "purplin"
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
- Agente de aprendizado de reforço para um ambiente de simulação física em 2D.
  - <span class="text-sm">Python, Gymnasium</span>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>
---

# Objetivos

<div class="flex items-center py-8">
<div class="flex flex-col mx-auto">
<div class="p-3 border border-purple-200 rounded-md shadow-md mb-8 w-150">
<span class="text-xl font-semibold mb-2 border-b-2 border-purple inline-flex">Objetivo Geral</span> <br>
<span class="ml-2 text-sm leading-relaxed">Desenvolver um agente por aprendizado por reforço para o ambiente Box2D Bipedal Walker.</span>
</div>

<div class="p-3 border border-purple-200 rounded-md shadow-md w-150">
<span class="text-xl font-semibold mb-2 border-b-2 border-purple inline-flex">Objetivos Específicos</span> <br>
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
layout: image-x
image: './img/related-works.jpg'
---

# Trabalhos Relacionados

- Tiago Reck Gambim. _Aprendizado por Reforço em Jogos de Estratégia_ <br> <span style="color: rgb(76, 29, 149, 0.4)">Trabalho de Conclusão de Curso (Graduação em Engenharia de Computação) - PUCRS, 2021.</span>

### <span class="text-xs">NOTA: Adicionar mais 2 trabalhos relacionados</span> 

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

# Metodologia

## Gymnasium

- Biblioteca contendo uma diversa coleção de diferentes ambientes para aprendizado por reforço.
 
<br>

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
image: './img/slide2.gif'
imageOrder: 2
---

# Metodologia

## Bipedal Walker

- Ambiente com um robô com 4 juntas que caminha num terreno levemente desigual.
- Para resolução é necessário 300 pontos em 1600 passos de tempo.
- Recompensas são obtidas por se mover para frente, totalizando 300 pontos ao final. 
  - Se o robô cair, -100 pontos. 
  - Aplicar torque ao motor custa uma pequena quantia de pontos.

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>

---

# Metodologia

## Bipedal Walker

### Estado consiste de (i) velocidade do ângulo do casco, (ii) velocidade angular, (iii) velocidade horizontal, (iv) velocidade vertical, (v) posição das juntas e sua velocidade angular, (vi) pernas estão em contato com o chão, e (vii) 10 medições de telêmetro.

| Espaço de ação  | Box(-1.0, 1.0, (4,), float32) |
|---|--|
| Forma do espaço de observação |  (24,) |
| Espaço de observação Máximo | [3.14, 5, 5, 5, 3.14, 5, 3.14, 5, 5, 3.14, 5, 3.14, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| Espaço de observação Mínimo | [-3.14, -5, -5, -5, -3.14, -5, -3.14, -5, 0, -3.14, -5, -3.14, -5, -0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1] |

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

### Solução

- Discretização do estado de observação do ambiente
- Definição das variáveis do ambiente necessárias para a solução (NOTA: adicionar assim que terminar)
- Divisão de cada uma dessas variáveis em x (NOTA, ainda em testes) partes iguais
- Etapas:
  - Implementação do Agente (α = X, γ = Y, ε = Z (NOTA))
  - Treinamento
  - Comparação

### <span class="text-xs">NOTA: Se houver grande modificação na metodologia devido a implementação, atualizar na fundamentação teórica</span>

</div>
<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>

---

# Resultados

<div class="flex flex-col">
  <div class="mx-auto">
    <img src="/img/resultados.png" class="w-100"/>
    <span class="text-xs">NOTA: Atualizar com resultado concreto médio (Epsilon + recompensa)</span>
  </div>
</div>

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>

---

# Resultados

<div class="grid grid-cols-2 gap-x-5 px-5">
<div>
  <img src="/img/resultados.png" class="max-w-full"/>
  <span class="text-xs">NOTA: Atualizar com resultado concreto melhor resultado (Epsilon + recompensa)</span>
</div>
<div>
  <img src="/img/resultados.png" class="max-w-full"/>
  <span class="text-xs">NOTA: Atualizar com resultado concreto pior resultado (Epsilon + recompensa)</span>
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
- O resultado do trabalho consegue trazer uma contribuição como mais uma referência de solução para a classe de problemas escolhido.
- Melhorias futuras:
  - Mais implementações para comparação (DQN, PPO, etc)
  - Implementação para ambientes mais complexos

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>

---

# Referências

- Richard S. Sutton and Andrew G. Barto. <br> _Reinforcement Learning: An Introduction._ <br> <span style="color: rgb(76, 29, 149, 0.4)">The MIT Press, Cambridge, MA, 2018.</span>
- Alexander Panin. <br> _Introduction to Reinforcement Learning: On-policy vs off-policy, Nov, 2020._ <br>
- Gelana Tostaeva. <br> _Introduction to Q-learning with OpenAI Gym, Abr, 2020._ <br>
- Costa Huang. <br> _CleanRL (Clean Implementation of RL Algorithms), Abr, 2020._ <br>

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

### <span class="text-xs">NOTA: Upar apresentação final, tirar mensagem de "em construção da raíz"</span>
### Link Apresentação: [mathsmadeira.com/ufrgs/INF5021/](https://mathsmadeira.com/INF5021/)

[GitHub Repo](https://github.com/msmadeira/INF5021)

<BarBottom  title="INF5021 - Matheus Madeira">
  <Item text="msmadeira/INF5021">
    <carbon:logo-github />
  </Item>
</BarBottom>