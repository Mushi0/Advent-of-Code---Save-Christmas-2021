import numpy as np

coord = np.array([0, 0]) # [horizontal position, depth]
commands = {'forward': np.array([1, 0]), 'down': np.array([0, 1]), 'up': np.array([0, -1])}
# read data from file
TXT_FILE = 'Data/Q2.txt'
with open(TXT_FILE) as f:
    while True:
        line = f.readline() # read one line from the file
        if not line:
            break
        command = line.split(" ") # split the command and the amount
        command[1] = int(command[1][:-1]) # convert the amount into integer
        coord += commands[command[0]]*command[1] # execute the command
# the answer
print(coord[0]*coord[1])
