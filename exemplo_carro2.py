
class Carro:
    def __init__(self, marca, modelo, cor, ano):
      self.marca = marca
      self.modelo =modelo
      self.cor = cor
      self.ano = ano

    def acelerar(self):
        print(f"carro {self.marca} {self.modelo} está acelerado")

    def frear(self):
        print(f"carro {self.marca} {self.modelo} está freando")    


#Criando objetos diferentes
carro1 = Carro("Hyundai", "I30", "Preto", "2012")
carro2 = Carro("Toyota", "Hilux", "Vermelho", "2023")

#Chamando Metodos
carro1.acelerar() #Usa os atributos do carro1
carro1.frear()

