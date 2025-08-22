'''class - Palavra chave no python para definir uma classe'''

'''Carro - Nome que damos a classe por convenção começa com letra maiuscula
 se for nome composto, usamos CamelCase ex:MinhaCasa'''

'''def - Palavra chave que define uma função ou método no Python'''

'''__init __-metodo construtor  da classe.
Ele e chamado automaticamente quando criamos a classe com um novo objeto. 
Serve para  inicializar atributos do objeto.'''


'''Self - Uma referecia ao proprio objeto que esta sendo criado
'''

class carro:
    def __init__(self, marca, modelo):
      self.marca = marca
      self.modelo =modelo

    def acelerar(self):
        print(f"carro {self.marca} {self.modelo} está acelerado")


#Criando objetos diferentes
carro1 = carro("Toyota", "corolla")
carro2 = carro("Honda", "Civic")
carro3 = carro("Mitsubishi", "Eclipse")

#Chamando Metodos
carro1.acelerar() #Usa os atributos do carro1
carro2.acelerar() #Usa os atributos do carro2
carro3.acelerar() #Use os atributos do carro3
