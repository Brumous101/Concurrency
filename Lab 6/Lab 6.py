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
	#print(f.read())
	lines = f.readlines()
	count = 0
	for line in lines:
		# count += 1
		# print("Line{}: {}".format(count, line.strip())
		pipeout.send(line.strip())
	pipeout.send("NONE")
	pipeout.close()
	
def grep(pattern,pipein, pipeout):
	data=pipein.recv()
	while data != "NONE":
		data=pipein.recv()
		#print("Message Received: "+data)
		if pattern in data:
			pipeout.send(data)
	pipeout.send("NONE")
	pipeout.close()
    
#def wc(pipein,pipeout):
 	#initialize a count variable to zero
	#Loop
	#read a line from pipein
	# if the line read is None then exit the loop
	# otherwise increment the count
	#after the loop, write the count to pipeout as a string: “Lines:”+str(count) 
	#write None to pipeout and terminate
	
def printer(pipein):
	data=pipein.recv()
	while data != "NONE":
		data=pipein.recv()
		print("Message Received: "+data)
	print("Finished")
            
if __name__ == '__main__':
	pipeCon1,pipeCon2=multiprocessing.Pipe()
	pipeCon3,pipeCon4=multiprocessing.Pipe()
	p1=multiprocessing.Process(target=cat,args=("sonnets.txt",pipeCon1,))
	p2=multiprocessing.Process(target=grep,args=("THEE",pipeCon2,pipeCon2,))
	#p3=multiprocessing.Process(target=wc,args=(pipeCon2,pipeCon3,))
	p4=multiprocessing.Process(target=printer,args=(pipeCon3,))
	p1.start()
	p2.start()
	#p3.start()
	p4.start()
	p1.join()
	p2.join()
	#p3.join()
	p4.join()
	print("done")
	input("enter to exit")
