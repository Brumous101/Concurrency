# Kyle Johnson
# ETEC3702 – Concurrency 5:00 PM
# Paul Yost
# 2-2-21
# Lab 3 – Semaphores

# Part 1: Concurrent Execution without Semaphores
# A
import time
import random
import threading

buffer = 0

def producer():
    s2consumer.acquire()
    global buffer
    for i in range(100):
        buffer = i
        # time.sleep(random.uniform(0.001,0.01))
        s1producer.acquire()
        s2consumer.release()
    print("Producer done.")
    

def consumer():
    global buffer
    for j in range(100):
        temp = buffer
        print(str(temp))
        # time.sleep(random.uniform(0.001,0.01))
        s2consumer.acquire()
        s1producer.release()
    print("Consumer done.")
    

s1producer = threading.Semaphore(1)
s2consumer = threading.Semaphore(1)

t1 = threading.Thread(target=producer,)
t2 = threading.Thread(target=consumer,)
t1.start()
t2.start()
t1.join()
t2.join()
print("Done.")

# B - Run program several times.
# C - The values are not correctly displayed.
# D - The runs did not produce the same results.
# E - Comment out the sleeps and run program.
# F - E changes the output by making the producer function call execute mostly before the consumer function call so you are left with the program printing "99" 100 times.

# Part 2
# A - Add the sleep instructions back in and add semaphores to the program so that the shared variable write / read operations are protected in each thread.
# B - Execute the program several times and observe the output. 
# C - All values are displayed correctly.
# D - Each run produced the same results.
# E - Comment out the sleep instructions again.
# F - It makes the code execute faster but it still produces the correct result!