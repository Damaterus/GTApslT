import psutil
import time
import os

process_name = "GTA5"
pid = None

for proc in psutil.process_iter():
    if process_name in proc.name():
       pid = proc.pid
p = psutil.Process(pid)
p.suspend()
time.sleep(5)
p.resume()
os.system("pause")
