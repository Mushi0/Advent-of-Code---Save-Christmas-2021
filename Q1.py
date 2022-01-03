import numpy as np

# read data from file
TXT_FILE = 'Q1.txt'
with open(TXT_FILE) as f:
    radar_data = f.read()
# convert data to a list of int
radar_data = radar_data.split('\n')[:-1]
radar_data = np.array([int(i) for i in radar_data])
# differences between two continuous number
diff = radar_data[1:] - radar_data[:-1]
# the answer
print(sum(diff > 0))
# =====================================
# or you can do it like this
# read data from file
TXT_FILE = 'Q1.txt'
with open(TXT_FILE) as f:
    radar_data = f.read()
# convert data to a list of int
radar_data = radar_data.split('\n')[:-1]
radar_data = np.array([int(i) for i in radar_data])
# the answer
print(sum((radar_data[1:] - radar_data[:-1]) > 0))
