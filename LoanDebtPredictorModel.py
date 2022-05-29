#!/usr/bin/env python
# coding: utf-8

# # Model Building

# ## Implementing Formula on our Dataset

# In[1]:


import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('FinalDataset.csv')
df.head()


# In[3]:


df.drop(columns = ['Unnamed: 0'], inplace = True)
df.head()


# ## Calculating Risk Factor

# In[4]:


from LoanCostFunction import loan_cost_prediction


# In[5]:


risk = []
cnt = 0
for i in range(0, 3000):
    risk.append(loan_cost_prediction(df['Total_Revenue'][i], df['profit_percentage_last_year'][i], df['simple_interest'][i], df['interest_rate'][i], df['amount_of_loan'][i], df['time_to_repay'][i], df['past_debt_to_repay'][i], df['sustainability'][i], df['competition_scale'][i], df['management_effectivity'][i], df['startup'][i], df['cibil_score'][i]))


# In[6]:


df['Risk_Factor'] = risk
df.head()


# ## Model Training

# In[7]:


target = df.iloc[:, -1]


# In[8]:


from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(df.drop('Risk_Factor',axis='columns'), target, test_size=0.3)


# In[9]:


from sklearn import tree
model = tree.DecisionTreeClassifier()
model.fit(X_train, Y_train)


# ## Predicting Testcases

# ### High Profit

# In[10]:


model.predict([[2200000, 10, 8, 0, 850, 2600000, 40, 10, 0, 0, 0, 15000000]])


# ### High Risk

# In[11]:


model.predict([[8650000, 6, 8, 1, 400, 3500000, 1, 3, 0, 0, 1, 9260000]])


# ### Less Profit

# In[12]:


model.predict([[8400000, 13, 8, 0, 500, 1230000, 25, 6, 0, 0, 1, 13468000]])


# ### Less Risk

# In[13]:


model.predict([[7800000, 12, 9, 0, 800, 1100000, 25, 10, 1, 0, 0, 9300000]])


# ### Score of the model

# In[14]:


model.score(X_test, Y_test)


# ### Making a function for model

# In[15]:


def main(a,b,c,d,e,f,g,h,i,j,k,l):
    return model.predict([[a,b,c,d,e,f,g,h,i,j,k,l]])
