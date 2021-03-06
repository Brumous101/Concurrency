# Kyle Johnson
# ETEC3702 – Concurrency 5:00 PM
# Paul Yost
# 3-24-21
# Lab 6 – Inter-Process Communication with Pipes

import multiprocessing
import time
import random
import os
import sys

def cat(filename,pipeout):
	f = open(os.path.join(sys.path[0], filename), "r")
	lines = f.readlines()
	for line in lines:
		pipeout.send(line)
	pipeout.send("None")
	pipeout.close()
	
def grep(pattern,pipein, pipeout):
	while True:
		data=pipein.recv()
		if data == "None":
			pipeout.send(data)
			pipeout.close()
			break
		if pattern.lower() in data.lower():
			pipeout.send(data)
    
def wc(pipein,pipeout):
 	#initialize a count variable to zero
	count = 0
	#Loop
	while True:
		data=pipein.recv()
		if data == "None":
			break
		else:
			count = count + 1
	pipeout.send("Lines:"+str(count))
	pipeout.send("None")
	pipeout.close()
	#read a line from pipein
	# if the line read is None then exit the loop
	# otherwise increment the count
	#after the loop, write the count to pipeout as a string: “Lines:”+str(count) 
	#write None to pipeout and terminate
	
def printer(pipein):
	while True:
		data=pipein.recv()
		if (data == "None"):
			break
		print(data)
            
if __name__ == '__main__':
	input("Enter for Program 1: cat “sonnets.txt” | grep “thee” | printer ")
	pipeCon1,pipeCon2=multiprocessing.Pipe()
	pipeCon3,pipeCon4=multiprocessing.Pipe()
	pipeCon5,pipeCon6=multiprocessing.Pipe()
	p1=multiprocessing.Process(target=cat,args=("sonnets.txt",pipeCon1,))
	p2=multiprocessing.Process(target=grep,args=("THEE",pipeCon2,pipeCon3,))
	p3=multiprocessing.Process(target=printer,args=(pipeCon4,))

	p1.start()
	p2.start()
	p3.start()
	p1.join()
	p2.join()
	p3.join()

	input("Enter for Program 2: cat “sonnets.txt” | grep “thee” | wc | printer")
	p1=multiprocessing.Process(target=cat,args=("sonnets.txt",pipeCon1,))
	p2=multiprocessing.Process(target=grep,args=("THEE",pipeCon2,pipeCon3,))
	p3=multiprocessing.Process(target=wc,args=(pipeCon4,pipeCon5,))
	p4=multiprocessing.Process(target=printer,args=(pipeCon6,))

	p1.start()
	p2.start()
	p3.start()
	p4.start()
	p1.join()
	p2.join()
	p3.join()
	p4.join()
	input("Enter to exit")
