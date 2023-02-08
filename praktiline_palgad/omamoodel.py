from datetime import date, datetime
#8/02/23
def Lisa_andmed(i:list,p:list):
    """
    param List i: Inimeste järjend
    param list: Palgade järjend
    rtype: list, list
    """
    n=int(input("Mitu inimest:"))
    for j in range(n):
        nimi=input("sissesta nimi:")
        palk=int(input("sissesta palk:"))
        i.append(nimi)
        p.append(palk)
        return i,p
def kustutamine(i:list,p:list):
    """
    param list i: inimeste järjend
    param listp: palgade järjend
    rtype: list, lsit
    """
    nimi=input("Sissesta nimi:")
    if nimi in i:
        n=i.count(nimi)
        for j in range(n):
            i.pop(ind)
            ind=i.index(nimi)
            p.pop(ind)

    return i,p
def suurim_palk(i:list,p:list):
    """
    """
    palk=max(p)
    ind=p.index(palk)
    nimi=i[ind]
    return palk,nimi
def väike_palk(i:list,p:list):
    """
    """
    palk=min(p)
    ind=p.index(palk)
    nimi=i[ind]
    return palk,nimi
def sorteerimine(i:list,p:list):
    """
    """
    v=int(input("palk 1-kaheneb,2-kasvab?"))
    if v==1:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]<p[k]:
                    abi=p[j] 
                    p[j]=p[k] 
                    p[k]=abi 
                    abi=i[j] 
                    i[j]=i[k]
                    i[k]=abi
    elif v==2:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,):
               if  p[j]<p[k]:
                    abi=p[j] 
                    p[j]=p[k] 
                    p[k]=abi 
                    abi=i[j] 
                    i[j]=i[k]
                    i[k]=abi
    return i,p
def vordsed_palgad(i:list,p:list):
    """
    """
    dublikatid=[x for x in p if p.count(x)>1]
    dublikatid=list(set(dublikatid))
    #python govno ne kakoi eto ne high level language
    for palk in dublikatid:
        n=p.count(palk)
        k=-1
        print(f"{palk} saavad kätte järgmised inimesed:")
        for j in range(n):
            k=p.index(palk,k+1)
            nimi=i[k]
            print(nimi)