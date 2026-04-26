'''

r - read = leitura;
w - writer = escrever
a - append = adicionar

'''

def ler_arquivo_jovens():
    print('Sistema de upload dos arquivos jovens')
    print('-' * 30)

    with open('arquivo_lido.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

ler_arquivo_jovens()