# there are a total of 256 characters in the ASCII
# so get a count of any character in a file/string
# we can create an array of 256 and then map the ascii value of 
# each character to the index of the array and then increment the count
from collections import defaultdict

def get_count_of_all_chars(string: str) -> dict:
    # create an array of size 256 and initialize it with
    
    # all elements as 0
    count = defaultdict(int)
    for i in string:
        count[i] += 1
        
    return dict(count)


print(list(get_count_of_all_chars("geeksforgeeks").values()))