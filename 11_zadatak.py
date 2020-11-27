"""
Napisati kod koji provjerava da li je zbir cifara datog trocifrenog broja dvocifren broj
"""
import math

input_number = int(input('Unesite jedan trocifreni broj po zelji: '))

# x - prva cifra, y - druga cifra, z - treca cifra
def number_x(input_number):
    x = (input_number//10)//10
    return x

def number_y(input_number):
    y = (input_number // 10)%10
    return y

def number_z(input_number):
    z = input_number % 10
    return z

prva_cifra = number_x(input_number)
druga_cifra = number_y(input_number)
treca_cifra = number_z(input_number)

zbir = prva_cifra + druga_cifra + treca_cifra
if zbir % 10 == 0:
    print("Zbir cifara ovog broja je dvocifren broj")
else:
    print("Zbir cifara ovog broja je trocifren broj ")

# nedovoljno dobro odradjen zadatak
# nijesam znao kako da provjerim da li je dvocifren ili trocifren broj