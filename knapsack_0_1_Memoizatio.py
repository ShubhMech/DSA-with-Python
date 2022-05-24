def knapsack(W, wt, val, n):Knapsack 
    
    kS= [[0 for x in range(W+1)] for j in range(n+1)]
    
    for i in range(W):
        for j in range(n):
            
            if i ==0 or j == 0:
                kS[i][j] = 0
            
            elif wt[i-1]<= j:
                KS[i][j] = max ( val[i-1] + KS[i-1][j-wt[i-1]], KS[i-1][j] )
                
            else:
                KS[i][j] = KS[i-1][j]
                
    return KS[n][W]

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))
