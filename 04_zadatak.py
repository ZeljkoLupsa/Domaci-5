"""
Napisati kod koji za datu osnovicu a i krak b jednakokrakog trougla racuna povrsinu 
i zapreminu tijela koje se dobija rotacijom trougla oko osnovice
"""
#u ovom slucaju visina trougla nam postaje poluprecnik baze
import math
a = 4
b = 7
r = math.sqrt(b*b - (a/2)*(a/2))
povrsina_baze = r * r * math.pi
povrsina_tijela = b * r * math.pi
povrsina_cijele_figure = povrsina_baze + povrsina_tijela
print('POVRSINA FIGURE: ', povrsina_cijele_figure)

zapremina_cijele_figure = (povrsina_baze * (a/2))/3 * 2
print('Zapremina dobijenog tijela iznosi:', zapremina_cijele_figure)