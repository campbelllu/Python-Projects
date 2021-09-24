#making a string reverser!
# word = input()
def word_Reversal(word):
	revWord = ""
	for i in range(len(word)):
		revWord += word[-(i+1)]
	print(revWord)
	#possibly make tihs a return

#Updated 9/21    
def word_Reversal2(word):
    return word[::-1]



#beautiful class. makes self-referencing libraries a thing!... for strings
# class SelfRefDict(dict):
   # def __getitem__(self, item):
       # return dict.__getitem__(self, item) % self

# dictionary = SelfRefDict({ #example for how to utilize
    # 'user' : 'gnucom',
    # 'home' : '/home/%(user)s',
    # 'bin' : '%(home)s/bin '
# })
# print( dictionary["home"]) #useless test
# print( dictionary["bin"])