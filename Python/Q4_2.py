import numpy as np

# read data from file
TXT_FILE = 'Data/Q4.txt'
with open(TXT_FILE) as f:
    draw = f.readline() # the random numbers to draw
    # convert the draw to a list of int
    draw = draw.split(',')
    draw[-1] = draw[-1][:-1]
    draw = [int(i) for i in draw]
    # initiate the winner
    winner = {'round': 0, 'last_draw': 0, 'score': 0}
    # loop through every board
    while True:
        # read the board from the file
        board = []
        if not f.readline():
            break
        for i in range(5):
            line = f.readline() # read one line from the file
            # convert the line to a list of int
            line = line.split(' ')
            line[-1] = line[-1][:-1]
            board.append([int(i) for i in line if i != ''])
        board = np.array(board) # convert board to np array
        i = 1
        # loop through draw
        while i < len(draw):
            last_draw = draw[i] # the last draw number
            board = np.where(board == last_draw, 0, board) # replace the last draw with 0
            # calculate the sum of each row and column
            sum_row = board.sum(axis = 1)
            sum_column = board.sum(axis = 0)
            # if there is one complete row or column
            if 0 in sum_row or 0 in sum_column:
                # if the new board is worse than the current winner, replace it
                if winner['round'] < i:
                    winner = {'round': i, 'last_draw': last_draw, 'score': sum(sum(board))*last_draw}
                break
            i += 1
# the answer
print(winner)
