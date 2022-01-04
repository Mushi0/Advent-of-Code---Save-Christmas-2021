# read data from file
TXT_FILE = 'Data/Q3.txt'
with open(TXT_FILE) as f:
    power_data = f.read()
power_data = power_data = power_data.split('\n')[:-1] # convert data to a matrix
power_data = [list(map(int, list(i))) for i in power_data] # transpose the matrix

# create the temporary data list
power_data_temp = power_data
i = 0
# iterate until finding the rating
while len(power_data_temp) > 1:
    # initoate the ones and zeros
    ones = []
    zeros = []
    # divide the data set into two
    for row in power_data_temp:
        if row[i] == 1:
            ones.append(row)
        else:
            zeros.append(row)
    # find the most common set
    if len(ones) >= len(zeros):
        power_data_temp = ones
    else:
        power_data_temp = zeros
    i += 1
    if i > len(power_data_temp[0]):
        i = 0
# the oxygen rating
oxygen = power_data_temp[0]
oxygen = ''.join([str(i) for i in oxygen]) # convert list to string

# create the temporary data list
power_data_temp = power_data
i = 0
# iterate until finding the rating
while len(power_data_temp) > 1:
    # initoate the ones and zeros
    ones = []
    zeros = []
    # divide the data set into two
    for row in power_data_temp:
        if row[i] == 1:
            ones.append(row)
        else:
            zeros.append(row)
    # find the most uncommon set
    if len(zeros) <= len(ones):
        power_data_temp = zeros
    else:
        power_data_temp = ones
    i += 1
    if i > len(power_data_temp[0]):
        i = 0
# the oxygen rating
CO2 = power_data_temp[0]
CO2 = ''.join([str(i) for i in CO2]) # convert list to string

# the answer
print(int(oxygen, 2)*int(CO2, 2))
