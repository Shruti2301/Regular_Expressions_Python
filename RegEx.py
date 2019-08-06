# -*- coding: utf-8 -*-


#IMPORTING LIBRARIES
import re
sentence = "I was born in year 1996"

re.match(r".*", sentence)

re.match(r".+", sentence)

re.match(r"[a-zA-Z]+", sentence)

re.match(r"ab?",sentence)

#----------------------------------------------------

#FINDING PATTERNS IN TEXT

sentence1 = "I was born in the year 1996"

re.match(r"[a-zA-Z]+", sentence1)

sentence2 = "1996 was year"

re.match(r"[a-zA-Z]+", sentence2)

# For a GLOBAL SEARCH : Use Search

re.search(r"[a-zA-Z]+", sentence2)

#----------------------------------------------------

#STARTS WITH

if re.match(r"^1996", sentence2):
    print("Match")
else:
    print("No Match")
    
# ENDS WITH

if re.match(r"born$", sentence1):
    print("Match")
else:
    print("No Match")    

#--------------------------------------------------
    
# Using SUB for Global Search + Global Replace

sentence3 = "I Love Avengers"

print(re.sub(r"Avengers","Justice League", sentence3))    
 
print(re.sub(r"[a-z]","0",sentence3))   

print(re.sub(r"[a-z]","0",sentence3, flags = re.I))

#---------------------------------------------------

# SHORTHAND CHARACTER CLASSES

import re

sen1 = "Welcome to the year 2018"
sen2 = "Just---@Jack place #fun"
sen3 = "I       Love      You"

sen1_modified = re.sub(r"\d","",sen1)  #Removing Digit

sen2_modified = re.sub(r"[@#\.]", "", sen1) #Replace character with space
                          
sen2_modified = re.sub(r"\w", "", sen2) # Replace words with space                      
                         
sen2_modified = re.sub(r"\w", " ", sen2)  #Replace Not a Word Character with space

sen2_modified = re.sub(r"\s", " ", sen2_modified) #Remove all spaces

sen2_modified = re.sub(r"\s + [a-z A-Z]\s", " ", sen2_modified) #Remove all spaces

sen3_modified = re.sub(r"\s+", " ",sen3)
 
sen3_modified = re.sub(r"\s+ Love\s+"," Hate",sen3)

#------------------------------------------------------

# PREPROCESSING USING REGEX

X = ["This is a wolf #scary", "Welcome here #missing", "11322 the no. to know", "Remember the name s- John", "I   Love   You"]
     
for i in range (len(X)):

     X[i] = re.sub(r"\w","",X[i]) #Remove ASCII Symbol
     X[i] = re.sub(r"\d","",X[i]) #Remove Digits
     X[i] = re.sub(r"\s+[a-z]\s+","",X[i],flags = re.I) #Remove Single Character 
     X[i] = re.sub(r'\s+'," ",X[i]) #Remove Extra Space
     X[i] = re.sub(r"'\s","",X[i])
     X[i] = re.sub(r"\s$","",X[i])
     
 #--------------------------------------------------------              
   