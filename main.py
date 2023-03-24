# print("Hello World")
# print('100' + '3')

# print(10 + 10) # sum
# print(10 - 10) # sub
# print(10 * 10) # multi
# print(10 / 10) # div
# print(10 // 10) # div with floor
# print(10 ** 2) # power
# print(2 % 3)

# Full_Name = 'dvir ezra'
#
# print(Full_Name.upper())
# print(Full_Name.lower())
# print(Full_Name.title())
# print(Full_Name[1:6])
# print(Full_Name[0:-1])
# print(Full_Name[::2])
# print(Full_Name[::-1])


import math


#
# x =int(input('please enter a number: '))
# y =int(input('please enter a number: '))
#
# print(x-y)
#
# z =int(input('please enter a number of pizza we order: '))
#
# e =print(z*8)
# e =(z*8)
#
# w =int(input('enter the number of eaters:'))
#
# d =(e//w)
# print(d)
#
# c = (d%z)
#
# print(c)


# name_from_the_user= input('enter the name: ')
#
# if name_from_the_user.count('i') == 2 or len(name_from_the_user)==8:
#    #if True
#    print('golden name')
# else:
#    print('naah not a golden name ')
#
#
# numbers1= int(input('pls enter the number: '))
# numbers2= int(input('pls enter the number: '))
# numbers3= int(input('pls enter the number: '))
#
# if numbers1 * numbers2 == numbers3:
#    print('hoolllllaaay')
# else:
#    print('such a loser')
#
################################################6
# numbers1=int(input('pls enther the number: '))
# numbers2=int(input('pls enther the number: '))
#
# if numbers1 > numbers2:
#    print(f'the small number is {numbers2} ')
# else:
#    print(f'the big number is {numbers1}')
#
##################################################7

# numbers1=int(input('pls enther the number: '))
# numbers2=int(input('pls enther the number: '))
# numbers3=int(input('pls enther the number: '))
#
# if  numbers2<numbers1>numbers3:
#    print(numbers1)
# elif numbers2>numbers3:
#    print(numbers2)
# else:
#    print(numbers3)
#
###################################################8

# numbers=int(input('enter the number: '))
#
# if numbers % 3 ==0:
#    print(True)
# else:
#    print(False)

####################################################9

# month = int(input("Enter a number between 1-12: "))
##year=int(input('enter year: '))
##if year % 400 == 0 or (year% 4== 0 and year % 100 != 0):
##    print(f'29 days in {month}')
#
# if month in [1, 3, 5, 7, 8, 10, 12]:
#    print("The month has 31 days.")
# elif month ==2:
#    print("The month has 28 or 29 days.")
# else:
#    print("The month has 30 days.")
#
####################################################10

# day_of_the_week=int(input('enter the number: '))
#
# num=int(day_of_the_week % 7)
# days_name=['sunday','mon','tus','wend','tus','fri','sat']
# print (num)
# if num==1:
#    print('sunday')
# elif num==2:
#    print('monday')
# elif num==3:
#    print('tusday')
#

# print (days_name[num-1])

##########################################################

# password = input('Enter the password: ')
#
# while not password.endswith('omg') and not \
#        password.startswith('mo'):
#    password = input('invalid password , Enter the password: ')
#
# print(f'the user insert a valid password is {password[0: 1]} ****')


################################################################# Loops Exercise 1#

# n = int(input("Enter a range: "))
#
# print("Result:", end=" ")
# while n >= 1:
#    print(n, end=" ")
#    n -= 1
################################################### 2
#
# word = input("Enter a word: ")  # ask user to enter a word
# reversed_word = word[::-1]     # reverse the word using slicing
# print("The reversed word is:", reversed_word)
#
#################################################### 3

# number = input("Enter a number: ")
# reversed_number = number[::-1]
# print(f'Result {reversed_number}')

############################################## 4

# for i in range(50):
#    if i % 7 == 0:
#        print(i, end=" ")
#    if i // 7 == 7:
#        break
############################################### 5

# x = [23, 4, -6, 23, -9, 21, 3, -45, -8]
#
# positive = []
# negative = []
#
# for i in x:
#    if i >= 0:
#        positive.append(i)
#    else:
#        negative.append(i)
#
# print("Result:")
# print("Positive:", positive)
# print("Negative:", negative)


############################################################# 10.3.23

# ef calculae_average(x, y, z):
#   '''

#   :param x:
#   :param y:
#   :param z:
#   :return:
#   '''
#   average = (x + y + z) // 3
#   print(average)


# um1 = int(input('enther the number: '))
# um2 = int(input('enther the number: '))
# um3 = int(input('enther the number: '))

# alculae_average(5, 10, 15)

########################################################### 8

# import math

# ef calculate_circumference(radius):
#   circumference = 2 * math.pi * radius
#   return circumference


# rint(calculate_circumference(5)) # Output: 31.41592653589793

########################################################### 9

# def add(x=0, y=0):
#    return x + y
#
# def sub(x=0, y=0):
#    return x - y
#
# def mul(x=0, y=0):
#    return x * y
#
# def div(x=0, y=0):
#    if y == 0:
#        raise ValueError("Cannot divide by zero")
#    return x / y
#
#
# x = float(input("Enter the first number: "))
# y = float(input("Enter the second number: "))
#
# print("Addition:", add(x, y))
# print("Subtraction:", sub(x, y))
# print("Multiplication:", mul(x, y))
# try:
#    print("Division:", div(x, y))
# except ValueError as e:
#    print(str(e))
#
###################################################### 10
#
# def getInRange(min, max):
#    while True:
#        num = int(input("Enter a number between {} and {}: ".format(min, max)))
#        if num >= min and num <= max:
#            print(num)
#            return num
#
#
# getInRange(10,20)
#
######################################################## 11
#
# def smallest_of_three(a, b, c):
#    return min(a, b, c)
#
######################################################### 12
#
# def smallest_of_all(*args):
#    return min(args)

# def classroom(num):
#    if num // 3:
#        print('fizz')
#    elif num // 5:
#        print('buzz')
#    if num // 3 and num // 5:
#        print('fizzbuzz')
#    else: print(num)
#
#
# classroom(10)


##############################################################
######################################################

# class Car:
#    def go(self):
#        print("Going......")
#
#    def breake(self):
#        print("Stoping")
#
#    def fill_it(self, num):
#        print(f"filling litter of gas {num}")
#
#
# mazda = Car()
# mazda.go()
#
# if isinstance(mazda, Car):  # בודק אם משתנה מסוג מזדה הוא מסוג קלאס קאר
#    """אם מזדה מסוג קאר"""
#    print(Car.go())
#
###################################
# import math
#
#
# class Circle():
#    def __init__(self, r):
#        self.r = r
#
#    def calc_area(self):
#        area = math.pi * self.r ** 2
#        return area
#
#    def calc_herkef(self):
#        herkef = 2 * math.pi * self.r
#        return herkef
#
#    def __str__(self):
#        return f"Circle -> radius : {self.r}"
#

# c1 = Circle(5)
# c2 = Circle(8)
#
# print(c1.calc_herkef())
# print(c2.calc_area())


#####################################

# a ='python'
# b = [1,2,3]
# aTup =(a,b)
# print(aTup[1][1:])

###################################### 24.03.23

# class BankAcount:
#    def __init__(self, balance=0, owner=' ', id=0, credit_score=0):
#        self.balance = balance
#        self.owner = owner
#        self.id = id
#        self.credit_score = credit_score
#
#    def deposite(self, amount):
#        self.balance += amount
#
#    def withdraw(self, amount):
#        self.balance += amount
#
#    def __str__(self):
#        return f'bank accoint {self.owner} id:{self.id}'
#
#    def __eq__(self, other):
#        return self.balance == other.balance
#
#    def __gt__(self, other):
#        return self.balance > other.balance
#
#    def __ge__(self, other):
#        return self.balance >= other.balance
#
#    def __len__(self):
#        return len(self.owner.split())
#
#
# acc1 = BankAcount(12, 'Dvir', 4, 5)
# acc2 = BankAcount(12, 'Raz', 4, 5)
# print(acc1 == acc2)

#################################################

class burger:
    def __init__(self, calories, topping, price):
        self.__calories = calories
        self.topping = topping
        self.__price = price

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, new_calories):
        if new_calories >= 0:
            self.__calories = new_calories

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if self.__price >= 0:
            self.__price = new_price

    def __str__(self):
        return f'Your burger price is {self.__price} \nCalories is {self.__calories} \nThe topping is {self.topping}'


McD = burger(500, 'carmel', 29.90)
print(McD)

##################################################################################

import datetime  # like all date with hour and minute
import time  # like a timer

x = datetime.datetime
y = time.time()

print(f'{x.day}/{x.month}/{x.year} \n{x.hour}:{x.second}')
