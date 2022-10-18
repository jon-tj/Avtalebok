
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

def _lagAvtale():
    avtaleListe.append(lagAvtale())

def lagAvtale():
    print("Du skriver nå en ny avtale:")
    return Avtale(input("Tittel: "),input("Sted: "),trydate("Dato (yyyy-mm-dd): "), trytime("Tid (hh:mm): "),tryint("Varighet (minutter): "),input('Personer: ').split(','))
def skrivAvtaleListe(avtaler,overskrift=""):
    if(not overskrift==""): print("_____"+overskrift+"_____")
    for i in range(len(avtaler)):
        print(f"\t{i}   {avtaler[i].tittel}" )

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
    handlinger=["Lag ny avtale","Les inn avtaler fra fil","Skriv avtaler til fil","Søk i avtaler","Avslutt"]
    funksjoner=[_lagAvtale,_lesAvtaleListeFraFil,_lagreAvtaleListe,_søkAvtaler,lambda:None]
    for i in range(len(handlinger)):
        print(f"{str(i+1)}: {handlinger[i]}")
    i=int(input("Velg en handling [1-5]: "))
    funksjoner[i-1]()
    if(not i==5): meny()

avtaleListe=[]
if __name__=="__main__":
    meny()
    
