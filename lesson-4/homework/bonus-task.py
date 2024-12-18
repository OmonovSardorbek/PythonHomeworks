import random
mylist = ['rock', 'paper', 'scissors']
point1, point2 = 0, 0

while not (point1 == 5 or point2 == 5):
    computer_choice = random.choice(mylist)  
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower() 
    if user_choice not in mylist:
        print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.\n")
        continue
    if computer_choice == user_choice:
        print(f"It's a draw! Computer chose {computer_choice}. Try again.\n")
    elif (computer_choice == "rock" and user_choice == "paper") or \
         (computer_choice == "paper" and user_choice == "scissors") or \
         (computer_choice == "scissors" and user_choice == "rock"):
        point2 += 1
        print(f"You win this round! Computer chose {computer_choice}.")
        print(f"Score -> Computer: {point1}, You: {point2}\n")
    else:
        point1 += 1
        print(f"You lost this round! Computer chose {computer_choice}.")
        print(f"Score -> Computer: {point1}, You: {point2}\n")

if point1 == 5:
    print(f"You Lost :( Final Score -> Computer: {point1}, You: {point2}")
elif point2 == 5:
    print(f"You Win :) Final Score -> Computer: {point1}, You: {point2}")
