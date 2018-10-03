import psutil
a = psutil.cpu_freq()
b = psutil.disk_partitions()
print(a,b)
