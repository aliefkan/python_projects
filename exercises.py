def prime_numbers(num):
    for i in range(2, num):
        if num % i == 0:
            print(f"Not a prime number. Because divided by {i}")
            break
    else:
        return print(f"{num} is a prime number")

prime_numbers(17)



def new_sum(current_sum, value):
        current_sum += value
        return current_sum
    # TODO: it should return the new sum (current_sum + value) if the value is valid float or int otherwise it should return just current_sum.

if __name__ == "__main__":
    total = 0
    while True:
        user_input = input("Please enter an input: ")
        try:
            user_input = float(user_input)
            total = new_sum(total, user_input)
            print(total)
        except ValueError:
            pass
        if user_input == "":
            print(total)
            break



def calculator(operand_1, operand_2, operator):
    try:
        operand1 = float(operand_1)
        operand2 = float(operand_2)

    except ValueError as e:
        print(e)
    except SyntaxError as e1:
        print(e1)
    except TypeError as e3:
        print(e3)

if __name__ == "__main__":
    print(calculator("1a", 2.1, "+")) # An example

a = int(input("dsa"))
b = int(input("gfg"))
c = input("dfdf")
print(eval())

from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
import hashlib

Tk().withdraw()
path = askdirectory(title="Select directory")

walker = os.walk(path)
unique_files = dict()

for folder, sub_folder, files in walker:
    for file in files:
        filepath = os.path.join(folder, file)
        filehash = hashlib.md5(open(filepath, "rb").read()).hexdigest()

        if filehash in unique_files:
            os.remove(filepath)
            print(f"{filepath} has been removed")
        else:
            unique_files[filehash] = path

def calculator(operand_1, operand_2, operator):
    result = 0
    options = ("+", "-", "/", "*")
    if operator not in options:
        raise ValueError("Uncorrect operator. It should be + - / * ")
    if is_number(operand_1) == False or is_number(operand_2) == False:
        raise TypeError("Operand_1 or Opearand_2 has a letter ")
    operand_1_n = float(operand_1)
    operand_2_n = float(operand_2)
    if operator == "/" and (operand_2_n == 0 or operand_2_n == 0.0):
        raise ValueError("Cannot divide by zero ")
    result = eval(f"operand_1_n {operator} operand_2_n")
    return result

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    ## print(calculator("1a", 2.1, "+")) # An example
    try:
        print(calculator("1", 0.1, "/"))
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except TypeError as te:
        print(f"TypeError: {te}")


def calculator(operand_1, operand_2, operator):
    operators = ["*","/","-","+"]
    if operator not in operators:
        raise ValueError(f"{operator} is not one of '*,-,+,/' operators.")
    check_if_numeric(operand_1)
    check_if_numeric(operand_2)
    num1 = float(operand_1)
    num2 = float(operand_2)
    if float(operand_2) == 0.0:
        raise ValueError("You cannot divide by 0")
    return eval(f"num1{operator}num2")
def check_if_numeric(num):
    try:
        float(num)
        return True
    except ValueError:
        return print("your input is not valid.")

if __name__ == "__main__":
    try:
        print(calculator("1a", 0, "/")) # An example

    except (ValueError, TypeError) as ve:
        print(f"ValueError: {ve}")

bill = float(input("How much was the bill? "))
payers = int(input("How many workers are there? "))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15. "))
each_person_should_pay = bill/payers
print(each_person_should_pay*percentage + each_person_should_pay)

heigth = float(input("h: "))
weigth = float(input("w: "))
bmi = weigth / heigth**2
print("your bmi is: "+ str(bmi))


# TODO: Define your class here
class Triangle:
    def __init__(self, perpendicular1, perpendicular2, hypotenuse):
        self.side_a = perpendicular1
        self.side_b = perpendicular2
        self.side_c = hypotenuse
    def area(self):
        area = self.side_a*self.side_b/2
        print(area)

if __name__ == "__main__":
    a = int(input("Enter first perpendicular: "))
    b = int(input("Enter first perpendicular: "))
    c = int(input("Enter first hypotenuse: "))
    triangle = Triangle(a, b, c)# Create new instance here

triangle.area()







class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    def is_valid(self):
        if self.side_a >= self.side_b + self.side_c:
            return False
        elif self.side_b >= self.side_a + self.side_c:
            return False
        elif self.side_c >= self.side_a + self.side_b:
            return False
        else:
            return True
    def classify(self):
        if self.side_b == self.side_c and self.side_b == self.side_a:
            return "Equilateral"
        elif self.side_b == self.side_c and self.side_b != self.side_a:
            return "Isosceles"
        elif self.side_b == self.side_a and self.side_b != self.side_c:
            return "Isosceles"
        elif self.side_c == self.side_a and self.side_b != self.side_a:
            return "Isosceles"
        else:
            return "Scalene"


if __name__ == "__main__":
    triangle = Triangle(1, 10, 3)
    print(triangle.is_valid())


#less than

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"Dog {self.name} is barking!Bark Bark!")

    def __str__(self):               #this is not enough by itself to see the result while sorting!
        return f"{self.name} and my height is {self.height} cm."

    def __repr__(self):               #this is what you should use to see result!!
        return f"{self.name}"

    def __lt__(self, other_dog):  #here you use lessthan = __lt__ to sort
        return self.height < other_dog.height   #if you want to sort them based on their name just change self.name < other_dog.name it like that

dogs = [Dog("Milo", 30), Dog("Fido", 15), Dog("Pluto", 45)]
print("Before", dogs)
dogs.sort(reverse=True)  #sorting it as reversed (ascending order) but you can use sort() for normal way
print("After", dogs)

#different comparison methods
# def __lt__(self, other_dog):
#     return self.name < other_dog.name
# def __eq__(self,other_dog): #equal
#     pass
# def __ne__(self,other_dog): #not equal
#     pass
# def __gt__(self,other_dog): #greater than
#     pass
# def __le__(self,other_dog): #less or equal than
#     pass
# def __ge__(self,other_dog): #greater or equal than
#     pass

#aritmetic magic methods

class Depth:
    def __init__(self, depth):
        self.depth = depth

    def __str__(self):
        return f"{self.depth}cm"

    def __add__(self, other_box):
        return Depth(self.depth + other_box.depth)

box1_depth = Depth(10)
box2_depth = Depth(245)
box3_depth = box1_depth + box2_depth
print(box3_depth)

# #some other ones
# def __sub__(self, other_box): #substract
#     pass
# def __mul__(self, other_box): #multiplication
#     pass
# def __div__(self, other_box): #division
#     pass
# def __iadd__(self, other_box): # for +=
#     pass
# def __isub__(self, other_box): # -=
#     pass
# def __imul__(self, other_box): # *=
#     pass
# def __idiv__(self, other_box): # /=
#     pass

import math


class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def is_valid(self):
        # Don't worry if you did something else, there many ways to do the same.
        if self.side_a + self.side_b <= self.side_c or self.side_a + self.side_c <= self.side_b or self.side_b + self.side_c <= self.side_a:
            return False

        return True

    def classify(self):
        # Don't worry if you did something else, there many ways to do the same.
        if self.side_a == self.side_b == self.side_c:
            return f"Equilateral({self.side_a}, {self.side_b}, {self.side_c})"
        elif self.side_a != self.side_b != self.side_c:
            return f"Scalene({self.side_a}, {self.side_b}, {self.side_c})"
        else:
            return f"Isosceles({self.side_a}, {self.side_b}, {self.side_c})"

    def __str__(self):
        return f"{self.classify()} ({self.side_a}), ({self.side_b}), ({self.side_c})"

    def area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        area = math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))
        return area

    def __lt__(self, other_triangle):
        return self.area() < other_triangle.area()


if __name__ == "__main__":
    triangle1 = Triangle(2, 2, 2)
    triangle2 = Triangle(3, 4, 5)
    triangles = [triangle1, triangle2]
    print(f"Area of {triangle1} = {triangle1.area()} ")
    print(f"Area of {triangle2} = {triangle2.area()} ")
    if triangle1 < triangle2:

        print(f"{triangle1} < {triangle2}")
    else:
        print(f"{triangle2} < {triangle1}")


row_1 = ["■", "■", "■"]
row_2 = ["■", "■", "■"]
row_3 = ["■", "■", "■"]
map = [row_1, row_2, row_3]
print(f"{row_1}\n{row_2}\n{row_3}")
your_choice = input("Where do you want?\n")
h = int(your_choice[0])
v = int(your_choice[1])
map[v-1][h-1] = "X"
print(f"{row_1}\n{row_2}\n{row_3}")

import random
def x_o():
    row_1 = ["■", "■", "■"]
    row_2 = ["■", "■", "■"]
    row_3 = ["■", "■", "■"]
    map = [row_1, row_2, row_3]
    print(f"{row_1}\n{row_2}\n{row_3}")
    coordinates = ["11", "12", "13", "21", "22", "23", "31", "32", "33"]
    while True:
        your_choice = input("Where do you want (rowcolumn)?\n")
        if your_choice not in coordinates:
            print("This spot is taken!")
            print(f"{row_1}\n{row_2}\n{row_3}")
            continue
        index_1 = coordinates.index(your_choice)
        coordinates.pop(index_1)
        computer = random.choice(coordinates)
        index_2 = coordinates.index(computer)
        coordinates.pop(index_2)
        h = int(your_choice[0])
        v = int(your_choice[1])
        h1 = int(computer[0])
        v1 = int(computer[1])
        map[v - 1][h - 1] = "X"
        map[v1 - 1][h1 - 1] = "O"
        print(f"{row_1}\n{row_2}\n{row_3}")
        if map[0][0] == "X" and map[0][1] == "X" and map[0][2] == "X" or map[0][0] == "O" and map[0][1] == "O" and map[0][2] == "O":
            print(f"Congratulations to {map[0][0]}!")
            break
        elif map[1][0] == "X" and map[1][1] == "X" and map[1][2] == "X" or map[1][0] == "O" and map[1][1] == "O" and map[1][2] == "O":
            print(f"Congratulations to {map[1][0]}!")
            break
        elif map[2][0] == "X" and map[2][1] == "X" and map[2][2] == "X" or map[2][0] == "O" and map[2][1] == "O" and map[2][2] == "O":
            print(f"Congratulations to {map[2][0]}!")
            break
        elif map[0][0] == "X" and map[1][1] == "X" and map[2][2] == "X" or map[0][0] == "O" and map[1][1] == "O" and map[2][2] == "O":
            print(f"Congratulations to {map[0][0]}!")
            break
        elif map[0][2] == "X" and map[1][1] == "X" and map[2][0] == "X" or map[0][2] == "O" and map[1][1] == "O" and map[2][0] == "O":
            print(f"Congratulations to {map[1][1]}!")
            break
x_o()

score = input("enter number").split()
for i in range(len(score)):
    score[i] = int(score[i])
score.sort(reverse=True)
print(score[0])

score = input("enter number").split()
highest = 0
for i in score:
    if i > highest:
        highest = i
print(highest)

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    elif i % 3 != 0 and i % 5 == 0:
        print("Buzz")
    else:
        print(i)


num = 0
for i in range(1, 1001):
    num+=1
    if i != num:
        print(num)


import itertools
num_list = [2,3,4,4,5,5,5]
num = 4_000_000
result = list(itertools.permutations([2,3,4,4,5,5,5], r=7))
num_li = []
for i in result:
    a = result.index(i)
    i = int(''.join(map(str, result[a])))
    if i > num:
        if i in num_li:
            pass
        else:
            num_li.append(i)
    else:
        pass
print(num_li)
print(len(num_li))

#spelling bee(7 letters max)
from itertools import permutations
def perm(a, b):
    possible_words = []
    for i in range(2, a+1):
        generator = [''.join(p) for p in permutations(b, r=i)]
        possible_words += generator
        i += 1
    return possible_words
def word_finger(letters, middle_letter):
    lenght = len(letters)
    li =  perm(lenght, letters)
    word_list = []
    with open("word_list.txt", "r") as fin:
        for line in fin.readlines():
            for word in line.split(" "):
                if middle_letter in word:
                    if word in li:
                        if len(word) >= 4:
                            word_list.append(word)
                else:
                    pass
    return word_list
your_letters = input("Enter the letters: ")
the_constant_letter = input("Enter the constant one: ")
print(f"The words suits to your problem are; ", word_finger(your_letters, "g"))
print(f"And amount of words we found for you; ", len(word_finger("lapemxg", "g")))

def conc(list1, list2):
    list3 = []
    for i in list1:
        for j in list2:
            if list1.index(i) == list2.index(j):
                k = i+j
                list3.append(k)
    return list3
li1 = ["m", "na", "i", "ef"]
li2 = ["y", "me", "s", "kan"]
print(conc(li1, li2))

def square(list1):
    sqrtlist = []
    for i in list1:
        a = i*i
        sqrtlist.append(a)
    return sqrtlist
li = [1, 3, 6, 8]
print(square(li))


def count_by(x, n):
    list_ = []
    a = 0
    for i in range(n):
        a += x
        list_.append(a)
    return list_

li = [1, 2, 3, 4, 5]
str1 = '*'.join(str(e) for e in li)
print(str1)
ev = eval(str1)
print(ev)

#to multiply every item in a list
def grow(arr):
    splitted = '*'.join(str(num) for num in arr)
    return eval(splitted)

# giving the list of numbers in inverted way (if + then - if - then +)
def invert(lst):
    list_ = []
    for i in lst:
        i*=-1
        list_.append(i)
    return list_

def reverse_seq(n):
    nums = []
    while n > 0:
        nums.append(n)
        n -= 1
    return nums
print(reverse_seq(5))

def find_smallest_int(arr):
    return min(arr)

def check(seq, elem):
    if elem in seq:
        return True
    else:
        return False

def is_divide_by(number, a, b):
    if number % a == 0 and number % b == 0:
        return True
    else:
        return False# good luck

def count_sheep(n):
    murmur = ""
    for i in range(1, n+1):
        murmur += f"{i} sheep..."
        i+=1
    return murmur
def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))

def boolean_to_string(b):
    if b == True:
        return "True"
    else:
        return "False"
def boolean_to_string(b):
    return str(b)

def make_negative( number ):
    if number >0:
        return number*(-1)
    else:
        return number
def make_negative( number ):
    return -abs(number)

def rental_car_cost(d):
    price = 0
    if d >= 7:
        price += d*40-50
        return price
    elif d <= 7 and d >= 3:
        price += d*40-20
        return price
    else:
        price = d*40
        return price

def rental_car_cost(d):
  return d * 40 - (d > 2) * 20 - (d > 6) * 30 #if d>2 then it is True and True equals to 1

def minimum(arr):
    return min(arr)
    #your code here...

def maximum(arr):
    return max(arr)

def min(arr):
    low = arr[0]
    for i in arr[1:]:
        if i < low:
            low = i
    return low

def max(arr):
    high = arr[0]
    for i in arr[1:]:
        if i > high:
            high = i
    return high

def min(arr):
    return sorted(arr)[0]

def max(arr):
    return sorted(arr)[-1]


def sum_digits(number):
    return eval('+'.join(str(abs(number))))
print(sum_digits(-12))

def filter_list(l):
    integers = []
    for i in l:
        if type(i) == int or type(i) == float:
            integers.append(i)
    return integers
print(filter_list([1,2,1.5,'a','b']))

def get_sum(a,b):
    result = 0
    if a==b:
        return a
    else:
        if a > b:
            while b <= a:
                result += b
                b += 1
        else:
            while a <= b:
                result += a
                a += 1
    return result
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))
print(get_sum(-1,3))
def get_sum(a, b):
    return (a + b) * (abs(a - b) + 1) // 2 #formula is S = n(a + l)/2 n=number of integers a= first term l=last term
print(get_sum(-1,3))

def mxdiflg(a1, a2):
    x = ''.join(a1) #turn list into string
    b = "x"
    all_x = [pos for pos, char in enumerate(x) if char == b]
    y = ''.join(a2)
    c = "y"
    all_y = [pos for pos, char in enumerate(y) if char == c]
    max = 0
    for i in all_x:
        if all_x == []:
            i = -1
            if all_y == []:
                j = -1
                val = abs(i-j)
            else:
                for j in all_y:

                    if max < val:
                        max = val
            else:
                val1 = abs(i-j)
                if max < val1:
                    max = val1
    return max


a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(a1,a2))

a = [1,3,5]
b = [0,2,4]
max = 0
for i in a:
    for j in b:
        val = abs(i-j)
        if max < val:
            max = val
print(max)

def find_divisible(num1, num2):
    num_list = []
    for num in range(1500, 2701):
        if num % num1 ==0 and num % num2 ==0:
            num_list.append(str(num))
    return num_list
print(','.join(find_divisible(7, 5)))

def celsius_to_fahrenheit(degree ,celsius = 0, fahrenheit = 0):
    if fahrenheit > 0:
        if celsius > 0:
            raise ValueError
        return 1.8*degree+32
    elif celsius > 0:
        if fahrenheit > 0:
            raise ValueError
        return (degree-32)*0.5556
print(celsius_to_fahrenheit(30, celsius = 1 , fahrenheit = 1))
print(celsius_to_fahrenheit(50, celsius = 1))

def reversing_sentence(sentence):
    return sentence[::-1]
print(reversing_sentence("hey how are you doing?"))

def how_many_odd_even(list_of_nums):
    odds = []
    evens = []
    for num in list_of_nums:
        if num % 2 ==0:
            odds.append(num)
        else:
            evens.append(num)
    return f"odds: {odds}, {len(odds)} characters.\nevens: {evens}, {len(evens)} characters."
li = (3,6,3,7,45,21365,8,32,52,46,"23",True,"sad")
print(how_many_odd_even(li))

def type_of_item(list_of_items):
    dic = {}
    for item in list_of_items:
        type_of_each = type(item)
        if type_of_each == int:
            dic[item] = 'int'
        elif type_of_each == str:
            dic[item] = 'str'
        elif type_of_each == float:
            dic[item] = 'float'
        else:
            dic[item] = 'boolean'
    return dic
print(type_of_item(li))

lis = [1,2,3,4]

win = lis[index % len(lis)]
print(win)

def factorial(num):
    if num >= 0:
        if num == 0:
            return 1
        else:
            a=1
            for i in range(num, 0, -1):
                a *= i
        return a
print(factorial(5))
def factorial(num):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)

def upper_and_lower(sentence):
    letters = []
    upper = 0
    lower = 0
    for i in range(len(sentence)):
        letters.append(sentence[i])
    for char in letters:

        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        else:
            pass
    return upper, lower
print(upper_and_lower("asjofdsjoDFSJOFDS"))

def prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            return f"not a prime number"
    return f"prime number"
print(prime_number(7))

def perfect_number(number):
    total = 0
    for i in range(1, number):
        if number % i == 0:
            total += i
    if (total + number)/2 == number:
        return f"perfect number"
    else:
        return f"not perfect number"
print(perfect_number(28))

def reversing_sentence(sentence):
    return sentence[::-1]
def palindrome(sentence):
    reverse = reversing_sentence(sentence)
    if sentence == reverse :
        return "Palindrome"
print(palindrome("madam"))

code = "print('oldu mu oldu')"
code_2 = '''
def calc(x,y):
    return x*y
print("multiplication of 2 and 3 is: ", calc(2,3))
'''
exec(code)
exec(code_2)
def multiply(x,y):
    return x*y
def sum(a,b):
    return a+b
def musum(z,q):
    return sum(multiply(z,q),q)
print(musum(2,3))

decision = False
while not decision:
    ilk_sayi = float(input("ilk sayı"))
    ikinci_sayi = float(input("ikinci sayı"))
    islem = input("*,-,/,+ birini gir")
    if islem == "*":
        print(f"{ilk_sayi} * {ikinci_sayi} =", ilk_sayi*ikinci_sayi)
    elif islem == "-":
        print(f"{ilk_sayi} - {ikinci_sayi} =", ilk_sayi - ikinci_sayi)
    elif islem == "+":
        print(f"{ilk_sayi} + {ikinci_sayi} =", ilk_sayi+ikinci_sayi)
    elif islem == "/":
        print(f"{ilk_sayi} / {ikinci_sayi} =", ilk_sayi/ikinci_sayi)
    else:
        print("geçersiz işlem")
    print("başka bir işlem yapmak ister misin?")
    karar = input("")
    if karar == "hayır":
        decision = True

a = 14
b = 3
print(a%b)

liste = [1,2,3,4,5,6,7]
value = 0
for sayı in liste[1:]:
    if sayı % 2 == 0:

        value += sayı
        print(value)


class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def is_valid(self):
        # Don't worry if you did something else, there many ways to do the same.
        if self.side_a + self.side_b <= self.side_c or self.side_a + self.side_c <= self.side_b or self.side_b + self.side_c <= self.side_a:
            return False

        return True


class Equilateral(Triangle):
    def __str__(self):
        return f"Equilateral: ({self.side_a}), ({self.side_b}), ({self.side_c})"


class Scalene(Triangle):
    def __str__(self):
        return f"Scalene: ({self.side_a}), ({self.side_b}), ({self.side_c})"


class Isosceles(Triangle):
    def __str__(self):
        return f"Isosceles: ({self.side_a}), ({self.side_b}), ({self.side_c})"


def create_triangle(side_a, side_b, side_c):
    if side_b == side_c and side_b == side_a:
        return Equilateral(side_a, side_b, side_c)
    elif side_b == side_c and side_b != side_a:
        return Isosceles(side_a, side_b, side_c)
    elif side_b == side_a and side_b != side_c:
        return Isosceles(side_a, side_b, side_c)
    elif side_c == side_a and side_b != side_a:
        return Isosceles(side_a, side_b, side_c)
    else:
        return Scalene(side_a, side_b, side_c)


if __name__ == "__main__":
    triangle = Triangle(2, 2, 2)
