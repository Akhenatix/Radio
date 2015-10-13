import urllib2
import pygame

mp3file = urllib2.urlopen("http://192.168.137.1:8125")
output = open('test.mp3','wb')
output.write(mp3file.read())
output.close()

pygame.mixer.init()
pygame.mixer.music.load("test.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue