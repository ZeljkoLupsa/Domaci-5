"""
Napisati kod koji za datu osnovicu a i krak b jednakokrakog trougla
 racuna povrsinu i zapreminu tijela koje se dobija rotacijom trougla oko visine
 spustene na osnovicu.
"""
import math

a = 4
b = 5
h = math.sqrt (b*b - ((1/2) * a) * ((1/2) * a))

povrsina_baze = ((1/2) * a) * ((1/2) * a) *  math.pi
povrsina_tijela = b * ((1/2) * a) * math.pi
povrsina_kupe = povrsina_baze + povrsina_tijela
print('POVRSINA KUPE IZNOSI: ', povrsina_kupe)

zapremina_kupe = (povrsina_baze * h)/3
print('ZAPREMINA KUPE IZNOSI:', zapremina_kupe)