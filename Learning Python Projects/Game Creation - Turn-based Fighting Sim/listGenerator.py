import math as m
import random as rand
from Character_Master import *

"""ListGenerator can have characters hard coded in, or could draw and save to a database or file storage system. Either way, the GUI's load button calls upon the getE-FList's, so all pulling can be done here in this file."""
#instantiate cheat code
#z = Character("Tank1", "Tank",1,5,2,5,3,5)
#name, role, level, speed, health, power, accuracy, defense

eList = [Character("Sixth", "Attacker",1,0,200,4,31,0), Character("Fifth", "Attacker",1,0,200,6,52,3), Character("Fourth", "Attacker",1,0,200,8,25,7)]
fList = [Character("Third", "Attacker",1,0,200,5,32,5), Character("Second", "Attacker",1,799,200,7,58,3), Character("First", "Attacker",1,799,200,9,20,5)]
def levelUp(list):
	for char in list:
		char.customLevelUp(29, 10, 2, 3, 2, 3)

# levelUp(eList)

# deadTom = Character("dead tom", "Tank",1,111,200,5,30,0)
# aliveGabe = Character("alive gabe", "Tank",1,111,300,5,30,0)
# print("health: {0}, status: {1}".format(deadTom.getHealth(),deadTom.getStatus()))
# deadTom.assignHealth(-200)
# print("health: {0}, status: {1}".format(deadTom.getHealth(),deadTom.getStatus()))
# deadTom.updateStatus()
# print("health: {0}, status: {1}".format(deadTom.getHealth(),deadTom.getStatus()))

# print("health: {0}, status: {1}".format(aliveGabe.getHealth(),aliveGabe.getStatus()))
# aliveGabe.assignHealth(-3)
# print("health: {0}, status: {1}".format(aliveGabe.getHealth(),aliveGabe.getStatus()))
# aliveGabe.updateStatus()
# print("health: {0}, status: {1}".format(aliveGabe.getHealth(),aliveGabe.getStatus()))
# print("health: {0}, status: {1}".format(deadTom.getHealth(),deadTom.getStatus()))
# john = Character("john", "Tank",1,111,2,5,3,5)
# eList.append(john)
# print(john in eList)
# eListUpdated = levelUp(eList)
# fListUpdated = levelUp(fList)


def getEList():
#spaghetti method in fillGUI, may need updating later
	return eList
	
def getFList():
	return fList
	
	
	
	# eList = [Character("Tank1", "Tank",1,5,2,5,3,5), Character("Fighter1", "Attacker",1,5,2,5,5,3), Character("Healer1", "Healer",1,5,2,5,3,5)]
# fList = [Character("Tank11", "Tank",1,5,2,5,3,5), Character("Fighter11", "Attacker",1,5,2,5,5,3), Character("Tank22", "Tank",1,5,2,5,3,5)]
# eListUpdated =[]
# fListUpdated = []