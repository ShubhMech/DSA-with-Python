count = 0
recur = 0

a = "GeeksforGeeks"
b = "Gks"

a = list(a)
b = list(b)

countb = len(b)

while True:
    s = []
    recur += 1
    try:
#         print(a)
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i]==b[j]:
                    print("Equals", countb)
                    s.append(a[i])
                    countb -= 1
                if countb==0:
                    count += 1
                    countb = len(b)
                    print("The Current Count is:", count)
                    for ii in s:
#                         print(a)
                        ind = a.index(ii)
                        a.pop(ind)
                        print(a)
                    
                    continue
    except:
        
        break
