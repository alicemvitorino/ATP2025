# TPC6
## Autor
Alice Miranda Vitorino, A111500, (![foto](foto.jpg))
## Resumo
Construi uma aplicação para analisar uma tabela meteorológica.
## Resultados
Código do jogo:
from matplotlib import pyplot as plt

def tempMed(tabMeteo):
    res = []
    for data, tmin, tmax, prec in tabMeteo:
        media = (tmin + tmax)/2
        res.append((data, media))
    return res

def guardarTabMeteo(tabMeteo):
    f = open("tabela_meteorologia.txt", "w")
    for data, tmin, tmax, prec in tabMeteo:
        ano, mes, dia = data
        f.write(f"{ano}-{mes}-{dia}|{tmin}|{tmax}|{prec}\n")
    f.close()

def carregarTabMeteo(): #depois do strip ele sabe qual é a data, tmin, tmax, prec, tendo em conta que agora só há uma linha?
    res = []
    f = open("tabela_meteorologia.txt", "r")
    for linha in f:
        linha = linha.strip()
        data, tmin, tmax, prec  = linha.split("|") 
        ano, mes, dia = data.split("-")
        res.append((((int(ano), int(mes), int(dia)), float(tmin), float(tmax), float(prec))))
    f.close()
    return res

def tempMin(tabMeteo):
    i = 1000000
    for data, tmin, tmax, prec in tabMeteo:
        if tmin < i:
            i = tmin
    return i

def amplitude_termica(tabMeteo):
    res = []
    for data, tmin, tmax, prec in tabMeteo:
        amplitudet = tmax - tmin
        res.append((data, amplitudet))
    return res

def precMax(tabMeteo):
    i = 0
    for data, tmin, tmax, prec in tabMeteo:
        if prec > i:
            i = prec
    return (data, prec)

def prec_p(tabMeteo):
    res = []
    p = float(input("Introduza um valor de precipitação: "))
    for data, tmin, tmax, prec in tabMeteo:
        if prec > p:
            res.append((data, prec))
    return res

def dias_prec_p(tabMeteo):
    res = 0
    temp = 0
    i = 0
    continua = True
    p = float(input("Introduza um valor de precipitação: "))
    while i < len(tabMeteo):
        prec = tabMeteo[i][3]
        if prec < p and prec > 0:
            temp = 1
            a = i + 1
            while a < len(tabMeteo) and continua:
                new_prec = tabMeteo[a][3]
                if new_prec < p and new_prec > 0:
                    temp = temp + 1
                else:
                    continua = False
                a = a + 1
            i = a
        if temp > res and temp > 1:
            res = temp
        i = i + 1
    return res

def grafico(tabMeteo):
    x = [f"{data[0]}/{data[1]}/{data[2]}" for data, tmin, tmax, prec in tabMeteo] #valores de x
    y_min = [tmin for data, tmin, tmax, prec in tabMeteo] #valores de ymin
    y_max = [tmax for data, tmin, tmax, prec in tabMeteo] #valores de ymax
    precs = [prec for data, tmin, tmax, prec in tabMeteo] #valores de yprec

    #gráfico de linhas/pontos
    plt.plot(x,y_min, label = "Temperatura mínima (ºC)", color = "red", marker = "o")
    plt.plot(x,y_max, label = "Temperatura máxima (ºC)", color = "green", marker = "d")
    plt.grid() #grelha atrás
    plt.legend() #legenda
    plt.xticks(rotation = 45) #datas em angulo para se ver melhor
    plt.show() #aparecer

    #Gráfico de barras
    plt.bar(x, precs, label = "Pluviosodade(mm)", color = "blue")
    plt.legend()
    plt.grid()
    plt.xticks(rotation = 45)
    plt.show()

    return

def print_tabMeteo(tabMeteo):
    print("""
          A tabela meteorológica dos últimos 7 dias é: """)
    for elem in tabMeteo:
        print(f""" 
            {elem} """)

def aplicação(tabMeteo):
    #menu
    while True:
        print("""
            (1) Consultar a temperatura média de cada dia
            (2) Guardar a tabela meteorológica num ficheiro
            (3) Carregar a tabela meteorológica de um ficheiro
            (4) Consultar a temperatura mínima mais baixa da tabela meteorológica
            (5) Consultar a amplitude térmica de cada dia
            (6) Consultar o dia em que a precipitação foi máxima
            (7) Consultar os dias em que a precipitação é superior a um determinado valor
            (8) Consultar o maior número consecutivo de dias com precipitação abaixo de um determinado valor
            (9) Desenhar um gráfico da temperatura mínima, máxima e pluviosidade
            (0) Sair da aplicação""")
        
        print_tabMeteo(tabMeteo)

        x = (int(input("Escolha o número correspondente à opção que deseja: ")))

        if x == 0:
            print("Escolheu a opção de sair")
            return
        
        elif x == 1:
            print(tempMed(tabMeteo))

        elif x == 2:
            guardarTabMeteo(tabMeteo)
            print("A sua tabela meteorológica foi guardada no ficheiro")

        elif x == 3:
            tabMeteo = carregarTabMeteo()
            print("A sua tabela meteorológica foi carregada do ficheiro")

        elif x == 4:
            print(f"A temperatura mínima mais baixa da tabela é {tempMin(tabMeteo)}")

        elif x == 5:
            print(amplitude_termica(tabMeteo))

        elif x == 6:
            print(precMax(tabMeteo))

        elif x == 7:
            print(prec_p(tabMeteo))

        elif x == 8:
            print(dias_prec_p(tabMeteo))

        elif x == 9:
            grafico(tabMeteo)

        else:
             print("Opção inválida. Escolha o número correspondente à opção que deseja:")

        (input("Prima enter para continuar!"))


tabMeteo = [((2025,10,21), 13, 19, 0),((2025,10,22), 10, 19, 0.2), ((2025,10,23), 12, 16, 0.01), ((2025,10,24), 9, 20, 0), ((2025,10,25), 12, 20, 0.3), ((2025,10,26), 15, 18, 0.02), ((2025,10,27), 11, 16, 0.5)]
aplicação(tabMeteo)