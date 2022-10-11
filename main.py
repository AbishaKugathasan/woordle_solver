from math import comb

hashmap_s1 = {}
arr = []
f = open("words_alpha.txt", "r")

#Get all the words that are 5 letters 
#Take an input where the _are unknown words
arr = ['_' for i in range(5)]

combination = input("Enter your woordle result: ")
print(combination)

#print out the acceptable words with those conditions 
Lines = f.readlines()
for x in Lines:
    if (len(x) == 6):
        #if the position and the letter of the word = to the hashmap position and word where position = VALUE and letter is the KEY
        if(combination[1] == x[1] and combination[2] == x[2] and combination[3] == x[3]): 
            print("Word", x)
        else:
            continue




        #do something
        #print("Word",x) 
    #else: 
        #continue 