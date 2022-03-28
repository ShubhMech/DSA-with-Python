def maxSubarraySum(arr, n) :
# 	sum=-10**1000
    sum_2= arr[0]
    sum_1=0
    for i in range(n):
        sum_1=sum_1+arr[i]
        if sum_1<0:
            sum_1= 0
        elif sum_1>sum_2:
            sum_2=sum_1
    print(sum_2)  
    
maxSubarraySum([1,2,-4,-5,-6],5)