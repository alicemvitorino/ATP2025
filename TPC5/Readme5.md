# TPC2
## Autor
Alice Miranda Vitorino, A111500, (![foto](foto.jpg))
## Resumo
Construi um aplicação para gestão de alunos.
## Resultados
Código do jogo:
def criarTurma(): #cria uma lista vazia
    turma = []
    return turma

def inserirAluno(turma):
    nome = input("Introduza o nome do aluno que deseja adicionar à sua turma: ")
    id = input("Introduza o ID do aluno: ")
    notaTPC = float(input("Introduza a nota do TPC do aluno: "))
    notaProj = float(input("Introduza a nota do projeto do aluno: "))
    notaTeste = float(input("Introduza a nota do teste do aluno: "))
    notas = [notaTPC,notaProj,notaTeste]
    aluno = (nome, id, notas)
    turma.append(aluno)

def encontrarAluno_id(turma):
    idProcurado = input("Qual o id do aluno que procura? ")
    alunoProcurado = None
    for aluno in turma:
        idAluno = aluno[1]
        if idAluno == idProcurado:
            alunoProcurado = aluno
        return alunoProcurado  

def guardarTurma(turma):
    fout = open("./TPC5/turma.txt", "wt")
    for aluno in turma:
        fout.write(f"{aluno[0]};{aluno[1]};{aluno[2][0]};{aluno[2][1]};{aluno[2][2]}\n")

    fout.close()

def carregarTurma():
    turma_ficheiro = criarTurma()
    fin = open("./TPC5/turma.txt", "rt")
    for linha in fin:
        # strip: remove o caracter especial de mudança de linha \n
        # split: parte a string no sitio do ; - devolve um array onde cada posição é uma porção da string ate ao separador
        elementos_linha = linha.strip().split(';') 
        # criar o aluno a partir dos elmentos individuais
        notas = [elementos_linha[2],elementos_linha[3],elementos_linha[4]]
        aluno = (elementos_linha[0], elementos_linha[1], notas)
        #adicionar o aluno a turma
        turma_ficheiro.append(aluno)
    return  turma_ficheiro


def aplicação():
    turma = None
    #menu
    while True:
        print("""
            (1)Criar uma turma
            (2)Inserir um aluno na turma
            (3)Listar a turma
            (4)Consultar um aluno por id
            (5)Guardar a turma em ficheiro
            (6)Carregar uma turma dum ficheiro
            (0)Sair da aplicação""")
    
        x = (int(input("Escolha o número correspondente à opção que deseja: ")))

        if x == 0:
            print("Escolheu a opção de sair")
            return
        
        elif x == 1:
            turma = criarTurma()
            print("Criou uma turma que neste momento se encontra sem alunos. Se quiser adicionar alunos escolha a opção 2.")

        elif x == 2:
            if turma is None:
                print("Não pode inserir um aluno na turma se ainda não criou uma turma para o adicionar. Escolha a opção 1 primeiro!")
            else:
                inserirAluno(turma)
                print("O aluno foi inserido na turma!")

        elif x == 3:
            if turma is None:
                print("Não pode consultar a turma se ainda não a criou. Escolha a opção 1 primeiro!")
            else:
                print(f"Esta é a sua turma neste momento: {turma}")

        elif x == 4:
            if turma is None:
                print("Não pode consultar um aluno na turma se ainda não criou uma turma. Escolha a opção 1 primeiro!")
            else:
                alunoProcurado = encontrarAluno_id(turma)
                if alunoProcurado is None:
                  print("Não existe nenhum aluno na turma com esse id!")
                else:
                    print(alunoProcurado)

        elif x == 5:
            if turma is None:
                print("Não pode guardar a turma num ficheiro se ainda não criou uma turma. Escolha a opção 1 primeiro!")
            else:
                guardarTurma(turma)

        elif x == 6:
            turma = carregarTurma()
            print("A turma foi carregada dp ficheiro")

        else:
            print("Opção inválida. Escolha o número correspondente à opção que deseja:")
                
aplicação()