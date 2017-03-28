# This test assignment is intended to screen out candidates with no Python programming skills at the pre-interview stage. The task is very simple and we don't think that a candidate will take more than an hour to complete it. Apart from checking the operability of a program developed as a result of the task, we will also carefully read the script. We believe that reading the script can help us better understand the professional level of a programmer. It is desirable that a candidate uses Python 3 to complete the task. The solution must be a python script with command line interface. Script input is a text file and the output is statistics of word occurrences. As a result, the program must print out all unique words from the text with the number of their occurrences. Words in output must be sorted by number of their occurrences in descending order, words with the equal number of occurrences must be sorted in alphabetic order. Each word and number of its occurrences must be printed on a new line in format: <word>: <frequency>.
import sys
from collections import Counter

with open(sys.argv[1]) as f:
    words_counter = Counter(line.strip() for line in f).items()

words_counter_sorted = sorted(words_counter, key=lambda x: (-x[1], x[0]))
for word, frequency in words_counter_sorted:
    print('{0}: {1}'.format(word, frequency))
