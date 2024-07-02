#if statement example
a = 15

if(a>12):
    print('15 is more than 12')
    # if true it will print if ot empty

#if-else statement 

if (10>5):
    print("wrong")
else:
    print("10 is greater than 5")


#nested if statement
x = 41

if x > 10:
    print("Above ten")
    if x > 20:
        print("and also above 20")

    else:
        print("but not above 20")
#parent true  vhayo vhane matrai vitra ko execute huncha


#if-elif ladder statement

i = 25
if (i == 10):
    print("i is 10")
elif (i == 15):
    print("i is 15")
elif (i == 20):
    print("i is 20")
else:
    print("i is not present")

#shorthand if-else 
i= 20
if i == 1:
    pass
elif i==20:
    print("Hello")



#handling user input

name = input("What is your name?")
print("Welcome",name)


