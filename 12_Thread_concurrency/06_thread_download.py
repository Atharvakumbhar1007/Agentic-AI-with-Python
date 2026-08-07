import threading
import requests
import time

def download(url):
    print(f"Starting download from {url}")

    resp = requests.get(url)

    print(f"Finished download from {url}, Size: {len(resp.content)} bytes")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/webp"
]

threads = []

start = time.time()

for url in urls:
    t = threading.Thread(target=download, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end = time.time()

print(f"\nTotal time: {end - start:.2f} seconds")