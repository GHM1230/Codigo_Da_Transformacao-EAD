class Celular:
    def __init__(self, marca, modelo):
        self.marca, self.modelo = marca, modelo
        self.bateria = 100

    def fazer_chamada(self, custo_bateria):
        print(f"\n---Chamada no {self.modelo}---")

        try:
            self.bateria -= (custo_bateria)
        except TypeError:
            print("Erro: custo de bateria deve ser um número!")
        else:
            print(f"sucesso! Bateria atual: {self.bateria}%")
        finally:
            print("sistema finalizado.")

meu_celular = Celular("Samsung", "S24")
meu_celular.fazer_chamada(90)