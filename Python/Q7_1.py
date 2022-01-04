import numpy as np

# read data from file
TXT_FILE = 'Data/Q7.txt'
with open(TXT_FILE) as f:
    positions = f.read()
# convert data set to a list of int
positions = positions.split(',')
positions[-1] = positions[-1][:-1]
positions = np.array([int(i) for i in positions])
positions = np.sort(positions)
N = len(positions)
if N % 2 == 0:
    # the answer
    print(sum(positions[int(N/2):] - positions[:int(N/2)]))
else:
    # the answer
    print(sum((positions[int(N/2) + 1:] - positions[:int(N/2)])))
