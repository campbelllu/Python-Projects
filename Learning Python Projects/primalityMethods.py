import time, math

def is_prime(n): #best test
	if n < 2 or n % 2 == 0:
		return False
	if n == 2:
		return True
	max_divisor = math.floor(math.sqrt(n))
	for i in range(3, 1+ max_divisor, 2):
		if n % i == 0:
			return False
	return True

def harvest_primes(file_name, low_range, high_range): #farm primes to file
	f = open(file_name, "a")
	for i in range(low_range, high_range):
		if is_prime(i) == True:
			f.write(str(i))
			f.write("\n")
	f.close()

# t0 = time.time()
# print("calculating primes now")
# harvest_primes("Prime List.txt", 15000000, x) #last cap was xM, so replace x to harvest more primes!
# t1 = time.time()
# print("time taken: ", t1-t0)

def file_length(file_name):
	with open(file_name) as f:
		for i,l in enumerate(f):
			pass
	return i + 1

prime_List = []

def fill_list(file_name): #fills list with all the primes, as int's from the strings in file format
	global prime_List
	f = open(file_name, "r")
	prime_List = list(map(int, f.read().splitlines())) #converts strings in file to ints here
	f.close()
	
t0 = time.time()
print("filling primes now")
fill_list("Prime List.txt")
t1 = time.time()
print("time taken: ", t1-t0)
print("length of primelist:", len(prime_List))
print(prime_List[len(prime_List)-1]) #see the last prime listed/harvested
# # print(*prime_List)
# # print(prime_List)

# print(file_length("Prime List.txt"))



# def is_prime1(n):
	# if n ==1:
		# return False #1 isn't prime
 
	# if n == 2:
		# print("2 = True")
		# return True
	# if n > 2 and n % 2 == 0:
		# print(n, "= False")
		# return False
 
	# max_divisor = math.floor(math.sqrt(n))
	# for d in range(3, 1 + max_divisor, 2):
		# if n % d ==0:
			# print(n, "= False")
			# return False
	# return True
 
# # t0 = time.time()
# # for  n in range(1, 200000):
 # # is_prime1(n)
# # t1 = time.time()
# # print("time taken: ", t1-t0)


# # V2:
# def is_prime2(n):
	# if n == 1:
		# return False #1 isn't prime
 
	# if n == 2:
		# print("2 = True")
		# return True
	# if n > 2 and n % 2 == 0:
		# print(n, "= False")
		# return False
 
	# max_divisor = math.floor(math.sqrt(n))
	# for d in range(3, 1 + max_divisor, 2):
		# if n % d ==0:
			# print(n, "= False")
			# return False
		# print(n, "= True")
	# return True
 
# # t0 = time.time()
# # for  n in range(1, 200000):
 # # is_prime2(n)
# # t1 = time.time()
# # print("time taken: ", t1-t0)