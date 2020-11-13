"""
Napisati kod koji za date katete a i b (a < b) pravouglog trougla
 racuna povrsinu i zapreminu tijela koje se dobija rotacijom oko hipotenuze.
"""
import math

a = 2
b = 4
c = math.sqrt(a*a + b*b)
r = math.sqrt(b*b-(c*c)*2/3)

baza = r * r * math.pi
velika_kupa = b * (2/3*c) * math.pi
manja_kupa = a * (1/3*c) *  math.pi
povrsina_tijela = velika_kupa + manja_kupa
print('POVRSINA DOBIJENOG TIJELA IZNOSI: ', povrsina_tijela)

zapremina_veceg_tijela = (baza * (2/3*c))/3
zapremina_manjeg_tijela = (baza * (21/3*c))/3
zapremnina_dobijenog_tijela = zapremina_manjeg_tijela + zapremina_veceg_tijela

print('ZAPREMINA DOBIJENOG TIJELA IZNOSI: ', zapremnina_dobijenog_tijela)