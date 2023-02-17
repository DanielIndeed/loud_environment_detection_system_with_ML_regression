#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import datetime

date_of_birth_str = input("Please enter your date of birth (YYYY-MM-DD): ")

date_of_birth = datetime.datetime.strptime(date_of_birth_str, "%Y-%m-%d").date()

today = datetime.date.today()
val_age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
absolute_timer_alg=0
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        exec(open(r"C:\Users\boscu\Code\Code test\All_in_1.py", mode="r", encoding="utf-8").read())

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    path = r"C:\Users\boscu\Code\Data"
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("done")


# In[ ]:




