"""
Dat je cetvorocifreni prirodan broj. Stampati poruku "Super"
ako vazi a c = b d
"""
numbers=[1,1,1,1]
#print(numbers[0:3])


def provjera(abcd):
    if abcd[0:1] == abcd[2:3]:
        return("super")
    else:
        return("Nije super")

print(provjera(numbers))