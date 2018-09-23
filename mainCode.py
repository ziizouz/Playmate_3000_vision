import multiprocessing as mp
import I2C
import numpy as np
import time
import cv2 as cv
import TCP_IP
com = [I2C, TCP_IP]
communication = 0
# A queue that will have the data shared between processes
sharedData = mp.Queue()
# A lock to block the access of critical section when either main code is writing or communication process is reading
lock = mp.Lock()
#start the I2C process or the TCP/IP
if __name__ == '__main__':
    proc = mp.Process(target=com[1].start, name='Communication', args=(sharedData, lock))

    proc.start()
    
    image = cv.imread(r"F:\sw\0.jpg")
    board = np.zeros((8, 8))
    pieces = np.zeros((8, 8, 3))
    piece = [1, 2, 3]
    arm = [7, 1, 10]
    i = 0
    while True:
            lock.acquire()
            while sharedData.empty() is False:
                sharedData.get()
            sharedData.put(["image" , image])
            sharedData.put(["pieces", pieces])
            sharedData.put(["board", board])
            sharedData.put(["piece", piece])
            sharedData.put(["arm", i])
            lock.release()
            i+=1