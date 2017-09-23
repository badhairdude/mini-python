import random

def hangMan():
    print('''

    Welcome to Chris's Hangman Game!

    Here are the rules:

    Type 'random' for a random word to be generated. (recommended if playing solo). Otherwise, type a word for the second player to guess

    You or your opponent will have 8 guesses or else you lose!

    GOOD LUCK!
    ''')

    word_input = input("Enter the word 'random' or a custom word to start.  ").lower()

    guesses = 8

    random_list = ['chocolate', 'banana', 'chair', 'building','rocket']
    final_guess = []

    if word_input == 'random':
        random_choice = random.randint(0,len(random_list)-1)
        final_word = random_list[random_choice]
        #to add hangman status
        for x in range((len(final_word))):
            final_guess.append("")
    else:
        final_word = word_input
        for x in range(len(final_word)):
            final_guess.append("")
        #to add hangman status

    blanks = "_" * len(final_word)
    for num in range(guesses, 0 , -1):


        attempt = input('What is your guess? You have ' + str(num) + ' guesses remaining. ')

        for letters in range(len(final_word)):
            if final_word[letters] in attempt:
                blanks = blanks[:letters] + final_word[letters] + blanks[letters+1:]
        for letters in blanks:
            print(letters, end = ' ')
        if blanks == final_word:
            print("You win! " + 'The word was ' + final_word)
            break
    if blanks != final_word:
        print('You lose!' + " The word was " + final_word)
    again = input("Play again? (yes or no) ").lower()
    if again == "yes":
        hangMan()
    else:
        return

hangMan()
