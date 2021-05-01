#!/usr/bin/env python
# coding: utf-8

# # Stats 4 Assignment

# # Problem Statement 1:
 Is gender independent of education level? A random sample of 395 people were
surveyed and each person was asked to report the highest education level they
obtained. The data that resulted from the survey is summarized in the following table:

           High School Bachelors Masters  Ph.d.  Total
Female     60          54        46       41     201
Male       40          44        53       57     194
Total      100         98        99       98     395

Question: 
    Are gender and education level dependent at 5% level of significance? In
other words, given the data collected above, is there a relationship between the
gender of an individual and the level of education that they have obtained?
# In[3]:


import scipy.stats as sts
from scipy.stats import norm
import math
import numpy as np
import pandas as pd
f_list = [60,54,46,41]
m_list = [40,44,53,57]
s = [40,60]
b = [44,54]
m = [53,46]
p = [57,41]
marks = m_list + f_list
print(marks)
sex =  ['Male','Male','Male','Male','Female','Female','Female','Female']
edu = ['High School', 'Bachelors', 'Masters', 'Ph.d.','High School', 'Bachelors', 'Masters', 'Ph.d.']
df_edu = pd.DataFrame({"Sex":sex,"Edu":edu,"Marks":marks})
print(df_edu)
cross_tab = pd.crosstab([df_edu.Sex,df_edu.Marks],df_edu.Edu,margins=True)


# In[8]:


df2 = pd.crosstab(df_edu.Sex, df_edu.Edu,df_edu.Marks, aggfunc="sum",margins=True)
df2.columns = ["Bachelors","High School","Masters","Ph.d.","row_totals"]
df2.index = ["Female","Male","col_totals"]
df2


# In[5]:


observed = df2.iloc[0:2,0:4]  
observed


# In[9]:


expected =  np.outer(df2["row_totals"][0:2],df2.loc["col_totals"][0:4]) / 395.0
expected = pd.DataFrame(expected)
expected.columns = ["Bachelors","High School","Masters","Ph.d."]
expected.index = ["Female","Male"]
expected


# In[7]:


chi_squared_stat = (((observed-expected)**2)/expected).sum().sum()
print(chi_squared_stat)


# In[10]:


crit = sts.chi2.ppf(q = 0.95,df = 3)  
print("Critical value")
print(crit)
p_value = 1 - sts.chi2.cdf(x=chi_squared_stat, df=3)  
print("P value")
print(p_value)


# In[11]:


sts.chi2_contingency(observed= observed)


# # Problem Statement 2:
Using the following data, perform a oneway analysis of variance using α=.05. Write
up the results in APA format.

[Group1: 51, 45, 33, 45, 67]
[Group2: 23, 43, 23, 43, 45]
[Group3: 56, 76, 74, 87, 56]
# In[14]:


Group1 = [51, 45, 33, 45, 67]
Group2 = [23, 43, 23, 43, 45]
Group3 = [56, 76, 74, 87, 56]

statistic, pvalue = sts.f_oneway(Group1,Group2,Group3)
print("F Statistic value {} , p-value {}".format(statistic,pvalue))
if pvalue < 0.05:
    print('True')
else:
    print('False')


# # Problem Statement 3:
Calculate F Test for given 10, 20, 30, 40, 50 and 5,10,15, 20, 25.
For 10, 20, 30, 40, 50:
# In[16]:


sts.f_oneway([10, 20, 30, 40, 50],[5,10,15, 20, 25])


# In[17]:


Group1 = [10, 20, 30, 40, 50]
Group2 = [5,10,15, 20, 25]
mean_1 = np.mean(Group1)
mean_2 = np.mean(Group2)
grp1_sub_mean1 = []
grp2_sub_mean2 = []
add1 = 0
add2 = 0
for items in Group1:
    add1 += (items - mean_1)**2
for items in Group2:
    add2 += (items - mean_2)**2
var1 = add1/(len(Group1)-1)
var2 = add2/(len(Group2)-1)

F_Test = var1/var2
print("F Test for given 10, 20, 30, 40, 50 and 5,10,15, 20, 25 is : ",F_Test)

