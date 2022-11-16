# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 10:44:13 2022

@author: PieHu
"""

class Kategori:
  def __init__(self,navn,id,prioritet=1):
    self.navn=navn
    self.id=id
    self.prioritet=prioritet
  def __str__(self):
    priorityLevels=["lav","vanlig","høy","svært høy", "det brenner på dass"] 
    return self.navn+f"(id: {self.id}, prioritet: {priorityLevels[ self.prioritet-1]})"

mineKategorier={}
mineKategorier["Ikke angitt"]=Kategori(0,0,0)

#Merk at id til kategori ikke trenger å være int. Dette gjør at man kan lage mer sofistikerte søk i avtaleboka seinere :)
def lagNyKategori():
    id=input("Id: ")
    mineKategorier[id]=Kategori(input("Navn: "), id, int(input("Prioritet (1-5): ")))

'''
Eksempelformat på kategori fil:
    minkategori;1;1 <- Vil vises som minkategori (id: 1, prioritet: lav)
'''
def lastInnKategorierFraFil(fildestinasjon):
  kategorier=open(fildestinasjon).read().split('\n')
  for i in range(len(kategorier)):
    verdi=kategorier[i].split(';')
    if(len(verdi)<2): continue #ikke last inn tomme/ufullstendige kategorier
    mineKategorier[verdi[1]]=Kategori(verdi[0],verdi[1],1 if len(verdi) <3 else int(verdi[2]) )

def lagreKategorierTilFil(fildestinasjon):
  result=""
  for k in mineKategorier:
      result+=f"{k.navn};{k.id};{k.prioritet}\n"
  f = open(fildestinasjon, "w")
  f.write(result)
  f.close()
