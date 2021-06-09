#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: June 9, 2021
# This program rounds numbers depending on the users input


# greet the user
def greet():
    print("Hello! This program will round a number for you!")


# this is the rounding function
def rounder(num, num_round):
    # makes the number larger by a factor of 10 * the number of decimal
    # places requested by the user
    num[0] = (num[0] * (10**num_round))

    # if the number is negative then we substract 0.5
    # and the oposite for positive, this is so that
    # any number with .5 will round correctly
    if (num[0] < 0):
        num[0] = num[0] - 0.5
    else:
        num[0] = num[0] + 0.5

    # turn it into an integer to get rid of all those pesky decimals
    num[0] = int(num[0])
    # now move the decimal place back to where it was originally
    num[0] = (num[0] / (10**num_round))

    if (num_round == 0):
        num[0] = int(num[0])


# main function
def main():
    # get the users inputs
    num = input("What is the number you wish to round: ")
    num_round = input("How many decimal places do you want: ")

    # make sure the users num can be an integer or float
    try:
        # make the array so that we can pass by reference
        num_array = []
        num = float(num)
        num_round = int(num_round)

        # if the rounder is less than 0 it is invalid input
        if(num_round < 0):
            print("You can not round to a negative number")
            main()

        # append the users number to the array so that we can pass it
        num_array.append(num)

        # call the rounding function
        rounder(num_array, num_round)

        # print the result to the user
        print(num_array[0])

    # if an error arose when converting the inputs
    except ValueError:
        print("Numbers were not acceptable")
        main()


# get the program started
if __name__ == "__main__":
    greet()
    main()
