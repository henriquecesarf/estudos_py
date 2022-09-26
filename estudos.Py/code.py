import numpy as np
import matplotlib.pyplot as plt

# Gráfico a apartir da função
x1 = np.linspace(-3, 3, num=100)
y1 = -x1**2+1
x2 = np.linspace(-3, 3, num=100)
y2 = +x2**0+0
x3 = np.linspace(-1, 1, num=100)
y3 = -x2*-3+1
plt.plot(x1, y1, 'bo')
plt.plot(x2, y2, 'go')
plt.plot(x3, y3, 'bo')
# plt.axis((-3, 6, -8, 6))

plt.show()
