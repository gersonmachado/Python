#Função para repetir a aplicação caso queira
cont= 's' #Variável
while cont == 's' or cont == 'S': #Enquanto o usuário responder s ou S

    #Título
    print('\n==== FUNÇÃO SOMAR ===== \n')

    #Entrada de dados
    n1=input('Digite um número:')
    n2=input('Digite outro número:')

    #Checar se os dados digitados são apenas números
    if n1.isnumeric()and n2.isnumeric() == True:

        #Sendo verdadeiro, converte-se em números inteiros para operar soma.
        n1=int(n1)
        n2=int(n2)
        soma= n1+n2

        #Exibir resultado da soma
        print(f'Resultado da soma de N1 e N2 é {soma}')

        #Input para repetição
        cont=input('\nDeseja realizar outra operação (S/N):')
        print('\n')

    #Exibir erro se não for números
    else:
        print('ERRO401: Digite somente números!')

        #Input vazio para o aplicativo não fechar automaticamente
        input()
else:
    print('Aplicação encerrada!')
    #Input vazio para o aplicativo não fechar automaticamente quando executado no Windows
    input()
