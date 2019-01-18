#!/usr/bin/env python
#-*- cording: utf-8 -*-

import pygame.mixer
import time

pygame.mixer.init()
pygame.mixer.music.load("se.mp3")
pygame.mixer.music.play()

while True:
	time.sleep(1)