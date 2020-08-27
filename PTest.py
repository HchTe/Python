s = "Wel_c_me to Ha_g_an" 
print(s)

dictionary = {}
dictionary[1] = 'water'
dictionary[2] = 'bicylce'
dictionary[3] = 'wardrobe'
dictionary[4] = 'bottle'
dictionary[5] = 'keyboard'

from random import *

r = randint(1, 5)
w =  dictionary[r]
l = len(w)
q = l - 1
e = (len(w)-2) * "_ " 
t = ( (w[0]) + e + (w [l-1]) )
print(t)

a = list(w)

word = []
word.extend(a)


for h in range (len(word)):
    word[h] = "_"
count = 0
while count < len(w) -2  :
    guess = input("Enter a guess:")
    guess = guess.lower()
    print(count)
    
    if count == len(w) -3:
        print("You Win!")

    for h in range(len(a)):
        if a[h]  == guess:
            word[h] = guess
            count = count + 1
            print( (w[0]) + (' '.join(word[1:q])) + (w[l-1])  )
        
        


