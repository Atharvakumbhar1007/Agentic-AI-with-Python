import threading


chai_stock = 0


def restock():
    global chai_stock

    for _ in range(100000):
        chai_stock += 1


threads = [
    threading.Thread(target=restock)
    for _ in range(2)
]

for t in threads:
    t.start()

for t in threads:
    t.join()


print("Chai stock:", chai_stock)

'''Your code is demonstrating multiple threads 
modifying the same shared variable.
This is an important concept for 
understanding race conditions and thread 
synchronization.'''