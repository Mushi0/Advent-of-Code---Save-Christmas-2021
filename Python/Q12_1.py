def path_exist(current, paths, uppwer, lower):
    '''
    Recursively count the existing path

    Input: current (str): the current position
            paths (list of lists): the list of all the paths
            upper, lower (sets): the sets of upper (lower) case caves
    Output: the count number
    '''
    # if the path leads to 'end', return 1 existing path
    if current == 'end':
        return 1
    else:
        # when the current position is a lower case cave
        if current in lower:
            new_lower = lower - {current}
        elif current in upper:
            new_lower = lower
        # if the current position is not in any set, it is not a valid path
        else:
            return 0

        count = 0 # initiate the counter
        # find all the paths from the current position and add up all the existing paths
        for path in paths:
            if path[0] == current:
                count += path_exist(path[1], paths, upper, new_lower)
            elif path[1] == current:
                count += path_exist(path[0], paths, upper, new_lower)
        return count

# read data from file
TXT_FILE = 'Data/Q12.txt'
with open(TXT_FILE) as f:
    map = f.read()
map = map.split('\n')[:-1]
# initiate the upper, lower sets and the paths list
upper = set(); lower = set()
paths = []
# create the sets
for path in map:
    path = path.split('-')
    paths.append(path)
    for cave in path:
        if cave.isupper():
            upper.add(cave)
        elif cave.islower() and cave != 'end':
            lower.add(cave)
        elif cave != 'end':
            print('"' + cave + '"' + ' should be upper or lower case string. ')
# the answer
print(path_exist('start', paths, upper, lower))
