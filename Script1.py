#Server Health Monitor

import psutil
from datetime import datetime

cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent
time = datetime.now()


print("===== SERVER HEALTH REPORT =====")
print("Time       :", time)
print("CPU Usage  :", cpu, "%")
print("RAM Usage  :", ram, "%")
print("Disk Usage :", disk, "%")



if cpu > 80:
    print("WARNING: High CPU Usage!")

if ram > 80:
    print("WARNING: High RAM Usage!")

if disk > 80:
    print("WARNING: Disk Almost Full!")


with open("monitor.log", "a") as file:
    file.write(f"{time} | CPU={cpu}% | RAM={ram}% | DISK={disk}%\n")


print("Report saved to monitor.log")