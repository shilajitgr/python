from collections import Counter

a = 'aaaaabbbbccc'
my_counter = Counter(a)
print(my_counter)   # creates a dictionary with the number of times each character appears
print(my_counter.most_common(2)) # prints the two most common characters with the appearence count
print(my_counter.most_common(2)[0][0]) # prints the most common character

