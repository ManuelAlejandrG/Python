class carro(object): #clase 
    def __init__(self,ruedas,puertas,color,modelo):
        self.ruedas=ruedas #atributos
        self.puertas=puertas #atributos 
        self.color=color #atributos
        self.modelo=modelo #atributos 
    
    def darModelo(self):  #metodo 
        return (self.modelo)
    
    def darColor(self): #metodo
        return self.color
    
    def Arranca(self):  #metodo 
        if self.ruedas ==4:
            return "El carro puede rodar "





A=carro(4,3,"azúl","aveo") #objeto 





A.Arranca()





class ordenador(object):
    def __init__(self,marca,RAM,Disco,OS):
        self.marca = marca 
        self.RAM=RAM
        self.DiscoDuro=Disco
        self.OS=OS




m=ordenador("lenovo",3,512,"ubuntu-windows")
m.OS





m.DiscoDuro
