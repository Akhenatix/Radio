import urllib2
# from urllib2 import request
# import urllib.request
import pygame
import os
import subprocess
import re
import time

def GetGps():
    str=subprocess.Popen("gpspipe -w -n 5 127.0.0.1:200", shell=True, stdout=subprocess.PIPE).stdout.read()
    parselon= re.findall('lon\":-{0,1}[0-9\.]+,',str)
    parselat= re.findall('lat\":-{0,1}[0-9\.]+,',str)

    if len(parselon)>0:
        longitude= re.findall('-{0,1}[0-9\.]+',parselon[0])[0]
        latitude= re.findall('-{0,1}[0-9\.]+',parselat[0])[0]
        print longitude
        print latitude
        return longitude,latitude
    return "0","0"



longitude = -20;
latitude = 20;
while True:
    time.sleep(2)
    longitude,latitude=GetGps();
    # Desactiver le pare feu
    print str("reading from server ") + longitude +" "+ latitude;
    requestURL = "http://192.168.137.1:8125/?longitude="+str(longitude)+"&latitude="+str(latitude);



    print "http://192.168.137.1:8125/?longitude="+str(longitude)+"&latitude="+str(latitude);

    mp3file = urllib2.urlopen("http://192.168.137.1:8125/?longitude="+str(longitude)+"&latitude="+str(latitude))


    print "file "
    output = open('musique.mp3','wb')
    output.write(mp3file.read())
    output.close()
    print "end"

    # from subprocess import call
    # print call(["wget", "-O", "musique.mp3", requestURL])



    # urllib.request.urlretrieve(requestURL, 'musique.mp3')



    print os.path.dirname(os.path.realpath(__file__))

    pygame.mixer.init()
    pygame.mixer.music.load("musique.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() == True:
        continue

    os.remove('musique.mp3');


