import numpy as np

point_table = {')': 1, ']': 2, '}': 3, '>': 4} # the point table
pair = {'(':  ')', '[': ']', '{': '}', '<': '>'} # the table for finding the pairs

# read data from file
TXT_FILE = 'Data/Q10.txt'
points = [] # intiate the points list
with open(TXT_FILE) as f:
    while True:
        line = f.readline() # read one line from the file
        if not line:
            break
        unpaired = [] # initiate the unpaired chunks
        incomplete = True
        # loop through all the characters in the line
        for char in line:
            # check whether the line is corrupted or not,
            # and record the unpaied chunks
            if char in pair.values():
                if pair[unpaired[-1]] == char:
                    unpaired = unpaired[:-1]
                else:
                    incomplete = False
                    break
            else:
                unpaired.append(char)
        # if the line is incomplete, calculate the point
        if incomplete:
            unpaired.reverse()
            point = 0
            for char in unpaired[1:]:
                point = point*5 + point_table[pair[char]]
            points.append(point)
# the answer
print(int(np.median(np.array(points))))
