import math

x = 1
y = 2
alfa = 30
beta = 45
a = 22
b = 33

# a
rez1 = (x*x*x)//3 - 3*(y*y)+ (((x+1) / ((2*y)+3)))
print(rez1)

# b
rez2 = -5 * math.sqrt(x + math.sqrt(y))
print(rez2)

# c
rez3 = 1 +(1 / (2 + (1 / (3 + 1/4))))
print(rez3)

# d
rez4 = 3*math.sin(2*alfa)*math.cos(2*beta) - 5*math.tan(alfa+beta)*math.tan(alfa+beta)
print(rez4)

# e
rez5 = math.sqrt(a*a + b*b - 2*a*b*math.sin(alfa))
print(rez5)