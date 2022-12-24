# INF5021

## Install
In order to install having swig@3 was needed `pip install swig@3`.
Also, I had a lot of different issues with Box2D, which only seized after installing it multiple times `pip install gym[box2d]`, `pip install box2d`.
Has do add `export PATH="/opt/homebrew/opt/swig@3/bin:$PATH"` to `.zshrc`, which is showing to only work