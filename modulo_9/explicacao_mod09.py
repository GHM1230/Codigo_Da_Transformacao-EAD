def aula_tratamento_erros():
    print("---Desafio 1: divisao---")

    try:

        numerador = int(input("Digite o numerador: "))
        denominador = int(input("Digite o denominador: "))
        resultado = numerador / denominador
    
    except ValueError:
        print("Erro: digite apenas números inteiros!")
    
    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero!")

    except Exception as erro:
        print(f"Erro inesperado: {erro}")

    else:
        print(f"Sucesso! Resultado: {resultado}")

    finally:
        print("---Fim da Divisão---")

aula_tratamento_erros()