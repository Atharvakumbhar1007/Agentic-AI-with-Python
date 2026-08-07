import threading
import time

def cpu_heavy():
    print(f"{threading.current_thread().name} started...")

    total = 0
    for i in range(10**7):
        total += i

    print(f"{threading.current_thread().name} DONE")

start = time.time()

threads = [
    threading.Thread(target=cpu_heavy, name="Thread-1"),
    threading.Thread(target=cpu_heavy, name="Thread-2")
]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(f"Time taken: {time.time() - start:.2f} seconds")