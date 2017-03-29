#version 0.2
#Authors:
#Alexander Yakovlev <a.yakovlev911@gmail.com> https://github.com/toxydose
#https://awake.pro/

import sys
#!!!!!
#import logging
#!!!!!
payload_input = ''

l='//'
mod_input=''
mod_output=''

def replacement():
	print ('DigiKeyboard.', end ='')
	print(
l.replace(' a', 'KEY_A').replace(' a ', 'KEY_A')
.replace(' b', 'KEY_B')
.replace(' c', 'KEY_C')
.replace(' d', 'KEY_D')
.replace(' e', 'KEY_E')
.replace(' f', 'KEY_F')
.replace(' g', 'KEY_G')
.replace(' h', 'KEY_H')
.replace(' i', 'KEY_I')
.replace(' j', 'KEY_J')
.replace(' k', 'KEY_K')
.replace(' l', 'KEY_L')
.replace(' m', 'KEY_M')
.replace(' n', 'KEY_N')
.replace(' o', 'KEY_O')
.replace(' p', 'KEY_P')
.replace(' q', 'KEY_Q')
.replace(' r', 'KEY_R')
.replace(' s', 'KEY_S')
.replace(' t', 'KEY_T')
.replace(' u', 'KEY_U')
.replace(' v', 'KEY_V')
.replace(' w', 'KEY_W')
.replace(' x', 'KEY_X')
.replace(' y', 'KEY_Y')
.replace(' z', 'KEY_Z')

#1-0 if needed

#f1-f12
.replace(' F1','KEY_F1')
.replace(' F2','KEY_F2')
.replace(' F3','KEY_F3')
.replace(' F4','KEY_F4')
.replace(' F5','KEY_F5')
.replace(' F6','KEY_F6')
.replace(' F7','KEY_F7')
.replace(' F8','KEY_F8')
.replace(' F9','KEY_F9')
.replace(' F10','KEY_F10')
.replace(' F11','KEY_F11')
.replace(' F12','KEY_F12')
#arrows 
.replace('LEFTARROW', 'KEY_ARROW_LEFT')
.replace('RIGHTARROW', 'KEY_ARROW_RIGHT')
.replace('UPARROW','KEY_ARROW_UP')
.replace('DOWNARROW','KEY_ARROW_DOWN')
.replace('LEFT', 'KEY_ARROW_LEFT')
.replace('RIGH', 'KEY_ARROW_RIGHT')
.replace('UP','KEY_ARROW_UP')
.replace('DOWN','KEY_ARROW_DOWN')
#keys
.replace('PRINTSCREEN','sendKeyStroke(KEY_PRT_SCR' )
.replace('TAB', 'sendKeyStroke(KEY_TAB')
.replace('SPACE', 'sendKeyStroke(KEY_SPACE')
.replace('CONTROL ALT','sendKeyStroke(MOD_ALT_RIGHT,')
.replace('CTRL ALT','sendKeyStroke(MOD_ALT_RIGHT,')
.replace('ESCAPE','sendKeyStroke(KEY_ESC' )
.replace('ENTER','sendKeyStroke(KEY_ENTER'),end = '')
	print(');')

def modreplacement():
	print ('DigiKeyboard.', end ='')
	print('sendKeyStroke(', end = '')

	print(l.replace (mod_input, '').replace(' a', 'KEY_A').replace(' a ', 'KEY_A')
.replace(' b', 'KEY_B')
.replace(' c', 'KEY_С')
.replace(' d', 'KEY_D')
.replace(' e', 'KEY_E')
.replace(' f', 'KEY_F')
.replace(' g', 'KEY_G')
.replace(' h', 'KEY_H')
.replace(' i', 'KEY_I')
.replace(' j', 'KEY_J')
.replace(' k', 'KEY_K')
.replace(' l', 'KEY_L')
.replace(' m', 'KEY_M')
.replace(' n', 'KEY_N')
.replace(' o', 'KEY_O')
.replace(' p', 'KEY_P')
.replace(' q', 'KEY_Q')
.replace(' r', 'KEY_R')
.replace(' s', 'KEY_S')
.replace(' t', 'KEY_T')
.replace(' u', 'KEY_U')
.replace(' v', 'KEY_V')
.replace(' w', 'KEY_W')
.replace(' x', 'KEY_X')
.replace(' y', 'KEY_Y')
.replace(' z', 'KEY_Z')

#1-0

#f1-f12
.replace(' F1','KEY_F1')
.replace(' F2','KEY_F2')
.replace(' F3','KEY_F3')
.replace(' F4','KEY_F4')
.replace(' F5','KEY_F5')
.replace(' F6','KEY_F6')
.replace(' F7','KEY_F7')
.replace(' F8','KEY_F8')
.replace(' F9','KEY_F9')
.replace(' F10','KEY_F10')
.replace(' F11','KEY_F11')
.replace(' F12','KEY_F12')

#arrows 
.replace('LEFTARROW', 'KEY_ARROW_LEFT')
.replace('RIGHTARROW', 'KEY_ARROW_RIGHT')
.replace('UPARROW','KEY_ARROW_UP')
.replace('DOWNARROW','KEY_ARROW_DOWN')
.replace('LEFT', 'KEY_ARROW_LEFT')
.replace('RIGH', 'KEY_ARROW_RIGHT')
.replace('UP','KEY_ARROW_UP')
.replace('DOWN','KEY_ARROW_DOWN')

.replace('PRINTSCREEN','sendKeyStroke(KEY_PRT_SCR' )
.replace('TAB', 'sendKeyStroke(KEY_TAB')
.replace('ESCAPE','KEY_ESC' )
.replace('SPACE', 'KEY_SPACE')
.replace(' ','')
.replace('ENTER','KEY_ENTER'),end = '')

	print(','+mod_output, end = '')				
	print(');')


#arguments
if len(sys.argv) == 2:
	payload_input = open(sys.argv[1], "r")
	sys.stdout = open("digipayload.ino", "w")
	z = len(open(sys.argv[1], "r").readlines())
elif len(sys.argv) == 3:
	payload_input = open(sys.argv[1], "r")
	sys.stdout = open(sys.argv[2]+'.ino', 'w')
	z = len(open(sys.argv[1], "r").readlines())
elif len(sys.argv) > 3:
	print('Too much Arguments')
	exit()
else:	
	payload_input = open('payload.txt', "r")
	sys.stdout = open("digipayload.ino", "w")
	z = len(open('payload.txt', "r").readlines())

#---------------
#Digispark program fragment
print('#include "DigiKeyboard.h"\n')
print('#define KEY_ESC     41\n')
print('#define KEY_BACKSPACE 42\n')
print('#define KEY_TAB     43\n')
print('#define KEY_PRT_SCR 70\n')
print('#define KEY_DELETE  76\n')

print('void setup() {\n')
print('DigiKeyboard.delay(5000);') #windows mozhet dolgo raspoznavat digispark potomu bylo resheno dobavlyat 5 sek delay vmesto 0.5sek
print('DigiKeyboard.sendKeyStroke(0);')
#---------------------------------------

for i in range(z):
	l = payload_input.readline().replace('\n', '')
	
	if len (l) < 1:
		print('', end = '')

	else:

		if 'REM' in l:
			print ('//', l)	
		
		else:
			if 'DELAY' in l:
				print ('DigiKeyboard.', end = '')
				print (l.replace('DELAY', 'delay(').replace(' ',''), end = '')
				print(');')
						
			elif 'STRING' in l:
				print ('DigiKeyboard.', end = '')
				print (l.replace('"', '")); DigiKeyboard.print(char(34)); DigiKeyboard.print(F("').replace('\\', '")); DigiKeyboard.print(char(92)); DigiKeyboard.print(F("').replace('STRING ','print(F("'), end = '')
				print ('")', end = '')
				print(');');
				
			elif (l == 'GUI') or (l == 'WINDOWS') or (l == 'CONTROL ESCAPE'):
				print('DigiKeyboard.sendKeyStroke(KEY_ESC,MOD_CONTROL_LEFT);')

			elif (l == 'GUI d') or (l == 'WINDOWS d'):
				print ('DigiKeyboard.sendKeyStroke(KEY_D,MOD_GUI_LEFT);')
			
			elif (l == 'WINDOWS r') or (l == 'GUI r'):
				print ('DigiKeyboard.sendKeyStroke(KEY_R,MOD_GUI_LEFT);')

			elif 'MENU' in l:
				print ('DigiKeyboard.sendKeyStroke(MOD_GUI_RIGHT);')
				
		#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!INVERCE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!	
			elif 'CTRL ALT' in l:
				replacement()
			elif 'ALT' in l:
				mod_input = 'ALT'
				mod_output = 'MOD_ALT_RIGHT'
				modreplacement()
			elif 'CTRL' in l:
				mod_input = 'CTRL'
				mod_output = 'MOD_CONTROL_LEFT'
				modreplacement()

			elif 'CONTROL' in l:
				mod_input = 'CONTROL'
				mod_output = 'MOD_CONTROL_LEFT'
				modreplacement()

		#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!		
			else:
				replacement()

		if len(l) <1:
			print('', end = '')
#Digispark program fragment
print('\n}')
print('\n')
print('void loop() {\n')
print('}\n')
#-----------------------------------

payload_input.close()
