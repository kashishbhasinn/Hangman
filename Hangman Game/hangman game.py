def display_word(word, guessed_letters):
    displayed = ""
    for letter in word:
        if letter in guessed_letters:
            displayed += letter
        else:
            displayed += "_"
    return displayed

def hangman():
    word_to_guess = input("Player 1, enter the word for guessing: ").lower()
    guessed_letters = []
    guesses_left = 5

    print("Let the guessing begin!")

    while True:
        print("\n" + display_word(word_to_guess, guessed_letters))
        guess = input("Player 2, guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            print("Wrong guess.")
            guesses_left -= 1

        if "_" not in display_word(word_to_guess, guessed_letters):
            print("\nCongratulations! You've guessed the word:", word_to_guess)
            break

        if guesses_left == 0:
            print("\nGame over! The word was:", word_to_guess)
            break

        print("Guesses left:", guesses_left)

if __name__ == "__main__":
    hangman()
