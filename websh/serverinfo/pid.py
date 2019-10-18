import psutil
#列出所有进程
pid = psutil.pids()
print(pid)
#实例化process对象，参数为一个进程pid
p = psutil.Process(2220)
pname = p.name()
p.exe()#进程bin路径
print(p)

