"""
12.03.2019, Salı, Ankara, Türkiye
Python Yazı & Tura Oyunu
Orçun Madran - madran.net
"""
from random import randint
yazi = 0
tura = 0
kere = int(input("Kaç kere? "))
for x in range(kere):
    gelen = randint(0,1)
    if gelen == 0:
        yazi += 1
    else:
        tura +=1
    print(str(x+1) + ". tur > Yazı:" +str(yazi) + " | Tura:" + str(tura))