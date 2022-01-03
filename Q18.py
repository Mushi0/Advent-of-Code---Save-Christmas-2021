def detect_downward(i, j, counted):
    '''
    Recursively count the basin points

    Input: i, j (int): the coordinate of the current point
            counted (list): the list of counted points
    Output: the count number
    '''
    number = heightmap[i][j] # the current number
    # if the number is 9, return 0
    if number == 9:
        return 0
    # if the number is smaller than 9 and it is not counted before,
    # count all the downward points around current point
    elif [i, j] not in counted:
        counted.append([i, j]) # add the current number to the list of counted number
        count = 1 # initiate the count
        # count all the downward points at the four directions
        # left
        if j != 0 and number < heightmap[i][j - 1]:
            count += detect_downward(i, j - 1, counted)
        # right
        if j != M - 1 and number < heightmap[i][j + 1]:
            count += detect_downward(i, j + 1, counted)
        # up
        if i != 0 and number < heightmap[i - 1][j]:
            count += detect_downward(i - 1, j, counted)
        # down
        if i != N - 1 and number < heightmap[i + 1][j]:
            count += detect_downward(i + 1, j, counted)
        return count
    else:
        return 0

# read data from file
heightmap = []
TXT_FILE = 'Q17.txt'
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
counts = []
# find the low points and count the points in the basin
for i in range(N):
    for j in range(M):
        number = heightmap[i][j]
        if (j == 0 or number < heightmap[i][j - 1]) \
        and (j == M - 1 or number < heightmap[i][j + 1]) \
        and (i == 0 or number < heightmap[i - 1][j]) \
        and (i == N - 1 or number < heightmap[i + 1][j]):
            counts.append(detect_downward(i, j, []))
counts.sort()
# answer
print(counts[-1]*counts[-2]*counts[-3])
