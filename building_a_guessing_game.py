secret_word = "Giraffe"
guess_word = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

if guess_count == 0:
    print("The secret word starts with letter G and ends with e")

while secret_word != guess_word and not(out_of_guesses):
    if guess_count < guess_limit:
        print("You have " + str(guess_limit - guess_count) + " guesses left")
        guess_word = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True


if out_of_guesses:
    print("Sorry...You are out of guesses")
else:
    print("Your guess is correct, You Win!!")