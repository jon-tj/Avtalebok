# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 12:27:40 2022

@author: PieHu
"""

mineSteder={}
    
# oppgave G
class Sted: 
    def __init__(self,id, navn,gatenavn, postnummer, poststed): 
        self.id = id
        self.navn = navn
        self.gatenavn = gatenavn
        self.postnummer = postnummer
        self.poststed = poststed
        
    def __str__(self):
        return f'Sted({self.id}, {self.navn}, {self.gatenavn},{self.postnummer},{self.poststed}'

mineSteder["Ikke angitt"]=Sted("Ikke angitt",0,0,0,0)

# Oppgave H  
def lagNyttSted():
     id=input("id: ")
     sted = Sted(id, input("navn: "), input("gatenavn: "), input("postnummer: "), input("poststed: "))
     mineSteder[id]=sted
 
'''
Format på sted fil:
    id;navn;gatenavn;postnummer;poststed
'''
def lastInnStederFraFil(fildestinasjon):
  steder=open(fildestinasjon).read().split('\n')
  for i in range(len(steder)):
    verdi=steder[i].split(';')
    if(len(verdi)<5): continue #ikke last inn tomme/ufullstendige steder
    mineSteder[verdi[1]]=Sted(verdi[0],verdi[1],verdi[2],verdi[3],verdi[4], )

def lagreStederTilFil(fildestinasjon):
  result=""
  for s in mineSteder:
      result+=f"{mineSteder[s].id};{mineSteder[s].navn};{mineSteder[s].gatenavn};{mineSteder[s].postnummer};{mineSteder[s].poststed}\n"
  f = open(fildestinasjon, "w")
  f.write(result)
  f.close()
