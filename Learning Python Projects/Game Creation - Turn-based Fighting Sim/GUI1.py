import tkinter as tk
import random as rand
import time as time
import queue as Q #.put() goes in, .get() goes out
from Character_Master import *
from listGenerator import *
from TurnMeterMethods import *

# documentation: https://drive.google.com/open?id=1bCMLm2fdisvO7qNyi9IsecJZRNDPs0RkCc0POEYYj-w

gameRunningFlag = False #attached to load data/update GUI button
takeActionButtonPressed = False
previousWinnerDefined = False
damageNumber = 0
tmChange = 0
actionSelection = ""
turnTaker = getWinner()#unused?
previousWinner = "" #Q.queue
### queues: .get(), .put(), .qsize()

#instance
window = tk.Tk()
#title the window
window.title("Fighters GUI")
#scroll bar 
# scrollbar = tk.Scrollbar(window)
# scrollbar.config(command=listbox.yview)
# scrollbar.grid(column=3, row=0, rowspan=3)
#sizes the window
#window.geometry("800x500")
#elements creations
display1Label = tk.Label(window, text="Hostile Targets")
display2Label = tk.Label(window, text="Friendly Targets")
statusDisplay1 = tk.Text(master=window, height=6, width=154)
statusDisplay2 = tk.Text(master=window, height=6, width=154)
statusDisplay1.configure(state='disabled')
statusDisplay2.configure(state='disabled')
actionDisplayLabel = tk.Label(window, text="Clicking Take Action! \nWill perform the following:")# \nUpdate by pressing action buttons.")
actionDisplay = tk.Text(master=window, height=2, width = 154)
actionDisplay.configure(state='disabled')
targetButtonsLabel = tk.Label(window, text="Choose Your Target")
targetSelection = tk.StringVar() #.get() returns selected RB's value
tarButtonEnemy1 = tk.Radiobutton(window, text = "enemy1", variable = targetSelection, value = 0, indicator = 0, background = "pink")
tarButtonEnemy2 = tk.Radiobutton(window, text = "enemy2", variable = targetSelection, value = 1, indicator = 0, background = "pink")
tarButtonEnemy3 = tk.Radiobutton(window, text = "enemy3", variable = targetSelection, value = 2, indicator = 0, background = "pink")
tarButtonFriend1 = tk.Radiobutton(window, text = "friend1", variable = targetSelection, value = 3, indicator = 0, background = "light blue")
tarButtonFriend2 = tk.Radiobutton(window, text = "friend2", variable = targetSelection, value = 4, indicator = 0, background = "light blue")
tarButtonFriend3 = tk.Radiobutton(window, text = "friend3", variable = targetSelection, value = 5, indicator = 0, background = "light blue")
chooseActionLabel = tk.Label(window, text="Choose an Action")
commonActionsLabel = tk.Label(window, text="Common Actions")

#action buttons
def updateActionDisplay(message):
	actionDisplay.configure(state='normal')
	actionDisplay.delete('1.0', tk.END)
	actionDisplay.tag_config("center", justify = tk.CENTER)
	actionDisplay.insert('end', message, 'center')
	actionDisplay.configure(state='disabled')
def actionAttack(): # WORKS!
	global actionSelection
	global takeActionButtonPressed
	global previousWinnerDefined
	global previousWinner
	actionSelection = "an attack"
	target = defineTarget(getEList(), getFList())
	previousWinner = getWinner() #.getName()
	previousWinnerDefined = True
	if takeActionButtonPressed == True:
		takeActionButtonPressed = False
	if target == None:
		updateActionDisplay("You must select a target!")
	else:
		updateActionDisplay("{0} will be performing {1} on {2}!".format(getWinner().getName(), actionSelection, target.getName()))
	# if getTMFlag() == False: #catch-all
		# TMEngine(getEList(), getFList())
def actionDefend():
	global actionSelection
	global takeActionButtonPressed
	global previousWinnerDefined
	global previousWinner
	actionSelection = "defending"
	target = defineTarget(getEList(), getFList())
	previousWinner = getWinner()
	previousWinnerDefined = True
	if takeActionButtonPressed == True:
		takeActionButtonPressed = False
	if target == None:
		updateActionDisplay("You must select a target!")
	else:
		updateActionDisplay("{0} will be performing {1} on {2}!".format(getWinner().getName(), actionSelection, target.getName()))
	# if getTMFlag() == False:
		# TMEngine(getEList(), getFList())
def actionFrenzy():
	global actionSelection
	global takeActionButtonPressed
	global previousWinnerDefined
	global previousWinner
	actionSelection = "frenzying"
	target = defineTarget(getEList(), getFList())
	previousWinner = getWinner()
	previousWinnerDefined = True
	if takeActionButtonPressed == True:
		takeActionButtonPressed = False
	if target == None:
		updateActionDisplay("You must select a target!")
	else:
		updateActionDisplay("{0} will be performing {1} on {2}!".format(getWinner().getName(), actionSelection, target.getName()))
	# if getTMFlag() == False:
		# TMEngine(getEList(), getFList())
def actionFlourish():
	global actionSelection
	global takeActionButtonPressed
	global previousWinnerDefined
	global previousWinner
	actionSelection = "flourishing"
	target = defineTarget(getEList(), getFList())
	previousWinner = getWinner()
	previousWinnerDefined = True
	if takeActionButtonPressed == True:
		takeActionButtonPressed = False
	if target == None:
		updateActionDisplay("You must select a target!")
	else:
		updateActionDisplay("{0} will be performing {1} on {2}!".format(getWinner().getName(), actionSelection, target.getName()))
	# if getTMFlag() == False:
		# TMEngine(getEList(), getFList())
def actiondelay():
	global actionSelection
	global takeActionButtonPressed
	global previousWinnerDefined
	global previousWinner
	actionSelection = "delaying"
	target = defineTarget(getEList(), getFList())
	previousWinner = getWinner()
	previousWinnerDefined = True
	if takeActionButtonPressed == True:
		takeActionButtonPressed = False
	if target == None:
		updateActionDisplay("You must select a target!")
	else:
		updateActionDisplay("{0} will be performing {1} on {2}!".format(getWinner().getName(), actionSelection, target.getName()))
	# if getTMFlag() == False:
		# TMEngine(getEList(), getFList())
def actionSHeal():
	global actionSelection
	global takeActionButtonPressed
	global previousWinnerDefined
	global previousWinner
	actionSelection = "small heal"
	target = defineTarget(getEList(), getFList())
	previousWinner = getWinner()
	previousWinnerDefined = True
	if takeActionButtonPressed == True:
		takeActionButtonPressed = False
	if target == None:
		updateActionDisplay("You must select a target!")
	else:
		updateActionDisplay("{0} will be performing {1} on {2}!".format(getWinner().getName(), actionSelection, target.getName()))
	# if getTMFlag() == False:
		# TMEngine(getEList(), getFList())
def actionMHeal():
	global actionSelection
	global takeActionButtonPressed
	global previousWinnerDefined
	global previousWinner
	actionSelection = "mega heal"
	target = defineTarget(getEList(), getFList())
	previousWinner = getWinner()
	previousWinnerDefined = True
	if takeActionButtonPressed == True:
		takeActionButtonPressed = False
	if target == None:
		updateActionDisplay("You must select a target!")
	else:
		updateActionDisplay("{0} will be performing {1} on {2}!".format(getWinner().getName(), actionSelection, target.getName()))
	# if getTMFlag() == False:
		# TMEngine(getEList(), getFList())
def actionTaunt():
	global actionSelection
	global takeActionButtonPressed
	global previousWinnerDefined
	global previousWinner
	actionSelection = "taunt"
	target = defineTarget(getEList(), getFList())
	previousWinner = getWinner() #.getName()
	previousWinnerDefined = True
	print("in actionTaunt(), previousWinner pre button reassign:", previousWinner.getName())
	print("in actionTaunt(), Winner pre button reassign:", getWinner().getName())
	
	print("in actionTaunt(), previousWinner post button reassign:", previousWinner.getName())
	print("in actionTaunt(), Winner post button reassign:", getWinner().getName())
	if takeActionButtonPressed == True:
		takeActionButtonPressed = False
	if target == None:
		updateActionDisplay("You must select a target!")
	else:
		updateActionDisplay("{0} will be performing {1} on {2}!".format(getWinner().getName(), actionSelection, target.getName()))
	# if getTMFlag() == False:
		# TMEngine(getEList(), getFList())
def actionRally():
	global actionSelection
	global takeActionButtonPressed
	global previousWinnerDefined
	global previousWinner
	actionSelection = "rally"
	target = defineTarget(getEList(), getFList())
	previousWinner = getWinner()
	previousWinnerDefined = True
	if takeActionButtonPressed == True:
		takeActionButtonPressed = False
	if target == None:
		updateActionDisplay("You must select a target!")
	else:
		updateActionDisplay("{0} will be performing {1} on {2}!".format(getWinner().getName(), actionSelection, target.getName()))
	# if getTMFlag() == False:
		# TMEngine(getEList(), getFList())
#useful functions
def characterStatus(charList): #returns string of character statuses
	strang = ""
	for char in charList:
		char.updateStatus() #catch all
		stats = "{0}, Role: {1}, Health: {2}/{3}, Status: {4}, Turn Meter: {5}/1000, Defending?: {6}, Taunting?: {7}".format(char.getName(), char.getRole(), char.getHealth(), char.getMaxHealth(), char.getStatus(), char.getTurnMeter(), char.checkDefenseFlag(), char.checkTauntFlag())
		strang +=  stats + "\n"
	return strang
def statusTextUpdate(enemyList, friendList): #update status textboxes up top with character statuses
	#unlock textboxes
	statusDisplay1.configure(state='normal')
	statusDisplay2.configure(state='normal')
	#post new character statuses after wiping old status display
	statusDisplay1.delete('1.0', tk.END)
	statusDisplay2.delete('1.0', tk.END)
	statusDisplay1.insert('end', characterStatus(enemyList))
	statusDisplay2.insert('end', characterStatus(friendList))
	#lock textboxes
	statusDisplay1.configure(state='disabled')
	statusDisplay2.configure(state='disabled')
def radioButtonUpdate(enemyList, friendList): #update radiobuttons
	tarButtonEnemy1.configure(text = enemyList[0].getName(), value = enemyList[0].getName())
	tarButtonEnemy2.configure(text = enemyList[1].getName(), value = enemyList[1].getName())
	tarButtonEnemy3.configure(text = enemyList[2].getName(), value = enemyList[2].getName())
		
	tarButtonFriend1.configure(text = friendList[0].getName(), value = friendList[0].getName())
	tarButtonFriend2.configure(text = friendList[1].getName(), value = friendList[1].getName())
	tarButtonFriend3.configure(text = friendList[2].getName(), value = friendList[2].getName())
#makes action buttons unavailable depending on character class/role
def actionButtonDeactivation(character):
	#changes button color and selectability based on role; determine role
	if character == "Empty":
		sHealButton.configure(background = "black", state = 'disabled')
		mHealButton.configure(background = "black", state = 'disabled')
		tauntButton.configure(background = "black", state = 'disabled')
		rallyButton.configure(background = "black", state = 'disabled')
		delayButton.configure(background = "black", state = 'disabled')
		flourishButton.configure(background = "black", state = 'disabled')
		attackButton.configure(background = "black", state = 'disabled')
		defendButton.configure(background = "black", state = 'disabled')
		frenzyButton.configure(background = "black", state = 'disabled')
	elif character != "Empty":
		if character.getRole() == "Attacker":
			sHealButton.configure(background = "black", state = 'disabled')
			mHealButton.configure(background = "black", state = 'disabled')
			tauntButton.configure(background = "black", state = 'disabled')
			rallyButton.configure(background = "black", state = 'disabled')
		if character.getRole() == "Healer" and character != "Empty":
			delayButton.configure(background = "black", state = 'disabled')
			flourishButton.configure(background = "black", state = 'disabled')
			tauntButton.configure(background = "black", state = 'disabled')
			rallyButton.configure(background = "black", state = 'disabled')
		if character.getRole() == "Tank" and character != "Empty":
			delayButton.configure(background = "black", state = 'disabled')
			flourishButton.configure(background = "black", state = 'disabled')
			sHealButton.configure(background = "black", state = 'disabled')
			mHealButton.configure(background = "black", state = 'disabled')
		if character.checkTauntFlag() == True and character != "Empty":
			tauntButton.configure(background = "black", state = 'disabled')
		if character.getHealth() <= (0.25*character.getMaxHealth()) and character != "Empty":
			mHealButton.configure(background = "black", state = 'disabled')
def defineTarget(eList, fList): #gets target from targetselection button
	if targetSelection.get() == None:
		return None
	else:
		for char in eList:
			if targetSelection.get() == char.getName():
				return char
		for char in fList:
			if targetSelection.get() == char.getName():
				return char
def getAction():
	return actionSelection
def actionButtonReset(): #might need to add in reset of command
	if attackButton['state'] == "disabled":
		attackButton.configure(background = "light green", state = 'normal')
	if frenzyButton['state'] == "disabled":
		frenzyButton.configure(background = "light green", state = 'normal')
	if defendButton['state'] == "disabled":
		defendButton.configure(background = "light green", state = 'normal')
	if delayButton['state'] == "disabled":
		delayButton.configure(background = "light green", state = 'normal')
	if flourishButton['state'] == "disabled":
		flourishButton.configure(background = "light green", state = 'normal')
	if sHealButton['state'] == "disabled":
		sHealButton.configure(background = "light green", state = 'normal')
	if mHealButton['state'] == "disabled":
		mHealButton.configure(background = "light green", state = 'normal')
	if tauntButton['state'] == "disabled":
		tauntButton.configure(background = "light green", state = 'normal')
	if rallyButton['state'] == "disabled":
		rallyButton.configure(background = "light green", state = 'normal') #BoutonLancer['command'] = noPlot

def fillGUI(): #currently used in upload button
	global gameRunningFlag
	if gameRunningFlag == False:
		gameRunningFlag = True
		statusTextUpdate(getEList(), getFList())
		radioButtonUpdate(getEList(), getFList())
		TMEngine(getEList(), getFList()) #might need updating as we update saving/loading/database/files
		updateActionDisplay("{0} goes first! \nChoose your target and action!".format(getWinner().getName()))
		actionButtonDeactivation(getWinner())
	else:
		pass
		
def quitGame():
	global gameRunningFlag
	if gameRunningFlag == True:
		gameRunningFlag = False
		updateActionDisplay("Goodbye.")
	else:
		pass

#listener
# if targetSelection.get() != None:
	# actionButtonDeactivation(getWinner())

def takeAction(event = None): #updates status and health of attacker and defender
	global winner
	global previousWinner
	global damageNumber
	global tmChange
	global takeActionButtonPressed
	global previousWinnerDefined
	target = defineTarget(getEList(), getFList())
	if previousWinner != None:
		print("in takeAction(), previousWinner:", previousWinner.getName())
	print("in takeAction(), Winner:", getWinner().getName())
	window.bind_all('s', takeAction) #holy shit keybindings work!
	
	if getTMFlag() == True and previousWinnerDefined == True and takeActionButtonPressed == False: #gotta pull the next winner 
		# print("gui, tmflag=true, iterating definewinners")
		defineWinner() #get the next winner from TMChar queue
	elif getTMFlag() == False and previousWinnerDefined == True and takeActionButtonPressed == False: #or make it
		print("gui, tmflag=false, engaging TMEngine again")
		TMEngine(getEList(), getFList())
	
	if getAction() == "an attack" and takeActionButtonPressed == False:
		if previousWinner.checkDefenseFlag() == True: #cancel defense flag on a non-defense action
			previousWinner.negateDefenseFlag()
		damageNumber = getWinner().attack(target)
		target.assignHealth(target.getHealth()-damageNumber) #deal dmg to target
		target.updateStatus() #now health and status are updated
		if target.checkDefenseFlag() == True:
			getWinner().assignHealth(getWinner().getHealth() - (0.05 * damageNumber))
			getWinner().updateStatus()
		takeActionButtonPressed = True
	elif getAction() == "defending" and takeActionButtonPressed == False:
		damageNumber  = getWinner().defend(target)
		target.assignHealth(target.getHealth()-damageNumber)
		target.updateStatus() #now health and status are updated
		if target.checkDefenseFlag() == True:
			getWinner().assignHealth(getWinner().getHealth() - (0.05 * damageNumber))
			getWinner().updateStatus()
		takeActionButtonPressed = True
	elif getAction() == "frenzying" and takeActionButtonPressed == False:
		if previousWinner.checkDefenseFlag() == True: #cancel defense flag on a non-defense action
			previousWinner.negateDefenseFlag()
		wasTargetDefendingBeforeFrenzy = target.checkDefenseFlag() #check for defense flag on target, special for frenzy's dispel
		damageNumber  = getWinner().frenzy(target)
		target.assignHealth(target.getHealth()-damageNumber)
		target.updateStatus() #now health and status are updated
		if wasTargetDefendingBeforeFrenzy == True:
			getWinner().assignHealth(getWinner().getHealth() - (0.05 * damageNumber))
			getWinner().updateStatus()
		takeActionButtonPressed = True
	elif getAction() == "flourishing" and takeActionButtonPressed == False:
		if previousWinner.checkDefenseFlag() == True: #cancel defense flag on a non-defense action
			previousWinner.negateDefenseFlag()
		tmChange = getWinner().flourish()
		if getWinner() in getEList(): #which team to take TM from?
			for char in getFList():
				if char.getStatus() == "Alive": #update TM
					char.removeTurnMeter(tmChange)
					char.updateStatus()
				if char.checkDefenseFlag() == True:
					getWinner().removeTurnMeter(0.05 * tmChange)
					getWinner().updateStatus()
		elif getWinner() in getFList():#which team to take TM from?
			for char in getEList():
				if char.getStatus() == "Alive": #update TM
					char.removeTurnMeter(tmChange)
					char.updateStatus()
				if char.checkDefenseFlag() == True:
					getWinner().removeTurnMeter(0.05 * tmChange)
					getWinner().updateStatus()
		takeActionButtonPressed = True
	elif getAction() == "delaying" and takeActionButtonPressed == False:
		if previousWinner.checkDefenseFlag() == True: #cancel defense flag on a non-defense action
			previousWinner.negateDefenseFlag()
		tmChange = getWinner().delay(target)
		target.removeTurnMeter(tmChange)
		target.updateStatus()
		if target.checkDefenseFlag() == True:
			getWinner().removeTurnMeter(0.05 * tmChange)
			getWinner().updateStatus()
		takeActionButtonPressed = True
	elif getAction() == "small heal" and takeActionButtonPressed == False:
		if previousWinner.checkDefenseFlag() == True: #cancel defense flag on a non-defense action
			previousWinner.negateDefenseFlag()
		getWinner().sHeal(target)
		takeActionButtonPressed = True
	elif getAction() == "mega heal" and takeActionButtonPressed == False:
		if previousWinner.checkDefenseFlag() == True: #cancel defense flag on a non-defense action
			previousWinner.negateDefenseFlag()
		getWinner().mHeal(target)
		takeActionButtonPressed = True
	elif getAction() == "taunt" and takeActionButtonPressed == False:
		if previousWinner.checkDefenseFlag() == True: #cancel defense flag on a non-defense action
			previousWinner.negateDefenseFlag() #redundant, as taunting again, but consistent in code to update stats
		damageNumber = getWinner().taunt(target)
		target.assignHealth(target.getHealth()-damageNumber) #deal dmg to target
		target.updateStatus() #now health and status are updated
		previousWinner.updateStatus()#taunt heals self, so gotta update self status too!
		if target.checkDefenseFlag() == True: 
			previousWinner.assignHealth(getWinner().getHealth() - (0.05 * damageNumber))
			previousWinner.updateStatus()
		takeActionButtonPressed = True
	elif getAction() == "rally" and takeActionButtonPressed == False:
		if previousWinner.checkDefenseFlag() == True: #cancel defense flag on a non-defense action
			previousWinner.negateDefenseFlag()		
		if getWinner() in getEList(): #which team to take TM from?
			getWinner().rally(getFList(), getEList())
		elif getWinner() in getFList():#which team to take TM from?
			getWinner().rally(getEList(), getFList())
		for char in getEList():
			char.updateStatus()
		for char in getFList():
			char.updateStatus()
		takeActionButtonPressed = True
	
	if takeActionButtonPressed == True and previousWinnerDefined == False:
		actionButtonReset()
		updateActionDisplay("{0} goes next! \nChoose your next target and action!".format(getWinner().getName()))
		actionButtonDeactivation(getWinner())
	else:
		if damageNumber == 0:
			actionButtonReset()
			updateActionDisplay("{0} missed {1}, doing 0 damage.\n{2} goes next!".format(previousWinner.getName(), target.getName(), getWinner().getName()))
			actionButtonDeactivation(getWinner())
		else:
			actionButtonReset()
			updateActionDisplay("{0} hit {2}, doing {1} damage.\n{3} goes next!".format(previousWinner.getName(), damageNumber, target.getName(), getWinner().getName()))
			actionButtonDeactivation(getWinner())
	previousWinnerDefined = False
	statusTextUpdate(getEList(), getFList()) #every press makes sure that textboxes are updated	
		
#elements commands
attackButton = tk.Button(window, text="Attack!", background = "light green", command = actionAttack )#, command = lambda: p(obj)
defendButton = tk.Button(window, text="Defend!", background = "light green", command = actionDefend)#, command=CURRENT_CHAR.attack(target))
frenzyButton = tk.Button(window, text="Frenzy!", background = "light green", command = actionFrenzy)#, command=CURRENT_CHAR.attack(target))
attackerActionsLabel = tk.Label(window, text="Attacker Actions")
delayButton = tk.Button(window, text="Delay!", background = "light green", command = actiondelay)#, command=CURRENT_CHAR.attack(target))
flourishButton = tk.Button(window, text="Flourish!", background = "light green", command = actionFlourish)#, command=CURRENT_CHAR.attack(target))
healerActionsLabel = tk.Label(window, text="Healer Actions")
sHealButton = tk.Button(window, text="Small Heal!", background = "light green", command = actionSHeal)#, command=CURRENT_CHAR.attack(target))
mHealButton = tk.Button(window, text="Mega Heal!", background = "light green", command = actionMHeal)#, command=CURRENT_CHAR.attack(target)) 
tankActionsLabel = tk.Label(window, text="Tank Actions")
tauntButton = tk.Button(window, text="Taunt!", background = "light green", command = actionTaunt)#, command=CURRENT_CHAR.attack(target))
rallyButton = tk.Button(window, text="Rally!", background = "light green", command = actionRally)#, command=CURRENT_CHAR.attack(target))
takeActionButton = tk.Button(window, text="Take Action!", background = "black", fg = "white", command = takeAction)
#update UI button // upload data to UI button
uploadButton = tk.Button(window, text="Update!", background = "grey", fg = "white", command = fillGUI)

#elements placements
display1Label.grid(column=1, row=0)
statusDisplay1.grid(column=0, row=1, columnspan=3)
display2Label.grid(column=1, row=2)
statusDisplay2.grid(column=0, row=3, columnspan=3)

actionDisplayLabel.grid(column=1,row=4)
actionDisplay.grid(column=0, row=5, columnspan=3)
takeActionButton.grid(column=1,row=6)

targetButtonsLabel.grid(column=1, row=7)
tarButtonEnemy1.grid(column=0, row=6)
tarButtonEnemy2.grid(column=0, row=7)
tarButtonEnemy3.grid(column=0, row=8)
tarButtonFriend1.grid(column=2, row=6)
tarButtonFriend2.grid(column=2, row=7)
tarButtonFriend3.grid(column=2, row=8)

chooseActionLabel.grid(column=1, row=9)
commonActionsLabel.grid(column=1, row=10)
attackButton.grid(column=0, row=11)
defendButton.grid(column=1, row=11)
frenzyButton.grid(column=2, row=11)
attackerActionsLabel.grid(column=1, row=12)
delayButton.grid(column=0, row=13)
flourishButton.grid(column=1, row=13)
healerActionsLabel.grid(column=1, row=14)
sHealButton.grid(column=0, row=15)
mHealButton.grid(column=1, row=15)
tankActionsLabel.grid(column=1, row=16)
tauntButton.grid(column=0, row=17)
rallyButton.grid(column=1, row=17)

uploadButton.grid(column=1, row=20) #will probably become a loading data button
### reserves space for more loading and saving buttons
###
###
###spaces for action and turn buttons

#Run it
window.mainloop()

#unnecessary if importing wildcard
# def makeGUI():
	# return ""
# #tests!
# #test list
# enemyList12 = [Character("Tank1", "Tank",1,5,2,5,3,5), Character("Fighter1", "Attacker",1,5,2,5,5,3), Character("Healer1", "Healer",1,5,2,5,3,5)]
# enemyList13 = [Character("Tank11", "Tank",1,5,2,5,3,5), Character("Fighter11", "Attacker",1,5,2,5,5,3), Character("Tank22", "Tank",1,5,2,5,3,5)]
# actionButtonDeactivation(enemyList12[0])
# # actionButtonReset()
# actionButtonDefinition()
# textUpdate(enemyList12, enemyList12)
# radioButtonUpdate(enemyList12, enemyList12)
# print(actionSelection)