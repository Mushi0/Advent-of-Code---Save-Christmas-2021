# read data from file
heightmap = []
TXT_FILE = 'Data/Q9.txt'
with open(TXT_FILE) as f:
    while True:
        line = f.readline() # read one line from the file
        if not line:
            break
        # convert the string to a list
        line = list(line)[:-1]
        line = [int(i) for i in line]
        heightmap.append(line) # append the heightmap
risk_level_sum = 0 # initiate the sum of risk level
# the shape of the map
N = len(heightmap)
M = len(heightmap[0])
# find the low points
for i, line in enumerate(heightmap):
    for j, number in enumerate(line):
        if (j == 0 or number < line[j - 1]) \
        and (j == M - 1 or number < line[j + 1]) \
        and (i == 0 or number < heightmap[i - 1][j]) \
        and (i == N - 1 or number < heightmap[i + 1][j]):
            risk_level_sum += (number + 1)
# answer
print(risk_level_sum)
