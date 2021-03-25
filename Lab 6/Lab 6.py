# Kyle Johnson
# ETEC3702 – Concurrency 5:00 PM
# Paul Yost
# 3-24-21
# Lab 6 – Inter-Process Communication with Pipes

import multiprocessing

def cat(filename,pipeout):
	#function opens the file specified and loops by reads a line at a time,
	# then writing each to the pipe specified by pipeout.
	# once all lines have been read, the function should write None 
	# to pipeout then terminate.

def grep(pattern,pipein,pipeout):
	#Loop
	# read a line from pipein
	# if the line read is None then write None to pipeout and terminate
	# if the pattern specified in contained in the line
	# then the line is written to pipeout.
	# lines not containing the pattern are discarded. 
    
def wc(pipein,pipeout):
 	#initialize a count variable to zero
	#Loop
	#read a line from pipein
	# if the line read is None then exit the loop
	# otherwise increment the count
	#after the loop, write the count to pipeout as a string: “Lines:”+str(count) 
	#write None to pipeout and terminate
	
def printer(pipein):
	#Loop
	# read a line
	# if the line is None then terminate
	# otherwise print the line out using print.
            
if __name__=="__main__":
    #create pipes

    #create processes

    #start processes

    #join processes

    #enter to exit

    #cat("sonnets.txt",p1write)
    #cat("thee",p1read)
