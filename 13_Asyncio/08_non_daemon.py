"""
A non-daemon thread in Python is a thread that keeps
the Python program alive until the thread finishes.
"""

import threading
import time


def monitor_tea_temp():
    for _ in range(5):
        print("Monitoring tea temperature...")
        time.sleep(2)


t = threading.Thread(
    target=monitor_tea_temp,
    daemon=False
)

t.start()

print("Main program done")