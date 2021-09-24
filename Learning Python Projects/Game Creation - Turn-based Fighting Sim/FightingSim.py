from Character_Master import *
from listGenerator import *
from TurnMeterMethods import *
import pygame as pygame
import sys as sys
from pygame.locals import *
import math as m
import time as time

# gameRunningFlag = False #attached to load data/update GUI button
# takeActionButtonPressed = False
# previousWinnerDefined = False
# damageNumber = 0
# tmChange = 0
# actionSelection = ""
# turnTaker = getWinner()#unused?
# previousWinner = "" #Q.queue
# ### queues: .get(), .put(), .qsize()

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
BLACK = (0, 0, 0)
BADGUYSIZE = 40
GOODGUYSIZE = 40
DARK_GRAY = pygame.Color('gray13')
SHADOW = (100,100,100)
WHITE = (255,255,255)
GREEN = (0,200,0)
LIGHTGREEN = (0,255,0)
BLUE = (0,0,128)
LIGHTBLUE = (0,0,255)
RED = (200,0,0)
LIGHTRED = (255,100,100)
PURPLE = (102,0, 102)
LITEPURPLE = (153,0,153)
#flags and clock
clock = pygame.time.Clock() #unused as of yet
startScreenFlag = False
playScreenFlag = False
noMegaHealFlag = False
noTauntFlag = False
portraitsMadeFlag = False
targetObj = None
#text and char screen
playScreenInstructionsX = m.floor(WINDOWWIDTH / 2)
playScreenInstructionsY = m.floor(WINDOWHEIGHT / 15)
charDisplayTop = m.floor((WINDOWHEIGHT / 15)+60)
charDisplayHeight = 300
charDisplayLeft = WINDOWWIDTH - (WINDOWWIDTH - 20) 
charDisplayWidth = WINDOWWIDTH - 40
charDisplayRect = pygame.Rect(charDisplayLeft, charDisplayTop, charDisplayWidth, charDisplayHeight)
#button sizes, positions
BUTTONWIDTH = 100
BUTTONHEIGHT = 30
button1Left = m.floor((WINDOWWIDTH/3)-50)
button2Left = m.floor((WINDOWWIDTH/2)-50)
button3Left = m.floor(2*(WINDOWWIDTH/3)-50)
button1Top = m.floor((WINDOWHEIGHT / 15) + 390)
button2Top = m.floor((WINDOWHEIGHT / 15) + 440)
button3Top = m.floor((WINDOWHEIGHT / 15) + 490)
defButton = pygame.Rect(button2Left, button1Top, BUTTONWIDTH, BUTTONHEIGHT)
atkButton = pygame.Rect(button1Left, button1Top, BUTTONWIDTH, BUTTONHEIGHT)
frenzyButton = pygame.Rect(button3Left, button1Top, BUTTONWIDTH, BUTTONHEIGHT)
classButton1 = pygame.Rect(button1Left+50, button2Top, BUTTONWIDTH, BUTTONHEIGHT)
classButton2 = pygame.Rect(button3Left-50, button2Top, BUTTONWIDTH, BUTTONHEIGHT)
escapeButton = pygame.Rect(button2Left, button3Top, BUTTONWIDTH, BUTTONHEIGHT)
atkButtonTextSpotX = button1Left + 50
atkButtonTextSpotY = button1Top + 15
defButtonTextSpotX = button2Left + 50
defButtonTextSpotY = button1Top + 15
frenzyButtonTextSpotX = button3Left + 50
frenzyButtonTextSpotY = button1Top + 15
cls1ButtonTextSpotX = button1Left + 100
cls1ButtonTextSpotY = button2Top + 15
cls2ButtonTextSpotX = button3Left
cls2ButtonTextSpotY = button2Top + 15
escButtonTextSpotX = button2Left + 50
escButtonTextSpotY = button3Top + 15
#initialize
pygame.init()
displaySurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Fighter\'s Simulator') #game name
pygame.mouse.set_visible(True)
#fonts
#SysFont(name, size, bold=False, italic=False) guide
titleFont = pygame.font.SysFont(None, 48, bold=True, italic=False)
instructionFont = pygame.font.SysFont(None, 36, bold=False, italic=True)
buttonFont = pygame.font.SysFont(None, 20, bold=False, italic=False)
# # set up sounds
# gameOverSound = pygame.mixer.Sound('match1.wav')
# pygame.mixer.music.load('tetrisc.mid')
# set up images
attackerImage = pygame.image.load('attacker.png')
resizedAttackerImage = pygame.transform.scale(attackerImage, (BUTTONWIDTH, BUTTONWIDTH))
tankImage = pygame.image.load('tank.png')
resizedTankImage = pygame.transform.scale(tankImage, (BUTTONWIDTH, BUTTONWIDTH))
healerImage = pygame.image.load('healer.png') #loads image
resizedHealerImage = pygame.transform.scale(healerImage, (BUTTONHEIGHT, BUTTONWIDTH))
#portrait positions
p4x = p1x = m.floor(WINDOWWIDTH/2) - 315
p1y = m.floor(WINDOWHEIGHT/2) + 45
p5x = p2x = m.floor(WINDOWWIDTH /2) - 80
p2y = m.floor(WINDOWHEIGHT/2) + 45
p6x = p3x = m.floor(WINDOWWIDTH/2) + 165
p3y = m.floor(WINDOWHEIGHT/2) + 45
# p4x = p1x
p4y = p1y - 195 
# p5x = p2x
p5y = p2y - 195
# p6x = p3x
p6y = p3y - 195
#portrait Objects, dictionaries
p1Obj = {'image': resizedAttackerImage,
		 'centerx': p1x,
		 'centery': p1y,
		 'rect': None
}
p2Obj = {'image': resizedAttackerImage,
		 'centerx': p2x,
		 'centery': p2y,
		 'rect': None
}
p3Obj = {'image': resizedAttackerImage,
		 'centerx': p3x,
		 'centery': p3y,
		 'rect': None
}
p4Obj = {'image': resizedAttackerImage,
		 'centerx': p4x,
		 'centery': p4y,
		 'rect': None
}
p5Obj = {'image': resizedAttackerImage,
		 'centerx': p5x,
		 'centery': p5y,
		 'rect': None
}
p6Obj = {'image': resizedAttackerImage,
		 'centerx': p6x,
		 'centery': p6y,
		 'rect': None
}

#player objects
p1 = None
p2 = None
p3 = None
p4 = None
p5 = None
p6 = None
playerObjects = []

#player1 details
p1Health_x = p1x + BUTTONWIDTH
p1Health_y = p1y - BUTTONHEIGHT
p1TM_x = p1x + BUTTONWIDTH
p1TM_y = p1y - 15
p1TauntFlagWords_x = p1x + BUTTONWIDTH
p1TauntFlagWords_y = p1y
p1TauntFlags_x = p1x + BUTTONWIDTH
p1TauntFlags_y = p1y + m.floor(BUTTONWIDTH/8)
p1DefendFlagWords_x = p1x + BUTTONWIDTH
p1DefendFlagWords_y = p1y + BUTTONHEIGHT - 5
p1DefendFlags_x = p1x + BUTTONWIDTH
p1DefendFlags_y = p1y + m.floor(BUTTONWIDTH/4)+12 #+ BUTTONHEIGHT +20
#player2 details
p2Health_x = p2x + BUTTONWIDTH
p2Health_y = p2y - BUTTONHEIGHT
p2TM_x = p2x + BUTTONWIDTH
p2TM_y = p2y - 15
p2TauntFlagWords_x = p2x + BUTTONWIDTH
p2TauntFlagWords_y = p2y
p2TauntFlags_x = p2x + BUTTONWIDTH
p2TauntFlags_y = p2y + m.floor(BUTTONWIDTH/8)
p2DefendFlagWords_x = p2x + BUTTONWIDTH
p2DefendFlagWords_y = p2y + BUTTONHEIGHT - 5
p2DefendFlags_x = p2x + BUTTONWIDTH
p2DefendFlags_y = p2y + m.floor(BUTTONWIDTH/4)+12
#player3 details
p3Health_x = p3x + BUTTONWIDTH
p3Health_y = p3y - BUTTONHEIGHT
p3TM_x = p3x + BUTTONWIDTH
p3TM_y = p3y - 15
p3TauntFlagWords_x = p3x + BUTTONWIDTH
p3TauntFlagWords_y = p3y
p3TauntFlags_x = p3x + BUTTONWIDTH
p3TauntFlags_y = p3y + m.floor(BUTTONWIDTH/8)
p3DefendFlagWords_x = p3x + BUTTONWIDTH
p3DefendFlagWords_y = p3y + BUTTONHEIGHT - 5
p3DefendFlags_x = p3x + BUTTONWIDTH
p3DefendFlags_y = p3y + m.floor(BUTTONWIDTH/4)+12 
#player4 details
p4Health_x = p4x + BUTTONWIDTH
p4Health_y = p4y - BUTTONHEIGHT
p4TM_x = p4x + BUTTONWIDTH
p4TM_y = p4y - 15
p4TauntFlagWords_x = p4x + BUTTONWIDTH
p4TauntFlagWords_y = p4y
p4TauntFlags_x = p4x + BUTTONWIDTH
p4TauntFlags_y = p4y + m.floor(BUTTONWIDTH/8)
p4DefendFlagWords_x = p4x + BUTTONWIDTH
p4DefendFlagWords_y = p4y + BUTTONHEIGHT - 5
p4DefendFlags_x = p4x + BUTTONWIDTH
p4DefendFlags_y = p4y + m.floor(BUTTONWIDTH/4)+12 #+ BUTTONHEIGHT +20
#player5 details
p5Health_x = p5x + BUTTONWIDTH
p5Health_y = p5y - BUTTONHEIGHT
p5TM_x = p5x + BUTTONWIDTH
p5TM_y = p5y - 15
p5TauntFlagWords_x = p5x + BUTTONWIDTH
p5TauntFlagWords_y = p5y
p5TauntFlags_x = p5x + BUTTONWIDTH
p5TauntFlags_y = p5y + m.floor(BUTTONWIDTH/8)
p5DefendFlagWords_x = p5x + BUTTONWIDTH
p5DefendFlagWords_y = p5y + BUTTONHEIGHT - 5
p5DefendFlags_x = p5x + BUTTONWIDTH
p5DefendFlags_y = p5y + m.floor(BUTTONWIDTH/4)+12 #+ BUTTONHEIGHT +20
#player6 details
p6Health_x = p6x + BUTTONWIDTH
p6Health_y = p6y - BUTTONHEIGHT
p6TM_x = p6x + BUTTONWIDTH
p6TM_y = p6y - 15
p6TauntFlagWords_x = p6x + BUTTONWIDTH
p6TauntFlagWords_y = p6y
p6TauntFlags_x = p6x + BUTTONWIDTH
p6TauntFlags_y = p6y + m.floor(BUTTONWIDTH/8)
p6DefendFlagWords_x = p6x + BUTTONWIDTH
p6DefendFlagWords_y = p6y + BUTTONHEIGHT - 5
p6DefendFlags_x = p6x + BUTTONWIDTH
p6DefendFlags_y = p6y + m.floor(BUTTONWIDTH/4)+12 #+ BUTTONHEIGHT +20

def terminate(): #ends program on ESC-press
	pygame.quit()
	sys.exit()
	
def drawText(text, font, color, surface, x, y):
	textobj = font.render(text, 1, color)
	textrect = textobj.get_rect()
	textrect.center = (x, y) #where is the thing placed
	surface.blit(textobj, textrect)

def updateButtons():
	global noMegaHealFlag, noTauntFlag
	noMegaHealFlag = False
	noTauntFlag = False
	#make default buttons
	pygame.draw.rect(displaySurface, WHITE, atkButton)
	pygame.draw.rect(displaySurface, WHITE, defButton)
	pygame.draw.rect(displaySurface, WHITE, frenzyButton)
	pygame.draw.rect(displaySurface, WHITE, classButton1)
	pygame.draw.rect(displaySurface, WHITE, classButton2)
	pygame.draw.rect(displaySurface, WHITE, escapeButton)
	drawText("Attack!", buttonFont, SHADOW, displaySurface, atkButtonTextSpotX, atkButtonTextSpotY)
	drawText("Defend!", buttonFont, SHADOW, displaySurface, defButtonTextSpotX, defButtonTextSpotY)
	drawText("Frenzy!", buttonFont, SHADOW, displaySurface, frenzyButtonTextSpotX, frenzyButtonTextSpotY)
	drawText("Escape Battle!", buttonFont, SHADOW, displaySurface, escButtonTextSpotX, escButtonTextSpotY)
	pygame.draw.rect(displaySurface, WHITE, classButton1)
	pygame.draw.rect(displaySurface, WHITE, classButton2)#clear all buttons and replace with proper labels
	# classButton2.fill(WHITE)
	if getWinner().getRole() == "Attacker":
		drawText("Delay!", buttonFont, SHADOW, displaySurface, cls1ButtonTextSpotX, cls1ButtonTextSpotY)
		drawText("Flourish!", buttonFont, SHADOW, displaySurface, cls2ButtonTextSpotX, cls2ButtonTextSpotY)
	if getWinner().getRole() == "Healer":
		drawText("Small Heal!", buttonFont, SHADOW, displaySurface, cls1ButtonTextSpotX, cls1ButtonTextSpotY)
		drawText("Mega Heal!", buttonFont, SHADOW, displaySurface, cls2ButtonTextSpotX, cls2ButtonTextSpotY)
		if getWinner().getHealth() <= (0.25*getWinner().getMaxHealth()):
			noMegaHealFlag = True
			#lines over class2Button
			pygame.draw.line(displaySurface, RED, (cls2ButtonTextSpotX-105, cls2ButtonTextSpotY-25), (cls2ButtonTextSpotX+5, cls2ButtonTextSpotY+25), 4)
			pygame.draw.line(displaySurface, RED, (cls2ButtonTextSpotX-105, cls2ButtonTextSpotY+25), (cls2ButtonTextSpotX+5, cls2ButtonTextSpotY-25), 4)
			# #lines over class1Button
			# pygame.draw.line(displaySurface, RED, (cls1ButtonTextSpotX-55, cls1ButtonTextSpotY-25), (cls1ButtonTextSpotX+55, cls1ButtonTextSpotY+25), 4)
			# pygame.draw.line(displaySurface, RED, (cls1ButtonTextSpotX-53, cls1ButtonTextSpotY+25), (cls1ButtonTextSpotX+55, cls1ButtonTextSpotY-25), 4)
	if getWinner().getRole() == "Tank":
		drawText("Taunt!", buttonFont, SHADOW, displaySurface, cls1ButtonTextSpotX, cls1ButtonTextSpotY)
		drawText("Rally!", buttonFont, SHADOW, displaySurface, cls2ButtonTextSpotX, cls2ButtonTextSpotY)	
		if getWinner().checkTauntFlag() == True:
			noTauntFlag = True
			#lines over class2Button
			# pygame.draw.line(displaySurface, RED, (cls2ButtonTextSpotX-105, cls2ButtonTextSpotY-25), (cls2ButtonTextSpotX+5, cls2ButtonTextSpotY+25), 4)
			# pygame.draw.line(displaySurface, RED, (cls2ButtonTextSpotX-105, cls2ButtonTextSpotY+25), (cls2ButtonTextSpotX+5, cls2ButtonTextSpotY-25), 4)
			# #lines over class1Button
			pygame.draw.line(displaySurface, RED, (cls1ButtonTextSpotX-55, cls1ButtonTextSpotY-25), (cls1ButtonTextSpotX+55, cls1ButtonTextSpotY+25), 4)
			pygame.draw.line(displaySurface, RED, (cls1ButtonTextSpotX-53, cls1ButtonTextSpotY+25), (cls1ButtonTextSpotX+55, cls1ButtonTextSpotY-25), 4)

def updateCharPortraits2():
	if p4 != None:
		displaySurface.blit(p4Obj['image'], p4Obj['rect']) 
	if p5 != None:
		displaySurface.blit(p5Obj['image'], p5Obj['rect']) 
	if p6 != None:
		displaySurface.blit(p6Obj['image'], p6Obj['rect']) 
	if p1 != None:
		print("p1 != none")
		displaySurface.blit(p1Obj['image'], p1Obj['rect']) 
	if p2 != None:
		displaySurface.blit(p2Obj['image'], p2Obj['rect']) 
	if p3 != None:
		displaySurface.blit(p3Obj['image'], p3Obj['rect'])

def updateCharPortraits(eList, fList): #updates pictures and adds player objects to list
	global p1,p2,p3,p4,p5,p6, portraitsMadeFlag
	
	if portraitsMadeFlag == False:
		portraitsMadeFlag = True
	for bad in eList: #make character portraits accurate
		if p4 == None:#assign players to easily callable slots
			p4 = bad
			classTracker = bad.getRole()
			playerObjects.append(p4)
			# print("badguy: {0}, classtracker updated?: {1}".format(bad,classTracker))
			if classTracker == 'Attacker':
				# print("p4, attacker")
				p4Obj['image'] = resizedAttackerImage
				p4Obj['rect'] = p4Obj['image'].get_rect()
				p4Obj['rect'].centerx = p4Obj['centerx']
				p4Obj['rect'].centery = p4Obj['centery']
			elif classTracker == 'Tank':
				# print("p4, tank")
				p4Obj['image'] = resizedTankImage
				p4Obj['rect'] = p4Obj['image'].get_rect()
				p4Obj['rect'].centerx = p4Obj['centerx']
				p4Obj['rect'].centery = p4Obj['centery']
			elif classTracker == 'Healer':
				# print("p4, healer")
				p4Obj['image'] = resizedHealerImage
				p4Obj['rect'] = p4Obj['image'].get_rect()
				p4Obj['rect'].centerx = p4Obj['centerx']
				p4Obj['rect'].centery = p4Obj['centery']
			displaySurface.blit(p4Obj['image'], p4Obj['rect'])
		elif p5 == None:
			p5 = bad
			classTracker = bad.getRole()
			playerObjects.append(p5)
			if classTracker == 'Attacker':
				p5Obj['image'] = resizedAttackerImage
				p5Obj['rect'] = p5Obj['image'].get_rect()
				p5Obj['rect'].centerx = p5Obj['centerx']
				p5Obj['rect'].centery = p5Obj['centery']
			elif classTracker == 'Tank':
				p5Obj['image'] = resizedTankImage
				p5Obj['rect'] = p5Obj['image'].get_rect()
				p5Obj['rect'].centerx = p5Obj['centerx']
				p5Obj['rect'].centery = p5Obj['centery']
			elif classTracker == 'Healer':
				p5Obj['image'] = resizedHealerImage
				p5Obj['rect'] = p5Obj['image'].get_rect()
				p5Obj['rect'].centerx = p5Obj['centerx']
				p5Obj['rect'].centery = p5Obj['centery']
			displaySurface.blit(p5Obj['image'], p5Obj['rect'])
		elif p6 == None:
			p6 = bad
			classTracker = bad.getRole()
			playerObjects.append(p6)
			if classTracker == 'Attacker':
				p6Obj['image'] = resizedAttackerImage
				p6Obj['rect'] = p6Obj['image'].get_rect()
				p6Obj['rect'].centerx = p6Obj['centerx']
				p6Obj['rect'].centery = p6Obj['centery']
			elif classTracker == 'Tank':
				p6Obj['image'] = resizedTankImage
				p6Obj['rect'] = p6Obj['image'].get_rect()
				p6Obj['rect'].centerx = p6Obj['centerx']
				p6Obj['rect'].centery = p6Obj['centery']
			elif classTracker == 'Healer':
				p6Obj['image'] = resizedHealerImage
				p6Obj['rect'] = p6Obj['image'].get_rect()
				p6Obj['rect'].centerx = p6Obj['centerx']
				p6Obj['rect'].centery = p6Obj['centery']
			displaySurface.blit(p6Obj['image'], p6Obj['rect'])
				
	for good in fList: #make character portraits accurate
		
		if p1 == None:#assign players to easily callable slots
			print("p1 === none")
			p1 = good
			classTracker = good.getRole()
			playerObjects.append(p1)
			if classTracker == 'Attacker':
				p1Obj['image'] = resizedAttackerImage
				p1Obj['rect'] = p1Obj['image'].get_rect()
				p1Obj['rect'].centerx = p1Obj['centerx']
				p1Obj['rect'].centery = p1Obj['centery']
			elif classTracker == 'Tank':
				p1Obj['image'] = resizedTankImage
				p1Obj['rect'] = p1Obj['image'].get_rect()
				p1Obj['rect'].centerx = p1Obj['centerx']
				p1Obj['rect'].centery = p1Obj['centery']
			elif classTracker == 'Healer':
				p1Obj['image'] = resizedHealerImage
				p1Obj['rect'] = p1Obj['image'].get_rect()
				p1Obj['rect'].centerx = p1Obj['centerx']
				p1Obj['rect'].centery = p1Obj['centery']
			displaySurface.blit(p1Obj['image'], p1Obj['rect'])	
		elif p2 == None:
			p2 = good
			classTracker = good.getRole()
			playerObjects.append(p2)
			if classTracker == 'Attacker':
				p2Obj['image'] = resizedAttackerImage
				p2Obj['rect'] = p2Obj['image'].get_rect()
				p2Obj['rect'].centerx = p2Obj['centerx']
				p2Obj['rect'].centery = p2Obj['centery']
			elif classTracker == 'Tank':
				p2Obj['image'] = resizedTankImage
				p2Obj['rect'] = p2Obj['image'].get_rect()
				p2Obj['rect'].centerx = p2Obj['centerx']
				p2Obj['rect'].centery = p2Obj['centery']
			elif classTracker == 'Healer':
				p2Obj['image'] = resizedHealerImage
				p2Obj['rect'] = p2Obj['image'].get_rect()
				p2Obj['rect'].centerx = p2Obj['centerx']
				p2Obj['rect'].centery = p2Obj['centery']
			displaySurface.blit(p2Obj['image'], p2Obj['rect'])
		elif p3 == None:
			p3 = good
			classTracker = good.getRole()
			playerObjects.append(p3)
			if classTracker == 'Attacker':
				p3Obj['image'] = resizedAttackerImage
				p3Obj['rect'] = p3Obj['image'].get_rect()
				p3Obj['rect'].centerx = p3Obj['centerx']
				p3Obj['rect'].centery = p3Obj['centery']
			elif classTracker == 'Tank':
				p3Obj['image'] = resizedTankImage
				p3Obj['rect'] = p3Obj['image'].get_rect()
				p3Obj['rect'].centerx = p3Obj['centerx']
				p3Obj['rect'].centery = p3Obj['centery']
			elif classTracker == 'Healer':
				p3Obj['image'] = resizedHealerImage
				p3Obj['rect'] = p3Obj['image'].get_rect()
				p3Obj['rect'].centerx = p3Obj['centerx']
				p3Obj['rect'].centery = p3Obj['centery']
			displaySurface.blit(p3Obj['image'], p3Obj['rect'])					
	# update surface
	pygame.display.update()
	
	#to change an image that already exists
	# ##playerObj = {'surface': pygame.transform.scale(L_SQUIR_IMG, (STARTSIZE, STARTSIZE)),
                 # 'facing': LEFT,
                 # 'size': STARTSIZE,
                 # 'x': HALF_WINWIDTH,
                 # 'y': HALF_WINHEIGHT,
                 # 'bounce':0,
                 # 'health': MAXHEALTH}
	#if playerObj['facing'] != LEFT: # change player image
                        # playerObj['surface'] = pygame.transform.scale(L_SQUIR_IMG, (playerObj['size'], playerObj['size']))
                    # playerObj['facing'] = LEFT
	# return
def updateCharText():
	global playerObjects
	
	for player in playerObjects:
		if player == p1:
			drawText("Health: {0}/{1}".format(player.getHealth(), player.getMaxHealth()), buttonFont, BLACK, displaySurface, p1Health_x, p1Health_y)
			drawText("TM: {0}/{1}".format(player.getTurnMeter(),"1000"), buttonFont, BLACK, displaySurface, p1TM_x, p1TM_y)
			
			drawText("Taunting?:", buttonFont, BLACK, displaySurface,p1TauntFlagWords_x, p1TauntFlagWords_y)
			drawText("{0}".format(player.checkTauntFlag()), buttonFont, BLACK, displaySurface, p1TauntFlags_x, p1TauntFlags_y)
			
			drawText("Defending?:".format(player.getTurnMeter(),"1000"), buttonFont, BLACK, displaySurface, p1DefendFlagWords_x, p1DefendFlagWords_y)
			drawText("{0}".format(player.checkDefenseFlag()), buttonFont, BLACK, displaySurface, p1DefendFlags_x, p1DefendFlags_y)
			pygame.display.update()
		elif player == p2:
			drawText("Health: {0}/{1}".format(player.getHealth(), player.getMaxHealth()), buttonFont, BLACK, displaySurface, p2Health_x, p2Health_y)
			drawText("TM: {0}/{1}".format(player.getTurnMeter(),"1000"), buttonFont, BLACK, displaySurface, p2TM_x, p2TM_y)
			
			drawText("Taunting?:", buttonFont, BLACK, displaySurface, p2TauntFlagWords_x, p2TauntFlagWords_y)
			drawText("{0}".format(player.checkTauntFlag()), buttonFont, BLACK, displaySurface, p2TauntFlags_x, p2TauntFlags_y)
			
			drawText("Defending?:".format(player.getTurnMeter(),"1000"), buttonFont, BLACK, displaySurface, p2DefendFlagWords_x, p2DefendFlagWords_y)
			drawText("{0}".format(player.checkDefenseFlag()), buttonFont, BLACK, displaySurface, p2DefendFlags_x, p2DefendFlags_y)
			pygame.display.update()
		elif player == p3:
			drawText("Health: {0}/{1}".format(player.getHealth(), player.getMaxHealth()), buttonFont, BLACK, displaySurface, p3Health_x, p3Health_y)
			drawText("TM: {0}/{1}".format(player.getTurnMeter(),"1000"), buttonFont, BLACK, displaySurface, p3TM_x, p3TM_y)
			
			drawText("Taunting?:", buttonFont, BLACK, displaySurface, p3TauntFlagWords_x, p3TauntFlagWords_y)
			drawText("{0}".format(player.checkTauntFlag()), buttonFont, BLACK, displaySurface, p3TauntFlags_x, p3TauntFlags_y)
			
			drawText("Defending?:".format(player.getTurnMeter(),"1000"), buttonFont, BLACK, displaySurface, p3DefendFlagWords_x, p3DefendFlagWords_y)
			drawText("{0}".format(player.checkDefenseFlag()), buttonFont, BLACK, displaySurface, p3DefendFlags_x, p3DefendFlags_y)
			pygame.display.update()
		elif player == p4:
			drawText("Health: {0}/{1}".format(player.getHealth(), player.getMaxHealth()), buttonFont, BLACK, displaySurface, p4Health_x, p4Health_y)
			drawText("TM: {0}/{1}".format(player.getTurnMeter(),"1000"), buttonFont, BLACK, displaySurface, p4TM_x, p4TM_y)
			
			drawText("Taunting?:", buttonFont, BLACK, displaySurface, p4TauntFlagWords_x, p4TauntFlagWords_y)
			drawText("{0}".format(player.checkTauntFlag()), buttonFont, BLACK, displaySurface, p4TauntFlags_x, p4TauntFlags_y)
			
			drawText("Defending?:".format(player.getTurnMeter(),"1000"), buttonFont, BLACK, displaySurface, p4DefendFlagWords_x, p4DefendFlagWords_y)
			drawText("{0}".format(player.checkDefenseFlag()), buttonFont, BLACK, displaySurface, p4DefendFlags_x, p4DefendFlags_y)
			pygame.display.update()
		elif player == p5:
			drawText("Health: {0}/{1}".format(player.getHealth(), player.getMaxHealth()), buttonFont, BLACK, displaySurface, p5Health_x, p5Health_y)
			drawText("TM: {0}/{1}".format(player.getTurnMeter(),"1000"), buttonFont, BLACK, displaySurface, p5TM_x, p5TM_y)
			
			drawText("Taunting?:", buttonFont, BLACK, displaySurface,p5TauntFlagWords_x, p5TauntFlagWords_y)
			drawText("{0}".format(player.checkTauntFlag()), buttonFont, BLACK, displaySurface, p5TauntFlags_x, p5TauntFlags_y)
			
			drawText("Defending?:".format(player.getTurnMeter(),"1000"), buttonFont, BLACK, displaySurface, p5DefendFlagWords_x, p5DefendFlagWords_y)
			drawText("{0}".format(player.checkDefenseFlag()), buttonFont, BLACK, displaySurface, p5DefendFlags_x, p5DefendFlags_y)
			pygame.display.update()
		elif player == p6:
			drawText("Health: {0}/{1}".format(player.getHealth(), player.getMaxHealth()), buttonFont, BLACK, displaySurface, p6Health_x, p6Health_y)
			drawText("TM: {0}/{1}".format(player.getTurnMeter(),"1000"), buttonFont, BLACK, displaySurface, p6TM_x, p6TM_y)
			
			drawText("Taunting?:", buttonFont, BLACK, displaySurface,p6TauntFlagWords_x, p6TauntFlagWords_y)
			drawText("{0}".format(player.checkTauntFlag()), buttonFont, BLACK, displaySurface, p6TauntFlags_x, p6TauntFlags_y)
			
			drawText("Defending?:".format(player.getTurnMeter(),"1000"), buttonFont, BLACK, displaySurface, p6DefendFlagWords_x, p6DefendFlagWords_y)
			drawText("{0}".format(player.checkDefenseFlag()), buttonFont, BLACK, displaySurface, p6DefendFlags_x, p6DefendFlags_y)
			pygame.display.update()
			
	return
	
#later needs to update to loading screen; now loads TM, and loads first character to screen
def pressKeyToLoad():
	global startScreenFlag, healerImage
	while startScreenFlag == True:
		for event in pygame.event.get():
			if event.type == QUIT:
				startScreenFlag = False
				terminate()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE: # pressing escape quits
					startScreenFlag = False
					terminate()
				if event.key == ord('l'): #gotta "GO"toStartScreen, then from there buttons will update stuff
					startScreenFlag = False
					TMEngine(getEList(), getFList())
					# playScreenFlag = True
					# print("playscreenflag in key to load: ", playScreenFlag)
					updatePlayScreen("{0} goes first! Click a picture/target then select an action!".format(
							getWinner().getName()))
					
#gotta make stuff show up: start screen has a load button on it, 
###load screen lets you choose what charactesr to load eventually,
def goToStartScreen():
	global startScreenFlag
	startScreenFlag = True
	displaySurface.fill(BLACK)
	drawText('Fighter\'s Simulator!', titleFont, WHITE, displaySurface, m.floor(WINDOWWIDTH / 2), m.floor(WINDOWHEIGHT / 2))
	drawText('Press L to load characters!', instructionFont, WHITE, displaySurface, 
				m.floor(WINDOWWIDTH / 2), m.floor(WINDOWHEIGHT / 2) + 50)
	pygame.display.update()
	pressKeyToLoad()
	return	

def updateTarget():
	global targetObj, playScreenFlag
	# print("made it into updateTarget")
	# print("playscreenflag in update target pre if: ", playScreenFlag)
	# if playScreenFlag == True:
		# playScreenFlag = False
	# print("playscreenflag in update target post if: ", playScreenFlag)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			terminate()
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE: # pressing escape quits
				terminate()
		#select p1
		if event.type == KEYDOWN:# or 
			if event.key == K_1:# or 
				if targetObj != p1:
					targetObj = p1
				print("target name: {0}".format(targetObj.getName()))
				print("k1 pressed")
				updatePlayScreen("{0} is taking a turn against {1}!".format(getWinner().getName(),targetObj.getName()))
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if p1Obj['rect'].collidepoint(event.pos):
				if targetObj != p1:
					targetObj = p1
				print("target name: {0}".format(targetObj.getName()))
				print("p1 clicked")
				updatePlayScreen("{0} is taking a turn against {1}!".format(getWinner().getName(),targetObj.getName()))
	# # for event in pygame.event.get():
            # # if event.type == pygame.QUIT:
                # # return
            # # elif event.type == pygame.MOUSEBUTTONDOWN:
                # # # If the left button is clicked we switch to the 'left_scene'
                # # # in the `current_scene` dictionary.
                # # if left_button.collidepoint(event.pos):
                    # # current_scene = states[current_scene['left_scene']]
                    # # print(current_scene)
                # # # If the right button is clicked we switch to the 'right_scene'.
                # # elif right_button.collidepoint(event.pos):
                    # # current_scene = states[current_scene['right_scene']]
                    # # print(current_scene)
					
					
def updatePlayScreen(textDisplay): #updates play screen text and buttons for each toon to go
	global playScreenFlag, charDisplayLeft, charDisplayTop, button11Left, button11Top, atkButton, charDisplayRect, targetObj
	# print("playscreenflag in updateplay screen pre if: ", playScreenFlag)
	if playScreenFlag == False:
		playScreenFlag = True
	# print("playscreenflag in updateplay screen post if: ", playScreenFlag)
	displaySurface.fill(BLACK) #clears screen to refill
	pygame.draw.rect(displaySurface, WHITE, charDisplayRect)#makes play square
	drawText(textDisplay,
		instructionFont, WHITE, displaySurface, playScreenInstructionsX, playScreenInstructionsY) 
	# #make default buttons went here. loading works fine, but if it breaks replace them here
	if portraitsMadeFlag == False:
		print("portraitsMADE FLAG, in if, before update =", portraitsMadeFlag)
		updateCharPortraits(getEList(), getFList())#update pic-buttons
		print("portraitsMADE FLAG, in if, after update =", portraitsMadeFlag)
	else:
		print("updating portraits part2")
		updateCharPortraits2()
	updateCharText()#update status texts
	print("portraitsMADE FLAG, out of if =", portraitsMadeFlag)
	updateButtons() # update buttons based on what class is going
	# updateTarget()
	
	pygame.display.update()
	
#method for shaking player characters when hit
#method for moving player characters forward when attacking/selected
	
###then battle screen has a place for characters to appear(check the catanimation program), choose actions from buttons(check out ink spill buttons), then update their health, turn meter, in bars probably
###can have symbols appear next to character if they are defending
###have icons shake when hit, move when performing action
def game_Loop():
	goToStartScreen()
	# print("outside while")
	i = 0
	while playScreenFlag:
		# i +=1
		# print("inside while: ", i)
		updateTarget()
		# while not playScreenFlag: 
			# time.sleep(1)
			
			
game_Loop()
