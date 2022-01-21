#!/usr/bin/env python
# coding: utf-8

# 1) print total items in list
# 2) print number of palindromes
# 3) print non-palindromes
# 4) print all palindromes in descending order
# Listp=[ "aba", "acca", "dad", "mom" ,"redivider","deified","civic", "radar", "level", "rotor", "kayak", "reviver", "racecar", "madam","refer", "list", "test", "hassan"," physics", "123321", "9797"]
# 
# 

# In[295]:


Listp=[ "aba", "acca", "dad", "mom" ,"redivider","deified","civic", "radar", "level", "rotor", "kayak", "reviver", "racecar", "madam","refer", "list", "test", "hassan"," physics", "123321", "9797"]
asc=[]
chek=False
count=0
ncount=0
for p in Listp:
    for i in range(1,len(p)+1):
        if p[len(p)-i]==p[i-1]:
#             print(p[len(p)-i],p[i-1])
            chek=True
        else:
            chek=False
            break
#     print(chek)
    
    if chek==True:
        count+=1
        asc.append(p)
        
    else:
        ncount+=1
#         print(ncount)    
        
print("Total items in list", len(Listp))
print("Number of palindromes",count)
print("Number of non-palindromes",ncount)
asc.sort(key=len,reverse=True)
print("palindromes in descending order ",asc)
    
        

