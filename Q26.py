import pandas as pd

# read data from file
TXT_FILE = 'Q25.txt'
with open(TXT_FILE) as f:
    dots_instructions = f.read()
# tidy up the data, create a list of dots and instructions
dots_instructions = dots_instructions.split('\n')[:-1]
divide_index = dots_instructions.index('')
dots = dots_instructions[:divide_index]
dots = [dot.split(',') for dot in dots]
dots = [[int(i) for i in dot] for dot in dots]
instructions = dots_instructions[divide_index + 1:]

# loop through all the instructions
for instruction in instructions:
    axis = ['x', 'y'].index(instruction[11])
    line = int(instruction[13:])
    # fold the paper
    for dot in dots:
        if dot[axis] > line:
            dot[axis] = 2*line - dot[axis]
        elif dot[axis] == line:
            dots.remove(dot)
# reverse the coordinate for plotting
for dot in dots:
    dot.reverse()
# transform list to tuple for the set() function
dots = list(set([tuple(dot) for dot in dots]))

# # ------------------pandas plot-----------------------
# # use the pandas to plot
# dots = pd.DataFrame([list(dot) for dot in dots])
# dots.plot.scatter(y = 0, x = 1, c = 'DarkBlue')

# ------------------manual plot-----------------------
# plot manually
dots.sort()
for i in range(6):
    for j in range(39):
        dot = dots[0]
        if dot == (i, j):
            print('#', end = '')
            dots.remove(dot)
        else:
            print('.', end = '')
    print()
