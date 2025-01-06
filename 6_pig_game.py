import random

def roll():
    roll= random.randint(1, 6)
    return roll


while True:

    players=input("Enter the number of players (2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            break
        else:
            print("Must be between 2 and 4 : ")
    else:
        print("Invalid input. Please enter a number between 2 and 4.")


max_score =50
player_score=[ 0 for _ in range (players)]

while max(player_score)<max_score:
    
    for i in range(players):
        
        print("\nPlayer number ",i+1, "turn has just started! \n")
        print("Your total score is :",player_score[i],"\n")
        current_score=0
        
        while True:
            should_roll=input("Would you like to roll? (y) ")
            if should_roll.lower()!="y":
                break

            value=roll()
            
            if value==1:
                print("You rolled a 1! Turns done! ")
                current_score=0
                break
            else:
                current_score+=value
                print(f"You rolled a {value}! ")


            print("Your current score is : ",current_score)
        
        player_score[i]+=current_score
        print("Your total score is: ",player_score[i])


max_score=max(player_score)
winning=player_score.index(max_score)
print("Player number",winning+1,"is the winner with the score of :",max_score )
