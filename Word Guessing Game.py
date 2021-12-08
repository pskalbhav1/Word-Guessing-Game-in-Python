#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import library - tkinter 
from tkinter import *

#Import Library - tkinter messagebox
from tkinter import messagebox

#Import random library
import random
from random import randint

#List of alphabetical characters
uppercase=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#List of easy words
word_list= ['MUMBAI','DELHI','BANGLORE','HYDRABAD','AHMEDABAD','CHENNAI','KOLKATA','SURAT','PUNE','JAIPUR','AMRITSAR','ALLAHABAD','RANCHI',
            'LUCKNOW','KANPUR','NAGPUR','INDORE','THANE','BHOPAL','PATNA','GHAZIABAD','AGRA','FARIDABAD','MEERUT','RAJKOT','VARANASI','SRINAGAR',
            'RAIPUR','KOTA','JHANSI']

#Hard words extracted from file
file = open('hard.txt','r')
#Read from file
word = file.readlines()
#Find the length of the list
length = len(word)

#COnvert the list to uppercase as it will be easier for us to handle
words=[]
for i in word:
    #COnvert each word in list to upper case
    i=i.upper()
    #Add the converted word to the new list
    words.append(i)

# Select random word from the list of hard words
def getRandomWord():
    random_no = randint(0,length)
    word = words[random_no].strip()
    return word 

#Create a new gui 
window = Tk()
#Name the tkinter window 
window.title('Word Guessing Game')

#The list of hangman photos to be displayed based on 
photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"),
PhotoImage(file="images/hang3.png"), PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"),
PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"), PhotoImage(file="images/hang8.png"),
PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]

#start a new game with new word and everything reset to start
def Start(choice):
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses =0
    #If choice is hard, select hard word
    if choice=="Hard":
        the_word=getRandomWord()
    #Else select easy word
    else:
        the_word=random.choice(word_list)
    #Take spaces into account if any
    the_word_withSpaces = " ".join(the_word)
    #Set the inital number of letters the word has in the form of dashes
    lblWord.set(' '.join("_"*len(the_word)))
    #print the word here just to verify working
    print(the_word)

def guess(letter):
    global numberOfGuesses
    #while the number of choices is less than 11
    if numberOfGuesses<11:
        #Convert the word to list 
        txt = list(the_word_withSpaces)
        #Keep a list of guesses letters/characters
        guessed = list(lblWord.get())
        #While some letter has been guessed by user
        if the_word_withSpaces.count(letter)>0:
            #Check if the letter is part of the word to be found
            for c in range(len(txt)):
                if txt[c]==letter:
                    guessed[c]=letter
                lblWord.set("".join(guessed))
                #If the word matches display a congratulations message
                if lblWord.get()==the_word_withSpaces:
                    messagebox.showinfo("Hangman","You guessed it!. The word is "+ the_word_withSpaces+"\n Choose hard or easy if you want to try again.")
                    #Reset the image to initial state
                    imgLabel.config(image=photos[0])
                    break
        else:
            #Increment the times tried
            numberOfGuesses += 1
            #Display the next hangman image
            imgLabel.config(image=photos[numberOfGuesses])
            #If the hangman is complete, then end the game by displaying message
            if numberOfGuesses==11:
                messagebox.showwarning("Hangman","Game Over. The correct word is "+ the_word_withSpaces+"\n Choose hard or easy if you want to try again.")

#Display the grid
imgLabel=Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)

#Display the labelword
lblWord = StringVar()
Label(window, textvariable  =lblWord,font=('Helvetica 10')).grid(row=0, column=3 ,columnspan=6,padx=10)

#Display the characters to be selected during the game
n=0
for c in uppercase:
    Button(window, text=c, command=lambda c=c: guess(c), font=('Helvetica 10'), width=4).grid(row=1+n//8,column=n%8)
    n+=1

#Easy and Hard levels
Button(window, text="Easy", command=lambda:Start("Easy"), font=("Helvetica 10")).grid(row=4, column=4)
Button(window, text="Hard", command=lambda:Start("Hard"), font=("Helvetica 10")).grid(row=4, column=5)

#Start the game with an easy question
Start("Easy")
#Tkinter gui 
window.mainloop()


# In[ ]:




