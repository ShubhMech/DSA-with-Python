def min_max(arr,low,high):
    if low==high:
        print("Returning for n=1")
        return arr[low]
    elif high-low==1:
        print("Returning for n=2")
        return min(arr[low],arr[high])
    
    elif low<high:
        mid= low+ (high-low)//2
        print(mid,arr[mid],arr[low:mid],arr[mid+1:high])
        min1= min_max(arr,low,mid)
        min2=min_max(arr,mid+1,high)
        return min(arr[mid],min1,min2)
    
min_max(arr,0,len(arr)-1)
