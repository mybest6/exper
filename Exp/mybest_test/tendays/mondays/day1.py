#encoding:utf-8
import threading
import time

def fun(n):
    print(n)
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('0')
    time.sleep(1)

t1 = threading.Thread(target=fun,args=('t1',))
t2 = threading.Thread(target=fun,args=('t2',))

t1.start()
t2.start()

# 线程的测试
