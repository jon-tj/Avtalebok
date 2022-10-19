
from datetime import date,time

class Avtale:
    def __init__(self,tittel, sted,dato,tid,varighet,personer):
        self.tittel=tittel
        self.sted=sted
        self.tid=tid
        self.dato=dato
        self.varighet=varighet
        self.personer=personer
    def __str__(self):
        return  self.tittel.upper()+": "+str(self.dato)+", kl "+str(self.tid)+" skal "+self.personerStreng()+" møte på "+self.sted+". Planlagt tid: "+str(self.varighet)+" minutter."
    def personerStreng(self):
        result=self.personer[0]
        for i in range(1,len(self.personer)-1,1):
            result+=", "+self.personer[i]
        if(len(self.personer)>1): result+=" og "+self.personer[-1]
        return result

#region get input functions
def tryint(prompt):
    try:
        return int(input(prompt))
    except:
        print("Verdien du skrev inn kunne ikke leses som et tall.")
        if(input("Prøv igjen? [y/n]: ").lower()[0]=="y"): return tryint(prompt)
        return 0
def trydate(prompt):
    try:
        args=input(prompt).split('-')
        return date(int(args[0]),int(args[1]),int(args[2]))
    except:
        print("Verdien du skrev inn kunne ikke leses som en dato.")
        if(input("Prøv igjen? [y/n]: ").lower()[0]=="y"): return trydate(prompt)
        return 0
    
def trytime(prompt):
    try:
        args=input(prompt).split(':')
        return time(int(args[0]),int(args[1]))
    except:
        print("Verdien du skrev inn kunne ikke leses som en dato.")
        if(input("Prøv igjen? [y/n]: ").lower()[0]=="y"): return trydate(prompt)
        return 0
#endregion


def skrivAvtaleListe(avtaler,overskrift=""):
    if(not overskrift==""): print("_____"+overskrift+"_____")
    for i in range(len(avtaler)):
        print(f"\t{i}   {avtaler[i].tittel}" )        

#region Create/edit
def _lagAvtale():
    avtaleListe.append(lagAvtale())

def lagAvtale():
    print("Du skriver nå en ny avtale:")
    return Avtale(input("Tittel: "),input("Sted: "),trydate("Dato (yyyy-mm-dd): "), trytime("Tid (hh:mm): "),tryint("Varighet (minutter): "),input('Personer: ').split(','))

def velgAvtale():
    if(len(avtaleListe)==0): return -1
    try:
        i= int(input(f"Velg en avtale [0-{len(avtaleListe)-1}]: "))
    except:
        return velgAvtale("Angitt verdi ikke gjenkjent som heltall. Prøv igjen: ")
    if(i<0):
        return 0
    if(i>=len(avtaleListe)):
        return len(avtaleListe)-1
def _endreAvtale(i=-1):
    if i==-1: i=velgAvtale()
    if i==-1: return
    p=[
       f"Tittel: {avtaleListe[i].tittel}",
       f"Sted: {avtaleListe[i].sted}",
       f"Dato: {avtaleListe[i].dato}",
       f"Tid: {avtaleListe[i].tid}",
       f"Varighet: {avtaleListe[i].varighet}min",
       f"Personer: {avtaleListe[i].personerStreng()}",
       "Lagre og gå ut"
       ]
    for j in range(len(p)):
        print(str(j+1)+" "+p[j])
    j=int(input("Endre eller gå ut [1-7]: "))-1
    
    if j==0:
        avtaleListe[i].tittel=input("Ny tittel: ")
    elif j==1:
        avtaleListe[i].sted=input("Nytt sted: ")
    elif j==2:
        avtaleListe[i].date=trydate("Ny dato [yyyy-: ")
    elif j==3:
        avtaleListe[i].date=trydate("Ny tid [hh:mm]: ")
    elif j==4:
        avtaleListe[i].varighet=tryint("Ny varighet: ")
    elif j==5:
        avtaleListe[i].personer=input("Nye personer: ").split(',')
    
    if not j==6: _endreAvtale(i)

def _slettAvtale():
    i=velgAvtale()
    if i==-1: return
    print(f"Du har valgt avtale {i}:\n\t{avtaleListe[i]}")
    if input("Ønsker du å slette? [y/n]: ").lower[0]=="y":
        del avtaleListe[i]

def _avtaleDetaljer():
    i=velgAvtale()
    if i==-1: return
    print(f"Avtale {i}:\n\t{avtaleListe[i]}")
#endregion

#region read/write file
def _lagreAvtaleListe():
    lagreAvtaleListe(avtaleListe,input("Destinasjonsfil: "))
def lagreAvtaleListe(avtaler,destinasjonsfil="mine avtaler.txt"):
    result=""
    for a in avtaler:
        for p in [a.tittel, a.sted,str(a.dato),str(a.tid),str(a.varighet)]: result+=p+","
        for person in a.personer: result+=person+","
        result=result[:-1]+"\n"
    f = open(destinasjonsfil, "w")
    f.write(result)
    f.close()
def _lesAvtaleListeFraFil():
    for avtale in lesAvtaleListeFraFil(input("Les fra fil: ")):
        avtaleListe.append(avtale)
def lesAvtaleListeFraFil(fil):
    f = open(fil, "r")
    tekst=f.read()
    f.close()
    avtaler=[]
    for avtale in tekst.split('\n'):
        args=avtale.split(',')
        if(len(args)<4): continue
        dato=args[2].split('-')
        tid=args[3].split(':')
        personer=args[:4]
        avtaler.append(Avtale(args[0],args[1],date(int(dato[0]),int(dato[1]),int(dato[2])),
                              time(int(tid[0]),int(tid[1]),int(tid[2])),int(args[4]),personer))
    return avtaler
#endregion

#region search functions
def avtalerGittDato(avtaleListe,dato):
    return søkAvtaler(avtaleListe,lambda avtale:date==avtale.date)
def avtalerGittTittel(avtaleListe,tittel):
    return søkAvtaler(avtaleListe,lambda avtale:tittel in avtale.tittel)
def _søkAvtaler():
    a=input("Søkeord: ")
    kriterie=lambda avtale:a in (avtale.tittel+avtale.sted)
    resultater=søkAvtaler(avtaleListe,kriterie)
    skrivAvtaleListe(resultater,f"Ditt søk ga {len(resultater)} resultater")
def søkAvtaler(avtaleListe,condition):
    result=[]
    for avtale in avtaleListe:
        if condition(avtale): result.append(avtale)
    return result
#endregion

def meny():
    print("Avtaleboka mi:")
    if(len(avtaleListe)==0): print("\tDu har ikke lagd noen avtaler enda.")
    else: skrivAvtaleListe(avtaleListe)
    handlinger=["Lag ny avtale",
                "Les inn avtaler fra fil",
                "Skriv avtaler til fil",
                "Søk i avtaler",
                "Avslutt"]
    funksjoner=[_lagAvtale,_lesAvtaleListeFraFil,_lagreAvtaleListe,_søkAvtaler,lambda:None]
    
    #Hvis vi ikke har noen avtaler enda, er det ikke vits å vise disse handlingene til brukeren.
    if(len(avtaleListe)>0):
        handlinger.insert(1,"Endre avtale")
        handlinger.insert(2,"Slett avtale")
        handlinger.insert(3,"Se avtaledetaljer")
        funksjoner.insert(1,_endreAvtale)
        funksjoner.insert(2,_slettAvtale)
        funksjoner.insert(3,_avtaleDetaljer)
    
    for i in range(len(handlinger)):
        print(f"{str(i+1)}: {handlinger[i]}")
    i=int(input(f"Velg en handling [1-{len(handlinger)}]: "))-1
    funksjoner[i]()
    if(not handlinger[i]=="Avslutt"): meny()

avtaleListe=[]
if __name__=="__main__":
    meny()
    