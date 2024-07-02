print("Hello, World!!")

# Assignment
Name = "USA"
Age = 2000
Gender = "Country"
pendingFees = True 
print (Name,Age,Gender,pendingFees)

print ("Types of name", type(Name))
print ("Types of name", type(Age))
print ("Types of name", type(Gender))
print ("Types of name", type(pendingFees))


# Operations
# Arthametic operation
# Addition
x= 8
y= 5

sum=(x+y)
print(sum)

# Multiplication
m=(x*y)
print(m)

# Division
D=(x/y)
print(D)

# Exponent
Exp=(x**y)
print(Exp)

#Floor Division
mm=(x//y)
print(mm)

# Modulus
mod= (x%y)
print(mod)


# Assignment Operator

# += add and assign

x += 10
print ("x += 10 ->",x)


# pyhton comparision operators

a= 22
b = 20 

print("a == b:", a == b) #(equal)

print("a != b:", a != b) #(not equal)

print("a > b:", a > b) #(greater than)

print("a < b:", a < b) #(less than)

print("a >= b:", a >= b) #(greater than or equals to)



#python logical operators
v= 20
u= 18

print (v and u)
print (v or u)
print (not a)

'''
this is multi line comment 
'''


# python identitynoperators
# is operator

a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b) # true, because both a and b point to the same object
print ( a is c) # false, because a and c point to different object

#python membership operators

#eg 1

fruit = "banana"
print("a" in fruit)
print("z" in fruit)


#eg 2
fruit = "apple"
print("a" not in fruit)
print("z" not in fruit)


# operator perecedence read yourself

#checking minimum value

g, h = 10, 20


#multi line asssign
i = 10
j = 20

min = i if i<j else j 

print = (min)

