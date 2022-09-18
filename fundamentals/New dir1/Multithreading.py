#Multithreading--->Split and executing stmts parallely, make execution easier.
import threading
import time
def calc_square(num):
    print("Calculate square")
    for i in num:
        time.sleep(.3)
        print("Square=",i*i)
def calc_cube(num):
    print("Calculate cube")
    for i in num:
        time.sleep(.3)
        print("Cube=",i*i*i)
ar=[2,3,4,5]
t1=threading.Thread(target=calc_square,args=(ar,))
t2=threading.Thread(target=calc_cube,args=(ar,))
t=time.time()   #Time after execution.
t1.start()
t2.start()#----|
t1.join() #    |
   #<----------|  if we keep t2.start() here the time of execution changes.
t2.join()
print("Time taken for execution",time.time()-t)
print("Finished execution of threads")