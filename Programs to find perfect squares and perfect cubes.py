#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Program to print all perfect squares between a given range:
#Perfect square

import math
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for num in range(start, end + 1):
   root = math.isqrt(num)
   if root ** 2 == num:
       print(num)


# In[3]:


# Program to print all perfect cubes between a given range:
#Perfect cubes

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for num in range(start, end + 1):
   # finding the cube root of the number
   root = num ** (1/3)
   # checking if the cube root is an integer
   if int(root + 0.5) ** 3 == num:
       print(num)


# In[ ]:




