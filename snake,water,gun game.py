import random
list=['s','w','g']

chance = 10
no_of_chance =0
computer_point = 0
human_point = 0

print("\t\t\t snake, water, gum game \n \n")
print("s for snake \n w for water \n g for game\n")


while no_of_chance < chance:
     _input = input('snake, water, gum:')
     _random= random.choice(list)

     if _input == _random:
         print("tie both a point to each \n")


     elif _input =="s" and _random =="g":


        
         computer_point = computer_point +1
         print(f"your guess {_input} and computer guess is {_random} \n")
         print("computer wins 1 point \n")
         print(f"computer point is {computer_point} and your point is {human_point} \n")

     elif _input =="s" and _random =="w":
         human_point = human_point +1
         print(f"your guess {_input} and computer guess is {_random} \n")
         print("human wins 1 point \n")
         print(f"computer point is {computer_point} and your point is {human_point} \n")

     elif _input == "w" and _random =="s":
        computer_point = computer_point +1
        print("your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer point is {computer_point} and your point is {human_point} \n")

     elif _input =="w" and _random =="g":
         human_point = human_point + 1
         print("your guess {_input} and computer guess is {_random} \n")
         print("computer wins 1 point \n")
         print(f"computer point is {computer_point} and your point is {human_point} \n")

     elif _input == "g" and _random == "w":
      computer_point = computer_point + 1
      print("your guess {_input} and computer guess is {_random} \n")
      print("computer wins 1 point \n")
      print(f"computer point is {computer_point} and your point is {human_point} \n")

     elif _input == "g" and _random == "s":
        human_point = human_point + 1
        print("your guess {_input} and computer guess is {_random} \n")
        print("human wins 1 point \n")
        print(f"computer point is {computer_point} and your point is {human_point} \n")

else:
    print("you have input wrong option \n")

    no_of_chance = no_of_chance +1
    print("human wins 1 point \n")
    print(f"computer point is {computer_point} and your point is {human_point} \n")


    if computer_point == human_point:
         print("TIE")

    elif computer_point> human_point:
         print("computer wins and you (looses")

    else:
        print("you win and computer loose")

print(f" your point is {human_point} and computer point is {computer_point} \n")
print("GAME OVER")