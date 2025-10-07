# TPC3
## Autor
Alice Miranda Vitorino, A111500, (![foto](foto.jpg))
## Resumo
Criei uma aplicação para manipulação de listas de inteiros
## Resultados
Código do jogo:

import random

def aplicação():
    res = []
    while True:
        #menu
        print("""
        (1) Criar Lista 
        (2) Ler Lista
        (3) Soma
        (4) Média
        (5) Maior
        (6) Menor
        (7) estaOrdenada por ordem crescente
        (8) estaOrdenada por ordem decrescente
        (9) Procura um elemento
        (0) Sair """)

        x = (int(input("Escolha o número correspondente à opção que deseja: ")))

        #opções
        if x == 0:
            print("Escolheu a opção de sair")
            return

        elif x == 1:
            res = [] #limpa a lista anterior
            N = int(input("Quantos elementos deseja na sua lista?"))
            i = 0
            while i < N:
                res.append(random.randint(1,100))
                i = i + 1
            print(res)

        elif x == 2:
            res = [] #limpa a lista anterior
            n = int(input("Quantos elementos deseja na sua lista?"))
            i = 0
            while i < n:
                num = int(input("Escolha um número para a sua lista: "))
                res.append(num)
                i = i + 1
            print(res) 
        
        elif x == 3:
            soma = 0
            for num in res:
                soma = soma + num
            print(f"A soma dos elementos da lista é {soma}!")

        elif x == 4:
            media = 0
            soma = 0
            quantidade = len(res) #guarda o número de elementos que a lista tem
            for num in res:
                soma = soma + num
            media = soma/quantidade
            print(f"A média dos elementos da lista é {media}!")

        elif x == 5:
            elem = res[0] #primeiro elemento da lista
            for num in res [1:]: #do segundo elemento da lista até ao fim
                if num > elem:
                    elem = num
            print(f"O maior elemento da lista é {elem}!")

        elif x == 6:
            elem = res[0]
            for num in res [1:]:
                if num < elem:
                    elem = num
            print(f"O menor elemento da lista é {elem}!")

        elif x == 7:
            cond = True
            i = 0
            while i < len(res) - 1 and cond:
                if res[i] > res[i + 1]:
                    cond = False
                i = i + 1
            if cond == False:
                print("Não, a lista não está ordenada por ordem crescente.")
            else:
                print("Sim, a lista está ordenada por ordem crescente")

        elif x == 8:
            cond = True
            i = 0
            while i < len(res) - 1 and cond:
                if res[i] < res[i + 1]:
                    cond = False
                i = i + 1
            if cond == False:
                print("Não, a lista não está ordenada por ordem decrescente.")
            else:
                print("Sim, a lista está ordenada por ordem decrescente")

        elif x == 9:
            a = int(input("Qual o número que procura dentro das lista?"))
            if a not in res:
                print("-1")
            else:
                i = 0
                while i < len(res): 
                    if res[i] == a:
                        print(f"O número {a} está na posição {i} da lista!")
                    i = i + 1

        else:
            print("Opção inválida. Escolha o número correspondente à opção que deseja:")
        
aplicação() #chama a função