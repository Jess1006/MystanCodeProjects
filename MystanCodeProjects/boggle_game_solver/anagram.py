"""
File: anagram.py
Name: Jess
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variables
dict_list = []                # the list that save the words in dict
ans = []                      # list of the ans


def main():
    """
    This function print out the anagrams the user input in the dictionary,
    and calculate the code efficiency
    """
    read_dictionary()
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    while True:
        word = input("Find anagrams for: ")
        if word == EXIT:
            break
        start = time.time()
        print('Searching...')
        find_anagrams(word)
        print(f'{len(ans)} anagrams: {ans}')
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')
        # renew
        ans.clear()


def read_dictionary():
    """
    read the dict file into the dict list
    """
    with open(FILE, 'r') as f:
        for line in f:
            words_lst = line.split()
            for word in words_lst:
                dict_list.append(word)


def find_anagrams(s):
    """
    :param s: (str) word
    """

    finding_helper(list(s), 0, len(s))


def finding_helper(list_s, index, len_s):
    """
    This function finds the anagrams in the dictionary

    :param list_s: (lst) word string => list of chars
    :param index:  (int) index starts from 0
    :param len_s:  (int) the length of the word string
    """
    # base case
    if index == len_s:
        ans_maybe = ''.join(list_s)
        if ans_maybe in dict_list:
            print('Found:', ans_maybe)
            print('Searching...')
            ans.append(ans_maybe)
        return

    # recursion
    for i in range(index, len_s):
        if index != i:
            if not duplicate(list_s, index, i):
                # if length of word more than ten chars, add with the early stopper
                if len_s > 10:
                    word = ''.join(list_s)
                    if has_prefix(word[:2]):
                        # choose(swap)
                        (list_s[index], list_s[i]) = (list_s[i], list_s[index])
                        # explore
                        finding_helper(list_s, index+1, len_s)
                        # un-choose
                        (list_s[index], list_s[i]) = (list_s[i], list_s[index])
                else:
                    # choose(swap)
                    (list_s[index], list_s[i]) = (list_s[i], list_s[index])
                    # explore
                    finding_helper(list_s, index + 1, len_s)
                    # un-choose
                    (list_s[index], list_s[i]) = (list_s[i], list_s[index])
        else:
            finding_helper(list_s, index + 1, len_s)


def duplicate(s, index, check):
    """
    This function checks whether there are duplications in the word string

    :param s: (lst) list of the word string
    :param index: (int) the char to check whether there's a duplication
    :param check: (int) the char that is being checked
    :return: (boolean)
    """
    for i in range(index, check):
        if s[i] == s[check]:
            return True
    return False


def has_prefix(sub_s):
    """
    early stopper
    :param sub_s: (str) sub string of the word
    :return: (boolean)
    """
    for word in dict_list:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
