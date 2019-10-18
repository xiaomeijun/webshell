import psutil
#cpu信息
cpu = psutil.cpu_times()
cpu.user
print(cpu.user)
#cpu逻辑个数
cpunum = psutil.cpu_count()
#cpu物理个数
cpuPhysical  = psutil.cpu_count(logical=False)
print(cpu)


#内存信息
mem = psutil.virtual_memory()
print(mem)
mem.total
mem.free
mem.percent

#磁盘信息
disk = psutil.disk_partitions()#磁盘完整信息
psutil.disk_usage('/')#分区信息
psutil.disk_io_counters()
psutil.disk_io_counters(perdisk=True)#单个分区io个数
print(disk)

#网络信息
net = psutil.net_io_counters(pernic=True)
print(net)

#当前用户
user = psutil.users()
print(user)
#开机时间
boottime=psutil.boot_time()
print(boottime)
