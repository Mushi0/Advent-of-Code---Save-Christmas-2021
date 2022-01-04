import numpy as np

# read data from file
TXT_FILE = 'Data/Q7.txt'
with open(TXT_FILE) as f:
    positions = f.read()
# convert data set to a list of int
positions = positions.split(',')
positions[-1] = positions[-1][:-1]
positions = np.array([int(i) for i in positions])
median = np.median(positions) # the median
# calculte the fuel
distances = np.absolute(positions - median)
min_fuel = int(sum(distances*(distances + 1)/2))
# brute force search below the median
i = 1
while True:
    # calculate the new fuel for median - i
    distances = np.absolute(positions - median - i)
    new_fuel = int(sum(distances*(distances + 1)/2))
    # find the smallest fuel cost
    if new_fuel < min_fuel:
        min_fuel = new_fuel
    else:
        break
    i += 1
# brute force search above the median
i = 1
while True:
    # calculate the new fuel for median + i
    distances = np.absolute(positions - median + i)
    new_fuel = int(sum(distances*(distances + 1)/2))
    # find the smallest fuel cost
    if new_fuel < min_fuel:
        min_fuel = new_fuel
    else:
        break
    i += 1
# the answer
print(min_fuel)
