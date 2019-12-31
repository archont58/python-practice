from random import randint

user_number = 0
secret_number = randint(1, 100)
tries = 0

while True:
    user_number = input("Enter a number from 1 to 100: ")
    try:
        user_number = int(user_number)
    except ValueError:
        print("Enter the number!")
        continue

    if user_number < secret_number:
        tries += 1
        print("Too small number!")
    elif user_number > secret_number:
        tries += 1
        print("Too many number!")
    else:
        tries += 1
        print("You guessed it! It took you " + str(tries) + "  tries")

        yes = ('yes', 'Yes', 'y', 'Y')
        no = ('no', 'No', 'n', 'N')

        while True:
            a = input("Would you like to play again? (yes/no, y/n) ")
            if a not in yes and a not in no:
                print("Incorrect answer!")
                continue
            else:
                break

        if a in yes:
            user_number = 0
            secret_number = randint(1, 100)
            tries = 0
            continue
        elif a in no:
            break
