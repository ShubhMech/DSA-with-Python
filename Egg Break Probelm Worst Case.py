#!/usr/bin/env python
# coding: utf-8

# In[313]:


def ispalindrome(arr,i,j):
#     arr2=arr[i:j+1]
    
    start = i
    end = j
    
    while start<end:
        if arr[start] != arr[end]:
            return False
        else:
            start +=1
            end -= 1
        return True

    


# In[285]:


# def ispalindrome(s, start, end):
#     while start < end:
#         if s[start] != s[end]:
#             return 0
#         start += 1
#         end -= 1
#     return 1


# In[334]:


def ispalindrome(arr,i,j):
#     arr2=arr[i:j+1]
    
    start = i
    end = j
    
    while start<=end:
        if arr[start] != arr[end]:
            return False
        
        start +=1
        end -= 1
        return True


def mm(arr,i,j,t):
    
    min_= 1e199

    if i>=j or ispalindrome(arr,i,j):
        t[i][j] = 0
        return t[i][j]
    
    elif t[i][j] != -1:
        return t[i][j]

    else:
        for k in range(i,j):
            
            if t[i][k] != -1:
                left = t[i][k]
            else:
                left = mm(arr,i,k,t)
                
            
            if t[k+1][j] != -1:
                right = t[k+1][j]
            else:
                right = mm(arr, k+1,j,t)
            
            temp = 1+ left + right
            min_ = min(min_,temp)
            
    return min_


mm(arr,0,len(arr)-1,t)



# import sys

# def isPalindrome(X, i, j):
 
#     while i <= j:
#         if X[i] != X[j]:
#             return False
#         i = i + 1
#         j = j - 1
 
#     return True
 

# def findMinCuts(X, i, j):
 

#     if i == j or isPalindrome(X, i, j):
#         return 0
 
#     min = sys.maxsize

 
#     for k in range(i, j):
 
#         count = 1 + findMinCuts(X, i, k) + findMinCuts(X, k + 1, j)
 
#         if count < min:
#             min = count
 
#     return min
 
# X = 'BABABCBADCD'
# findMinCuts(X, 0, len(X) - 1)


# In[328]:


arr = ["a","b","c","b", "a"]
arr = ["B","A","B","A","B","C","B","A","D","C","D"]
# arr = []
# arr= ["A","B","C","D"]


# In[316]:


arr


# In[317]:


t = [[-1 for i in range(1001)] for j in range(1001) ]


# In[319]:


mm(arr,0,len(arr)-1
  )


# In[296]:


50,20, 20,30, 30,40


# In[217]:


arr = [1, 2, 3, 4, 3]


# In[320]:


mm(arr,0,len(arr)-1)


# In[310]:


# ispalindrome(arr,0,len(arr)-1)


# In[321]:


ispalindrome(["a","b","c","b","a"],0,4)


# In[325]:


arr=["n","i","t","i","n"]


# In[326]:


mm(arr, 0, len(arr)-1)


# In[312]:


arr


# In[3]:


a = "GeeksforGeeks"
b = "Gks"


# In[6]:


countb= len(b)
count = 0
a = "GeeksforGeeks"
b = "Gks"
a = list(a)
b = list(b)

def afunc(a,b, recur_count):   
    countb= len(b)  
    global count
    print(count)
    recur_count += 1
    if recur_count > 100:
        return
    for i in range(len(a)):
        for j in range(len(b)):
            if countb == 0:
                count += 1
                afunc(a,b,recur_count
                     )

            if b[j] == a[i]:
                countb -= 1
                a[i] = 0

        
            
        


# In[7]:


afunc(a,b,0)


# In[8]:


count


# In[3]:


count = 0
recur = 0

a = "GeGeksksfsorGeeks"
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


# In[4]:


count


# In[5]:


a


# In[23]:


count


# In[5]:


a


# In[366]:


b


# In[369]:


count


# In[6]:



def count(a, b):
	m = len(a)
	n = len(b)

	lookup = [[0] * (n + 1) for i in range(m + 1)]


	for i in range(n+1):
		lookup[0][i] = 0


	for i in range(m + 1):
		lookup[i][0] = 1

	for i in range(1, m + 1):
		for j in range(1, n + 1):

			if a[i - 1] == b[j - 1]:
				lookup[i][j] = lookup[i - 1][j - 1] + lookup[i - 1][j]

			else:

				lookup[i][j] = lookup[i - 1][j]

	return lookup[m][n]


if __name__ == '__main__':
	a = "GeeksforGeeks"
	b = "Gks"

	print(count(a, b))


# In[36]:


def afunc(arr,i,j, expr,dict1={}):
    
    if i>j:
        return True
    
    elif i==j:
        
        if expr == True:
            if arr[i]== True:
                return True
            else: 
                return False
            
        if expr == False:
            if arr[i]==False:
                return True
            else: 
                return False
            
    if str(i)+str(j)+str(expr) in dict1.keys():
        return dict1[str(i)+str(j)+str(expr)]
    
    else:
        
            
        ans = 0

        for k in range(i,j,2):

            lt = afunc(arr,i,k-1,True,dict1)
            lf = afunc(arr,i,k-1,False,dict1)
            rt = afunc(arr,k+1,j,True,dict1)
            rf = afunc(arr,k+1,j,False,dict1)

            if arr[k] == "|":

                if expr == True:

                    ans += lt*rt + lt*rf + lf*rt
                else:
                    ans += lf*rf

            elif arr[k] == "&":

                if expr == True:
                    ans += lt*rt
                else:
                    ans += lf*rf + lf*rt + lt*rf

            elif arr[k] == "^":
                if expr == True:
                    ans += lt*rf + lf*rt
                else:
                    ans += lf*rf + lt*rt

        dict1[str(i)+str(j)+str(expr)] = ans

        print(dict1)
        return ans     


# In[37]:


arr = "T|T&F^F"


# In[38]:


afunc(arr,0,len(arr)-1,False)


# In[71]:


def afunc(e,f):
    if e== 1:
        return f
    if f==0 or f== 1:
        return f   
    min_ans = 1e199
    for x in range(1,f+1):
        min_temp = 1 + max(afunc(e-1,x-1),afunc(e,f-x))

        min_ans  = min(min_ans, min_temp)
    return min_ans
                       


# In[73]:


afunc(2,4)


# In[ ]:





# In[ ]:





# In[ ]:




