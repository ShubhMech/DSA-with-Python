def candyStore(candies,N,K):
    # code here
    candy = 0
    spent = 0

    candies.sort()

    while len(candies) >0:
        print(candies)
        spent += candies.pop(0)
        print(spent)
        if len(candies)>0:
            candies.pop(-1)
        if len(candies)>0:
            candies.pop(-1)
            
        print(candies)
        candy += K+1

    return spent
