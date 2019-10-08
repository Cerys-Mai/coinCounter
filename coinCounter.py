'''This is a program to find the minium number of coins to make a total'''

import sys
for line in sys.stdin:

    #variable that converts input to int value
    total = int(line)

    #set up coins with different values
    coinOne = 5
    coinTwo = 3
    coinThree = 1

    #variable to count the number of coins used
    count = 0

    #variable to count up to total
    sum = 0

    #loop to count ot total
    while sum<total:
        sum = sum + coinOne
        count += 1
        if sum>total:
            sum = sum - coinOne
            count -= 1

    while sum<total:
        sum = sum + coinTwo
        count += 1
        if sum>total:
            sum = sum - coinTwo
            count -= 1

    while sum<total:
        sum = sum + coinThree
        count += 1
        if sum>total:
            sum = sum - coinThree
            count -= 1

    #print count
    print(count)
