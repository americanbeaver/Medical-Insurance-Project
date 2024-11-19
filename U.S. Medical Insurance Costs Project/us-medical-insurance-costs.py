#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# In[14]:


import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
data = pd.read_csv('insurance.csv')

# Display the first few rows of the dataframe
data.head()


# In[11]:


# Extract each column and store in individual variables
ages = data['age']
sexes = data['sex']
bmi_values = data['bmi']
children_counts = data['children']
smoker_statuses = data['smoker']
regions = data['region']
charges = data['charges']


# In[7]:


average_age = round(data['age'].mean())
print('The average age of policy holders in this data set is',average_age,'.')


# In[8]:


# Find the region with the highest count of individuals
majority_region = data['region'].value_counts().idxmax()
count_majority_region = data['region'].value_counts().max()

# Display the result with a print statement
print(f"The majority of individuals are from the {majority_region} region, with a total count of {count_majority_region} individuals.")


# In[9]:


# Calculate the average charges for smokers and non-smokers
average_cost_smokers = data[data['smoker'] == 'yes']['charges'].mean()
average_cost_non_smokers = data[data['smoker'] == 'no']['charges'].mean()

# Display the results with print statements
print(f"The average cost for smokers is ${average_cost_smokers:.2f}.")
print(f"The average cost for non-smokers is ${average_cost_non_smokers:.2f}.")


# In[13]:


# Filter the data for individuals with at least one child
data_with_children = data[data['children'] >= 1]

# Calculate the average age for individuals with at least one child
average_age_with_children = data_with_children['age'].mean()

# Display the result rounded to the nearest integer
average_age_with_children_rounded = round(average_age_with_children)
print(f"The average age of individuals with at least one child is {average_age_with_children_rounded} years.")


# In[ ]:




