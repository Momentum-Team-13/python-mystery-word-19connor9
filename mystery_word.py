import random


def guess_check(val, letters_guessed):
    valid = True
    if len(val) != 1:
        valid = False
    if val.isdigit():
        valid = False
    if val in letters_guessed:
        print(f"Letter {val} has been guessed already")
        valid = False
    return valid


def play_game():

    playing_game = True
    guess_word = (getWord())
    answer_list = list(guess_word)
    guess_list = []

    for letter in answer_list:
        guess_list.append("_")
    print(answer_list)
    print(guess_list)
    print(f"The word you must guess is {len(answer_list)} letters long")
    incorrect_letters = []
    letters_guessed = []
    while playing_game:

        is_valid = False
        while is_valid == False:
            val = input("Enter your guess:").lower()
            is_valid = guess_check(val, letters_guessed)
            if is_valid == False:
                print("Invalid input try again.")

        letters_guessed.append(val)
        if val not in answer_list:
            incorrect_letters.append(val)
            print(
                f"{val} is incorrect you have {8-len(incorrect_letters)} guesses left!")

        guess_list = guess(val, answer_list, guess_list)

        print(guess_list)

        if guess_list == answer_list:
            print("Congratulations, you won!")
            playing_game = False

        if len(incorrect_letters) >= 8:
            playing_game = False
            print("You have run out of guesses!")
            play_again = input("Do you want to play again? Y/N").lower()
            if play_again == "y":
                play_game()


def guess(val, answer_list, guess_list):
    index = -1
    for letter in answer_list:
        index += 1
        if letter == val:
            print(f"Letter {val} was correct at position {index+1}")
            guess_list[index] = answer_list[index]
    return guess_list


def getWord():
    with open("words.txt") as open_file:
        read_file = open_file.read()
       # print(read_file)
    word_list = read_file.split()
    random_word = random.choice(word_list)
###

###
    return random_word


if __name__ == "__main__":
    play_game()
