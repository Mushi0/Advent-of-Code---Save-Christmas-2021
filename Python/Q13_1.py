# read data from file
TXT_FILE = 'Data/Q13.txt'
with open(TXT_FILE) as f:
    dots_instructions = f.read()
# tidy up the data, create a list of dots and instructions
dots_instructions = dots_instructions.split('\n')[:-1]
divide_index = dots_instructions.index('')
dots = dots_instructions[:divide_index]
dots = [dot.split(',') for dot in dots]
dots = [[int(i) for i in dot] for dot in dots]
instructions = dots_instructions[divide_index + 1:]

# find the first instruction: axis and line
first_instruction = instructions[0]
first_axis = ['x', 'y'].index(first_instruction[11])
first_line = int(first_instruction[13:])
# fold the paper
for dot in dots:
    if dot[first_axis] > first_line:
        dot[first_axis] = 2*first_line - dot[first_axis]
    elif dot[first_axis] == first_line:
        dots.remove(dot)
# transform list to tuple for the set() function
dots = [tuple(dot) for dot in dots]
# the answer
print(len(set(dots)))
