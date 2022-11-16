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


# Oppgave H  
def bruker_sted(): 
     info = Sted(input("id: "), input("navn: "), input("gatenavn: "), input("postnummer: "), input("poststed: "))
     return info
 
#Oppgave I
mineSteder = []
def lagreStedTilFil():
  result = ""
  for k in mineSteder:
      result += f'({k._id};{k.navn}; {k.gatenavn};{k.postnummer};{k.poststed};\n)'
  f = open(mineSteder, "w")
  f.write(result)
  f.close()
