import numpy as np
from random import randint
import matplotlib.pyplot as plt


def linear_regression(vx, vy):
    mean_x = np.mean(vx)
    mean_y = np.mean(vy)

    fac = vx - mean_x
    a = np.sum(vy * fac) / np.sum(vx * fac)
    b = mean_y - a * mean_x
    return a, b


f = 50
n = 100
x = np.array([i for i in range(n)])
y = np.array([j + randint(0, f) - randint(0, f) for j in range(n)])
lin_a, lin_b = linear_regression(x, y)

plt.title("linear regression")
plt.xlabel("abscissa (y)")
plt.ylabel("ordinate (x)")

plt.plot(x, y, "ro")
plt.plot(x, np.vectorize(lambda v: lin_a * v + lin_b)(x), "-b")
plt.show()
