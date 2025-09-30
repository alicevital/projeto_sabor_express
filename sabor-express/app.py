import os

restaurantes = [{'nome':'pizzaria atlantico', 'categoria': 'pizzaria', 'ativo': False}, 
                {'nome': 'Leitao', 'categoria': 'jantar e almoço', 'ativo': False},
                {'nome': 'Tata', 'categoria': 'lanchonete', 'ativo': False}
]

def exibir_programa():
    '''Função que exibe o título do programa'''
    print('𝑺𝒂𝒃𝒐𝒓 𝑬𝒙𝒑𝒓𝒆𝒔𝒔\n')

def exibir_opcoes():
    '''Função que exibe as opções para o usuário interagir com o programa'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Função que exibe a frase de finalizar programa'''
    exibir_subtitulos("Finalizando programa...")

def voltar_ao_menu():
    '''Função que permite o usuário voltar ao menu de opções'''
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    '''Função que exibe a mensagem de opção inválida e retorna ao menu principal'''
    print('Opção inválida\n')
    voltar_ao_menu()

def exibir_subtitulos(texto):
    '''Função para exibir todos os subtítulos de cada opção do menu principal e 
    também limpa o console com a função os.system'''
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''função de cadastrar novos restaurantes por nome, categoria e ativo e insere na lista de restaurantes com a função append()'''
    exibir_subtitulos("Cadastro de novos restaurantes")

    nome_do_restaurante = input("Digite o nome do restaurante: ")
    categoria = input("Digite a categoria que o seu restaurante faz parte: ")

    dados_do_restaurante = {'nome': nome_do_restaurante,
                            'categoria': categoria,
                            'ativo': False}
    
    restaurantes.append(dados_do_restaurante)

    print(f"O restaurante {nome_do_restaurante} foi cadastrado!")
    voltar_ao_menu()

def listar_restaurantes():
    '''Função de listar todos os restaurante da lista, com o laço for, mostra cada chave de cada item da lista'''
    exibir_subtitulos("Listando restaurantes...")

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante} | {categoria} | {ativo}')
        
    voltar_ao_menu()

def ativar_ou_desativar_restaurante():
    '''Função de modificar o estado do restaurante, para ativo ou desativado'''
    exibir_subtitulos('Alternando estados dos restaurantes')
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado!")

    voltar_ao_menu()    

def escolher_opcao():
    '''função para mostrar o input de escolher opção e com base na opção escolhida, retorna a função necessária'''
    try:
        opcao_escolhida = int(input('Digite a opção que você deseja: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            ativar_ou_desativar_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Função main que exibe 3 funções: a função do título do programa, função de exibir opções e função de escolher opções'''
    os.system('cls')
    exibir_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()