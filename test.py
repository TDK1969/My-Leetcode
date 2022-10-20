import os
import gc
import psutil
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024 / 1024
    print(f"{hint} memory used: {memory}")

show_memory_info("initial")
def func():
    a = [1 for _ in range(10000000)]
    show_memory_info("created a")
func()
show_memory_info("exit func")
gc.collect()
show_memory_info("finish")

a = "tdk1969"
b = "tdl1969"
print()