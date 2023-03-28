# Notes

Informações extras para cada Ponto

## Slide Introdução

- Simulação física é uma área de extrema relevância para a computação, porém são problemas de grande complexidade.
- Isso tanto para estudar características físicas, quanto para resolver problemas do mundo real.
  - Mas uma simulação física, geralmente necessita de muitas variáveis devida a alta complexidade desses problemas no nosso cotidiano. Uma alternativa para diminuir a complexidade desses problemas e ainda assim conseguir os estudar é ir para o mundo 2D.
- Esse trabalho busca servir como mais uma referência de como podemos usar inteligência artificial, mais especificamente, para resolver essa classe de problemas.

# Slide Fundamentação Teórica I

- Problemas de aprendizado por reforço envolvem entender o que fazer, como mapear situações a ações, de maneira a maximizar uma recompensa. 
  - Onde a agente não é ensinado que ações tomar, ele deve descobrir qual a maior recompensa tentando, as suas ações influenciam seus resultados futuros. 
  - Notadamente, esse agente deve ser capaz de compreender o estado do ambiente e ser capaz de tomar decisões que afetem esse estado.
  - Uma distinção clara de outro método, como por exemplo aprendizado supervisionado, é que esse aprende por um conjunto de exemplos organizados por um supervisor externo.
  - Já aprendizado por reforço um agente deve aprender a partir de sua própria experiência.
- Dito isso, aprendizado por reforço é composto por interações entre um agente e o ambiente, que é o mundo que o agente vive e interage.
- Existem diversos algoritmos diferentes para reinforcement learning, sendo divididos entre off-policy e on-policy.
  - On-policy o agente escolhendo as ações de acordo com uma policy,
  - Off-policy o agente não escolhendo as ações, aprendendo por exploração.
- A nossa tecnica escolhida então se centra em On-policy learning, que é Q-Learning
- O modelo trabalha com uma tabela Q, que contém um valor aproximado da função para cada estado. 
  - Essa tabela começa zerada.
  - Começa então o processo de aprendizado, podendo ser feito exploração, ou escolhendo a opção com maior recompensa.
  - Quando o agente escolhe uma ação e muda para outro estado o seu valor recompensa será recalculado, normalmente pela Equação de Bellman.

# Slide Fundamentação Teórica II

- Recapitulando então

# Slide Trabalhos Relacionados I

- De trabalhos relacionados temos o trabalho do Tiago Reck Gambim, Aprendizado por Reforço em jogos de estratégia.
  TCC de Engenharia de Computação na PUCRS. Que basicamente foca em desenvolver um ambiente, e um agente para o jogo Battle for Wesnoth, um jogo
  de estratégia em turnos em um mapa hexagonal. Esse trabalho se relaciona bem pelo fato de usar as mesmas ferramentas, referências e abordagem.

EXPLICAR UM POUCO MELHOR O JOGO

# Slide Trabalhos Relacionados II

- Desenvolvimento de um deep learning framework capaz de resolver problemas de locomoção parcialmente observáveis. Baseado em Recurrent Deterministic Policy Gradient (RDPG).
- Algumas melhorias: (i) tail-step boostrap da diferença temporal, injeção de experiências externas de outros agentes, entre outros.
- Utilização do ambiente Bipedal Walker do OpenAI Gym no modo Hardcore.

ESCREVER NOTAS COM BASE NO ARTIGO

# Slide Trabalhos Relacionados III

- Desenvolvimento de um algoritmo híbrido de DDPG e PPO para resolver o problema BipedalWalker Hardcore.
- Um algoritmo off-policy (DDPG) e um on-policy (PPO) trabalhando juntos.
- Trazendo a eficiência de dados off-policy e usando o gradiente de alta variância de on-policy.

ESCREVER NOTAS COM BASE NO ARTIGO

# Metodologia I

- Biblioteca contendo uma diversa coleção de diferentes ambientes para aprendizado por reforço.

# Metodologia II

- Box2D é uma engine de física para jogos 2D. Para quem conhece o ambiente de simuladores de física, essa engine seria uma versão simplificada de MuJoCo, enquanto MuJoCo é um simulator de propósito geral podendo lidar com simulação de física avançada ou mais simples 2D, o Box2D é só para jogos 2D mesmo.

# Metodologia III

- Estado consiste de (i) velocidade do ângulo do casco, (ii) velocidade angular, (iii) velocidade horizontal, (iv) velocidade vertical, (v) posição das juntas, sua velocidade angular e se a perna está em contato com o chão, e (vii) 10 medições de telêmetro.

# Metodologia Solução I

- Como o estado de observação é contínuo, o único jeito de se conseguir desenvolver uma solução com Q-learning seria discretizar esse espaço.

# Conclusão

- Foi possível obter um maior aprofundamento na área de IA, desenvolvendo habilidades práticas tanto com ferramentas bem utilizadas na área, quanto com a formulação de soluções.
- O resultado do trabalho consegue trazer uma contribuição como mais uma referência de desenvolvimento para a classe de problemas escolhido.
- Melhorias futuras:
  - Mais implementações para comparação (TP3, PPO, etc)
  - Implementação para ambientes mais complexos



## DDPG Notes

Adaptacao das ideias de DeepQLearning para espacos de acao contínuos
aprende uma q-function e uma policy,
off-policy data e bellman equation pra aprender a q-function e usa a q-function pra aprender a policy.
ao invés de usar um argmax  em cima de todas possiveis acoes no estado (impossivel em um espaco de acoes contínuo)
tenta conseguir um approximator para a*(s)
usa MSBE para aproximar a q-function
para achar uma policy det4erministica, como o espaco de acao é continuo, podemos assumir que q-function é diferenciavel com respeito a acao
entao apenas é performado um gradient ascent 

actor-critic, model free, deterministic policy gradient
Ideia de lidar com espaço de ações contínuos
Não conseguimos lidar com espaços de ações contínuos em q-learning e deep-q learning
discretizar o espaço de açõ3es faz com que tenhamos uma quantidade enorme de ações
deterministic -> policy manda a action ao invés de stochastic que manda uma probabilidade de cada ação.

treinada off-policy com samples de um replay buffer para minimizar correlacoes entre amostras
batch normalization

o comportamento de um agente é definido por uma política que mapeia estados para uma funcao de probabilidade de ações
off-policy simplifica a equacao de bellman já que nao tem que calcular com base em uma expectativa de retorno da distribuicao probabilistica de acoes

em DDPG:
Um Ator especifica uma política de maneira deterministica, mapeando estados para uma ação específica
O Critico usa a ação de bellman em cima do resultado do agente, o ator entao é atualizado encadeamento pelo crítico.

aprender em mini-batches, não online.
replay buffer é um cache.
a cada tempo o ator e o critico sao atualizados sampleando um minibatch uniformemente do buffer.

uma cópia do ator e critico (target actor and critic) para "soft" update os valores, fazendo com que os target values mudem devagar, aumentando a estavilidade
usa os targets para ter targets estaveis e treinar o critico sem divergencia.
target network delays the propagation of value estimations

como os valores de observacao podem ser de tipos diferentes, tamanhos diferentes, eles sao normalizados com uma tecnica de 
batch normalization, normaliza cada dimensao dos samples para ter uma media de unidade e variancia

para explorar tem uma política diferente, que adiciona um noise a política do ator, de maneira que a ação é sampleada e adicionada
um noise.



Trick Two: Target Networks. Q-learning algorithms make use of target networks. The term

r + \gamma (1 - d) \max_{a'} Q_{\phi}(s',a')

is called the target, because when we minimize the MSBE loss, we are trying to make the Q-function be more like this target. Problematically, the target depends on the same parameters we are trying to train: \phi. This makes MSBE minimization unstable. The solution is to use a set of parameters which comes close to \phi, but with a time delay—that is to say, a second network, called the target network, which lags the first. The parameters of the target network are denoted \phi_{\text{targ}}.

In DQN-based algorithms, the target network is just copied over from the main network every some-fixed-number of steps. In DDPG-style algorithms, the target network is updated once per main network update by polyak averaging:

\phi_{\text{targ}} \leftarrow \rho \phi_{\text{targ}} + (1 - \rho) \phi,

where \rho is a hyperparameter between 0 and 1 (usually close to 1). (This hyperparameter is called polyak in our code).

Ornstein–Uhlenbeck