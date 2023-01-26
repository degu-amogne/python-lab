"""
Name :- Ermiyas Lishan 
ID :- DBUR/1236
"""
import random

def play_game():
    three_options = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice ምርጫዎን ያስገቡ (rock, paper, scissors): ").lower()
    print(" ")
    print(f"( የእርሶ ምርጫ ) User Choices 👉 : " ,user_choice)
    c = 0
    
    while user_choice not in three_options:
        user_choice = input("Invalid choice! የተሳሳተ ምርጫ ነው ያስገቡት !! Please enter 'rock', 'paper', or 'scissors': ")

    
    computer_choice = random.choice(three_options)
    print("( የኮምፒውተር ምርጫ ) Computer Choices 👉 : ", computer_choice)
    print (" ")

    result = ""
    grade = " "
    if user_choice == computer_choice:
        grade = "( 😊 ከኮምፒዩተሩ ጋር እኩል ወጥተዋል ‼️😊 ) Draws"
        result = "draws"
        print(" ")
    elif user_choice == "rock" and computer_choice == "scissors":
        grade = "( እንኳን ደስ አሎት 💐 አሸንፈዋል 💐 ) you Win "
        result = "win"
        print(" ")
    elif user_choice == "paper" and computer_choice == "rock":
        grade = "( እንኳን ደስ አሎት 💐 አሸንፈዋል 💐 ) You Win "
        result = "win"
        print(" ")
    elif user_choice == "scissors" and computer_choice == "paper":
        grade = " (እንኳን ደስ አሎት 💐 አሸንፈዋል 💐 ) You Win"
        result = "win"
        print(" ")
    else:
        grade = "( ድጋሚ ይሞክሩ 😚 ተሸንፈዋል 😔 ) you Lose !!"
        result = "lose"
    print(grade + "!")
    return result
print(" ")
user_wins = 0
computer_wins = 0
draws = 0

while True:
    result = play_game()
    if result == "win":
        user_wins += 1
    elif result == "lose":
        computer_wins += 1
    else:
        draws += 1

        print(" ")
    print("( እርሶ ያሸነፉት ) User Wins 👍", user_wins)
    print("( ኮምፒውተር ያሸነፈው ) Computers Wins 👎", computer_wins)
    print("( እኩል የወጣችሁት) Draws 🤝", draws)
    print(" ")

    play_again = input("Do you want to play again ? ድጋሚ መጫወት ይፈልጋሉ መልሶ አዎ ከሆነ \"Yes\" ብለው ላኩልን ⁉️ (yes/no) ").lower()
    if play_again != "yes":
        print("ጌሙን ስለተጫወቱ እናመሰግናለን 🤝 , Thank you for playing this game! 🤝")
        break
