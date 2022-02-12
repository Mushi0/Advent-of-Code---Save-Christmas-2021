from collections import Counter
from datetime import datetime

# read data from file
TXT_FILE = 'Data/Q14.txt'
with open(TXT_FILE) as f:
    polymer_pairs = f.read()
# tidy up the data, create the polymer string and list of rules
polymer_pairs = polymer_pairs.split('\n')[:-1]
polymer = polymer_pairs[0]
pair_rules = polymer_pairs[2:]
pair_rules = dict([rule.split(' -> ') for rule in pair_rules])

start = datetime.now()

# 10 steps
for i in range(10):
    # find all the insertions
    insertion = list(zip(list(polymer[:-1]), list(polymer[1:])))
    insertion = [''.join(pair) for pair in insertion]
    insertion = [pair_rules[pair] for pair in insertion]
    # insert the insertion
    result_polymer = [None]*(len(polymer) + len(insertion))
    result_polymer[::2] = polymer
    result_polymer[1::2] = insertion
    # update the polymer list
    polymer = result_polymer
# count all the elements in the polymer
count = Counter(result_polymer)
# the answer
print(max(count.values()) - min(count.values()))

print('Time: ', datetime.now() - start)

#====================================================================

# import numpy as np
# from datetime import datetime
#
# def insert(nb_steps, polymer):
#     '''
#     Recursively count the appearance of elements in the polymer
#
#     Input: nb_steps (int): the number of steps
#             polymer (str): the original polymer (2 chars)
#     Output: the count numbers in the order of alphabet
#     '''
#     # if this is the last step, return the count
#     if nb_steps == 0:
#         result = np.zeros(np_alph)
#         result[alphabet.index(polymer[0])] += 1
#         return result
#     # else, insert the new element and return the sum of the counts
#     else:
#         nb_steps -= 1
#         insertion = pair_rules[polymer]
#         result = insert(nb_steps, polymer[0] + insertion) + insert(nb_steps, insertion + polymer[1])
#         return result
#
# # read data from file
# TXT_FILE = 'Data/Q14.txt'
# with open(TXT_FILE) as f:
#     polymer_pairs = f.read()
# # tidy up the data, create the polymer string and list of rules
# polymer_pairs = polymer_pairs.split('\n')[:-1]
# polymer = polymer_pairs[0]
# pair_rules = polymer_pairs[2:]
# pair_rules = dict([rule.split(' -> ') for rule in pair_rules])
# # the set of all the elemnts appear in the polymer
# alphabet = list(set(pair_rules.values()))
# np_alph = len(alphabet)
#
# start = datetime.now()
#
# count_polymer = np.zeros(np_alph) # initialize the count
# # loop theough all the pairs in the polymer
# for i in range(len(polymer) - 1):
#     count_polymer += insert(10, polymer[i:i + 2])
# count_polymer[alphabet.index(polymer[-1])] += 1
# # the answer
# print(max(count_polymer) - min(count_polymer))
#
# print('Time: ', datetime.now() - start)
