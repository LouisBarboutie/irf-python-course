import numpy as np

with open('input.txt', 'r') as f:
    content = f.read()

vals = content.split()
list1 = [int(v) for v in vals[0::2]]
list2 = [int(v) for v in vals[1::2]]

list1.sort()
list2.sort()

diff = []
for i1, i2 in zip(list1, list2):
    diff.append(abs(i2 - i1))
print(sum(diff))

test = np.genfromtxt('input.txt', delimiter=7)
print(test)
