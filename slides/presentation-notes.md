# Notes

Informações extras para cada Ponto

## Slide 2

- Isso tanto para estudar características físicas, quanto para resolver problemas do mundo real.
  - Mas uma simulação física, geralmente necessita de muitas variáveis devida a alta complexidade desses problemas no nosso cotidiano. Uma alternativa para diminuir a complexidade desses problemas e ainda assim conseguir os estudar é ir para o mundo 2D.

# Slide 4

- De trabalhos relacionados temos o trabalho do Tiago Reck Gambim, Aprendizado por Reforço em jogos de estratégia.
TCC de Engenharia de Computação na PUCRS. Que basicamente foca em desenvolver um ambiente, e um agente para o jogo Battle for Wesnoth, um jogo
de estratégia em turnos em um mapa hexagonal. Esse trabalho se relaciona bem pelo fato de usar as mesmas ferramentas, referências e abordagem.

# Slide 5

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

# Slide 10

- Como o estado de observação é contínuo, o único jeito de se conseguir desenvolver uma solução seria discretizar esse espaço.
