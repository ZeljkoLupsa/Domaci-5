"""
Napisati kod koji ucitava dva cijela broja m i n i stampa poruku
-x je djeljiv sa y
-x nije djeljiv sa y
Npr. 15 je djeljiv sa 3
     15 nije djeljiv sa 4
"""
n = int(input('Unesite prvi zeljeni broj: '))
m = int(input('Unesite prvi zeljeni broj: '))
def poruka(n, m):
    if n % m == 0:
        return (n , "je djeljiv sa ", m)
    else:
        return (n , "nije djeljiv sa ", m)

print(poruka(n, m))