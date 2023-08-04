# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.​
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;​
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

valor = int(input("Qual valor voce deseja sacar? "))

if(valor < 10 or valor >600):
    print("Valor inválido.\n");
else:
    print("caixa eletronico");
    cont100 = valor //100
    valor -= cont100 *100

    cont50 = valor //50
    valor -= cont50 *50

    cont10 = valor //10
    valor -= cont10 *10

    cont5 = valor //5
    valor -= cont5 *5

    cont1 = valor //1
    valor -= cont1 *1

    print(f"Quantidade total de notas: \nNotas de R$ 100: {cont100} \nNotas de R$ 50: {cont50} \nNotas de R$ 10: {cont10} \nNotas de R$ 5: {cont5} \nNotas de R$ 1: {cont1} \n")
