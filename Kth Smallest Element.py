def partition(arr,low,high):
    i=low-1
    pivot= arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i +=1
            arr[i],arr[j]=arr[j],arr[i]
        
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return (i+1)
        
        
        
def kthSmallest(arr,low,high,k):
    
    pi= partition(arr,low,high)
    
    if pi-low == k-1:
        return arr[pi]
    
    elif (pi - low > k - 1): 

        return kthSmallest(arr, low, pi - 1, k)
    
    else:

        return kthSmallest(arr, pi + 1, high, k - pi + low - 1)


      
arr = [12, 3, 5, 7, 4, 19, 26]
n = len(arr)
k = 3;
print("K'th smallest element is",
    kthSmallest(arr, 0, n - 1, k))
