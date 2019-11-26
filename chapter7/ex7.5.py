# A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.
active=True

while active:
    Age=int(input("please enter your age : "))
    if Age >= 1 and Age <= 3:
        print("your ticket is free!! ")
    if Age > 3 and Age<=12:
        cost=10
        print("your tickrt is $10")
    if Age > 12 and Age <=100:
        cost = 15
        print("your tickrt is $15")
    if Age == 0 or  Age >100:
         active=False