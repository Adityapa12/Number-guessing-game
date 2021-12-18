import random
number = int(input("enter a number :"))
winning_number = random.randint(1,100 )  
guess = 1
game_over = False

while not game_over:
    if number==winning_number:
        print(f"you win and you guess {guess} times ")

        game_over = True
    else:
        if number<winning_number:
            print("too low")
            
        else:
            print("too high")
        guess+=1
        number = int(input("guess again :")) 
        