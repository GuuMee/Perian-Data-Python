import random
# GET GUESS
def get_guess():
    return list(input("What is your guess?"))

#GENERATE COMPUTER CODE 123
def generate_code():
    digits = [str(num) for num in range(10)] #creating a list of everynumber from 0 to 9

    #Shuffle the digits
    random.shuffle(digits)
    #Then grab the first three after the Shuffle
    return digits[:3] #return first three

#GENERATE THE CLUES
def generate_clues(code, user_guess):

    #First off I just wanna check if the user gets matches a code
    if user_guess == code:
        #if it does, I've cracked it and we're ready to go
        return "CODE CRACKED!"
    #otherwise I'm going to find an empty list calledclues
    clues = []
    #then using the special enumerate function I'm going to go through the index and numbers again
    #(you could have done thi without enumberate by just saying indexical 0 and then adding to index for every iteration for loop. But it's kind of just say convenience function)
    for ind,num in enumerate(user_guess):
        #Then I will say if the number the user guess is equal to the code at the specific index location
        if num == code[ind]:    #index location
            #that I'n going to append the word "match"
            clues.append("Match")
        #else if the number is in the code then I append close
        elif num in code:
            clues.append("Close")
            #!!! I write the check for the match before I check If it's close or not.
    if clues == []:
        return ["Nope"]
    else:
        return clues

#RUN GAME LOGIC
print("Welcome Code Breaker!")

secret_code = generate_code()

clue_report = ''

while clue_report != "CODE CRACKED!":

    guess = get_guess()

    clue_report = generate_clues(guess, secret_code)
    print("here is the result of your guess:")
    for clue in clue_report:
        print(clue)
        #And this keeps going over and over and over again untill I actually have a clue report that says code cracked
        # because remember generate_clues returns "CODE CRACKED" once have actually gotten the correct code.






#print(type(x)) #it's string
