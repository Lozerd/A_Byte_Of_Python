import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1, 1.01, 0.1)

sin = (1 / (np.sin(x) ** 2 + 1))
tan = np.tan(sin) + 1
log = np.log((x ** 2) + 1) / np.log(tan)
exp = np.exp(abs(x) / 10)
result = log * exp
# result = np.log(x) / np.log()
print(f"{tan[12]}\n{log[3]}\n{exp[12]}\n{result}")

plt.plot(result, color='green')
plt.show()
