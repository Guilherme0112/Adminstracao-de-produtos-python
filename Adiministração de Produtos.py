carrinho = list()
while True:
    start_app = input('Deseja começar? ').strip().upper() [0]

    while start_app == 'S':
        print('''
        [1] Cadastrar Produto
        [2] Ver Produtos
        [3] Editar Quantidade
        [4] Excluir Produto
        [5] Sair do Programa
        ''')
        nav = input('O que deseja fazer? ').strip() [0]
        if nav == '1':  #record the values ​​in the list
            print('=-' * 20)
            product = input('Digite o nome do produto: ')
            amount = int(input('Digite a quantidade do produto: '))
            products = list()
            products.append(product)
            products.append(amount)
            carrinho.append(products)
            print('=-' * 20)
            print('Produto cadastrado com sucesso!')
            print('=-' * 20)
        elif nav == '2': #shows each value in the list
            print('=-' * 20)
            for sublist in enumerate(carrinho):
                print(f'{sublist[0]} | {sublist[1]}')
            print('=-' * 20)
        elif nav == '3': #updating list values
            print('=-' * 20)
            print('''
            [1] Vendeu 
            [2] Comprou
            [3] Voltar
            ''')
            print('=-' * 20)
            update_list = input('Você vendeu produtos ou repôs o estoque? ')
            print('=-' * 20)
            if update_list == '1':
                for sublist in enumerate(carrinho):
                    print(f'{sublist[0]} | {sublist[1]}')
                print('=-' * 20)
                update_id = int(input('Qual o id produto? '))
                update_amount = int(input(f'Digite o total de produtos vendidos do {carrinho[update_id]}: '))
            elif update_list == '2':
                print('comprou')
                print('=-' * 20)
            elif update_list == '3':
                print()
            else: 
                print('=-' * 20)
                print('Valor Inválido!')
                print('=-' * 20)
        elif nav == '4': #removing value from list
            print('=-' * 20)
            for sublist in enumerate(carrinho):
                print(f'{sublist[0]} | {sublist[1]}')
            print('=-' * 20)
            remove = int(input('Qual produto deseja remover da lista? '))
            print('=-' * 20)
            remove_warn = input(f'Deseja remover o produto {carrinho[remove]}? [S/N] ').upper().strip() [0]
            if remove_warn == 'S':
                carrinho.pop(remove)
                print('Produto removido com sucesso!')
                print('=-' * 20)
            elif remove_warn == 'N':
                print('=-' * 20)
                print('Você cancelou a exclusão.')
                print('=-' * 20)
            elif remove_warn != 'S' and 'N':
                print('Valor inválido!')
        elif nav == '5': #end of program
            print('=-' * 20)
            print('Programa encerrado!')
            print('=-' * 20)
            break
        else:
            print('=-' * 20)
            print('Valor Inválido!')
            print('=-' * 20)
    if start_app == 'N':
        print('Programa encerrado!')
        print('=-' * 20)
        break
    elif start_app != 'S' and 'N':
        print('=-' * 20)
        print('Valor inválido! Tente Novamente.')
        print('=-' * 20)
    break