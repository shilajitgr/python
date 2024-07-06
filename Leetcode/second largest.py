data = [11,1,10,1,7,5,0,7]

high = data[0]
high_ii = None

for num in data[1:]:
    if not high_ii or (num > high_ii and num != high):
        high_ii = num
        
        if num > high:
            high_ii, high = high, high_ii
            
            
print(high_ii)
            