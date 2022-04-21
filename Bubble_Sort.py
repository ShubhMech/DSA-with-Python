def bubbles(a,n):
    for i in range(n-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
    if n>1:
        bubbles(a,n-1)
