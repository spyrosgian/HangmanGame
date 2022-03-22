#------------------------------------------------------------------------------
#Palindrome                                                       
#Script-Created-by-SG-March-2020
#------------------------------------------------------------------------------

# Clear cmd window
import os
os.system('cls')

#Process command line arguments 
import sys
File_name = sys.argv [1]
No_Guesses = sys.argv [2]

# 1. Checking if words.txt exists
# 2. Opening and reading words.txt and and storing them in a list L

try:
    file = open (sys.argv[1]+'.txt','r')
    L = file.readlines()
    file.close()
except IOError:
    print ('Unable to locate txt file.') ; print ('')
    exit(1)

# Length of L and removing two last characters (\n)
LenL = len (L) 
for i in range (LenL-1):
    s0 = L[i]
    s0 = s0[:-1]
    s0 = s0.lower()
    L[i] = s0

# Select a random word from List L
import random
if len (L) == 1:
    w1 = L [0]
else:
    for i in range (LenL-1):
        w0 = random.randint(0, LenL-1)
    w1 = L[w0]

# Number of guesses and game beggining
rt0 = int(sys.argv[2])
print ('-'*20)
print ('Game now starts.') ; print ('You have', rt0, 'guesses.')
print ('-'*20)

# Length of random word w1 and printing asterisk for each letter
lenw1 = len (w1)
print ('') ; print ('|', '*'*lenw1, '|') ; print ('')
w2 = ('*'*lenw1)
w2 = list (w2) 
w3 = list (w1) 

# While loop for number of guesses rt0 and empty string s1
count0 = 0 
s1 = ''

while count0 < rt0:
    rt1 = count0 + 1
    print ('> Guess', rt1) ; print ('')
    print ('   Characters used so far:', s1)

    # Users input-guess-character
    l = input ('  Please enter your guess: ') ; print ('')
    l = l.lower ()

    # Checking if user has already used this letter as input
    if s1.find (l) > 0:
        print ('  Character has already been selected.') ; print ('')
    else:
        # Checking if user's input is alphabetic & if input's length is equal to 1
        if l.isalpha () == True and len (l) ==1:
            count0 = count0 + 1
            s1 = s1 + ' ' + l

            # Checking if word w1 contains letter l
            count1=0
            for c in w1:
                if c == l:
                    w2[count1] = l
                if w2 == w3:
                    print ('  Well done. The word was', w1)
                    exit(0)
                if count0 == rt0 and w2 != w3:
                    print ('  Better luck next time. The word was:', w1)
                    exit (0)
                count1 = count1 + 1
            w4 = ''.join (w2)
            print ('|', w4, '|') ; print ('')

        # Checking if input is the hidden word w1
        elif w1 == l:
            print ('  Well done. The word was', w1)
            exit (0)
        else:
            print ('  Invalind input. Please try again.') ; print ('')

#-End-of-Script----------------------------------------------------------------
#------------------------------------------------------------------------------