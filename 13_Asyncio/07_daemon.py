'''A daemon thread in Python is a background thread that does not keep the Python program alive 
when all non-daemon threads have finished.'''
import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temperature...")
        time.sleep(2)
        
t = threading.Thread(target=monitor_tea_temp, daemon=True)
t.start()

print("Main program done")