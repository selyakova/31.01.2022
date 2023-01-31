
from Oma_modul import *
palgad=[]
nimed=[]
#palgad=loe_failist("Palgade_file.txt")
#print(palgad)
#nimed=loe_failist("Nimede_file.txt")
#print(nimed)

while True:
    print("-----------------------") 
    print("0-loe failist \n1-andmete lisamine \n2-salvestame failisse \n3-kustuta nimi järgi\n4-kellel on suurem palk "))
    v=int(input())
    if v==0:
        palgad=[]
        nimed=[]
        palgad=loe_failist("Palgade_file.txt")
        nimed=loe_failist("Nimede_file.txt")
        print(palgad)
        print(nimed)       
    elif v==1:
        palgad, nimed=elem_listisse(palgad,nimed)
        print(palgad)
        print(nimed)

    elif v==2:
        list_failisse(palgad,"Palgade_file.txt")
        list_failisse(nimed,"Nimede_file.txt")

    elif v==3:
        palgad,nimed=kustutamine(input("Sisesta nimi: "),palgad,nimed)
        print(palgad)
        print(nimed)

    elif v==4:
        maksimaalne_palk(palgad,nimed)



