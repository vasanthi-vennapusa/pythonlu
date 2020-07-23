#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python program to check if  
# given number is prime or not 
  
num = int(input("Enter the value of n :" ))
  
# If given number is greater than 1 
if num > 1: 
      
   # Iterate from 2 to n / 2  
    for i in range(2, num): 
         
       # If num is divisible by any number between  
       # 2 and n / 2, it is not prime  
        if (num % i) == 0: 
            print(num, "is not a prime number") 
            break
        else: 
            print(num, "is a prime number") 
else: 
    print(num, "is not a prime number") 


# In[3]:


num = int(input("Enter the value of n :" ))
hold=num
sum=0
if num <=0:
    print("Enter a whole positive number!")
else:
    while(num > 0):
        sum +=num
        num -=1
    print("The sum is", sum)


# In[ ]:




