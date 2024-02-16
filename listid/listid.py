#vokaali = ["a, e, i, o, u, õ, ä, ö, ü"]

#konsonanti = "qwertpsdfghklzxcvbnmj"

#markid = punctuation

#v = k = m = t = 0

#tekst = input("Sisesta sõna või laused: ").lower()

#tekst_list = list(tekst)

#for sümbol in tekst_list:

#    if sümbol in vokaali:

#        v += 1

#    elif sümbol in konsonanti:

#        k += 1

#    elif sümbol in markid:

#        m += 1

#    elif sümbol == " ":

#        t += 1

#print("Vokaali:", v)

#print("Konsonanti:", k)

#print("Kirjuvahemärgid", m)

#print("Tühikud:", t)


#nimed = []

#for i in range(5):

#    nimi = input("Sisesta nimi: ").capitalize()

#    nimed.append(nimi)

#print("Loetelu oli: ", nimed)

#nimed.sort()

#print("Loetelu sorteeritud: ", nimed)

#for n in range(len(nimed)):

#    print(n + 1, ".", nimed[n], sep="")

#print("Vimasena oli lisatud: ", nimi)

#uued_nimed = []

#for nimi in nimed:

#    if nimi not in uued_nimed:

#        uued_nimed.append(nimi)

#print(uued_nimed)

#uued_nimed = list(set(nimed))


#vanused = []

#for i in range(5):

#    vanus = int(input("Sisesta vanus: "))

#    vanused.append(vanus)

#maksimum = max(vanused)

#minimum = min(vanused)

#summa = sum(vanused)

#keskmine = summa / len(vanused)

## Kuva ekraanile nimi koos vanusega

#for i in range(5):

#    print(nimed[i], "on ", vanused[i], "aastat vana")


#from random import *

#arvud = []

#N = int(input("Mitu rida joonistame? "))

#S = input("Sisesta sümbol: ")

## loendi täitmine

#for p in range(N):

#    arvud.append(randint(1, 100))

## diagrammi loomine

#for p in range(N):

#    print(arvud[p] * S)


#Indeks = ["TallinnNarva, Narva-Jõesuu,Kohtla-Järve,Ida-Virumaa, Lääne-Virumaa, Jõgevamaa,Tartu linnTartumaa, Põlvamaa, Võrumaa, ValgamaaViljandimaa, Järvamaa, Harjumaa, Raplamaa,Pärnumaa,Läänemaa, Hiiumaa, Saaremaa"]

#while True:

#    while True:

#        try:

#            indeks = int(input("Sisesta viienumbriline indeks: "))  # 10000,15478,98564

#            indeks_elemendide_arv = len(str(indeks))

#            if indeks_elemendide_arv == 5:

#                print("5 numbriline indeks")

#                break

#            else:

#                print("On vaja 5numbriline arv(indeks)")

#        except:

#            print("Vale andmetüüp!")

#    arv1 = indeks // 10000

#    print(arv1)

#    # symbolid = list(str(indeks))

#    print(f"Sa elad piirkonnas {Indeksid[arv1 - 1]}")


#rida = []

#N = randint(2, 25)

#for i in range(N):

#    rida.append(choice(ascii_uppercase))

#print(rida)

#kogus = int(input("Mitu elemendi vahetame oma vahel "))

#if len(rida) // 2 >= kogus:

#    for i in range(kogus):

#        a = rida[i]

#        rida[i] = rida[len(rida) - i - 1]

#        rida[len(rida) - 1 - i] = a

#print(rida)



#6
#from random import *
#from string import *

#nimekirja1=[]
#nimekirja=[]
#n=int(input("Nimekirja suurus: "))
#for i in range(n):
#    arv=randint(10,100)
#    nimekirja1.append(arv)
#    nimekirja.append(arv)
#maksimum=nimekirja[0]
#for arv in nimekirja:
#    if arv>maksimum:
#        maksimum=arv
#vajavarv=maksimum/len(nimekirja)
#for i in range(len(nimekirja)):
#    if nimekirja[i]==maksimum:
#        nimekirja[i]=vajavarv
#print(nimekirja1)
#print(nimekirja)
 

#9
#name = input("Sisestage oma nimi")
#if name.isalpha():
#    print("Tere {}!".format(name.capitalize()))
#    letter_count = len(name)
#    print("tähtede arv nimes:", letter_count)
#else:
#    print("nimi peab sisaldama ainult tähti")




#12 
#import random

#numbers = [random.randint(1, 100) for _ in range(10)]
#print("nimekirja:", numbers)

#min_index = numbers.index(min(numbers))
#max_index = numbers.index(max(numbers))
#numbers[min_index], numbers[max_index] 
#numbers[max_index], numbers[min_index]

#print("loend pärast min ja max väärtuste muutmist:", numbers)


#15