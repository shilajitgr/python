"""
task:

write two regexes:
1) check if the range of postal code is between 100000 and 999999
2) there must not be more than 1 alternating repeating digits

alternating repeating digits are digits that occur at an interval of one digit
eg: 124421 - there no such digits here
    121442 - here 1 is the only such digit
    122121 - here both 1 and 2 are examples of such digits
"""

import re

regex_integer_in_range = r"^[1-9]\d{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=(\d)(\d)\1)"	# Do not delete 'r'.
P = input()
print(bool(re.match(regex_integer_in_range, P)))
print(len(re.findall(regex_alternating_repetitive_digit_pair, P)))