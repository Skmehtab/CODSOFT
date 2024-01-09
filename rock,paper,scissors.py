#importing random
import random

#conditions to win the game
def winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        print("It's a tie!")
    elif((user_choice=="paper" and computer_choice=="scissors") or
        (user_choice=="rock" and computer_choice=="paper") or
        (user_choice=="scissors" and computer_choice=="rock")):
        print("Computer wins the game.")
    else:
        print("You win the game.")
            
#getting information
def game():
    while True:
        #user selecting his move
        user_choice=input("Enter your move(rock/paper/scissors): ")
        print("You chose", user_choice)

        #computer selecting its move
        computer_choice=random.choice(['rock','paper','scissors'])
        print("Computer chose", computer_choice)
        
        #determing the winner
        result=winner(user_choice,computer_choice)
        print(result)
        
        #asking for another round
        play_again=input("Do you want to play again? (yes/no): ").lower()
        if play_again =="no":
            print ("Thanks for Playing.")
            break                        

if __name__ =="__main__":
    game()