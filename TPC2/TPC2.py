print("O jogo começa com uma caixa que contém 21 fósforos. Em cada jogada cada jogador escolhe se pretende retirar da caixa 1,2,3 ou 4 fósforos. Perde o jogo quem retirar o último fósforo.")
a = (input("Deseja jogar em primeiro ou segundo lugar?"))
import random

f = 21
while f > 0:
    if a == "primeiro":
        #Jogador joga
        x = int(input("Quantos fósforos deseja retirar?"))
        while x not in [1, 2, 3, 4] or x > f:
        #while x != 1 and x != 2 and x != 3 and x != 4:
            x = int(input("Erro!!! Tem de escolher um número entre 1 e 4: "))
            
        print(f"Retirou {x} fósforos!")
        f = f - x
        print(f"Restam {f} fósforos.")
        if f == 0:
            print("Retirou o último fósforo. Perdeu:(")
            break

         #Computador joga
        y = min(5 - x, f)  # Para não retirar mais do que o que resta   
        print(f"Eu retiro {y} fósforos!")
        f = f - y
        print(f"Restam {f} fósforos.")

    else:
        #Computador joga
        resto = f % 5
        if resto == 1:
            y = random.randint(1, min(4, f))
        else:
            y = min((f - 1) % 5, f)  # leva para 1, 6, 11, 16, ...
            
        print(f"Eu retiro {y} fósforos!")
        f = f - y
        print(f"Restam {f} fósforos!")
        if f == 0:
            print("Eu retirei o último fósforo. Ganhou :)")
            break 
            
        #Jogador joga
        x = int(input("Quantos fósforos deseja retirar?"))
        while x not in [1, 2, 3, 4] or x > f:
            x = int(input("Erro!!! Tem de escolher um número entre 1 e 4: "))
            
        print(f"Retirou {x} fósforos!")
        f = f - x
        print(f"Restam {f} fósforos.")
        if f == 0:
            print("Retirou o último fósforo. Perdeu :(")
            break
                 

