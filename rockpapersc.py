# import streamlit as st
# import random


# st.title('streamlite project')
# st.title('welcome to rock paper scissor game')



# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         return "It's a tie!"
#     elif (
#         (user_choice == "Rock" and computer_choice == "Scissors")
#         or (user_choice == "Paper" and computer_choice == "Rock")
#         or (user_choice == "Scissors" and computer_choice == "Paper")
#     ):
#         return "You win!"
#     else:
#         return "You lose!"


# def main():
#     st.title("Rock, Paper, Scissors Game")
#     user_choice = st.radio("Choose your move:", ("Rock", "Paper", "Scissors"))

#     choices = ["Rock", "Paper", "Scissors"]
#     computer_choice = random.choice(choices)

#     st.write(f"You chose: {user_choice}")
#     st.write(f"Computer chose: {computer_choice}")

#     result = determine_winner(user_choice, computer_choice)
#     st.write(result)

# if __name__ == "__main__":
#     main()


import streamlit as st
import random

def play_round(player_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
    else:
        result = "You lose!"
    
    st.write(f"You chose: {player_choice}")
    st.write(f"Computer chose: {computer_choice}")
    st.write(result)
    st.write('---')

def main():
    st.title("Rock Paper Scissors Game")
    
    rounds = st.sidebar.slider('Number of Rounds', min_value=1, max_value=10, value=3)
    
    st.write("Choose your move:")
    player_choice = st.radio('', ['Rock', 'Paper', 'Scissors'])
    
    if st.button('Play'):
        for _ in range(rounds):
            play_round(player_choice)

if __name__ == "__main__":
    main()