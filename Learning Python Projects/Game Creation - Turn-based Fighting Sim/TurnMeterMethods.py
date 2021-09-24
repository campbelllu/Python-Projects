import tkinter as tk
import random as rand
import math as m
import queue as Q #.put() goes in, .get() goes out
from Character_Master import *
from listGenerator import *

TMRemoved = 0
TMGained = 0
TMChar = Q.Queue()
### queues: .get(), .put(), .qsize()
TMCharList = []
TMFlag = False
# turnTaker = None
winnerChosenFlag = False #currently unused
manyWinnersFlag = False #seems unused after size comparison used instead
winner = None


######FIRST AND FOREMOST! gotta let the first turn goer go first, THEN start filling up TMChar with the new tiebreaker!




def getWinner():
	return winner
def setWinner(winrar):
	winner = winrar
def addToTMChar(person):
	TMChar.put(person)
def getTMChar():
	return TMChar
def getTMCharSpecific(num): #unused as tmchar is now queue, not list
	return TMChar[num]
def resetTMChar(): #unused directly
	TMChar = []
def getTMFlag():
	return TMFlag	
def setTMFlag():
	TMFlag = True
def cancelTMFlag():
	TMFlag = False	
def getManyWinnersFlag():
	return manyWinnersFlag 
def setManyWinnersFlag():
	manyWinnersFlag = True
def cancelManyWinnersFlag():
	manyWinnersFlag = False

"""need to get rid of testing lines in tMC()"""
def findFirstTurnTaker(eList, fList): #returns the first action taker to the program. used once upon starting up
	highest = 0
	turnTaker = None
	for char in eList:
		if char.getSpeed() > highest:
			highest = char.getSpeed()
			turnTaker = char
	for char in fList:
		if char.getSpeed() > highest:
			highest = char.getSpeed()
			turnTaker = char
	return turnTaker

def addTurnMeterToTeam(charList): #add to team's TM
	for char in charList:
		if char.getStatus() == "Alive": #leaves out any unconscious or dead players
			char.addTurnMeter(char.getSpeed())

def tieBreaker(TheList): #compares stats of any tying characters, puts winners in TMChar-queue, to be used by other programs
	global TMChar
	global TMFlag
	global manyWinnersFlag
	difference = 0
	smallestDifference = 5000
	turnTaker = None
	statBreaker = 0
	numBreaker = rand.randrange(1,1200,1)
	for char in TheList: #check list for lucky winner
		statBreaker = m.floor((char.getSpeed() + char.getAccuracy() + char.getPower()) / 3)
		difference = m.fabs(statBreaker-numBreaker)
		if difference < smallestDifference:
			smallestDifference = difference
			turnTaker = char
	TMChar.put(turnTaker)
	turnTaker.assignTurnMeter(0)
	if turnTaker in TheList: #threw an error, so if prevents it, but might need reverting if i squash this bug!
		TheList.remove(turnTaker)

def turnMeterChecker(charList1, charList2): #check everyone's TM, flips TMflag if someone gets added
	global TMCharList
	global TMFlag
	for char in charList1:
		if char.getStatus() == "Alive": #leaves out any unconscious or dead players
			if char.getTurnMeter() == 1000:
				TMCharList.append(char)#adds TM winner to TMChar list addToTMChar(char)
				if TMFlag == False: #flip it
					TMFlag = True
	for char in charList2:
		if char.getStatus() == "Alive": #leaves out any unconscious or dead players
			if char.getTurnMeter() == 1000:
				TMCharList.append(char) #adds TM winner to TMChar list addToTMChar(char)
				if TMFlag == False: #flip it
					TMFlag = True

def defineWinner(): #pulls a winner out of TMChar, eventually flips flag back to null to generate more TM
	global TMChar
	global TMCharList
	global TMFlag
	global manyWinnersFlag
	global winner
	
	if TMChar.qsize() > 0:
		winner = TMChar.get()
		if TMChar.qsize() > 0:#to catch any non-flag when it needs to be flagged after winner assigned
			if TMFlag == False: 
				TMFlag = True
	if TMChar.qsize() == 0:
		if TMFlag == True:
			TMFlag = False
		if manyWinnersFlag == True:
			manyWinnersFlag = False
			

def TMEngine(eList, fList): #checks all char's TM, adds TM to teams until turn takers join TMChar
	global TMCharList
	global TMFlag
	while TMFlag == False:#see if the lists contain winners
		turnMeterChecker(eList,fList)
		if TMFlag == False:#they didn't have winners, so do this
			addTurnMeterToTeam(eList)
			addTurnMeterToTeam(fList)
			turnMeterChecker(eList,fList)
	while len(TMCharList) > 0:
		tieBreaker(TMCharList)
	if TMFlag == True:
		defineWinner()