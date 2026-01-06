from snake_water_gun_game import game
import tkinter as tk

root = tk.Tk()
root.title("Snake, Water, Gun Game")

rules_text = """
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

=== Example ===
You: Snake | Computer: Water → You win
You: Gun | Computer: Snake → You win
You: Water | Computer: Water → Draw

Choose wisely and enjoy the game!
"""

label = tk.Label(
    root,
    text=rules_text,
    justify="left",
    font=("Arial", 10)
)
label.pack(padx=10, pady=10)

button = tk.Button(
    root,
    text="Start Game",
    width=25,
    command=game   # ✅ correct
)
button.pack(pady=10)

root.mainloop()
