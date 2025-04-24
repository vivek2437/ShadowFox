import random

# Word list and hints
words_with_hints = {
    "python": "A popular programming language",
    "hangman": "A classic word guessing game",
    "internship": "A training program for students",
    "github": "A platform for version control",
    "algorithm": "A step-by-step problem-solving procedure"
}

# Choose a random word and its hint
word, hint = random.choice(list(words_with_hints.items()))
word = word.lower()
guessed_letters = []
tries = 6

# Hangman stages
stages = [
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / 
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |    
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |    
       |
    """,
    """
       ------
       |    |
       |    O
       |    |
       |    
       |
    """,
    """
       ------
       |    |
       |    O
       |    
       |    
       |
    """,
    """
       ------
       |    |
       |    
       |    
       |    
       |
    """
]

# Display intro
print("Welcome to Hangman!")
print(f"Hint: {hint}")
print("_ " * len(word))

# Game loop
while tries > 0:
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetical letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        tries -= 1
        print("Wrong guess!")
    else:
        print("Good guess!")

    # Show current progress
    display_word = [letter if letter in guessed_letters else "_" for letter in word]
    print(" ".join(display_word))
    print(stages[6 - tries])

    # Check win condition
    if "_" not in display_word:
        print("Congratulations! You guessed the word.")
        break

# Check loss
if tries == 0:
    print(f"Sorry, you're hanged! The word was '{word}'.")
