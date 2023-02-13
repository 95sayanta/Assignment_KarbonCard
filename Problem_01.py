#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import sklearn


# In[2]:


def mean(df, col_name):
    summ = 0
    count =0
    for i in range(len(df)):
        if type(df[col_name][i]) != str:
            summ += df[col_name][i]
            count+=1
        else:
            pass
    return summ/count
        


# In[3]:


def std_dev(df, col_name, mean):
    diff = 0
    count = 0
    for i in range(len(df)):
        if type(df[col_name][i]) != str:
            diff += ((df[col_name][i] - mean)**2)
            count+=1
        else:
            pass
    return np.sqrt(diff/count)


# In[4]:


def replace_with_mean(df, col_name,col_mean):
    for i in range(len(df)):
        if df[col_name][i] == 'o':
            df[col_name][i] = col_mean
    return df
    


# In[5]:


def ques(df):
    all_col_mean = []
    all_col_std =[]
    for i in df.columns:
        col_mean = mean(df, i)
        df = replace_with_mean(df, i,col_mean)
        std = std_dev(df, i, col_mean)
        df[i] = (df[i] - col_mean)/std
        all_col_mean.append(col_mean)
        all_col_std.append(std)
    return df , all_col_mean, all_col_std


# In[6]:


data = pd.DataFrame([
                   [180000, 110, 18.9, 1400], 
                   [360000, 905, "o", 1800], 
                   [230000, 230, 14.0, 1300], 
                   ['o', 450, 13.5, 1500]], 
    
                   columns=['Col A', 'Col B',
                            'Col C', 'Col D'])
  
# view data
display(data)


# In[ ]:





# In[7]:


df,mean,std = ques(data)


# In[8]:


print(df)


# In[9]:


print(std)


# In[10]:


print(mean)


# In[ ]:




