class Celular:
    def __init__(self, marca, modelo):
        self.marca, self.modelo = marca, modelo

    def verificar_status(self):
        try:
            entrada =input(f"bateria do {self.modelo}: ")
            nivel = float(entrada)
            if nivel < 0 or nivel > 100:
                print("valor inválido: digite de 0 e 100!")
            
            elif nivel < 15:
                print(f"bateria em {nivel}%! carrege já!")
            
            elif nivel < 85:
                print(f"bateria em {nivel}%! carga excelente!")
            else:
                print(f"bateria em {nivel}%! bateria cheia!")
        except ValueError:
            print("Erro: digite apenas números!")

cel = Celular("Samsung", "S24")
cel.verificar_status()
