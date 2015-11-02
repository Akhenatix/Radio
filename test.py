import urllib2
import pygame
import os
from gps import *
from time import *
import time
import threading
from socketIO_client import SocketIO

gpsd = None  # seting the global variable

os.system('clear')  # clear the terminal (optional)


class GpsPoller(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global gpsd  # bring it in scope
        gpsd = gps(mode=WATCH_ENABLE)  # starting the stream of info
        self.current_value = None
        self.running = True  # setting the thread running to true

    def run(self):
        global gpsd
        while gpsp.running:
            gpsd.next()  # this will continue to loop and grab EACH set of gpsd info to clear the buffer


if __name__ == '__main__':
    gpsp = GpsPoller()  # create the thread

    gpsp.start()  # start it up



# mp3file = urllib2.urlopen("http://192.168.137.101:3000/download")
# output = open('test.mp3','wb')
# output.write(mp3file.read())
# output.close()



def on_aaa_response(*args):
    print(args[0])
    mp3file = urllib2.urlopen(args[0])
    output = open('test.mp3', 'wb')
    output.write(mp3file.read())
    output.close()
    pygame.mixer.init()
    pygame.mixer.music.load("test.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


with SocketIO('http://192.168.137.101', 3000) as socketIO:
    socketIO.on('recu', on_aaa_response)
    print "Begin"
    while(1):

        print gpsd.fix.latitude
        print gpsd.fix.longitude
    socketIO.wait(seconds=5)


#
# def on_response(*args):
#     print 'on_response', args
#
# import logging;
# logging.basicConfig(level=logging.DEBUG)
#
# socketIO = SocketIO('localhost', 8080)
# socketIO.on('news', on_response)
#
# socketIO.wait(seconds=1)
# pygame.mixer.init()
# pygame.mixer.music.load("test.mp3")
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy() == True:
#     continue
#
