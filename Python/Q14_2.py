# from collections import Counter
# from datetime import datetime
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
#
# # 40 steps
# for i in range(40):
#     start = datetime.now()
#     # find all the insertions
#     insertion = list(zip(list(polymer[:-1]), list(polymer[1:])))
#     insertion = [''.join(pair) for pair in insertion]
#     insertion = [pair_rules[pair] for pair in insertion]
#     # insert the insertion
#     result_polymer = [None]*(len(polymer) + len(insertion))
#     result_polymer[::2] = polymer
#     result_polymer[1::2] = insertion
#     # update the polymer list
#     polymer = result_polymer
#     print('Time: ', datetime.now() - start)
# # count all the elements in the polymer
# count = Counter(result_polymer)
# # the answer
# print(max(count.values()) - min(count.values()))

#====================================================================

# import numpy as np
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
#         result = np.zeros(nb_alph)
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
# nb_alph = len(alphabet)
#
# count_polymer = np.zeros(nb_alph) # initialize the count
# # loop theough all the pairs in the polymer
# for i in range(len(polymer) - 1):
#     count_polymer += insert(40, polymer[i:i + 2])
# count_polymer[alphabet.index(polymer[-1])] += 1
# # the answer
# print(max(count_polymer) - min(count_polymer))

# #====================================================================
# # Merge sort
# from collections import Counter
#
# def insert(polymer):
#     '''
#     Splits the string to two substring and recursively insert the element
#
#     Input: nb_steps (int): the number of steps
#             polymer (str): the original polymer
#     Output: the result string
#     '''
#     len_polymer = len(polymer)
#     # if only one char, return it
#     if len_polymer == 1:
#         return polymer
#     # else, return the two substring
#     else:
#         half_len = len_polymer//2
#         return insert(polymer[:half_len]) + pair_rules[polymer[half_len - 1: half_len + 1]] + \
#                 insert(polymer[half_len:])
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
#
# # polymer = 'NNCB'
# # pair_rules = {'CH': 'B', 'HH': 'N', 'CB': 'H', 'NH': 'C', 'HB': 'C', \
# #             'HC': 'B', 'HN': 'C', 'NN': 'C', 'BH': 'H', 'NC': 'B', \
# #             'NB': 'B', 'BN': 'B', 'BB': 'N', 'BC': 'B', 'CC': 'N', 'CN': 'C'}
#
# new_polymer = polymer
# for i in range(40):
#     new_polymer = insert(new_polymer)
#
# # count all the elements in the polymer
# count = Counter(new_polymer)
# # the answer
# print(max(count.values()) - min(count.values()))

#====================================================================

import numpy as np
from datetime import datetime
from functools import lru_cache

@lru_cache(maxsize = None)
def insert(nb_steps, polymer):
    '''
    Recursively count the appearance of elements in the polymer

    Input: nb_steps (int): the number of steps
            polymer (str): the original polymer (2 chars)
    Output: the count numbers in the order of alphabet
    '''
    # if this is the last step, return the count
    if nb_steps == 1:
        return pair_rules_count[polymer]
    # else, insert the new element and return the sum of the counts
    else:
        nb_steps -= 1
        insertion = pair_rules[polymer]
        result = insert(nb_steps, polymer[0] + insertion) + insert(nb_steps, insertion + polymer[1])
        return result

# read data from file
TXT_FILE = 'Data/Q14.txt'
with open(TXT_FILE) as f:
    polymer_pairs = f.read()
# tidy up the data, create the polymer string and list of rules
polymer_pairs = polymer_pairs.split('\n')[:-1]
polymer = polymer_pairs[0]
pair_rules = polymer_pairs[2:]
pair_rules = dict([rule.split(' -> ') for rule in pair_rules])
# the set of all the elemnts appear in the polymer
alphabet = list(set(pair_rules.values()))
nb_alph = len(alphabet)
pair_rules_count = dict()
for pair in pair_rules.keys():
    result = np.zeros(nb_alph)
    result[alphabet.index(pair[0])] += 1
    result[alphabet.index(pair_rules[pair])] += 1
    pair_rules_count[pair] = result

start = datetime.now()

count_polymer = np.zeros(nb_alph) # initialize the count
# loop theough all the pairs in the polymer
for i in range(len(polymer) - 1):
    count_polymer += insert(40, polymer[i:i + 2])
count_polymer[alphabet.index(polymer[-1])] += 1
# the answer
print(max(count_polymer) - min(count_polymer))

print('Time: ', datetime.now() - start)
