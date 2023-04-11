# Guessing Game Challenge....!!!!

# Guess the number and it tell you how close is your gussing power take you.

# Rules and Direction to play:

print("Welcome to Guessing Game!!!")
print("Rule's of the game:")
print("You have to guess any number between 1 to 100 .")
print("If your guess number within 10 digit range, You make WARM! guess.")
print("If your guess number further away from 10 digit range, You make COLD! guess.")
print("If your guess is closer to previous guess, You guess is GETTING WARMER! .")
print("If your guess is further from previous guess, You guess is GETTING COLDER! .")
print("LET'S PLAY..!!")

# 1 > Pguess > 100 print("OUT OF BOUNDS")
# Pguess<10 print("WARM!") Pguess>10 print("COLD!")
# NPguess near Pguess print("WARMER!") NPguess farther Pguess print("COLDER!")
# Pguess == num print("CORRECT GUESS!!")
# number += 1

from random import randint
num = randint(0,100)
num
#print(num)

guess_list = [0]

while True:
    guess_num = int(input("Guess the number between 1 to 100: "))

    if guess_num < 1 and guess_num >= 100:
        print("OUT OF BOUND..!!")
        print("Please try again:")
        continue
    if guess_num == num:
        print("CORRECT..!! You are Amazing.")
        print("You guess it in only {l}".format(l = len(guess_list)))
        break

    guess_list.append(guess_num)

    if guess_list[-2]:
        if abs(num - guess_num) < abs(num - guess_list[-2]):
            print("GETTING WARMER!")
        else:
            print("GETTING COLDER!")
    
    else:
        if abs(num - guess_num) <= 10:
            print("WARM!")
        else:
            print("COLD!")
