import threading
import os
import time

def func():
    time.sleep(5)
    print("finish")

threading.Thread(target=func).start()
# a=threading.Thread(target=func, daemon=True)
# a.start()
# a.join()

print("aaa")