import urllib2
# from urllib2 import request
# import urllib.request
import pygame
import os


longitude = -20;
latitude = 20;

# Desactiver le pare feu
print str("reading from server ") + str(longitude) +" "+ str(latitude);
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


