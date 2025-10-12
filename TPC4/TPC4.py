#sala1 = (150, [17], "Twilight")
#sala2 = (200, [], "Hannibal")
#sala3 = (100, [], "Cinderela")
#sala4 = (250, [2,3], "Spider Man")
#Bragaparque = [sala1, sala2]

def listar(cinema): #dá o nome dos filmes de cada sala
    i = 0
    while i < len(cinema):
        sala = cinema[i]
        filmeSala = sala[2]
        print(filmeSala)
        i = i + 1
#listar(Bragaparque)

def disponivel(cinema, filme, lugar): #diz se o lugar que a pessoa procura para ver um determinado filme num determinado cinema está ocupado ou não
    res = False
    i = 0
    while i < len(cinema):
        sala = cinema[i]
        filmeSala = sala[2]
        lugaresOcupados = sala[1]
        nlugares = sala[0]
        if filmeSala == filme:
            if lugar <= nlugares:
                res = True
            a = 0
            while a < len(lugaresOcupados):
                lugarSala = lugaresOcupados[a]
                if lugarSala == lugar:
                    res = False
                a = a + 1
        i = i + 1 
    return res
#print(disponivel(Bragaparque, "Twilight", 17))
#print(disponivel(Bragaparque, "Twilight", 32)) 

def vendebilhete(cinema, filme, lugar): #Verifica se o lugar está disponivel e vende um bilhete
    if disponivel(cinema, filme, lugar):
        i = 0
        while i < len(cinema):
            sala = cinema[i]
            filmeSala = sala[2]
            lugaresOcupados = sala[1]
            if filmeSala == filme:
                lugaresOcupados.append(lugar)
            i = i + 1
    else:
        print("Lugar indisponivel!")
    return cinema
#print(vendebilhete(Bragaparque, "Twilight", 32))
#print(vendebilhete(Bragaparque, "Twilight", 17))


def listardisponibilidades(cinema):
    i = 0
    while i < len(cinema):
        sala = cinema[i]
        filmeSala = sala[2]
        lugaresSala = sala[0]
        lugaresIndisponiveis = sala[1]
        print(f"A sala {i + 1} está a exibir o filme {filmeSala} e tem {lugaresSala - len(lugaresIndisponiveis)} lugares disponíveis.")
        i = i + 1
#listardisponibilidades(Bragaparque)

def inserir(cinema, novaSala): #insere a sala apenas se esta não existir
    res = True 
    i = 0 
    while i < len(cinema):
        sala = cinema[i]
        filme = sala[2]
        if filme == novaSala[2]:
            res = False
        i = i + 1
    if res:
        cinema.append(novaSala)
    else:
        print("Não é possível adicionar esta sala, já existe uma sala com este filme.")
    return cinema

#print(inserir(Bragaparque, sala3))

def inserir_2(cinema, sala):
    res = True
    if sala in cinema:
        res = False
    else:
        cinema.append(sala)
    return res 
#print(inserir_2(Bragaparque,sala1))
#print(inserir_2(Bragaparque,sala3))

def remover(cinema, sala): #remove uma sala
    if sala is None:
        print("Sala inválida")
        return cinema
    
    i = 0
    while i < len(cinema):
        if cinema[i] == sala:
            cinema.remove(sala)
        i = i + 1
    return cinema
#print(remover(Bragaparque, sala1))
#print(remover(Bragaparque, sala4))

def sair():
    print("Escolheu a opção de sair")

def criarSala():
    filme = input("Que filme deseja adicionar?")
    nlugares = int(input("Quantos lugares deseja que a sua sala tenha?"))
    return (nlugares, [], filme)

def obterSala(cinema):
    filme = input("Que filme está a dar na sala que deseja remover?")  
    i = 0
    resSala = None
    while i < len(cinema):
        sala = cinema[i]
        filmeSala = sala[2]
        if filmeSala == filme:
            resSala = sala 
        i = i + 1
    return resSala 

def gerirCinemas():
    
    sala1 = (150, [17], "Twilight")
    sala2 = (200, [], "Hannibal")
    Bragaparque = [sala1, sala2]

    while True: #menu
        print("""
            (1) Filmes em exibição no Braga Parque
            (2) Ver se o lugar que deseja está disponivel
            (3) Comprar bilhete no Braga Parque
            (4) Opções de filmes e os respetivos lugares disponiveis
            (5) Adicionar uma sala de cinema
            (6) Remover uma sala de cinema
            (0) Sair """)

        x = (int(input("Escolha o número correspondente à opção que deseja: ")))

        #opções
        if x == 0:
            sair()
            return

        elif x == 1:
            listar(Bragaparque)

        elif x == 2:
            filme = input("Que filme deseja ver?")
            lugar = int(input("Em que lugar deseja ficar?"))
            print(f"{disponivel(Bragaparque, filme, lugar)}")

        elif x == 3:
            filme = input("Que filme deseja ver?")
            lugar = int(input("Em que lugar deseja ficar?"))
            Bragaparque = vendebilhete(Bragaparque, filme, lugar)

        elif x == 4:
            listardisponibilidades(Bragaparque)

        elif x == 5:
            sala = criarSala()
            Bragaparque = inserir(Bragaparque, sala)

        elif x == 6:
            sala = obterSala(Bragaparque)
            Bragaparque = remover(Bragaparque, sala)
        
        else:
            print("Opção inválida. Escolha o número correspondente à opção que deseja:")

gerirCinemas()   



        
    
    


            





