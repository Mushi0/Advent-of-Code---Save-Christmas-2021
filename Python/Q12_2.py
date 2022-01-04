def path_exist(current, paths, uppwer, lower, visited_lower, visited_twice):
    '''
    Recursively count the existing path

    Input: current (str): the current position
            paths (list of lists): the list of all the paths
            upper, lower (sets): the sets of upper (lower) case caves
            visited_lower (set): the set of visited lower case caves
            visited_twice (boolean): True if one of the lower cave has been visited twice
    Output: the count number
    '''
    # if the path leads to 'end', return 1 existing path
    if current == 'end':
        return 1
    else:
        new_visited_lower = visited_lower.copy()
        new_lower = lower
        # when the current position is a lower case cave
        if current in lower:
            # start position
            if current == 'start':
                new_lower -= {'start'}
            # add the current cave to the visited cave set
            new_visited_lower.add(current)
            # if one cave is visited twice, set the boolean to True
            if (not visited_twice) and (current in visited_lower):
                visited_twice = True
            # if visited twice, remove all the caves visited from the lower set
            if visited_twice:
                new_lower = lower - new_visited_lower
        # if the current position is not in any set, it is not a valid path
        elif current not in upper:
            return 0

        count = 0 # initiate the counter
        # find all the paths from the current position and add up all the existing paths
        for path in paths:
            if path[0] == current:
                count += path_exist(path[1], paths, upper, new_lower, new_visited_lower, visited_twice)
            elif path[1] == current:
                count += path_exist(path[0], paths, upper, new_lower, new_visited_lower, visited_twice)
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
print(path_exist('start', paths, upper, lower, set(), False))
