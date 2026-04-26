import os
import json

def configurar_sistema():
    if not os.path.exists("uploads_projetos"):
        os.makedirs("uploads_projetos")

def listar_projetos():
    arquivos = [f for f in os.listdir("uploads_projetos") if f.endswith(".json")]
    print('\n'+ '~' * 40)
    print('   PROJETOS CADASTRADOS:')
    print('~' * 40)

    if not arquivos:
        print("Nenhum projeto encontrado.")

        return []

    for i, arquivo in enumerate(arquivos, 1):
        nome_exibicao = arquivo.replace("projeto_", "").replace(".json", "").replace("_", " ")
        print(f"{i}. {nome_exibicao.title()}")

    return arquivos

def gerenciar_projeto():
    arquivos = listar_projetos()
    if not arquivos:
        return

    try:

        escolha = int(input("\nEscolha um numero do projeto para gerenciar (ou '0' para voltar): "))

        if escolha == 0:
            return

        nome_arquivo = arquivos[escolha - 1]
        caminho = f"uploads_projetos/{nome_arquivo}"

        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)

        print(f"\n---Dados Atuais---")
        print(f"aluno: {dados['aluno']}")
        print(f"projeto: {dados['projeto']}")

        confirmar = input("\nDeseja alterar as informações do projeto? (s/n): ").lower()

        if confirmar == 's':
            dados['aluno'] = input(f"Novo nome [{dados['aluno']}]: ")
            dados['projeto'] = input("Novo resumo: ") or dados['projeto']

            with open(caminho, "w", encoding="utf-8") as f:
                json.dump(dados, f, ensure_ascii=False, indent=4)
            print("Projeto atualizado com sucesso!")

    except (ValueError, IndexError):
        print("[ERRO] Escolha inválida. voltando ao menu.")

def fazer_upload_json():

    print('\n'+ '~' * 40)
    print('   NOVO UPLOAD DE PROJETO')
    print('~' * 40)
    nome_aluno = input("Nome do aluno: ").strip()
    resumo = input("Resumo do projeto: ")

    dados = {"aluno": nome_aluno, "projeto": resumo}

    nome_fich = f"projeto_{nome_aluno.replace(' ', '_')}.json"

    caminho = f"uploads_projetos/projetos_{nome_fich}.json"

    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    print(f"\n[SUCESSO] Projeto de {nome_aluno} guardado em {caminho}!")

def menu():
    configurar_sistema()
    while True:
        print('\n'+ '~' * 40)
        print('   SISTEMA DE ARQUIVOS JOVENS 3.0')
        print('~' * 40)
        print("1. Inserir novo projeto")
        print("2. Listar e Alterar projetos")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            fazer_upload_json()
        elif escolha == '2':
            gerenciar_projeto()
        elif escolha == '3':
            print("Encerrando... Até logo!")
            break
        else:
            print("\n[ERRO] Opção inválida!")

menu()