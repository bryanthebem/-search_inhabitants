#7) A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e o número de filhos.
# Faça um programa que leia esses dados para um número não determinado de pessoas e retorne a média de salário da população,
# a média do número de filhos, o maior salário e o percentual de pessoas com salário inferior ao salário mínimo.

LS = []
LF = []
opcao = 1
while (opcao == 1 or opcao ==  2):
    print('1 - cadastrar familia: ')
    print('2 - relatorio estatistico: ')
    print('3 - sair do programa: ')
    opcao = int(input('Digite a opcão: '))
    if opcao == 1:
        sal = float(input('Digite o salario da familia: '))
        filhos = int(input('Digite a quantidade de filhos: '))
        LS.append(sal)
        LF.append(filhos)
    elif opcao == 2:
        mediaS = sum(LS)/len(LS)
        mediaF = sum(LF)/len(LF) 
        
        LS.sort(reverse = True) 
        cont = 0
        for i in range(0,len(LS)):
            if LS[i] < 1220:
                cont = cont + 1
        print('media de salario das familias: %.2f'% mediaS, 'media de filhos: %.2f'% filhos)
        print('maior salario: ', LS[0])
        print('percentual de familias abaixo da media salarial: %.2f' %((cont/len(LS)) * 100), '%')