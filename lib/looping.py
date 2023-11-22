#!/usr/bin/env python3

def happy_new_year():
    countdown = 10
    
    while countdown > 0:
        print(countdown)
        countdown -= 1
    
    print("Happy New Year!")
    

def square_integers(int_list):
    square_intagers = [int * int for int in int_list]
    print(square_intagers)
    return square_intagers

def fizzbuzz():
    counter = 1

    while counter <= 100:
        if counter % 3 == 0 and counter % 5 == 0:
            print("FizzBuzz")
            counter += 1
        elif counter % 3 == 0:
            print("Fizz")
            counter += 1
        elif counter % 5 == 0:
            print("Buzz")
            counter += 1
        else:
            print(counter)
            counter += 1

