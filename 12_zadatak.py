"""
Napisati kod koji za 3 data cijela broja x, y, z stampa najveci od njih.
"""
x = int(input('Unesite prvi broj: '))
y = int(input('Unesite drugi broj: '))
z = int(input('Unesite treci broj: '))

def check(x, y, z):
    if x>y and y>z:
        return (x, "je najveci broj")
    elif y>x and y>z:
        return (y, "je najveci broj")
    else:
        return (z,"je najveci broj")
print(check(x, y, z))