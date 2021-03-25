# Kyle Johnson
# ETEC3702 – Concurrency 5:00 PM
# Paul Yost
# 2-9-21
# Lab 4 – Condition Variables for Selective Waiting
import time
import random
import threading

class Buffer(object):
    def __init__(self):
        self.amount = 0
        self.buffer=[]
        self.count=0
        self.MAX_ITEMS=10
        self.condition=threading.Condition()
    def fabricate_and_give_to_painting_buffer1(self,item):
        PaintBuffer.condition.acquire()
        while(PaintBuffer.count == PaintBuffer.MAX_ITEMS):
            PaintBuffer.condition.wait()
            print("Fab1 halted")
        print("Fab1 produced Car",PaintBuffer.amount)
        PaintBuffer.buffer.append(item)
        PaintBuffer.count+=1
        PaintBuffer.amount+=1
        print("Fab1 sent Car",PaintBuffer.amount," to painting queue")
        PaintBuffer.condition.notifyAll()
        PaintBuffer.condition.release()
    def fabricate_and_give_to_painting_buffer2(self,item):
        PaintBuffer.condition.acquire()
        while(PaintBuffer.count == PaintBuffer.MAX_ITEMS):
            PaintBuffer.condition.wait()
            print("Fab2 halted")
        print("Fab1 produced Car",PaintBuffer.amount)
        PaintBuffer.buffer.append(item)
        PaintBuffer.count+=1
        PaintBuffer.amount+=1
        print("Fab2 sent Car",PaintBuffer.amount," to painting queue")
        PaintBuffer.condition.notifyAll()
        PaintBuffer.condition.release()
    def take_from_painting_buffer_give_to_finishing_buffer(self):
        PaintBuffer.condition.acquire()
        FinishBuffer.condition.acquire()
        while(PaintBuffer.count == 0):
            PaintBuffer.condition.wait()
            print("paint buffer halted as nothing to paint")
        while(FinishBuffer.count == FinishBuffer.MAX_ITEMS):
            FinishBuffer.condition.wait()
            print("finish buffer halted as too full")
        item=PaintBuffer.buffer.pop(0)
        print("Painting queue received Car", item)
        PaintBuffer.count-=1
        FinishBuffer.buffer.append(item)
        FinishBuffer.count+=1
        print("Painting sent Car", item, "to Finishing")
        FinishBuffer.condition.notifyAll()
        PaintBuffer.condition.notifyAll()
        FinishBuffer.condition.release()
        PaintBuffer.condition.release()
    def take_from_finishing_buffer_and_ship(self):
        FinishBuffer.condition.acquire()
        while(FinishBuffer.count == 0):
            print("finish buffer halted as nothing to finish")
            FinishBuffer.condition.wait()
        item=FinishBuffer.buffer.pop(0)
        print("Shipped Car",item)
        FinishBuffer.count-=1
        FinishBuffer.condition.notifyAll()
        FinishBuffer.condition.release()
        return item

def fabricate1_10():
    while PaintBuffer.amount < 9:
        time.sleep(random.uniform(0.001,0.01))
        PaintBuffer.fabricate_and_give_to_painting_buffer1(PaintBuffer.amount)
def fabricate2_10():
    while PaintBuffer.amount < 9:
        time.sleep(random.uniform(0.001,0.01))
        PaintBuffer.fabricate_and_give_to_painting_buffer2(PaintBuffer.amount)
def paint_and_finish_10():
    for i in range(10):
        time.sleep(random.uniform(0.001,0.01))
        PaintBuffer.take_from_painting_buffer_give_to_finishing_buffer()
def ship_10():
    for i in range(10):
        time.sleep(random.uniform(0.001,0.01))
        FinishBuffer.take_from_finishing_buffer_and_ship()

PaintBuffer = Buffer()
FinishBuffer = Buffer()

fab1=threading.Thread(target=fabricate1_10)
fab2=threading.Thread(target=fabricate2_10)
painttofinish=threading.Thread(target=paint_and_finish_10)
shipping=threading.Thread(target=ship_10)

fab1.start()
fab2.start()
painttofinish.start()
shipping.start()

fab1.join()
fab2.join()
painttofinish.join()
shipping.join()