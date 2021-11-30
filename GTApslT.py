import psutil
import time
import os
import psutil

process_name = "gtav"
pid = None

for proc in psutil.process_iter():
    if process_name in proc.name():
       pid = proc.pid
p = psutil.Process(pid)
p.suspend()
time.sleep(5)
import os
p.resume()
os.system("pause")
