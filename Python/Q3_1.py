import numpy as np

gamma = ''; epsilon = ''
# read data from file
TXT_FILE = 'Data/Q3.txt'
with open(TXT_FILE) as f:
    power_data = f.read()
power_data = power_data = power_data.split('\n')[:-1] # convert data to a matrix
power_data = np.array([list(map(int, list(i))) for i in power_data]).T # transpose the matrix
# find the most frequent number
for row in power_data:
    most_freq = np.bincount(row).argmax()
    gamma += str(most_freq) # gamma rate
    epsilon += str(1 - most_freq) # epsilon rate
# the answer
print(int(gamma, 2)*int(epsilon, 2))
