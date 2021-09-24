import math

fib_cache = {}

def fib(n):
	#if we have stored value in cache, return it
	if n in fib_cache:
		return fib_cache[n]
	#regular fibonacci code otherwise modified to cache new values
	if n == 1:
		value = 1
	elif n == 2:
		value = 1
	elif n > 2:
		value = fib(n-1) + fib(n-2)
		
	#cache the value and return it via normal fibonacci methods
	fib_cache[n] = value
	return value
	
	
for n in range(1,86):
	print(n, ";", fib(n))
	


