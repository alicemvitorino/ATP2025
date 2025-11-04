# TPC7
## Autor
Alice Miranda Vitorino, A111500, (![foto](foto.jpg))
## Resumo
Resolvi o teste de afrição.
## Resultados
Código do jogo:
1.
a)
def ncomuns():
    x = int(input("Quantos números deseja que a sua 1º lista tenha? "))
    lista1 = []
    i = 0
    while i < x:
        num = int(input("Introduza um número à sua lista: "))
        lista1.append(num)
        i = i + 1
    print(f"A sua 1º lista é: {lista1}")

    x = int(input("Quantos números deseja que a sua 2º lista tenha? "))
    lista2 = []
    i = 0
    while i < x:
        num = int(input("Introduza um número à sua lista: "))
        lista2.append(num)
        i = i + 1
    print(f"A sua 2º lista é: {lista2}")

    res = []
    for num in lista1:
        if num not in lista2:
            res.append(num)
    for num in lista2:
        if num not in lista1:
            res.append(num)
    print(f"A lista formada pelos elementos não comuns às suas duas listas é: {res} ")
ncomuns()

b)
def pal_3():
    res = []
    texto = input("Escreva uma pequena frase sem pontuação: ")
    palavras = texto.split()
    for pal in palavras:
        if len(pal)>3:
            res.append(pal)
    print(f"As palavras na sua frase que têm mais do que três letras são: {res}")
pal_3()

c)
def par_indice_valor():
    res = []
    par = []
    x = int(input("Quantos animais deseja que a sua lista tenha? "))
    i = 0
    while i < x:
        elem = (input("Introduza um animal à sua lista: "))
        res.append(elem)
        i = i + 1
    
    i = 0
    while i < len(res):
        par.append((i,res[i]))
        i = i + 1
    print(par) 
par_indice_valor() 

2.
a)
def strCount():
    s = input("Escreva uma string: ")
    subs = input("Escreva uma substring: ")
    res = 0
    i = 0
    tamanho_subs = len(subs)
    while i <= len(s) - tamanho_subs:
        if s[i:i+tamanho_subs] == subs: #o i está incluído e o i + tamanho_subs não
            res =  res + 1
            i = i + tamanho_subs  
        else:
            i = i + 1
    return res         
strCount()

b)
def produtoM3():
    x = int(input("Quantos números deseja que a sua lista tenha? "))
    res = []
    i = 0
    while i < x:
        num = int(input("Introduza um número à sua lista: "))
        res.append(num)
        i = i + 1

    numeros = []
    while len(numeros) <= 3:
        i = 1000000
        for num in res:
            if num < i:
                i = num
        numeros.append(i)
        res.remove(i)
    print(numeros[0]*numeros[1]*numeros[2])
produtoM3()

c)
def reduxInt():
    x = (int(input(("Introduza um número positivo: "))))
    while x > 10:
        num1 = x // 10
        num2 = x % 10
        x = num1 + num2
    print (x)
reduxInt()

d)
def myIndexOf():
    s1 = input("Escreva uma pequena frase sem pontuação: ").lower()
    s2 = input("Escreva outra pequena frase sem pontuação: ").lower()
    frase1 = s1.split()
    frase2 = s2.split()
    i = 0
    res = True
    while i < len(frase2) and res:
        if frase2[i] in frase1:
            print(i)
            res = False
        i = i + 1
    if res:
        print("-1")
myIndexOf()

3.
instagram = [{
    "id": "p1", 
    "conteudo": "A tarefa de avaliação é talvez a mais ingrata das tarefas que um professor tem de realizar...",
    "autor": "jcr",
    "dataCriacao": "2023-07-20",
    "comentarios": [{"comentario": "Completamente de acordo...", "autor": "prh"}, {"comentario": "Mas há quem goste...", "autor": "jj"}]},
    {
    "id": "p2", 
    "conteudo": "Carpe diem!",
    "autor": "AliceVitorino",
    "dataCriacao": "2025-10-31",
    "comentarios": [{"comentario": "O que significa isso?", "autor": "jp"}, {"comentario": "Aproveita o dia;)", "autor": "GabrielaSantos"}]
    }]

a)
def quantosPost(redeSocial):
    return len(redeSocial)
quantosPost(instagram)

b)
def postsAutor(redeSocial, autor):
    i = 0
    res = []
    while i < len(redeSocial):
        if redeSocial[i]["autor"] == autor:
           res.append(redeSocial[i])
        i = i + 1
    return res
postsAutor(instagram, "AliceVitorino")

c)
def autores(redeSocial):
    i = 0
    res = []
    while i < len(redeSocial):
        autor = redeSocial[i]["autor"]
        res.append(autor)
        i = i + 1
    ordenada = sorted(res)
    return ordenada
print(autores(instagram))

d)
def insPost(redeSocial, conteudo, autor, dataCriacao, comentarios):
    post = {}
    input("Vamos criar um post!")
    x = len(redeSocial)
    post["id"] = (f"p{x + 1}")
    post["conteudo"] = conteudo
    post["autor"] = autor
    post["dataCriacao"] = dataCriacao
    post["comentarios"] = comentarios
    redeSocial.append(post)
    return redeSocial
print(insPost(instagram, "Passeio ao teatro Circo", "GuilhermeSilva", "2025-11-02", []))

e)
def remPost(redeSocial, id):
    i = 0
    while i < len(redeSocial):
        post = redeSocial[i]
        if post["id"] == id:
            redeSocial.remove(post) ## isto remove conteudo! por indice seria del redeSocial[i] 
            print("O post foi removido")
        i = i + 1
remPost(instagram, "p1")

f)
def postsPorAutor(redeSocial):
    distrib = {}
    for elem in redeSocial:
        if elem["autor"] in distrib:
            distrib[elem["autor"]] = distrib[elem["autor"]] + 1
        else:
            distrib[elem["autor"]] = 1
    return distrib
print(postsPorAutor(instagram))

g)
def comentadoPor(redeSocial, autor):
    i = 0
    post_com_comentarios_autor = []
    while i < len(redeSocial):
        comentarios_post = redeSocial[i]["comentarios"]
        for comentario in comentarios_post:
            if comentario["autor"] == autor:
                post_com_comentarios_autor.append(redeSocial[i])
        i = i + 1
    return post_com_comentarios_autor
print(comentadoPor(instagram, "jp"))