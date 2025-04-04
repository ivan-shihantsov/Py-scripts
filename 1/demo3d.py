#!/usr/bin/env python3

import random
from matplotlib import animation, pyplot as plt


current_point = [0, 0, 0]

# Creating an empty figure
fig = plt.figure()

# Set up 3D axes - empty subplots
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim3d([-100, 100])
ax.set_ylim3d([-100, 100])
ax.set_zlim3d([-100, 100])

# Initialize the data arrays
x_data, y_data, z_data = [], [], []

# Define the sliding window size (num of points)
slide_window_size = 30


def change_position ():
    global current_point
    # axis = random.randint (0, 2)
    # print(f"axis = {axis}")
    
    for axis in range(3):
        delta = random.randint (-5, 5)
        # print(f"delta = {delta}")
    
        current_point[axis] += delta
        # print(f"x = {current_point[0]} | y = {current_point[1]} | z = {current_point[2]}")


def update_plot(i):
    global x_data, y_data, z_data

    # Append the data to the arrays
    change_position()
    x_data.append(current_point[0])
    y_data.append(current_point[1])
    z_data.append(current_point[2])

    # Remove old data that is outside the sliding window
    if len(x_data) > slide_window_size:
        x_data = x_data[1:]
        y_data = y_data[1:]
        z_data = z_data[1:]

    # очистить plot целиком. перерисовывается он тоже целиком - со всеми точками
    ax.clear()

    ax.set_xlim3d([-100, 100])
    ax.set_ylim3d([-100, 100])
    ax.set_zlim3d([-100, 100])
    # вот тут можно сделать ax.scatter() вместо ax.plot() - это изменить тип графика
    ax.plot(x_data, y_data, z_data)


def main():
    # Animate the plot - interval between points appear
    ani = animation.FuncAnimation(fig, update_plot, interval=100)

    # Displaying the plot
    plt.show()


main()