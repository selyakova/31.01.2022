def loe_failist(file:str)->list:
    """Loeme failist read ja lisame järjendisse
    :param str file: Faili nimetus
    """
    f=open(file,'r',encoding="utf-8-sig")
    mas=[]
    for rida in f:
        mas.append(rida.strip())
    f.close()
    return mas

def list_failisse(mas:list,file:str):
    """Salvestame loetelu faillisse
    :param str file: Faili nimetus
    :param list mas: loetelu
    """
    f=open(file,"w",encoding="utf-8-sig")
    for item in mas:
        f.write(item+"\n")
    f.close()

def elem_listisse(palgad:list,nimed:list):
    n=int(input("Mitu inimesi lisame?"))
    for j in range(n):
        nimi=input("Nimi: ")
        nimed.append(nimi)
        palk=input("Palk: ")
        palgad.append(palk)
    return palgad,nimed

def kustutamine(nimi:str,palgad:list,nimed:list):
    n=nimed.count(nimi)
    pos=0
    for j in range(n):
        ind=nimed.index(nimi,pos)
        pos=ind
        nimed.remove(nimi)
        palgad.pop(ind)
    return palgad,nimed
#def str_to_int(mas: list)->list:
#    for m in mas:
#        ind=mas.index(m)
#        m=mas.pop(ind)
#        m=int(m)
#        mas.insert(m,)
#    return mas
def maksimaalne_palk(palgad:list,nimed:list):
    #for palk in palgad:
    #    if rida.isdigit():
    #        mas.append(int(rida).strip())
    #    else:
    #        mas.append(rida.strip())
    p=list(map(int,palgad))
    max_palk=max(palgad)
    n=palgad.count(max_palk)
    pos=0
    print(f"Suurem palk on {max_palk} eur\nInimeste nimed: ")
    for j in range(n):
        ind=palgad.index(max_palk,pos)
        nimi=nimed[ind]
        print(f"{nimi}")
        pos=ind+1

    


