import random
n = random.randint(0, 3) #Computador
print ('''ESCOLHA AS OPÇÕES:
1- papel
2- tesoura
3- pedra''')
num = int (input('Qual você escolhe? ')) #Jogador
if n == 1:
    if num == 1:
        print('O computador jogou PAPEL!')
        print('Empatou!!! tente novamente!!!')
    elif num == 2:
        print('O computador jogou PAPEL!')
        print('VOCÊ GANHOU!!!')
    elif num == 3:
        print('O computador jogou PAPEL!')
        print('VOCÊ PERDEU!!!')
elif n == 2:
    if num == 1:
        print('O computador jogou TESOURA!')
        print('VOCÊ PERDEU!!!')
    elif num == 2:
        print('O computador jogou TESOURA!')
        print('Empatou!!! tente novamente!!!')
    elif num == 3:
        print('O computador jogou TESOURA!')
        print('VOCÊ GANHOU!!!')
elif n == 3:
    if num == 1:
        print('O computador jogou PEDRA!')
        print('VOCÊ GANHOU!!!')
    elif num == 2:
        print('O computador jogou PEDRA!')
        print('VOCÊ PERDEU!!!')
    elif num == 3:
        print('O computador jogou PEDRA!')
        print('Empatou!!! tente novamente!!!')
    else:
        print('INVÁLIDO!!!')