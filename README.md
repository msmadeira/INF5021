# INF5021

## Install
In order to install having swig@3 was needed `pip install swig@3`.
Also, I had a lot of different issues with Box2D, which only seized after installing it multiple times `pip install gym[box2d]`, `pip install box2d`.
Had to add `export PATH="/opt/homebrew/opt/swig@3/bin:$PATH"` to `.zshrc`.

### For DDPG
Python 3.6 is required.

Run `pip install -r requirements.txt` inside `ddpg` folder.

## TODO 
- [ ] Resolver comentários marcados como 'XXXXX'
- [ ] Atualizar imagem de resultados DDPG
- [ ] Gravar vídeo para demo
- [ ] Upload final presentation to website
- [ ] Treinar e diminuir tempo de apresentação
- [ ] Extra: tirar mensagem de "em construção da raíz" de mathsmadeira.com
