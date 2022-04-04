def afunc(arr,low,high):
    # print(low,high)
    if low==high:
        if arr[low]== 10**7:
            print(low)
            return
    else:
        mid= low+ (high-low)//2
        print(low,mid,high)
        if arr[mid]==10**7:
            print("mid is:", mid)
            if arr[mid-1]==10**7:
                afunc(arr,low,mid)
            else: print("This is it")
        elif arr[mid]< 10**7:
            afunc(arr,mid+1,high)
arr=[0,2,2,3,4,4,10**7,10**7,10**7,10**7,10**7]
arr=
afunc(arr,0,len(arr)-1)        