# Python program to find the element occurring odd number of times

def getOddOccurrence(arr):


    res = 0
    
    # Traverse the arraya
    for element in arr:
        # XOR with the result
        print(res)
        res = res ^ element

    return res

# Test array
arr = [ 2, 2,3,4,4,5,5,6,6,7,7]

print("%d" % getOddOccurrence(arr))
