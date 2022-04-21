def sel(a,i):
#     print(a)
    min=i
    for j in range(i,len(a)):
        
        if a[j]<a[min]:
            min=j
#             print(f"i is {i}, j is {j}, min is {min}")
    a[min],a[i]=a[i],a[min]
    i +=1
    
    if i<len(a)-1:
#         print(i)
        
        sel(a,i)
        


