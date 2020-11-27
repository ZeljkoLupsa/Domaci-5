"""
Napisati kod koji ucitava brojeve x, a i b i provjerava da li x pripada intervalu [a, b]
i stampa odgorvarajucu poruku: "pripada" ili "ne pripada"
"""
x = int(input("Unesite broj koji zelite provjeriti"))
a = 1
b = 100
def check_range(x):
    if x in range (1,100):
        return ("Pripada")
    else:
        return("Ne pripada")
print(check_range(x))
        
