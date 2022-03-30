def Bit_Generation(A,n):
    # global B
    if n==len(A):
        print(A) 
    else:
        # print(n+1)
        A[n]=1 
        # B.append(A)
        # count += 1
        # print(A)
        Bit_Generation(A,n+1)
        A[n]=0
        # B.append(A)
        # count +=1
        # print(A)
        Bit_Generation(A,n+1)
    
n1=2


A= [None]*n1
Bit_Generation(A,0)
