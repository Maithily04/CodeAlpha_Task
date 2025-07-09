import random

def hangman():
    # 1. Predefined list of words
    word_list = ["apple", "robot", "chair", "pizza", "grape"]
    
    # 2. Choose a random word
    secret_word = random.choice(word_list)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6
    
    # 3. Create a display list with underscores
    display_word = ["_" for _ in secret_word]

    print("Welcome to Hangman!")
    print("Guess the word. You have 6 incorrect guesses.\n")

    # 4. Main game loop
    while wrong_guesses < max_wrong_guesses and "_" in display_word:
        print("Word: " + " ".join(display_word))
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.\n")
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    display_word[i] = guess
        else:
            wrong_guesses += 1
            print(f"Wrong guess! You have {max_wrong_guesses - wrong_guesses} tries left.\n")

    # 5. Game end conditions
    if "_" not in display_word:
        print("Congratulations! You guessed the word: " + secret_word)
    else:
        print("Game over! The word was: " + secret_word)

# Run the game
hangman()
