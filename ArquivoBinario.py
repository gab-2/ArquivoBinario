import pickle

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone: ")
    email = input("Digite o e-mail do contato: ")
    
    contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email
    }
    
    return contato

def salvar_contatos(contatos):
    with open('contatos.bin', 'wb') as arquivo:
        pickle.dump(contatos, arquivo)

def carregar_contatos():
    try:
        with open('contatos.bin', 'rb') as arquivo:
            contatos = pickle.load(arquivo)
    except FileNotFoundError:
        contatos = []
    
    return contatos

def main():
    contatos = carregar_contatos()

    while True:
        print("\nMenu:")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            contato = adicionar_contato()
            contatos.append(contato)
            salvar_contatos(contatos)
            print("Contato adicionado com sucesso!")

        elif escolha == '2':
            print("\nLista de Contatos:")
            for i, contato in enumerate(contatos, 1):
                print(f"{i}. Nome: {contato['nome']}")
                print(f"   Telefone: {contato['telefone']}")
                print(f"   E-mail: {contato['email']}")
        
        elif escolha == '3':
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()