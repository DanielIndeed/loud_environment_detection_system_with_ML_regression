#!/usr/bin/env python
# coding: utf-8

# In[ ]:

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


# In[ ]:

train_train_data, test_train_data, train_labels, test_labels = train_test_split(
    train_data, 
    labels, 
    test_size = 0.01, 
    random_state = 4000,
)

rf = RandomForestRegressor(
    n_estimators = 1000, 
    random_state = 42
) 

rf.fit(train_train_data, train_labels)


# In[ ]:


predictions = rf.predict(test_train_data)
errors = abs(predictions - test_labels)
np.set_printoptions(suppress=True)

