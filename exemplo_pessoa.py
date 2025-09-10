from exemplo_carro2 import Carro

class Pessoa:
    
    def __init__(self, nome, idade, cidade, exemplo_carro2:Carro):
      self.nome = nome
      self.idade =idade
      self.cidade = cidade
      self.exemplo_carro2 =exemplo_carro2
     

    def apresentar(self):
        print(f"A pessoa {self.nome} tem {self.idade} de idade e mora em {self.cidade}")

    def dirigir(self):
       print(f"{self.nome} estou digirindo {self.exemplo_carro2.marca} {self.exemplo_carro2.cor} {self.exemplo_carro2.ano} ")
       self.exemplo_carro2.acelerar()

meu_carro = Carro("Toyota", "Corolla", "Vermelho", "2012")

#Criando objetos diferentes

pessoa1 = Pessoa("Luiz", "16 anos", "São Paulo",meu_carro)                 


#Chamando Metodos
pessoa1.apresentar() 
pessoa1.dirigir()


