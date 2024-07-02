marks = float(input("Your Score: "))
if (marks > 90):
    print("Your Score is A.")
elif (marks > 75):
    print("Your Score is B.")
elif (marks > 65):
    print("Your Score is C.")
elif (marks > 40):
    print("Your Score is D.")
else:
    print("Your are failed.") 




# write a program to calculate the electricity bill(accept number of unit from user) according to the following criteria
'''
unit                       price
first 100 units            no charge
next 100 units             rs5 per unit 
after 200 units            Rs 10 per unit
'''
price = 0
unit = int(input("Number of input"))
if (unit==100):
    price = 0
    
elif (unit<200):
    price = (unit-100) * 5

elif(unit>200):
    price = (100*5) +(unit-200) * 10
    print(price)
