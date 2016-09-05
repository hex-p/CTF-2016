#!/usr/bin/python
# -*- coding:utf-8 -*-

import random, sys, socket

'''Tokyo Westerns CTF : Make a Palindrome - 50 pts'''

#Variables and socket configuration

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "ppc1.chal.ctf.westerns.tokyo"
port = 31111
port = int(port)
s.connect((host,port)) 
dt = s.recv(1024) #We get the first data (some explanations)
compteur = 0


while compteur < 30:
	dt = s.recv(1024)
	data = dt	
	p1 = dt.find('Input:')
	p2 = dt.find('Answer:')
	if compteur == 0:
		donnee = dt[p1+7:p2-1]	#Get the current input
	else:
		donnee = dt[p1+7:p2]
		dt = s.recv(1024)
	print data	#Display Input and answer
	string = donnee
	chaine = string.split(" ")
	del(chaine[0])	#Delete the number of words information
	i = 0
	palindrome = []
	joined_pal=[]

	while i==0:
		palindrome = sorted(chaine, key=lambda k: random.random()) #Generate random phrase with all words
		joined_pal = ''.join(palindrome)
		if joined_pal == ''.join(reversed(joined_pal)):
			i = 1	#If the string could be read verse/reverse : this is a palindrome !

	print ("Send : " +' '.join(palindrome))
	p = ' '.join(palindrome)+"\n"
	s.send(p)
	compteur += 1

flag = s.recv(1024) # Once with finish the game, we get the flag.
print flag
