import random
the_number = random.randint(100,999)
print(the_number)
def main(number):
    if number == the_number: #for true answer
        print('Correct answer!')
        exit()
    for i in str(number):
        for j in str(the_number):
            if i == j and (str(number).index(i) == str(the_number).index(j)): #for one true digit in right place
                print('Fermi!')

                take_number()
    for i in str(number):
        for j in str(the_number):
            if i == j and (str(number).index(i) != str(the_number).index(j)): #for correct digit but wrong place
                print('Pico!')

                take_number()
    else:
        print('Bagels!')

        take_number()

def take_number():

    while True:
        your_guess = int(input("Enter a number from 100 to 999: "))
        if your_guess < 100 or your_guess > 999:
            print("Your guess is not in the limits.")
            continue
        else:
            main(your_guess)

take_number()

