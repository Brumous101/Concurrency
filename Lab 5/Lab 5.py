# Kyle Johnson
# ETEC3702 – Concurrency 5:00 PM
# Paul Yost
# 2-16-21
# Lab 5 – Improving Performance of I/O-Bound Processes
import urllib.request
import time
import threading

fileList=["images-assets.nasa.gov/image/PIA04921/PIA04921~orig.jpg","images-assets.nasa.gov/image/PIA10600/PIA10600~orig.jpg","images-assets.nasa.gov/image/GSFC_20171208_Archive_e001925/GSFC_20171208_Archive_e001925~orig.jpg","images-assets.nasa.gov/image/PIA11999/PIA11999~orig.jpg","images-assets.nasa.gov/image/GSFC_20171208_Archive_e001262/GSFC_20171208_Archive_e001262~orig.jpg","images-assets.nasa.gov/image/PIA15536/PIA15536~orig.jpg","images-assets.nasa.gov/image/PIA00583/PIA00583~orig.jpg","images-assets.nasa.gov/image/GSFC_20171208_Archive_e001762/GSFC_20171208_Archive_e001762~orig.jpg","images-assets.nasa.gov/image/PIA05185/PIA05185~orig.jpg","images-assets.nasa.gov/image/PIA03225/PIA03225~orig.jpg"]
threadList=[]
barrier1 = threading.Barrier((len(fileList)))

def downloadSequential(filesToDownloadList):
    start_time_func= time.time()
    print("Start Sequential")
    for i in range(len(filesToDownloadList)):
        downloadFile(filesToDownloadList[i])
    total_time_func=(time.time()-start_time_func)
    #print("Total time to download all files in the file list sequentially: " + str(total_time_func))
    return total_time_func
    
def downloadFile(file):
    start_time_file = time.time()
    url_of_file = file
    name_of_file = url_of_file.split("/")
    output_file_name = name_of_file[ len(name_of_file)-1 ]
    urllib.request.urlretrieve("http://"+url_of_file, output_file_name)
    print("File name: "+ str(output_file_name) + str(" took ") + str(time.time() - start_time_file) + str(" seconds to download.") )

# Uses Barriers
def downloadConcurrent2(filesToDownloadList):
    start_time_concurrent = time.time()
    num = barrier1.n_waiting
    barrier1.wait()
    downloadFile(filesToDownloadList[num])
    barrier1.reset() 
    total_time=(time.time()-start_time_concurrent)
    return total_time

def downloadConcurrent(filesToDownloadList):
    start_time = time.time()
    print("Start Concurrent: ")
    for i in range(len(fileList)):
        thread_name = "t" + str(i)
        thread_name=threading.Thread(target=downloadConcurrent2,args=(fileList,))
        threadList.append(thread_name)
    for i in range(len(threadList)):
        threadList[i].start()
    for i in range(len(threadList)):
        threadList[i].join()
    total_time = time.time() - start_time
    return total_time

def main():
    Seqtime=downloadSequential(fileList)
    print("Seqtime = " + str(Seqtime))
    Contime=downloadConcurrent(fileList)
    print("Contime = " + str(Contime))
    SpeedUp = Seqtime/Contime
    print("The calculated speedup is: " + str(SpeedUp))
    SpeedUp += 0.005
    Percentage = (int(SpeedUp*100) - 100)
    if(Seqtime > Contime):
        print("The concurrent function is about: " + str(Percentage) +"% faster.")
    else:
        print("The concurrent function is about: " + str(Percentage) +"% slower.")

main()


