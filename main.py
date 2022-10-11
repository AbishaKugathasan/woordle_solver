from math import comb

arr = []
f = open("words_alpha.txt", "r")
input_length = 0

#input from the user 
while (input_length != 5): 
    combination = input("Enter your woordle result: ")
    input_length = len(combination)

#Create an array that holds letters that are valid 
for x in range(len(combination)): 
    if(combination[x] != "_"):
        arr.append(x)

#Compare the words in the dictionary and user input 
Lines = f.readlines()
for x in Lines:
    if (len(x) == 6):
        if (len(arr) == 4): 
            if((combination[arr[len(arr)-1]] == x[arr[len(arr)-1]]) and (combination[arr[len(arr)-2]] == x[arr[len(arr)-2]]) and (combination[arr[len(arr)-3]] == x[arr[len(arr)-3]]) and (combination[arr[len(arr)-4]] == x[arr[len(arr)-4]])):
                print(x)
        elif (len(arr) == 3): 
            if((combination[arr[len(arr)-1]] == x[arr[len(arr)-1]]) and (combination[arr[len(arr)-2]] == x[arr[len(arr)-2]]) and (combination[arr[len(arr)-3]] == x[arr[len(arr)-3]])):
                print(x)
        elif (len(arr) == 2): 
            if((combination[arr[len(arr)-1]] == x[arr[len(arr)-1]]) and (combination[arr[len(arr)-2]] == x[arr[len(arr)-2]])):
                print(x)
        elif (len(arr) == 1): 
            if((combination[arr[len(arr)-1]] == x[arr[len(arr)-1]])):
                print(x)            
        else:
            continue