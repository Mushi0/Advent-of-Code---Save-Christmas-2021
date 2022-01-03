point_table = {')': 3, ']': 57, '}': 1197, '>': 25137} # the point table
pair = {'(':  ')', '[': ']', '{': '}', '<': '>'} # the table for finding the pairs

# read data from file
TXT_FILE = 'Q19.txt'
point = 0 # initiate the points
with open(TXT_FILE) as f:
    while True:
        line = f.readline() # read one line from the file
        if not line:
            break
        unpaired = [] # initiate the unpaired chunks
        # loop through all the characters in the line
        for char in line:
            # if the character is the closing symbol, check if it's correct
            if char in pair.values():
                if pair[unpaired[-1]] == char:
                    unpaired = unpaired[:-1]
                else:
                    point += point_table[char]
                    break
            # else, add the character to the unpaired list
            else:
                unpaired.append(char)
# the answer
print(point)
