"""
    filter all the odd elements in the list and sq them
"""

"""
Take-aways:

1) Learn Python Lambda
2) Learn Pandas indepth
3) Learn about filter and map
4) Learn SQL in-depth
5) Implement decorators from scratch
"""

def sq_odd_elements():
    inp = range(1, 20)

    output = [x ** 2 for x in inp if x % 2 == 1]
    print(*output, sep="\n")
    
# sq_odd_elements()

import pandas as pd
from pandas import concat

dataframe = pd.read_csv("/Users/shilajit/code/python/Interview/dataframe.csv", sep=",")

print(dataframe.shape)
df2 = concat([dataframe, dataframe])
print(df2.shape)

"""
User table – [ user_id, username, email, address ]
Order table – [ order_id, user_id, date, amount]
 
These are tables for a Pizza store, where orders and users coming to the store 
are stored in these table. Can you write a query that prints the total amount spent 
by each distinct user in this store in the month of Feb 2022? 
(Follow up – Print only users who spent more than Rs. 1000)
"""
