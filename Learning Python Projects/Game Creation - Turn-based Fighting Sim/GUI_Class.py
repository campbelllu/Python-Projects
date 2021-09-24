import tkinter as tk
import random as rand
from Character_Master import *

#top: text displays of character health, statuses, etc
#middle: radio buttons for who to target
#bottom: buttons for actions 
class GUI:
	"""creates a GUI upon demand!"""
	window = tk.Tk()
	#title the window
	window.title("Fighters GUI")
	display1Label = tk.Label()
	display2Label = tk.Label()
	statusDisplay1 = tk.Text()
	statusDisplay2 = tk.Text()
	targetButtonsLabel = tk.Label()
	tarButtonEnemy1 = tk.Radiobutton()
	tarButtonEnemy2 = tk.Radiobutton()
	tarButtonEnemy3 = tk.Radiobutton()
	tarButtonFriend1 = tk.Radiobutton()
	tarButtonFriend2 = tk.Radiobutton()
	tarButtonFriend3 = tk.Radiobutton()
	commonActionsLabel = tk.Label()
	#attack
	attackButton = tk.Button()
	defendButton = tk.Button()
	frenzyButton = tk.Button()
	attackerActionsLabel = tk.Label()
	msButton = tk.Button()
	flourishButton = tk.Button()
	healerActionsLabel = tk.Label()
	sHealButton = tk.Button()
	mHealButton = tk.Button() 
	tankActionsLabel = tk.Label()
	tauntButton = tk.Button()
	stunButton = tk.Button()
	window.update()
	#instance
	def actionAttack(self):
		self.actionSelection = "attack"
	def actionDefend(self):
		self.actionSelection = "defend"
	def actionFrenzy(self):
		self.actionSelection = "frenzy"
	def actionFlourish(self):
		self.actionSelection = "flourish"
	def actionMS(self):
		self.actionSelection = "multiStrike"
	def actionSHeal(self):
		self.actionSelection = "sHeal"
	def actionMHeal(self):
		self.actionSelection = "mHeal"
	def actionTaunt(self):
		self.actionSelection = "taunt"
	def actionStun():
		self.actionSelection = "stun"
	def __init__(self):
		
		#sizes the window
		#window.geometry("800x500")
		#top window textboxes display character statuses
		display1Label = tk.Label(self.window, text="Hostile Targets")
		display2Label = tk.Label(self.window, text="Friendly Targets")
		statusDisplay1 = tk.Text(master=self.window, height=7, width=60)
		statusDisplay2 = tk.Text(master=self.window, height=7, width=60)
		display1Label.grid(column=0, row=0)
		statusDisplay1.grid(column=0, row=1)
		display2Label.grid(column=2, row=0)
		statusDisplay2.grid(column=2, row=1)
		# statusDisplay1.configure(state='disabled')
		# statusDisplay2.configure(state='disabled')
		#choose your target label and buttons
		targetButtonsLabel = tk.Label(self.window, text="Choose Your Target")
		targetButtonsLabel.grid(column=1, row=3)
		targetSelection = tk.StringVar()
		tarButtonEnemy1 = tk.Radiobutton(self.window, text = "enemy1", variable = targetSelection, value = 0, indicator = 0, background = "pink")
		tarButtonEnemy2 = tk.Radiobutton(self.window, text = "enemy2", variable = targetSelection, value = 1, indicator = 0, background = "pink")
		tarButtonEnemy3 = tk.Radiobutton(self.window, text = "enemy3", variable = targetSelection, value = 2, indicator = 0, background = "pink")
		tarButtonFriend1 = tk.Radiobutton(self.window, text = "friend1", variable = targetSelection, value = 3, indicator = 0, background = "light blue")
		tarButtonFriend2 = tk.Radiobutton(self.window, text = "friend2", variable = targetSelection, value = 4, indicator = 0, background = "light blue")
		tarButtonFriend3 = tk.Radiobutton(self.window, text = "friend3", variable = targetSelection, value = 5, indicator = 0, background = "light blue")
		tarButtonEnemy1.grid(column=0, row=2)
		tarButtonEnemy2.grid(column=0, row=3)
		tarButtonEnemy3.grid(column=0, row=4)
		tarButtonFriend1.grid(column=2, row=2)
		tarButtonFriend2.grid(column=2, row=3)
		tarButtonFriend3.grid(column=2, row=4)
		#action buttons and labels available for each character
		# actionSelection = tk.StringVar() pretty sure this ain't a thing
		#gives program which button selection player chooses
		actionSelection = ""
		commonActionsLabel = tk.Label(self.window, text="Common Actions")
		commonActionsLabel.grid(column=1, row=5)
		#attack
		attackButton = tk.Button(self.window, text="Attack!", background = "light green", command = self.actionAttack)#, command=CURRENT_CHAR.attack(target)); command = lambda: p(obj)
		attackButton.grid(column=0, row=6)
		#defend
		defendButton = tk.Button(self.window, text="Defend!", background = "light green",command = self.actionDefend)#, command=CURRENT_CHAR.attack(target));; command = lambda: assignDamageDone(user, user.attack(target))
		defendButton.grid(column=1, row=6)
		#frenzy
		frenzyButton = tk.Button(self.window, text="Frenzy!", background = "light green",command=self.actionFrenzy)#, command=CURRENT_CHAR.attack(target))
		frenzyButton.grid(column=2, row=6)
		#attacker actions
		attackerActionsLabel = tk.Label(self.window, text="Attacker Actions")
		attackerActionsLabel.grid(column=1, row=7)
		#multi-strike
		msButton = tk.Button(self.window, text="Multi-Strike!", background = "light green",command = self.actionMS)#, command=CURRENT_CHAR.attack(target))
		msButton.grid(column=0, row=8)
		#flourish
		flourishButton = tk.Button(self.window, text="Flourish!", background = "light green",command = self.actionFlourish)#, command=CURRENT_CHAR.attack(target))
		flourishButton.grid(column=1, row=8)
		#healer actions
		healerActionsLabel = tk.Label(self.window, text="Healer Actions")
		healerActionsLabel.grid(column=1, row=9)
		#small heal
		sHealButton = tk.Button(self.window, text="Small Heal!", background = "light green",command = self.actionSHeal)#, command=CURRENT_CHAR.attack(target))
		sHealButton.grid(column=0, row=10)
		#mega heal
		mHealButton = tk.Button(self.window, text="Mega Heal!", background = "light green",command = self.actionMHeal)#, command=CURRENT_CHAR.attack(target)) 
		mHealButton.grid(column=1, row=10)
		#tank actions
		tankActionsLabel = tk.Label(self.window, text="Tank Actions")
		tankActionsLabel.grid(column=1, row=11)
		#taunt
		tauntButton = tk.Button(self.window, text="Taunt!", background = "light green",command = self.actionTaunt)#, command=CURRENT_CHAR.attack(target))
		tauntButton.grid(column=0, row=12)
		#stun
		stunButton = tk.Button(self.window, text="Stun!", background = "light green",command = self.actionStun)#, command=CURRENT_CHAR.attack(target))
		stunButton.grid(column=1, row=12)
	#assigns button functions based on who is doing what to whom

	#returns string of character statuses
	def characterStatus(self, charList):
		strang = ""
		print("character statusing")
		for char in charList:
			stats = "{0}, Role: {1}, Health: {2}/{3}, Status: {4}".format(char.getName(), char.getRole(), char.getHealth(), char.getMaxHealth(), char.getStatus())
			strang +=  stats + "\n"
		return strang

	#updates text displays of character statuses
	def textUpdate(self, enemyList, friendList):
		#unlock textboxes
		print("updating text")
		# self.statusDisplay1.configure(state='normal')
		# self.statusDisplay2.configure(state='normal')
		#post new character statuses; might have to wipe old status display
		self.statusDisplay1.insert(tk.END, self.characterStatus(enemyList))
		self.statusDisplay2.insert('end', self.characterStatus(friendList))
		#lock textboxes
		# self.statusDisplay1.configure(state='disabled')
		# self.statusDisplay2.configure(state='disabled')
	
	def radioButtonUpdate(self, enemyList, friendList):
		self.tarButtonEnemy1.configure(text = enemyList[0].getName())
		self.tarButtonEnemy2.configure(text = enemyList[1].getName())
		self.tarButtonEnemy3.configure(text = enemyList[2].getName())		
		self.tarButtonFriend1.configure(text = friendList[0].getName())
		self.tarButtonFriend2.configure(text = friendList[1].getName())
		self.tarButtonFriend3.configure(text = friendList[2].getName())

	def actionButtonDef(self):
		self.attackButton.configure(command = self.actionAttack)
		#defend
		self.defendButton.configure(command = self.actionDefend)
		#frenzy
		self.frenzyButton.configure(command = self.actionFrenzy)#, command=CURRENT_CHAR.attack(target))
		#multi-strike
		self.msButton.configure(command = self.actionMS)#, command=CURRENT_CHAR.attack(target))
		#flourish
		self.flourishButton.configure(command = self.actionFlourish)#, command=CURRENT_CHAR.attack(target))
		#small heal
		self.sHealButton.configure(command = self.actionSHeal)#, command=CURRENT_CHAR.attack(target))
		#mega heal
		self.mHealButton.configure(command = self.actionMHeal)#, command=CURRENT_CHAR.attack(target)) 
		#taunt
		self.tauntButton.configure(command = self.actionTaunt)#, command=CURRENT_CHAR.attack(target))
		#stun
		self.stunButton.configure(command = self.actionStun)#, command=CURRENT_CHAR.attack(target))
	#makes action buttons unavailable depending on character class/role
	def actionButtonDeactivation(self, character):
		#changes button color and selectability based on role; determine role
		if character.getRole() == "Attacker":
			self.sHealButton.configure(background = "black", state = 'disabled')
			self.mHealButton.configure(background = "black", state = 'disabled')
			self.tauntButton.configure(background = "black", state = 'disabled')
			self.stunButton.configure(background = "black", state = 'disabled')
		if character.getRole() == "Healer":
			self.msButton.configure(background = "black", state = 'disabled')
			self.flourishButton.configure(background = "black", state = 'disabled')
			self.tauntButton.configure(background = "black", state = 'disabled')
			self.stunButton.configure(background = "black", state = 'disabled')
		if character.getRole() == "Tank":
			self.msButton.configure(background = "black", state = 'disabled')
			self.flourishButton.configure(background = "black", state = 'disabled')
			self.sHealButton.configure(background = "black", state = 'disabled')
			self.mHealButton.configure(background = "black", state = 'disabled')
	
	#gets target from radio buttons
	def getTarget():
		return targetSelection.get()

	def actionButtonReset(self): #might need to add in reset of command
	# print(msButton['state'])
	# print(flourishButton['state'])
	# print(sHealButton['state'])
	# print(mHealButton['state'])
	# print(tauntButton['state'])
	# print(stunButton['state'])
		if msButton['state'] == "disabled":
			msButton.configure(background = "light green", state = 'normal')
		if flourishButton['state'] == "disabled":
			flourishButton.configure(background = "light green", state = 'normal')
		if sHealButton['state'] == "disabled":
			sHealButton.configure(background = "light green", state = 'normal')
		if mHealButton['state'] == "disabled":
			mHealButton.configure(background = "light green", state = 'normal')
		if tauntButton['state'] == "disabled":
			tauntButton.configure(background = "light green", state = 'normal')
		if stunButton['state'] == "disabled":
			stunButton.configure(background = "light green", state = 'normal') #BoutonLancer['command'] = noPlot

# textUpdate(enemyList12, enemyList12)
# radioButtonUpdate(enemyList12, enemyList12)
# radioButtonUpdate(enemyList13, enemyList13)
# actionButtonReset()

	def guiStart(self):
		self.window.mainloop()
		
	def guiUpdateBeginning(self, character, enemylist, friendlist):
		""" Updates GUI after taking lists of enemies and friends from main"""
		self.window.update()
		# eList = fillEnemyList(enemyList)
		# fList = fillFriendlyList(friendlist)
		self.textUpdate(enemylist,friendlist)
		self.radioButtonUpdate(enemylist,friendlist)
		# self.actionButtonDef()
		# self.actionButtonDeactivation(character)

	def guiUpdateEnd(self):
		self.actionButtonReset()
		self.actionSelection = ""
	
	def getAction(self):
		return actionSelection
	# def defineTarget():
		# target = getTarget()

#Run it
# window.mainloop()
# while True:
	# print(actionSelection)

#examples
#test list
	# enemyList12 = [Character("Tank1", "Tank",1,5,2,5,3,5), Character("Fighter1", "Attacker",1,5,2,5,5,3), Character("Healer1", "Healer",1,5,2,5,3,5)]
	# enemyList13 = [Character("Tank11", "Tank",1,5,2,5,3,5), Character("Fighter11", "Attacker",1,5,2,5,5,3), Character("Tank22", "Tank",1,5,2,5,3,5)]

	#main hands list of characters to GUI, GUI updates info for user to see
	#functions that fill dictionary with character info, return those lists
	# def fillEnemyList(self, charList):
		# enemyList = []
		# for chars in charList:
			# enemyList.append(chars)
		# return enemyList

	# def fillFriendlyList(self, charList):
		# friendlyList = []
		# for chars in charList:
			# friendlyList.append(chars)
		# return friendlyList
#top ---- needs formatting bruh
# deadEnemyName= "Dead Enemy"
# unconsciousEnemyName = "Unconscious Enemy"
# deadFriendName = "Dead Friend"
# unconsciousFriendName = "Unconscious Friend"
# nameDisplay = tk.Text(master=window) #height=16, width=60
# roleDisplay = tk.Text(master=window)
# healthDisplay = tk.Text(master=window)
# statusDisplay = tk.Text(master=window) 
#make read only
 #works!
# statusDisplay1.insert('end', "test text post close")

# buttonLabel = tk.Label(window, text="What is your name?")
# #.pack() is more useful for single columns and rows
# #grid is best for entire sheet
# buttonLabel.grid(column=1, row=0)
# #entry field field needs to be above functions for them to see it
# name_field = tk.Entry()
# name_field.grid(column=1, row=1)

# #functions
# def phrase_generator():
	# phrases = ["hello ","hey there, ", "aloha, "]
	# name = str(name_field.get())
	# if name == "":
		# return ""
	# else:
		# return phrases[rand.randint(0,2)] + name + "."
	
# def phrase_display():
	# greeting = phrase_generator()
		
	# #then create the text field
	# greeting_display = tk.Text(master=window, height=10, width=30)
	# greeting_display.grid(column=1, row=4)
	# #insert greeting into text field
	# greeting_display.insert(tk.END, greeting)
	
# phrase_display()

# button1 = tk.Button(window, text="Add name!", command=phrase_display)
# button1.grid(column=1, row=2)

# #text fields
# text_field = tk.Text(master=window, height=10, width=30)
# text_field.grid(column=4,row=3)
# #button
# button2 = tk.Button(window, text="Button")
# button2.grid(column=4, row=4)

# #target buttons -- might have to do this manually to name each button
# rbVar = tk.StringVar()
# #need to fill #dictionary to create multiple buttons
# targets = {"enemy1" : "0",
	      # "enemy2" : "1",
	      # "enemy3" : "2",
		  # "friend1" : "3",
	      # "friend2" : "4",
	      # "friend3" : "5"}	  
# #loop creates multiple buttons rather than making them separately
# i = 0 #counters and stuff, could learn how to make these in for loop but this be faster
# j = 1
# for (text, value) in targets.items():
	# if i <= 2:
		# # print("i:", i, "j:", j)
		# tk.Radiobutton(window, text = text, variable = rbVar, value = value, indicator = 0, background = "pink").grid(column=i,row=j)
		# # print("i:", i, "j:", j)
		# i += 1
	# else:
		# # print("i:", i, "j:", j)
		# j = 2
		# i += 1
		# # print("i:", i, "j:", j)
		# tk.Radiobutton(window, text = text, variable = rbVar, value = value, indicator = 0, background = "light blue").grid(column=(i-4),row=(j))