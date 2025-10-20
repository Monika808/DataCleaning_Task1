#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('KaggleV2-May-2016.csv')
print(df.head())


# In[3]:


print("Before cleaning:")
print(df.info())
print("\nMissing values:\n", df.isnull().sum())


# In[4]:


#remove duplicates
df = df.drop_duplicates()


# In[5]:


#standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")


# In[6]:


#fix datatype
df['scheduledday'] = pd.to_datetime(df['scheduledday'], errors='coerce')
df['appointmentday'] = pd.to_datetime(df['appointmentday'], errors='coerce')


# In[7]:


#handle -ve or invalid ages
df = df[df['age'] >= 0]


# In[8]:


#standardize text columns
df['gender'] = df['gender'].str.upper().str.strip()
df['no-show'] = df['no-show'].str.capitalize().str.strip()


# In[9]:


#check for nulls after conversions
print("\nAfter cleaning, missing values:\n", df.isnull().sum())


# In[10]:


#save cleaned dataset
df.to_csv("cleaned_medical_appointments.csv", index=False)
print("\n✅ Cleaned dataset saved as 'cleaned_medical_appointments.csv'")


# In[11]:


#print summary
print("\nSummary of Cleaning:")
print(f"Total Rows after cleaning: {len(df)}")
print(f"Columns: {list(df.columns)}")
print("Data types:\n", df.dtypes)


# In[ ]:




