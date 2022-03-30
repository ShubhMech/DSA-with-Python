def Hanoi_Tower(n,src, dest, temp):
    if n>=1:
        Hanoi_Tower(n-1,src,temp,dest)
        print(f"Moving from {src} to {dest}")
        Hanoi_Tower(n-1,temp,dest,src)
Hanoi_Tower(5,1,3,2)