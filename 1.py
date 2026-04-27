import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)

# The Actor: notice the comma! (ax.plot returns a list)
line, = ax.plot([], [], lw=2)

# The Director: 'frame' is automatically passed as an incrementing integer
def update(frame):
    x = np.linspace(0, 2*np.pi, 1000)
    y = np.sin(x + frame / 100.0) # Shift the sine wave based on frame
    line.set_data(x, y)          # Update the actor's data
    return line,                 # Return the actor

ani = FuncAnimation(fig, update, frames=100, interval=20)
plt.show()