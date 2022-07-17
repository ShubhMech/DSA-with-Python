#!/usr/bin/env python
# coding: utf-8

# In[1]:


arr= ["a","b"]


# In[2]:


arr


# In[3]:


pattern = []


# In[115]:


# def backtracking(arr,index):
#     print(index)
#     if index == len(arr):
#         print("".join(arr), len(arr))
#         return
#     elif index < len(arr):
#         arr.insert(index," ")
# #         print (arr)
#         backtracking(arr,index+2)
        
#         arr.pop(index)
#         backtracking(arr,index+1)


# In[116]:


# backtracking(arr, 1)


# In[117]:


len(arr)


# In[123]:


arr = ["a","b","c","d","e","f"]


# In[124]:


# def backtrack(arr,index,ans):
    
#     if index < len(arr):
#         ans.append(arr[index])
#         backtrack(arr,index+1,ans)
        
#         ans[index] = (arr[index].upper())
#         backtrack(arr,index+1,ans)
        
        
    
    

    
#     else:
#         print(arr)
#         return
    


# In[125]:


# "s".upper()


# In[126]:


# backtrack(arr,0,[])


# In[149]:


arr= ["a",1,"b",2,"C"]


# In[152]:


def permutation(arr,ind,ans=[0]*len(arr)):
    if ind == len(arr):
        print(ans)
        return
    
    elif ind< len(arr):

        ans[ind]= (arr[ind])
        permutation(arr,ind+1,ans)
        
        if type(arr[ind]) == str:
        
            ans[ind] = (arr[ind].upper())
            permutation(arr,ind+1,ans)
    else:
        return

        


# In[153]:


permutation(arr,0)


# In[ ]:





# In[154]:


def permutation(arr,ind,ans=[0]*len(arr)):
    if ind == len(arr):
        print(ans)
        return
    
    elif ind< len(arr):

        ans[ind]= (arr[ind])
        permutation(arr,ind+1,ans)
        
        if type(arr[ind]) == str and arr[ind].upper() == arr[ind]:
        
            ans[ind] = (arr[ind].lower())
            permutation(arr,ind+1,ans)
        
        elif type(arr[ind]) == str and arr[ind].upper() != arr[ind]:
            ans[ind] = (arr[ind].upper())
            permutation(arr,ind+1,ans)
    else:
        return

    


#         ans[ind]= (arr[ind])
#         permutation(arr,ind+1,ans)
        
#         if type(arr[ind]) == str:
        
#             ans[ind] = (arr[ind].upper())
#             permutation(arr,ind+1,ans)
#     else:
#         return

        


# In[158]:


arr


# In[157]:


permutation(arr,0)


# In[ ]:




