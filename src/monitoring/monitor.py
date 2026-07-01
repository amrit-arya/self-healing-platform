import psutil
cpu = psutil.cpu_percent()
memory = psutil.virtual_memory()
disk = psutil.disk_usage('/')
print(f"CPU Usage: {cpu}%")
print(f"RAM Usage: {memory.percent}%")
print(f"Disk Usage: {disk.percent}%")
