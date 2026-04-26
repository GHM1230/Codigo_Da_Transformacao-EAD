'''
class Carro:
    def __init__(self,marca ,cor ):
        self.marca = marca
        self.cor = cor

def buzinar(self):
    print(f'O {self.marca} da cor {self.cor} fez bip bip!')

meu_carro = Carro('Toyota Corolla', 'vermelho')
carro_cliente = Carro('Honda Civic', 'azul')

meu_carro.buzinar()

carro_cliente.buzinar()

EXERCICIO PRATICO: SIMULE UM CARREGAMENTO DE UM SMARTPHONE, quando estiver a 5%,mensagem, quando estiver 85%, avise que esta carregado.

'''

class Celular:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False
        self.bateria = 100

    def ligar(self):
        self.ligado = True
        print(f'O {self.marca} {self.modelo} está ligado.')

    def carregar(self):
        self.bateria = 100
        print(f'{self.modelo} está carregado.')

meu_celular = Celular('Xiaomi', 'Redmi Note 13')
meu_celular.ligar()
meu_celular.bateria = 5
print(f'Bateria do {meu_celular.modelo} está com {meu_celular.bateria}% de bateria.')