# oppgave G
class Sted: 
    def __init__(self,_id, navn,gatenavn, postnummer, poststed): 
        self._id = _id
        self.navn = navn
        self.gatenavn = gatenavn
        self.postnummer = postnummer
        self.poststed = poststed
        
    def __str__(self):
        return f'Sted({self._id}, {self.navn}, {self.gatenavn},{self.postnummer},{self.poststed}'


# Oppgave H  
def bruker_sted(): 
     info = Sted(input("id: "), input("navn: "), input("gatenavn: "), input("postnummer: "), input("poststed: "))
     return info
 
