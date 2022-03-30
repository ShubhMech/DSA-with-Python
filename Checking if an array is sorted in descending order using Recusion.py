def is_sorted(arr,n):
    if n==0:
        print ("The array is sorted!")
    else:
        if arr[n]<arr[n-1]:
            print(arr[n],arr[n-1])
            print("Looks sorted so far")
            is_sorted(arr,n-1)
        else:
            print("Array is not sorted in descending order")
            

arr=[1,2,3,4,5,6,7,8,9,10][::-1]
n= len(arr)-1
is_sorted(arr,n)