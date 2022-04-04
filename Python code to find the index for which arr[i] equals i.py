
def afunc(arr,low,high):
    print(low,high)
    if low==high:
        if arr[low]==low:
            return low
        else: return -1
    else:
        mid= low+ (high-low)//2
        
        if arr[mid]==mid:
            print("mid is:", mid)
            return mid
            
        a=afunc(arr,low,mid)
        b=afunc(arr,mid+1,high)
        
        # if a==b and a==-1:
        #     print("Not Found")
        # else:
        #     print("Found",a ,b, mid)
arr=[0,11,2,13,4,15,6,7,8,9,15]           
arr=[0,2,2,3,4,4,6,7,6,8,9]
afunc(arr,0,len(arr)-1)        

        