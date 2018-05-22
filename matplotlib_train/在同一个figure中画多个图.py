import matplotlib.pyplot as plt
import numpy as np

plt.figure()

x = np.arange(-10, 10)
y1 = x ** 2
y2 = 2 * x + 1
y3 = x ** 3
y4 = x * x - x

# subplot(共几行,共几列,第几个)
plt.subplot(2, 2, 1)
plt.plot(x, y1)

plt.subplot(2, 2, 2)
plt.plot(x, y2)

plt.subplot(2, 2, 3)
plt.plot(x, y3)

plt.subplot(2, 2, 4)
plt.plot(x, y4)

plt.show()
