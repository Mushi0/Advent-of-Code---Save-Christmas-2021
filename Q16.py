# read data from file
TXT_FILE = 'Q15.txt'
count = 0
unique_segments = {2: 1, 4: 4, 3: 7, 7: 8}
digit_map = ['']*10
with open(TXT_FILE) as f:
    while True:
        # initial for 0, 2, 3, 5, 6, 9
        zero_six_nine = []
        two_three_five = []
        line = f.readline() # read one line from the file
        if not line:
            break
        line = line.split(' | ') # split the digits and the output
        output = line[1].split(' ') # convert the output to list
        output[-1] = output[-1][:-1]
        output = [set(digit) for digit in output]
        digits = line[0].split(' ') # convert the 10 digits to list
        digits = [set(digit) for digit in digits]
        for digit in digits:
            digit_len = len(digit)
            # find numbers 1, 4, 7, 8
            if digit_len in unique_segments:
                digit_map[unique_segments[digit_len]] = digit
            # find numbers 0, 6, 9
            elif digit_len == 6:
                zero_six_nine.append(digit)
            # find numbers 2, 3, 5
            elif digit_len == 5:
                two_three_five.append(digit)
        four_not_in_one = digit_map[4] - digit_map[1]
        # distinguish between 0, 6, and 9
        for digit in zero_six_nine:
            if not digit_map[1].issubset(digit):
                digit_map[6] = digit
            elif not four_not_in_one.issubset(digit):
                digit_map[0] = digit
            else:
                digit_map[9] = digit
        # distinguish between 2, 3, and 5
        for digit in two_three_five:
            if digit_map[1].issubset(digit):
                digit_map[3] = digit
            elif four_not_in_one.issubset(digit):
                digit_map[5] = digit
            else:
                digit_map[2] = digit
        # find the output number
        output_number = ''
        for digit in output:
            output_number += str(digit_map.index(digit))
        count += int(output_number)
# the answer
print(int(count))
