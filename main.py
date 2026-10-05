from datetime import datetime
import time

print("AutoRF started")

for i in range(60):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] AutoRF is alive... ({i+1}/60)")
    time.sleep(1)

print("AutoRF finished")
