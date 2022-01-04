import numpy as np

NB_DAYS = 80 # number of days

# read data from file
TXT_FILE = 'Data/Q6.txt'
with open(TXT_FILE) as f:
    fish = f.read()
# convert data set to a list of int
fish = fish.split(',')
fish = np.array([(float(i) + 1.) for i in fish])
# loop through NB_DAYS days
for i in range(NB_DAYS):
    fish -= np.ones(len(fish)) # count down
    nb_new = sum(fish == 0) # how many new born laternfishes
    fish = np.where(fish == 0, 7, fish) # reset the count down
    fish = np.append(fish, [9]*nb_new) # add the new born fishes
# the answer
print(len(fish))
# =====================================
# or you can do it like this
# read data from file
TXT_FILE = 'Data/Q6.txt'
with open(TXT_FILE) as f:
    fish = f.read()
# convert data set to a list of int
fish = fish.split(',')
fish = np.array([int(i) for i in fish])
nb_new = 0 # initiate the number of new born fish
# loop through NB_DAYS days
for i in range(NB_DAYS):
    fish = np.where(fish > 0, fish - 1, 6) # count down and reset
    fish = np.append(fish, [8]*nb_new) # add the new born fishes
    nb_new = sum(fish == 0) # how many new born laternfishes next turn
# the answer
print(len(fish))
# =====================================
# or you can do it like this
# read data from file
TXT_FILE = 'Data/Q6.txt'
with open(TXT_FILE) as f:
    fish = f.read()
# convert data set to a list of int
fish = fish.split(',')
fish = np.array([int(i) for i in fish])
fish = list(np.bincount(fish))
fish += [0]*(9 - len(fish))
nb_new = 0 # initiate the number of new born fish
# loop through NB_DAYS days
for i in range(NB_DAYS):
    new_fish = fish[1:] + [nb_new] # count down and add the new born
    new_fish[6] += fish[0] # reset count down
    nb_new = new_fish[0] # number of new born fishes
    fish = new_fish
# the answer
print(sum(fish))
