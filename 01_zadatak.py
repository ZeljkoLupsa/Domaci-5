"""
Napisati kod koji za date katete a i b (a < b) pravouglog trougla racuna povrinu
 i zapreminu tijela koje se dobija rotacijom trougla oko manje katete.
"""
import math

a = 5
b = 7
c = math.sqrt(a*a + b*b)
#print(c)
baza = b * b * math.pi
#print(baza)
tijelo = c * b * math.pi
#print(tijelo)

povrsina = baza + tijelo
print('POVRSINA KUPE IZNOSI:' , povrsina)

zapremina_kupe = (baza*a)/3
print('ZAPREMINA KUPE IZNOSI: ', zapremina_kupe)


