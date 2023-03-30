# Notes

## Capa

Boa tarde, meu nome é Matheus Madeira e o meu trabalho é: "Aprendizado por reforço em simulação física 2D".

## Introdução

- Temos que simulação física é uma área de extrema relevância para a computação, tanto para estudar características físicas, 
  - quanto para resolver problemas do mundo real. Porém geralmente complexo, então uma boa simplificação é ir para o espaço 2D.
- Esse trabalho busca servir como mais uma referência de aplicação de IA.

## Objetivos

LER SLIDE

## Fundamentação Teórica I

- Problemas de aprendizado por reforço envolvem entender como mapear situações a ações, de maneira a maximizar uma recompensa. 
  - Onde o agente não é ensinado que ações tomar, ele deve descobrir qual a maior recompensa tentando. 
  - Notadamente, esse agente deve conseguir compreender o estado do ambiente e conseguir tomar decisões que afetem esse estado.
- Esse ambiente tem um espaço de ações possíveis e um espaço de observação (estado)
- Existem diversos algoritmos diferentes para reinforcement learning, sendo divididos entre off-policy e on-policy.
  - On-policy o agente escolhendo as ações de acordo com uma policy,
  - Off-policy o agente não escolhendo as ações, aprendendo por exploração.
- Especificamente sobre Q-learning, algoritmo off-policy
- O modelo trabalha com uma tabela Q, que contém um valor aproximado da função para cada estado. Que durante o processo de aprendizado é preenchida.
  - Faz uso de exploração em alguns momentos e tomando a ação de maior valor em outros.
  - Quando o agente escolhe uma ação e muda para outro estado o seu valor recompensa será recalculado, normalmente pela Equação de Bellman.

## Fundamentação Teórica II

- Recapitulando então

## Fundamentação Teórica III

- DDPG
- Deep Deterministic Policy Gradients, basicamente uma adaptação das ideias de Deep Q-learning (Q-learning para espaços de observação contínuos) e DPG.
- Usado para espaços de ação e observação contínuos.
- O que essa mistura nos diz? nos diz que o algoritmo aprende uma Q-function e uma Policy em simultâneo.
- Isso acontece se treinando uma rede neural para aprender uma q-function e usando a q-function para aprender uma policy, essa policy tentando ser algo que aproxime 
  - a melhor ação dado um estado.
- Para realizar isso que descrevi aqui, o algoritmo usa então uma estrutura de 4 redes neurais, uma Actor, uma critic e duas target.
  - Um Ator especifica uma política de maneira deterministica, mapeando estados para uma ação específica
  - O Crítico avalia a política do agente com uma equação, o ator entao é atualizado em encadeamento pelo crítico.
  - Como nós estamos tentando minimizar o erro, fazemos uma comparação do valor esperado com o valor obtido.
    - Para isso temos uma cópia do ator e critico (target actor and critic), atualizados de maneira mais suave, fazendo com que os target values mudem devagar
    - aumentando a estabilidade, feito para treinar o crítico sem divergencia.

## Fundamentação Teórica IV

- Aqui temos uma representação um pouco mais gráfica do Algoritmo.
- Então temos um Agente interagindo com um estado: EXPLICAR
- Aqui se pode observar o uso de uma ténica interessante de Replay Buffer, basicamente, DDPG não aprende ‘online’, ele aprende em batches
  - Se as redes fossem atualizadas a cada passo, teríamos informações com muita relação entre elas, não sendo ótimo para treinamento.
  - Então se pega ‘samples’ de uma memória e atualiza tudo em simultâneo.

## Slide Trabalhos Relacionados I

- De trabalhos relacionados temos o trabalho do Tiago Reck Gambim, Aprendizado por Reforço em jogos de estratégia.
  Um TCC de Engenharia de Computação na PUCRS. Que basicamente foca em desenvolver um ambiente, e um agente para o jogo Battle for Wesnoth, um jogo
  de estratégia em turnos num mapa hexagonal. Esse trabalho se relaciona bem pelo fato de usar as mesmas ferramentas, referências e abordagem.

## Slide Trabalhos Relacionados II

- Desenvolvimento de um deep learning framework capaz de resolver problemas de locomoção parcialmente observáveis. Baseado em Recurrent Deterministic Policy Gradient (RDPG).
- Algumas melhorias: (i) uso de memória temporal para conhecimento de estados passados (trajectory scanning), 
  - injeção de experiências externas de outros agentes, entre outros.
- Se relaciona pela utilização do ambiente Bipedal Walker do OpenAI Gym no modo Hardcore.

## Slide Trabalhos Relacionados III

- Desenvolvimento de um algoritmo híbrido de DDPG e PPO para resolver o problema BipedalWalker Hardcore.
- Um algoritmo off-policy (DDPG) e um on-policy (PPO) trabalhando juntos.
- Usando DDPG para aprender de experiências passadas e PPO para melhorar a performance atual.
- Relaciona por também usar Bipedal Walker.

## Metodologia I

- Foi feita a utilização de Gymnasium uma biblioteca contendo uma diversa coleção de diferentes ambientes para aprendizado por reforço.
- EXPLICAR CÓDIGO

## Metodologia II

- Agora sobre nosso ambiente. Box2D Bipedal Walker.
- O Box2D, uma engine de física para jogos 2D. Para quem conhece simuladores de física, essa engine seria equivalente uma versão simplificada de MuJoCo, 
  - enquanto MuJoCo é um simulator de propósito geral podendo lidar com simulação de física avançada, o Box2D é só para jogos 2D mesmo.
- Temos um robô com 4 juntas que caminha num terreno levemente desigual
- Com objetivo de 300 pontos em 1600 passos de tempo, sendo que, uma queda da -100 pontos e torque no motor para andar custa pontos.

## Metodologia III

- Agora uma descrição mais técnica do ambiente;
- Temos um espaço de ação de 4 elementos contínuos variando de -1 a 1
- Um espaço de observação de 24 variáveis de observação variando de maneiras diferentes.
- Estado de observação consiste de 
  - (i) velocidade do ângulo do casco
  - (ii) velocidade angular
  - (iii) velocidade horizontal
  - (iv) velocidade vertical
  - (v) posição das juntas, sua velocidade angular e se a perna está em contato com o chão
  - e (vii) 10 medições de telêmetro.

## Metodologia Solução I - I

- Apesar do espaço ter muitas variáveis e ser contínuo, foi feito uma tentativa inicial com Q-learning
  - Visto que, pelas informações disponíveis parecia mostrar um ambiente que poderiamos ter algum resultado interessante com essa técnica.
- Para isso foi então necessário: LER SLIDE

## Metodologia Solução I - II

LER SLIDE

## Metodologia Solução I Resultados

LER SLIDE

## Metodologia Solução II - I

- Como a gente não conseguiu ganhar do ambiente, mesmo nosso robô caminhando (vou mostrar em seguida). Uma outra abordagem foi utilizada principalmente por questão de comparação.
- Utilizando uma técnica completamente adequada ao desafio, DDPG, feito para espaços de observação e ação contínuos.
- Como uma rede neural DDPG é capaz de resolver diversos problemas diferentes sem precisar de modificação, apenas mudar os hiperparâmetros, não se foi construída uma
  - implementação do zero, se obteve uma rede neural codificada utilizando PyTorch para Gym, se atualizou para usar Gymnasium e foi feita umas modificações extras para 
  - funcionar no trabalho.
- LER ETAPAS

## Metodologia Solução II - II

LER SLIDE

## DEMO

SÓ MOSTRAR E FALAR

# Conclusão

- Foi possível obter um maior aprofundamento na área de IA, desenvolvendo habilidades práticas tanto com ferramentas bem utilizadas na área, quanto com a formulação de soluções.
- Eu vejo que o resultado do trabalho consegue trazer uma contribuição como mais uma referência de desenvolvimento para a classe de problemas escolhido.
- Podemos observar que mesmo com estratégias simples, um bom entendimento do problema e uma boa formulação pode fazer com que tenhamos resultados interessantes. (Formiga x bazuca)
- Melhorias futuras:
  - Mais implementações para comparação (TP3, PPO, etc)
  - Implementação para ambientes mais complexos.
