"""

Exercise 1 : Create three variables (a,b,c) to same value of any integer &
do the following
a) Divide a by 10
b) Multiply b by 50
c) Add c value by 60""'
"""
a = b = c = 1000

# divide A by 10

a = a / 10

print(a)

# Multiply B by 50

b = b * 50

print(b)

# add C value by 60

c = c + 60

print(c)

"""
#Exercise 2 : Create a String variable of 5 characters and replace the 3rd
character with G 
"""

module = ["abc", "def", "pqr", "jkl", "stu", "vwx"]
module.pop(3)
print(module)
module[3] = "g"
print(module)

""" 
Exercise 3 : Create two values (a,b) of int,float data type & convert the
vise versa, Hint : convert a from int to float datatype & b from
float to int datatype
"""
a = 10   # int
b = 30.50  # float
print(float(a))
print(int(b))
