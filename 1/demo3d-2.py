#!/usr/bin/env python3

from matplotlib import animation, pyplot as plt
import pandas as pd
import numpy as np

# Create initial empty dataframe
df = pd.DataFrame(columns=['x', 'y', 'z', 'time'])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def update_plot(frame):
    global df
    # Generate random data and append to dataframe

    data={'x': np.random.rand(), 'y': np.random.rand(), 'z': np.random.rand(), 'time': frame}
    df_extended = pd.DataFrame(data, df.columns)
    
    df = pd.concat([df, df_extended])

    # Remove old data that is more than 10 seconds old
    df = df[(df['time'] - df['time'].iloc[-1]) < 10]

    # Clear the plot and draw the new data
    ax.clear()
    ax.plot(df['x'], df['y'], df['z'])

ani = animation.FuncAnimation(fig, update_plot, interval=1000)
plt.show()
