
import numpy as np
import matplotlib.pyplot as plt
from gol import GameOfLife
from matplotlib.animation import FuncAnimation

gol = GameOfLife()

init = np.random.randint(0, 2, (100,100))
init[:3,:3] = 1
init[3,3] = 1

gol.set_state(init)

# Make the animation and propagate game.
fig, ax = plt.subplots(figsize=(5,5))
game_w = ax.imshow(init, vmin=0, vmax=1, cmap='binary')

def init_f():
    plt.axis('off')

    return game_w,

def animate(frame):
    game_w.set_data(gol.get_state())
    ax.set_title('Time step: {:>4d}'.format(frame))
    gol.update()
    return game_w,

anim = FuncAnimation(fig, animate, 1000, init_func=init_f, interval=100)
plt.show()


