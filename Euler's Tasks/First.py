# Syntactic sugar
import time

start = time.time()
summary = sum([x for x in range(1, 100) if x % 3 == 0 or x % 5 == 0])
print(summary)
print(time.time() - start)

# Another way, using more time because of many other functions
# import time
#
# start = time.time()
# summary = []
# for i in range(1, 100):
#     if i % 3 == 0:
#         summary.append(i)
#     elif i % 5 == 0:
#         summary.append(i)
# summary = sum(summary)
# print(summary)
#print('Time needed', time.time() - start)
