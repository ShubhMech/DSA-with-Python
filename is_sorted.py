def is_sorted(arr,n):
    if n==0:
        return 
    else:
        if arr[n]>arr[n-1]:
            print(arr[n],arr[n-1])
            print("Looks sorted so far")
            is_sorted(arr,n-1)
        else:
            print("Array is not sorted in ascending order")
            

arr=[1,2,3,4,15,6,7,8,9,10]
n= len(arr)-1
is_sorted(arr,n)