from system_monitor import monitor_all
from process_monitor import monitor_process

from init import INTERVAL

import time

COUNT = 5

for i in range(COUNT):
    print("==================================PROCESS STATUS START================================================")
    monitor_process()
    print("==================================PROCESS STATUS STOP================================================")

    print("==================================SYSTEM DATA START================================================")
    monitor_all()
    print("==================================SYSTEM DATA STOP================================================")
    time.sleep(INTERVAL)
