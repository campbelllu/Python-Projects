import math as m

DEFAULT_RANGE = range(1,101)
def DEFAULT_WORK(j): #easily updatable 
	if j % 3 == 0 and j % 5 == 0:
		return "FIZZBUZZ"
	elif j % 5 == 0: 
		return "buzz"
	elif j % 3 == 0:
		return "fizz"
	else:
		return j

fizzy_boi = [] 

def fizzBuzz(range):
	for i in range:
		fizzy_boi.append(DEFAULT_WORK(i))
		
def getFizzList():
	return fizzy_boi
# use tests
fizzBuzz(DEFAULT_RANGE)
print(fizzy_boi)
# print(*fizzy_boi)