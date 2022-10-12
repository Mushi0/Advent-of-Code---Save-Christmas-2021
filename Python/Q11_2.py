import numpy as np

NB_STEPS = 100

# read data from file
TXT_FILE = 'Data/Q11.txt'
with open(TXT_FILE) as f:
    energy_level = f.read()
# convert data to a numpy array (matrix)
energy_level = energy_level.split('\n')[:-1]
energy_level = np.array([[int(i) for i in line] for line in energy_level])

M, N = energy_level.shape
i = 0
# loop through NB_STEPS of steps
while True:
    energy_level += 1 # each octopus gain 1 energy
    changes = True
    already_flashed = [] # initiate the octopuses already flashed
    # loop until all the flashes are over (no change after one round)
    while changes:
        changes = False # initiate the status
        flash = np.where(energy_level > 9) # find all the octopuses ready to flash
        # if there are octopuses ready to flash, the loop doesn't end
        if len(flash[0]) > 0:
            changes = True
        for j in range(len(flash[0])):
            # flash[0][j], flash[1][j] is the coordinate of the flashing octopus
            x = flash[0][j]; y = flash[1][j]
            # add one to all the adjacent octopuses
            for k in range(max(0, x - 1), min(x + 2, M)):
                for l in range(max(0, y - 1), min(y + 2, N)):
                    if [k, l] not in already_flashed:
                        energy_level[k][l] += 1
        for j in range(len(flash[0])):
            # change the already flashed octopus to 0 and add it to the list
            x = flash[0][j]; y = flash[1][j]
            energy_level[x][y] = 0
            already_flashed.append([x, y])
    # print(len(np.where(energy_level == 0)[0]))
    i += 1
    # if all the octopuses flash at the same time
    if len(np.where(energy_level == 0)[0]) == M*N:
        # the answer
        print(i)
        break
