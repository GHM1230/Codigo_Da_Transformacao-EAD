import requests

def consulta_cep(cep):
    url =f'https://viacep.com.br/ws/{cep}/json/'

    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        return dados
    else:
        return 'erro na consulta ⚠'

print('=Aula de API com python: consulta de CEP =')
meu_cep = '05001000'
resultado = consulta_cep(meu_cep)

if isinstance(resultado, dict):
    print(f'Endereço: {resultado['logradouro']}')
    print(f'Bairro: {resultado['bairro']}')
    print(f'Cidade: {resultado['localidade']}')