import random

words = ["snake","water","gun"]

print("""


=== 🐍 Snake – 💧 Water – 🔫 Gun : Game Rules ===

Welcome to the Snake Water Gun game!

=== Choices ===

You can choose one option:

- Snake
- Water
- Gun

=== Winning Rules ===

- Snake drinks Water → Snake wins 🐍

- Water damages Gun → Water wins 💧

- Gun kills Snake → Gun wins 🔫

=== Draw Rule ===

If both you and the computer choose the same option, the game is a draw.

== Example ==

You: Snake | Computer: Water → You win

You: Gun | Computer: Snake → You win

You: Water | Computer: Water → Draw

=== Choose wisely and enjoy the game! ===


""")

while True:

    computer = random.choice(words)
    user = input("Choose ('Snake','Water','gun')  or Enter 'Stop' to stop the game: ").strip().lower()
    if user == "stop":
        print("Thanks for playing")
        break
    if user not in words:
        print("invalid choice, pls choose ('snake','water','Gun')")
        continue
    if computer == user:
        print(f"You = {user} and Computer = {computer}")   
        print("Its a draw")
    elif (computer == "snake" and user == "water") or (computer == "water" and user == "gun") or (computer == "gun" and user == "snake"):
        print(f"You = {user} and Computer = {computer}")   
        print("Computer won")
    else:
        print(f"You = {user} and Computer = {computer}")  
        print("You won")
