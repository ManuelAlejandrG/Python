class Persona(object):
    def __init__(self,Nombre,sexo,edad):
        self.Nombre=Nombre
        self.sexo=sexo
        self.edad=edad
    def Sexo(self):
        return self.sexo
    
    def Edad(self):
        return self.edad
    def Nombre(self):
        return self.Nombre

Juan=Persona("Juan","Masculino",35)

Juan.Edad()
class Personal(Persona):
    def __init__(self,Nombre,sexo,edad,Carnet,especialidad):
        
        Persona.__init__(self,Nombre,sexo,edad)
        self.Carnet=Carnet
        self.especialidad=especialidad
        
    def Carnet(self):
        return self.Carnet
    
    def Especialidad(self):
        return self.especialidad
    
    def informacion(self):
        if self.Carnet > 20000:
        
            return "Es estudiante"
        else:
            return "No es estudiante"
        
MAG=Personal("Manuel","masculino", 25, 20305,"CEIF")

