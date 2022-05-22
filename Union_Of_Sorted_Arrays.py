def doUnion(a,n,b,m):
    i=0
    j=0
    count = n+m
    
    while i<n and j <m:
        if a[i]<b[j]:
            i += 1
            
        elif a[i]>b[j]:
            j += 1
            
    
        else:
            i +=1
            j +=1
            count -=1
    return count




a= [1,2,3,4,5,6]
b= sorted([6,5,14,13,12,9])

union= doUnion(a,len(a),b,len(b))
