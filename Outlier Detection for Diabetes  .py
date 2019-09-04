#!/usr/bin/env python
# coding: utf-8

#  <h1><center>Outlier Detection for Diabetes</center></h1>

# In[2]:


#import libraries


# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


#import dataset, https://www.kaggle.com/uciml/pima-indians-diabetes-database/discussion/24182


# In[5]:


x = pd.read_csv("C:/Users/Daniel/Desktop/diabetes.csv")


# ## Data Exploration

# In[6]:


x.shape


# In[7]:


datadict = pd.DataFrame(x.dtypes)
datadict


# In[8]:


x.describe()


# In[9]:


x.head()


# In[10]:


x.tail()


# In[11]:


x.sample(5)


# ### Missing Values

# In[12]:


x.isnull().sum()


# ### Univariate Analysis

# In[13]:


fig, axes = plt.subplots(3, 3, figsize=(16, 10))

sns.distplot(x['Pregnancies'],ax=axes[0,0])
sns.distplot(x['Glucose'],ax=axes[0,1])
sns.distplot(x['BloodPressure'],ax=axes[0,2])
sns.distplot(x['SkinThickness'],ax=axes[1,0])
sns.distplot(x['Insulin'],ax=axes[1,1])
sns.distplot(x['BMI'],ax=axes[1,2])
sns.distplot(x['DiabetesPedigreeFunction'],ax=axes[2,0])
sns.distplot(x['Age'],ax=axes[2,1])
sns.countplot('Outcome',data= x ,ax=axes[2,2])


# ### Bivariate Analysis

# In[14]:


fig, axes = plt.subplots(2, 4, figsize=(16, 10))
sns.boxplot(x="Outcome", y="Pregnancies", data=x,ax=axes[0,0])
sns.boxplot(x="Outcome", y="Glucose", data=x,ax=axes[0,1])
sns.boxplot(x="Outcome", y="BloodPressure", data=x,ax=axes[0,2])
sns.boxplot(x="Outcome", y="SkinThickness", data=x,ax=axes[0,3])
sns.boxplot(x="Outcome", y="Insulin", data=x,ax=axes[1,0])
sns.boxplot(x="Outcome", y="BMI", data=x,ax=axes[1,1])
sns.boxplot(x="Outcome", y="DiabetesPedigreeFunction", data=x,ax=axes[1,2])
sns.boxplot(x="Outcome", y="Age", data=x,ax=axes[1,3])


# ### Correlation  

# In[15]:


x.corr()


# In[16]:


plt.figure(figsize=(12, 8))

sns.heatmap(x.corr(),annot = True)


# ## AVF Outlier Detection

# In[17]:


#Get AVF Score 

AVF_list = []
columns = list(x.columns)
for i in range(len(x)):
    freq_sum = []   
    for c in range(len(columns)):
        
        #gets frequency of each unique value from data per column, stores in dataframe  
        freq_table = pd.DataFrame(x[columns[c]].value_counts()) 
        
        #moves frequency values from index to value column, fixes format of the table     
        freq_table['value'] = freq_table.index       
        
        #gets value from a cell  
        value = x.iloc[i,c]
       
        #gets frequency associated with value of cell
        freq = freq_table[columns[c]][value] 
     
        #appends each frequency to a list to later sum
        freq_sum.append(freq)     
   
    #takes sum of frequencies for each attribute and divides by # of columns, this is done per record 
    AVF = sum(freq_sum)/len(columns)
    
    #create a list of each AVF score per record and add all records to AVF column
    AVF_list.append(AVF)
    
x["AVF"]= AVF_list 


# In[18]:


#Sort dataset least to greatest by AVF score
o = x.sort_values("AVF")
#Number of outliers
#10%
k = round(len(x)*.1)
outliers = o.iloc[:k]
outliers


# ## Univariate Analysis of Outliers

# In[19]:


fig, axes = plt.subplots(3, 3, figsize=(16, 10))

sns.distplot(outliers['Pregnancies'],ax=axes[0,0])
sns.distplot(outliers['Glucose'],ax=axes[0,1])
sns.distplot(outliers['BloodPressure'],ax=axes[0,2])
sns.distplot(outliers['SkinThickness'],ax=axes[1,0])
sns.distplot(outliers['Insulin'],ax=axes[1,1])
sns.distplot(outliers['BMI'],ax=axes[1,2])
sns.distplot(outliers['DiabetesPedigreeFunction'],ax=axes[2,0])
sns.distplot(outliers['Age'],ax=axes[2,1])
sns.countplot('Outcome',data= outliers,ax=axes[2,2])


# ## Bivariate Analysis of Outliers 

# In[20]:


fig, axes = plt.subplots(2, 4, figsize=(16, 10))
sns.boxplot(x="Outcome", y="Pregnancies", data=outliers,ax=axes[0,0])
sns.boxplot(x="Outcome", y="Glucose", data=outliers,ax=axes[0,1])
sns.boxplot(x="Outcome", y="BloodPressure", data=outliers,ax=axes[0,2])
sns.boxplot(x="Outcome", y="SkinThickness", data=outliers,ax=axes[0,3])
sns.boxplot(x="Outcome", y="Insulin", data=outliers,ax=axes[1,0])
sns.boxplot(x="Outcome", y="BMI", data=outliers,ax=axes[1,1])
sns.boxplot(x="Outcome", y="DiabetesPedigreeFunction", data=outliers,ax=axes[1,2])
sns.boxplot(x="Outcome", y="Age", data=outliers,ax=axes[1,3])


# In[24]:


#Sort dataset greatest to least by AVF score
n = x.sort_values("AVF", ascending = False)
#Number of normal
#90%
k = round(len(x)-k)
norm = n.iloc[:k]
norm


# ## Univariate Analysis without Outliers

# In[22]:


fig, axes = plt.subplots(2, 4, figsize=(16, 10))

sns.distplot(norm['Pregnancies'],ax=axes[0,0])
sns.distplot(norm['Glucose'],ax=axes[0,1])
sns.distplot(norm['BloodPressure'],ax=axes[0,2])
sns.distplot(norm['SkinThickness'],ax=axes[0,3])
sns.distplot(norm['Insulin'],ax=axes[1,0])
sns.distplot(norm['BMI'],ax=axes[1,1])
sns.distplot(norm['DiabetesPedigreeFunction'],ax=axes[1,2])
sns.distplot(norm['Age'],ax=axes[1,3])


# ## Biunivariate Analysis without Outliers

# In[23]:


fig, axes = plt.subplots(2, 4, figsize=(16, 10))
sns.boxplot(x="Outcome", y="Pregnancies", data=norm,ax=axes[0,0])
sns.boxplot(x="Outcome", y="Glucose", data=norm,ax=axes[0,1])
sns.boxplot(x="Outcome", y="BloodPressure", data=norm,ax=axes[0,2])
sns.boxplot(x="Outcome", y="SkinThickness", data=norm,ax=axes[0,3])
sns.boxplot(x="Outcome", y="Insulin", data=norm,ax=axes[1,0])
sns.boxplot(x="Outcome", y="BMI", data=norm,ax=axes[1,1])
sns.boxplot(x="Outcome", y="DiabetesPedigreeFunction", data=norm,ax=axes[1,2])
sns.boxplot(x="Outcome", y="Age", data=norm,ax=axes[1,3])

