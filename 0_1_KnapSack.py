def knapsack(W,weights,values,n):
    
    if n==0 or W == 0:
        return 0
    elif weights[n-1]>W:
        return knapsack(W,weights,values,n-1)
    else:
        print(val[n-1]+knapsack(W-weights[n-1],weights,values,n-1))
        print(knapsack(W,weights,values,n-1))
        return max(val[n-1]+knapsack(W-weights[n-1],weights,values,n-1),knapsack(W,weights,values,n-1))

    
    
val = [60, 100, 120,80]
wt = [10, 20, 30,40]
W = 50
n = len(val)
print( knapsack(W, wt, val, n))
