"""Creates an animation of the logistic map converging"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from pathlib import Path

def logistic_map(x: np.ndarray, r: np.ndarray) -> np.ndarray:
    """Implements the logistic map function"""
    return r[:, None] * x * (1-x)

# Settings
n_starts = 1
n_r = 50_000
max_iter = 250

# Use numpy arrays for vectorized operations 
vals = np.zeros((n_r, n_starts, max_iter+1))
vals[:,:,0] = np.random.rand(n_r, n_starts)
r = np.linspace(0, 4, n_r)
for i in range(max_iter):
    vals[:,:,i+1] = logistic_map(vals[:,:,i], r)

# Set up the graphs and keep track of the scatter artists speed up the animation
fig, ax = plt.subplots()
scatters = []
for i in range(n_starts):
    scatters.append(ax.scatter(r, vals[:,i,0], s=0.05, label=f'x0 = {vals[0,i,0]:.2f}'))
ax.set_xlim(0, 4)
ax.set_xlabel('r')
ax.set_ylabel('$x_n$')
ax.legend()

def animate(index: int):
    """Generates a frame for the animation"""
    print(f'Animating frame {index}/{max_iter}', end='\r')
    ax.set_title(f'Frame n={index+1}')
    for i in range(n_starts):
        scatters[i].set_offsets(np.c_[r, vals[:,i,index]])
    
    return

ani = animation.FuncAnimation(
    fig,
    animate,
    repeat=True,
    frames=max_iter,
    interval=50,
)

writer = animation.PillowWriter(
    fps=15,
    bitrate=1800
)

ani.save('animation.gif', writer=writer)

print('\nAnimation complete!')