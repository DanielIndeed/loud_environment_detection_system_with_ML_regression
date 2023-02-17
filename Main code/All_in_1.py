#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

Arduino = pd.read_csv(r"C:\Users\boscu\Code\Data\Arduino text.txt", names=['Db']) # Read in data

avg_val_Db = int(Arduino['Db'].mean())

k = int(Arduino.count(numeric_only=True))

if avg_val_Db >= 80:
	absolute_timer_alg=float(k*0.1)
else:
	absolute_timer_alg=0
if absolute_timer_alg > 60:
	absolute_timer_alg=0
absolute_timer_alg=float(absolute_timer_alg)

from Model_trainer import rf,RandomForestRegressor,train_test_split,np

input_data = {'Age': [val_age],
              'Noise level': [avg_val_Db],
              'Time exposure': [absolute_timer_alg],
              'Earplugs': [0]
             }

input_data = pd.DataFrame(input_data)
input_labels = np.array(input_data['Earplugs']) # Labels are the values we want to predict

input_data = input_data.drop('Earplugs', axis = 1) # Remove the labels from the features and axis 1 refers to the columns

input_data_list = list(input_data.columns) # Saving factor names for later use
input_data = np.array(input_data) # Convert to numpy array

predictions = rf.predict(input_data)

print(input_data)
print(predictions)

from win10toast import ToastNotifier
from PIL import Image
import time

if predictions[0] > 0.8 and predictions[0] < 1.5:
    toast1 = ToastNotifier()
    toast1.show_toast(
        "Earplugs are recommended",
        "If not available, withdrawal from the environment is also an option.",
        duration = 20,
        icon_path = r"C:\Users\boscu\Code\Images\1.ico",
        threaded = True,
    )
    im1 = Image.open(r"C:\Users\boscu\Code\Images\1.png") 
    im1.show()
    time.sleep(3600)
elif predictions[0] > 1.5 and predictions[0] < 2.5:
    toast2 = ToastNotifier()
    toast2.show_toast(
        "Earplugs are required",
        "If not available, withdrawal from the environment is also an option.",
        duration = 20,
        icon_path = r"C:\Users\boscu\Code\Images\2.ico",
        threaded = True,
    )
    im2 = Image.open(r"C:\Users\boscu\Code\Images\2.png") 
    im2.show()
    time.sleep(3600)


# In[ ]:




