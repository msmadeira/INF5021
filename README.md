# INF5021

## Install
In order to install having swig@3 was needed `pip install swig@3`.
Also, I had a lot of different issues with Box2D, which only seized after installing it multiple times `pip install gym[box2d]`, `pip install box2d`.
Had to add `export PATH="/opt/homebrew/opt/swig@3/bin:$PATH"` to `.zshrc`.

## TODO
- [X] deixar mais suscinto o texto;
- [X] númerar slides;
- [X] Fundamentação teórica antes dos trabalhos relacionados;
- [X] Relacionar MuJoCo;
- [X] Informações divulgação
- [X] Melhorar a explicação de DDPG;
- [ ] Reread taking notes for presentation: https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8581309 
- [ ] Reread taking notes for presentation: chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://ijisrt.com/assets/upload/files/IJISRT21NOV126.pdf
- [ ] Resolver comentários marcados como 'XXXXX'
- [ ] Atualizar imagem de resultados DDPG
- [ ] Gravar vídeo para demo
- [ ] Prepare presentation notes
- [ ] Upload final presentation to website
- [ ] Add https://www.youtube.com/watch?v=jDll4JSI-xo&t=822s to references
- [ ] Extra - tirar mensagem de "em construção da raíz" de mathsmadeira.com


deterministic -> policy manda a action ao invés de stochastic que manda uma probabilidade de cada ação.
