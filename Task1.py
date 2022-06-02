#!/usr/bin/env python
# coding: utf-8

# # Q1:

# In[1]:


from datetime import datetime
now=datetime.now()
print("Current date and time is", now)


# # Q2:

# In[4]:


num_list=list(map(int,input().split()))
num_tuple=tuple(map(int,input().split()))
print(num_list)
print(num_tuple)


# # Q3:

# In[5]:


color_list = ["Red","Green","White" ,"Black"]
print(color_list[0])
print(color_list[-1])


# # Q5:

# In[11]:


a=int(input())
for i in range(a+1):
    #i=i+1
    if(i%2==0):
        print(i)


# # Q6:

# In[17]:


list1=list(input().split())
list2=list(input().split())
print(list((set(list1)-set(list2)))+list((set(list2)-set(list1))))


# # Q7:

# In[36]:


List=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
maxi=0
index=0
max_index=0
for i in List:
    sum=0
    for j in i:
        sum+=j
    if sum>maxi:
        maxi=sum
        max_index=index
    index+=1    
    maxi=max(sum,maxi)
    
print(maxi)
print(List[max_index])


# In[26]:


num=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
print(max(num,key=sum)) 


# # Q8:
# 

# In[51]:


#l=list(map(int,[22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]))
l=[22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
#print(type(l[0]))
length=len(l)                                 #doubt??
print(sum(list(map(round,l))*length))


# # Q9:

# In[55]:


color=['red', 'green', 'blue', 'white', 'black', 'orange']
remove_words=['white', 'orange']
for i in remove_words:
    color.remove(i)
print(color)    

    


# # Q10:

# In[66]:


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
d={}
d.update(dic1)
d.update(dic2)              # any other efficient approach?
d.update(dic3)
d


# # Q11
#    

# In[68]:


d={"value1":1,"Value1":2,"Value3":3}
ans=1
for i in d:
    ans*=d[i]
print(ans) 


# # Q12

# In[77]:


t1=(1,2,33,4,4,5,5,3)
print(t1[3])
print(t1[-4])


# # Q13

# In[87]:


t2=('Akshit',1,'Rahul',3)
d={}
length=len(t2)
for i in range(length+1):
    d[t2[i]]=t2[i+1]   # why out of range error
    i+=2
    if(i>length):
        break
print(d)    
    


# In[92]:


t2=(('Akshit',1),('Rahul',3))
dict1=dict((x,y) for x,y  in t2)
print(dict1)


# # Q14:

# In[101]:


s1={1,2,3,4}
s1.clear()
s1


# # Q15:

# In[107]:


s1={1,2,3,4,5,6,7}
s2={3,4,7,8}
s1
print(s1.issuperset(s1))
print(s1.issuperset(s2))


# In[ ]:




