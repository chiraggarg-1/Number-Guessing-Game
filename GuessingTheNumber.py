import random
random_number = random.randint(1,100)

while True:
    try:
        guess_number = int(input("Enter the Any Number From 1 to 100 "))
        if guess_number < random_number:
            print("Number is Too Low!!!")

        elif guess_number > random_number:
            print("Number is Too High!!!")

        else:
            print("Congratulations! You Guessed The Number")
            break

    except ValueError:
        print("Please Enter Valid Input")
