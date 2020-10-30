import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.1, 0.1)
x1, y1 = [0, 80], [0, 0]  # отрезок, с началом и концом координат в массиве
plt.plot(x1, y1, marker='.')
# y(0) = 80
plt.plot(x ** 2 - x - 6)
plt.show()

# x = np.arange(-10, 10.01, 0.01)
# plt.plot(x, np.sin(x), x, np.cos(x), x, -x)
# plt.xlabel(r'$x$')
# plt.ylabel(r'$f(x)$')
# plt.title(r'$f_1(x)=\sin(x),\ f_2(x)=\cos(x),\ f_3(x)=-x$')
# plt.grid(True)
# plt.show()

# x = np.arange(-10, 10.01, 0.01)
# plt.plot(x, np.sin(x), x, np.cos(x), x, -x)
# plt.show()

# x = np.arange(-10, 10.01, 0.01)
# plt.plot(x, x**3)
# plt.show()
