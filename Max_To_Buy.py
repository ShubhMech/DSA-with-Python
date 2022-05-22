def candyStore(candies,N,K):
    spent = 0
    candies.sort()
    index = N-1
    
    while N >=index:
        print(candies,index,N
             )
        spent += candies[index]
        index -= 1 
        
        N -= K
        print(N)

    return spent
