import numpy as np
import re

# read data from file
TXT_FILE = 'Data/Q5.txt'
map = np.zeros([1000, 1000])
with open(TXT_FILE) as f:
    # loop through every line
    while True:
        line = f.readline() # read the line
        if not line:
            break
        # convert the line to a list of coordinates
        coord = re.findall(r'(.*?),(.*?) -> (.*?),(.*?)\n', line)[0]
        coord = [int(i) for i in coord]
        # vertical lines
        if coord[0] == coord[2]:
            x = coord[0] # x coordinate
            # add one to every points on the line segment
            for y in range(min([coord[1], coord[3]]), max([coord[1], coord[3]]) + 1):
                map[x][y] += 1
        # horizontal lines
        elif coord[1] == coord[3]:
            y = coord[1] # y coordinate
            # add one to every points on the line segment
            for x in range(min([coord[0], coord[2]]), max([coord[0], coord[2]]) + 1):
                map[x][y] += 1
sum(sum(np.where(map >= 2, 1, 0)))
