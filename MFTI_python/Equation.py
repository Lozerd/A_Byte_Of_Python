import numpy as np

x = [1, 10, 1000]

sinus = 1 / (np.sin(x) + 1)
e = np.e ** sinus
temp_x = [(1 / (x[0] * 5)) + 5 / 4, (1 / (x[1] * 5)) + 5 / 4, (1 / (x[2] * 5)) + 5 / 4]
x = [x[0] ** 2+1, x[1] ** 2+1, x[2] ** 2+1]
log = np.log(temp_x) / np.log(x)
print(f"{log}")
