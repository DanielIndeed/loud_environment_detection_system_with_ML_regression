#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestRegressor

train_data = pd.read_csv(r'D:\My Documents\I3C\Data\Dataset1.csv', delimiter=',')

labels = np.array(train_data['Earplugs'])
criteria = np.array(train_data['Criteria'])

train_data = train_data.drop('Earplugs', axis = 1)
train_data = train_data.drop('Criteria', axis = 1)

train_data_list = list(train_data.columns)
train_data = np.array(train_data)


# In[2]:


train_train_data, test_train_data, train_labels, test_labels = train_test_split(
    train_data, 
    labels, 
    test_size = 0.25, 
    random_state = 4000,
)

rf = RandomForestRegressor(
    n_estimators = 520, 
    random_state = 42
) 

rf.fit(train_train_data, train_labels)


# In[3]:


predictions = rf.predict(test_train_data)
errors = abs(predictions - test_labels)
np.set_printoptions(suppress=True)
print(errors)


# In[4]:


import matplotlib.pyplot as plt
x = list(range(np.count_nonzero(predictions) + np.count_nonzero(predictions==0)))
y = test_labels

mean_errors=round(np.mean(errors), 2)

a = x
b = predictions
fig = plt.scatter(x, y, color = "blue", label="answers")
ax = plt.scatter(a, b, color = "red", label="predictions", alpha=0.9)
plt.legend(loc="upper left")
plt.ylim(-0.1, 2.5)

plt.figtext(0.32,0.02, 'Mean absolute error: ' +str(mean_errors),fontsize='large')

plt.savefig('C:\Users\boscu\Code\Graphs', dpi=2000)
plt.show()


# In[ ]:




