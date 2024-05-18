import random

def get_top_of_range():
    while True:
        top_of_range = input("Give a range ")

        if top_of_range.isdigit():
            top_of_range = int(top_of_range)

            if top_of_range>0:
                return top_of_range
            else:
                print("Please enter a no larger than 0 next time")
        else:
            print("Please enter a right number")
           

def get_user_guess():
     while True:
        user_guess = input("Make a guess: ")
        if user_guess.isdigit():
            return int(user_guess)
        else:
            print('Please type a number next time.')


def main():
    top_of_range = get_top_of_range()
    random_no =  random.randint(0,top_of_range)
    gusses  = 0

    while True:
        gusses+=1
        user_no = get_user_guess()
        if user_no == random_no:
            print( "You got it")
            break
        elif user_no < random_no:
            print("Too low")
        else:
            print("Too high")
    print("You take ", gusses, "guess to win ")

if __name__ == "__main__":
    main()
