import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


G = 6.67430e-11
mass_sun = 1.989e30
mass_earth = 5.972e24 
mass_jupiter = 1.898e27 


time_step = 60 * 60 * 24  
total_steps = 10000


earth_pos = np.array([1.8e11, 0.0])
earth_vel = np.array([0.0, 24000.0])
jupiter_pos = np.array([7.785e11, 0.0])
jupiter_vel = np.array([0.0, 12500.0])


earth_path = []
jupiter_path = []


for step in range(total_steps):
   
    r_earth = -earth_pos
    distance_earth = np.linalg.norm(r_earth)
    force_earth = G * mass_sun * mass_earth / (distance_earth ** 3) * r_earth
    acceleration_earth = force_earth / mass_earth
    earth_vel = earth_vel + acceleration_earth * time_step
    earth_pos = earth_pos + earth_vel * time_step
    earth_path.append(earth_pos.copy())

    
    r_jupiter = -jupiter_pos
    distance_jupiter = np.linalg.norm(r_jupiter)
    f_jupiter = G * mass_sun * mass_jupiter / (distance_jupiter ** 3) * r_jupiter
    acc_jupiter = f_jupiter / mass_jupiter
    jupiter_vel = jupiter_vel + acc_jupiter * time_step
    jupiter_pos = jupiter_pos + jupiter_vel * time_step
    jupiter_path.append(jupiter_pos.copy())


earth_x, earth_y = zip(*earth_path)
jupiter_x, jupiter_y = zip(*jupiter_path)


fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor("black")
ax.set_xlim(-9e11, 9e11)
ax.set_ylim(-9e11, 9e11)
ax.set_aspect('equal')


sun = ax.plot(0, 0, 'yo', markersize=12, label='Sun')[0]
earth_dot, = ax.plot([], [], 'bo', label='Earth')
jupiter_dot, = ax.plot([], [], 'orange', marker='o', label='Jupiter')
earth_line, = ax.plot([], [], 'b-', alpha=0.5)
jupiter_line, = ax.plot([], [], 'orange', alpha=0.5)


time_text = ax.text(0.05, 0.95, '', transform=ax.transAxes, color='white', fontsize=12)

ax.legend()


def update(frame):
    
    earth_dot.set_data([earth_x[frame]], [earth_y[frame]])
    jupiter_dot.set_data([jupiter_x[frame]], [jupiter_y[frame]])

    
    earth_line.set_data(earth_x[:frame+1], earth_y[:frame+1])
    jupiter_line.set_data(jupiter_x[:frame+1], jupiter_y[:frame+1])

    
    time_in_days = frame * (time_step / (60 * 60 * 24)) 
    time_text.set_text(f'Time: {int(time_in_days)} days')

    return earth_dot, jupiter_dot, earth_line, jupiter_line, time_text


ani = FuncAnimation(fig, update, frames=total_steps, interval=20, blit=True)
plt.show()
