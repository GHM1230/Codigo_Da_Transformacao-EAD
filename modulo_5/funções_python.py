def calcula_media(notas):
    return sum(notas) / len(notas) 

def verificar_aprovacao(media):
    if media >= 7:
          return "Aprovado"
    else:
      return "Reprovado"

def exibir_resultado(notas):
     media = calcula_media(notas)
     status = verificar_aprovacao(media)
     print(f"Média: {media:.2f} - Situação: {status}")

notas = [8.5, 7.0, 9.0]
exibir_resultado(notas)