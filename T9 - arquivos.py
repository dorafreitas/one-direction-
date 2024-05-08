#1
def questao1():
    variavel = input("Entre o seu nome: ")
    f = open('meu_arquivo.txt', 'w')
    f.write(variavel)
    f.close()

#2
def questao2():
    variavel2 = input("Escreva o nome de um arquivo de texto: ")
    f = open(variavel2, 'w')
    texto = input("Escreva o conteudo a ser impresso ao arquivo: ")
    f.write(texto)
    f.close()

#3
def questao3():
    f = open('arquivo-exemplo.txt', 'r')
    exemplo = f.read()

    
    f = open("novo_arquivo_questao3.txt", "w")
    f.write(exemplo)
    f.close()

#4
def questao4():
    numero = input("Escreva um número para o arquivo: ")
    f = open('arquivo-exemplo.txt', 'r')
    for linha in f:
        partes = linha.split (';')
        if numero == partes [0]:
            print (partes [1])
    f.close() 
    
    
    

