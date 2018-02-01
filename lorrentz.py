import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random


def lorenz(x, y, z, a=10, b=28, c=2.667):
    x_dot = a*(y - x)
    y_dot = b*x - y - x*z
    z_dot = x*y - c*z
    return x_dot, y_dot, z_dot

def get_params():
    while True:
        val = input("Enter a b c (delimited by space) or Press `d` for default value: ")
        if val == 'd' or val == 'D':
            return 10,28,2.667
        elif len(val.split()) == 3:
            val = val.split()
            try:
                a = float(val[0])
                b = float(val[1])
                c = float(val[2])
                return a,b,c
            except:
                print("\nInvalid Input. Try again.")
                continue

dt = 0.01
stepCnt = 10000

# Need one more for the initial values
xs = np.empty((stepCnt + 1,))
ys = np.empty((stepCnt + 1,))
zs = np.empty((stepCnt + 1,))

#M
# Setting initial values
xs[0], ys[0], zs[0] = (0., 1., 1.05)
#getting parameters
a,b,c = get_params()


# Stepping through "time".
for i in range(stepCnt):
    # Derivatives of the X, Y, Z state
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i],a,b,c)
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)

fig = plt.figure()
ax = fig.gca(projection='3d')

clrs = ['red','green','blue','black','yellow', 'magenta', 'cyan']
clr = random.choice(clrs)
ax.plot(xs, ys, zs, lw=0.5, color=clr)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.show()
