# read data from file
TXT_FILE = 'Data/Q8.txt'
count = 0
unique_segments = [2, 4, 3, 7]
with open(TXT_FILE) as f:
    while True:
        line = f.readline() # read one line from the file
        if not line:
            break
        line = line.split(' | ') # split the digits and the output
        output = line[1].split(' ') # convert the output to list
        output[-1] = output[-1][:-1]
        # count the number of 1, 4, 7, and 8
        for digit in output:
            if len(digit) in unique_segments:
                count += 1
# the answer
print(count)
