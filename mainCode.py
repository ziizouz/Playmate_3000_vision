from multiprocessing import Process, Lock
import I2C
import cv2 as cv
import TCP_IP

com = [I2C, TCP_IP]
communication = 0
#start the I2C process or the TCP/IP
proc = Process(target=com[1].start(), name='Test')
proc.start()
#image = cv.imread()
