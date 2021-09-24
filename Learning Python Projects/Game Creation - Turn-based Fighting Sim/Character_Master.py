import math as m
import random as rand

class Character:
	"""The Character class allows for the creation of player controlled characters. It manages their stats, and tracks their stat progression."""
	#attributes/stats that characters will have
	"""Every instantiation of a character has at least one stat point in each category. No stat may be over 10 at level one. Twenty-one points total may be spread amongst each starting stat. This eliminates ridiculously stacked stats on a level one character: If they are too strong, their other stats are still low."""
	name = ""
	role = ""
	level = 1
	speed = 1
	health = 1
	maxHealth = 1
	power = 1
	accuracy = 1
	defense = 1
	armor = m.floor(0.3*(health) + 0.3*(power) + 0.8*(defense))
	dodge = 2
	#m.ceil(2 + 0.05*(defense) + 0.01*(willpower) - 0.05*(health))
	status = "Alive"
	# DefendFlag = False
	# FrenzyFlag = False #wth is this?
	# TauntFlag = False
	damageDone = 0
	turnMeter = 0
		
	#one-step constructor
	"""Allows for the generation of a new player character."""
	#instantiate cheat code
	#z = Character("Chris",1,1,1,1,1,1,1)
	#self, name, role, level, speed, health, power, accuracy, defense
	def __init__(self, name, role, level, speed, health, power, accuracy, defense):
		self.name = name
		self.role = role
		self.level = level
		self.speed = speed
		self.health = health
		self.maxHealth = health
		self.power = power
		self.accuracy = accuracy
		self.defense = defense
		self.status = "Alive"
		self.turnMeter = 0
		self.DefendFlag = False
		self.FrenzyFlag = False #wth is this?
		self.TauntFlag = False
		self.armor = m.floor(0.3*(health) + 0.3*(power) + 0.8*(defense))
		self.dodge = m.ceil(2 + 0.05*(speed) + 0.1*(defense) + 0.01*(power) - 0.05*(health))
		if self.dodge <= 0:
			self.dodge = 2
	
	#return stats functions
	#def getStats(self):
		#getStats returns stats as a dictionary, check stats prints them
		#want to return all values at once, maybe as a printed statement, maybe just as a dictionary of values, maybe just as a check... ah ha!
		# level, speed, health, power, accuracy, defense
	def checkStats(self):
		print("{8}'s stats:\nRole = {9} \nLevel = {0} \nSpeed = {1} \nHealth = {2} \nMaxHealth = {10} \nPower = {3} \nAccuracy = {4} \nDefense = {5} \nArmor = {6} \nDodge = {7} \nTurn Meter = {11}\n".format(self.level, self.speed, self.health, self.power, self.accuracy, self.defense, self.armor,  self.dodge, self.name, self.role, self.maxHealth, self.turnMeter))
		
	def getName(self):
		return self.name
	
	def getRole(self):
		return self.role
	
	def getLevel(self):
		return self.level
		
	def getSpeed(self):
		return self.speed
		
	def getDefense(self):
		return self.defense	
	
	def getHealth(self):
		return self.health
		
	def getMaxHealth(self):
		return self.maxHealth
	
	def getPower(self):
		return self.power
		
	def getAccuracy(self):
		return self.accuracy
		
	def getArmor(self):
		return self.armor
	
	def getDodge(self):
		return self.dodge
		
	def getStatus(self):
		global status
		return self.status
		
	def checkDefenseFlag(self):
		"""This function checks the target for a defense tag. Then adjust attack values accordingly."""
		if self.DefendFlag == True:
			return True
		else:
			return False
		
	def checkFrenzyFlag(self):
		"""This function checks the target for a frenzy tag. Then adjust attack values accordingly."""
		if self.FrenzyFlag == True:
			return True
		else:
			return False
		
	def checkTauntFlag(self):
		"""This function checks the target for a taunt tag. Then adjust attack values accordingly."""
		if self.TauntFlag == True:
			return True
		else:
			return False
		
	def getDamageDone(self):
		return self.damageDone
	
	def getTurnMeter(self):
		return self.turnMeter
		
	#actions
	#all characters can attack, defend, frenzy
	#healers can't delay or taunt, but have 2 heals
	#tanks can taunt and rally, but can't multi-strike or heal
	#attackers can delay and flourish, but can't heal, taunt, or rally
	"""attack() determines if an attack hits, if that hit is then a critical hit, and then returns how much damage the hit does."""
	def attack(self, target):
		hitChance = m.ceil(self.getAccuracy() - target.getDodge())
		# print("hitChance:", hitChance)
		critChance = 2 * hitChance #crit chance is based off of regular hit chance still
		critLuck = rand.randrange(1,100,1)
		hitLuck = rand.randrange(1,100,1)
		#make sure that hit chance isn't negative (self-strike?)
		if hitChance <= 0:
			hitChance = 0
			critChance = 2
		damage =  max(1, m.ceil((0.7*self.getPower()) - target.getArmor()))
		if damage <= 0: #make sure that damage isn't below zero
			damage = 0
		critDamageModifier = 1.5
		if hitChance >= 100: #if hitchance > 100: hit and auto crit, very^2 minor chance to do this
			if damage <= 0: #calculate their guaranteed critical hit, modified by armor, first for weaklings
				return  max(1, m.ceil((1 + (0.1 * self.getPower()) - (0.05 * target.getArmor())) * critDamageModifier))
			else: #otherwise dmg done is:
				return  max(1, m.ceil(damage * critDamageModifier))
		elif hitChance == 0: #if a hit lands when hitchance is 0, make it crit-able for frenzy
			badHitLuck = rand.randrange(1,100,1)
			if badHitLuck > 1: #calculate if it's a hit, 99% chance to miss still
				return 0
			else: #hit
				if critLuck <= critChance: #crit!
					if damage == 0:
						return  max(1, m.ceil((1 + (0.1 * self.getPower()) - (0.05 * target.getArmor())) * critDamageModifier))
					elif damage > 0:
						return  max(1, m.ceil(damage * critDamageModifier))
					else: #a catch all that should never be tripped, just in case
						return  max(1, m.ceil(damage * 1.5))
				else: #non-crit
					if damage == 0:
						return  max(1, m.ceil(1 + ((0.1 * self.getPower()) - (0.05 * target.getArmor()))))
					elif damage > 0:
						return  max(1, m.ceil(damage))
					else: #a catch all that should never be tripped, just in case
						return  max(1, m.ceil(damage))
		else: #we've covered full hit/auto crit, and zero hit, now everything else; can crit
			if hitLuck <= hitChance: #hit! calculate if the hit is critical and return damage done
				if critLuck <= critChance: #crit!
					if damage == 0:
						return  max(1, m.ceil((1 + (0.1 * self.getPower()) - (0.05 * target.getArmor())) * critDamageModifier))
					elif damage > 0:
						return  max(1, m.ceil(damage * critDamageModifier))
					else: #a catch all that should never be tripped, just in case
						return  max(1, m.ceil(damage * 1.5))
				else: #non-crit
					if damage == 0:
						return  max(1, m.ceil(1 + ((0.1 * self.getPower()) - (0.05 * target.getArmor()))))
					elif damage > 0:
						return  max(1, m.ceil(damage))
					else: #a catch all that should never be tripped, just in case
						return  max(1, m.ceil(damage))
			else: #miss
				return 0
			
	def defend(self, target):
		"""Defend is an action that doubles defense (or armor and dodge?), but halves damage done! It cannot crit, but the armor boosts last until cancelled by an attacker using Frenzy against the Defender, or by using an action other than Defend. If hit, reflects 5% of the damage back onto the attacker."""
		if self.checkDefenseFlag() == False:
			self.assignDefenseFlag()
			self.assignDefense(2*self.getDefense())
			self.updateArmor()
			self.updateDodge()
		hitChance = m.ceil(self.getAccuracy() - target.getDodge())
		critLuck = rand.randrange(1,100,1)
		hitLuck = rand.randrange(1,100,1)
		if hitChance <= 0:
			hitChance = 0
		damage =  m.ceil(0.5*((0.7*self.getPower()) - target.getArmor()))
		if damage <= 0:
			damage = 0
		#hit without any crit chance
		if hitChance >= 100: #if hitchance > 100: hit 
			if damage <= 0: #calculate their guaranteed hit, modified by armor, first for weaklings
				return  max(1, m.ceil((1 + (0.1 * self.getPower()) - (0.05 * target.getArmor()))))
			else: #otherwise dmg done is:
				return  max(1, m.ceil(damage))
		elif hitChance == 0: #if a hit lands when hitchance is 0
			badHitLuck = rand.randrange(1,100,1)
			if badHitLuck > 1: #calculate if it's a hit, 99% chance to miss still
				return 0
			else: #hit
				return  max(1, m.ceil(damage))
		else: #we've covered full hit/auto crit, and zero hit, now everything else; can crit
			if hitLuck <= hitChance: #hit!
				if damage == 0:
					return  max(1, m.ceil(1 + ((0.1 * self.getPower()) - (0.05 * target.getArmor()))))
				elif damage > 0:
					return  max(1, m.ceil(damage))
				else: #a catch all that should never be tripped, just in case
					return  max(1, m.ceil(damage))
			else: #miss
				return 0
		#make sure that attackers have to check for damage done to self if they crit the defending target
		
	def frenzy(self, target):
		"""Frenzy is an action that doubles damage done for this specific turn's attack, but reduces aim to 1/4 of its usual! Damage is calculated before crit, making it scale spectacularly when it does hit. Frenzy also removes any buffs or taunts from the target, regardless of if it hits the target."""
		#remove all buffs and taunts
		target.negateTauntFlag()
		target.negateFrenzyFlag()
		target.negateDefenseFlag()
		hitChance = m.ceil((0.25 * m.floor(self.getAccuracy())) - target.getDodge())
		critChance = 2 * hitChance #crit chance is based off of regular hit chance still
		critLuck = rand.randrange(1,100,1)
		hitLuck = rand.randrange(1,100,1)
		if hitChance <= 0:
			hitChance = 0
			critChance = 2
		damage =  max(1, m.ceil((2 * (0.7*self.getPower())) - target.getArmor()))
		if damage <= 0:
			damage = 0
		critDamageModifier = 1.5 #crits are just too OP otherwise
		if hitChance >= 100: #if hitchance > 100: hit and auto crit, very^2 minor chance to do this
			if damage <= 0: #calculate their guaranteed critical hit, modified by armor, first for weaklings
				return  max(1, m.ceil((1 + (0.1 * self.getPower()) - (0.05 * target.getArmor())) * critDamageModifier))
			else: #otherwise dmg done is:
				return  max(1, m.ceil(damage * critDamageModifier))
		elif hitChance == 0: #if a hit lands when hitchance is 0, make it crit-able for frenzy
			badHitLuck = rand.randrange(1,100,1)
			if badHitLuck > 1: #calculate if it's a hit, 99% chance to miss still
				return 0
			else: #hit
				if critLuck <= critChance: #crit!
					if damage == 0:
						return  max(1, m.ceil((1 + (0.1 * self.getPower()) - (0.05 * target.getArmor())) * critDamageModifier))
					elif damage > 0:
						return  max(1, m.ceil(damage * critDamageModifier))
					else: #a catch all that should never be tripped, just in case
						return  max(1, m.ceil(damage * 1.5))
				else: #non-crit
					if damage == 0:
						return  max(1, m.ceil(1 + ((0.1 * self.getPower()) - (0.05 * target.getArmor()))))
					elif damage > 0:
						return  max(1, m.ceil(damage))
					else: #a catch all that should never be tripped, just in case
						return  max(1, m.ceil(damage))
		else: #we've covered full hit/auto crit, and zero hit, now everything else; can crit
			if hitLuck <= hitChance: #hit! calculate if the hit is critical and return damage done
				if critLuck <= critChance: #crit!
					if damage == 0:
						return  max(1, m.ceil((1 + (0.1 * self.getPower()) - (0.05 * target.getArmor())) * critDamageModifier))
					elif damage > 0:
						return  max(1, m.ceil(damage * critDamageModifier))
					else: #a catch all that should never be tripped, just in case
						return  max(1, m.ceil(damage * 1.5))
				else: #non-crit
					if damage == 0:
						return  max(1, m.ceil(1 + ((0.1 * self.getPower()) - (0.05 * target.getArmor()))))
					elif damage > 0:
						return  max(1, m.ceil(damage))
					else: #a catch all that should never be tripped, just in case
						return  max(1, m.ceil(damage))
			else: #miss
				return 0
		# be sure to add other buff removals as they are added to the game
		
	#uses speed to make multiple strikes, they can't do dmg, but remove turn meter from toon
	def delay(self, target):
		hitCount = m.floor(self.getSpeed()/10) * 20
		hitChance = m.ceil(self.getAccuracy() - target.getDodge())
		# print("hitcount: {0}, hit chance: {1}".format(hitCount, hitChance))
		if hitChance <= 0:
			hitChance = 0
			return 0
		else:
			badHitLuck = rand.randrange(1,100,1)
			if badHitLuck > hitChance:
				return 0
			else:
				return hitCount
	
	#does aoe removal of 15% turn meter
	def flourish(self):
		return 150
		
	#small heal adds turn meter after use, is a small heal otherwise	
	def sHeal(self, target):
		"""Heal is an action that returns health to a character. It might heal very little, but then adds turn meter based on initial health missing."""
		#healing done scales with how much health is left, simulating difficulty to focus
		TMGain = target.getMaxHealth()-target.getHealth()
		self.turnMeter += (TMGain * 10)
		healStrength = m.floor(0.65*self.getHealth()) + m.floor(0.25 * TMGain)
		target.assignHealth(target.getHealth() + healStrength)
		
	#mega heal heals massively, but makes user lose health	
	def mHeal(self, target):
		"""Mega Heal is an action that returns massive health to a character and makes healer lose health equal to 25% of their MaxHealth."""
		healStrength = m.floor(0.75 * self.getMaxHealth())
		healthLoss = m.floor(0.25 * self.getMaxHealth())
		if (self.getHealth()-healthLoss) > 0:
			self.assignHealth(self.getHealth()-healthLoss)
		else:
			self.assignHealth((self.getMaxHealth()-(self.getMaxHealth()-1)))
		target.assignHealth(target.getHealth() + healStrength)
			
	#taunt offers a minor self heal, activates defend, and makes targets hit only you into dispelled
	def taunt(self, target):
		"""Taunt is an action that forces all opposing characters to attack the target. Taunt lasts until cancelled or dispelled. Grants a minor self-heal, and then performs the Defend-action."""
		if self.checkTauntFlag() == False:
			self.assignTauntFlag()
			self.assignHealth(self.getHealth()+(m.floor(0.15*self.getHealth())))
			return self.defend(target)
		else:
			self.assignHealth(self.getHealth()+(m.floor(0.15*self.getHealth())))
			return self.defend(target)
			
	#removes enemy TM, gives it to team mates 
	def rally(self, eList, fList):
		#remove enemy TM
		for chars in eList:
			chars.removeTurnMeter(100)
		#give TM to team
		for chars in fList:
			chars.addTurnMeter(100)
		
	#LevelUp functions for each class
	"""customLevelUp() is for player input-dependent stats per level up. All others are custom per naming standard. 20 stat points available per level up:
	A focused toon has one +10 stat, one +7 stat, one +3 stats, and the rest are +1's. A generalist toon has three +5 stats, one +3 stats, one +2, and the rest are +1's. Pillars have +10 to one stat, one +4, two +3's, and the rest are +1's. +3 to all stats is the final character stat-frame."""
			
	def customLevelUp(self, howMany, speedMod, healthMod, powerMod, accuracyMod, defenseMod):
		# for i in range howMany:
		self.level += howMany
		self.speed += speedMod * howMany
		self.health += healthMod * howMany
		self.maxHealth += healthMod * howMany
		self.power += powerMod * howMany
		self.accuracy += accuracyMod * howMany
		self.defense += defenseMod * howMany
		self.armor = m.floor(0.3*(self.health) + 0.3*(self.power) + 0.8*(self.defense))
		self.dodge = m.ceil(2 + 0.05*(self.speed) + 0.1*(self.defense) + 0.01*(self.power) - 0.05*(self.health))
		if self.dodge <= 0:
			self.dodge = 2
			
	def allThreesLevelUp(self, howMany):
		self.level += 1 * howMany
		self.speed += 3 * howMany
		self.defense += 3 * howMany
		self.health += 3 * howMany
		self.power += 3 * howMany
		self.accuracy += 3 * howMany
		self.armor = m.floor(0.3*(self.health) + 0.3*(self.power) + 0.8*(self.defense))
		self.dodge = m.ceil(0.02 + 0.05*(self.speed) + 0.05*(self.defense) + 0.01*(self.power) - 0.05*(self.health))
		if self.dodge <= 0:
			self.dodge = 2
	
	#change stats functions|
	"""Allows for manipulation of character stats."""
	def assignName(self, newName):
		self.name = newName
		
	def assignRole(self, newRole):
		self.role = newRole
		
	def assignLevel(self, newLevel):
		self.level = newLevel
		
	def assignSpeed(self, newSpeed):
		self.speed = newSpeed
		
	def assignDefense(self, newDef):
		self.defense = newDef
	
	def assignHealth(self, newHealth): #must adjust maxHealth to increase health height, otherwise heals, and has infinite depth
		self.health = newHealth
		if self.health > self.maxHealth:
			self.health = self.maxHealth
		
	def assignMaxHealth(self, newMaxHealth):
		self.maxHealth = newMaxHealth
		
	def assignFocus(self, newFocus):
		self.focus = newFocus
	
	def assignpower(self, newpower):
		self.power = newpower
		
	def assignAccuracy(self, newAccuracy):
		self.accuracy = newAccuracy
		
	def assignArmor(self, newArmor):
		self.armor = newArmor
		
	def updateArmor(self):
		self.armor = m.floor(0.3*(self.health) + 0.3*(self.power) + 0.8*(self.defense))
	
	def assignDodge(self, newDodge):
		self.dodge = newDodge
		
	def updateDodge(self):
		self.dodge = m.ceil(2 + 0.05*(self.speed) + 0.1*(self.defense) + 0.01*(self.power) - 0.05*(self.health))
		if self.dodge <= 0:
			self.dodge = 2
	
	def assignDefenseFlag(self):
		self.DefendFlag = True
		
	def negateDefenseFlag(self):
		if self.DefendFlag == True:
			self.DefendFlag = False
			self.assignDefense(0.5*self.getDefense())
			self.updateArmor()
			self.updateDodge()
		else:
			self.DefendFlag = False
		
	def assignFrenzyFlag(self):
		self.FrenzyFlag = True
		
	def negateFrenzyFlag(self):
		self.FrenzyFlag = False
		
	def assignTauntFlag(self):
		self.TauntFlag = True
		
	def negateTauntFlag(self):
		self.TauntFlag = False
		
	def assignDamageDone(self, damage):
		self.damageDone = damage
		
	def assignTurnMeter(self, num):
		self.turnMeter = num
		if self.turnMeter < -1000:
			self.turnMeter = -1000
		if self.turnMeter > 1000:
			self.turnMeter =1000
	
	def addTurnMeter(self, num):
		self.turnMeter += num
		if self.turnMeter > 1000:
			self.turnMeter = 1000
		
	def removeTurnMeter(self, num):
		self.turnMeter -= num
		if self.turnMeter < -1000:
			self.turnMeter = -1000
			
	def assignStatus(self, status):
		self.status = status
	def updateStatus(self):
		global status
		#updates status of character between alive, unconscious, dead
		if self.getHealth() <= -10:
			self.status = "Dead"
		elif self.getHealth() > -10 and self.getHealth() <= 0:
			self.status = "Unconscious"
		else: #health >= 1
			self.status = "Alive"