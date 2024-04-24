#1.
def imprimir_informações(nome, idade, cidade):
    print("nome:", nome, sep=" ", end =" - ")
    print("idade:", idade, sep=" ", end=" - ")
    print("cidade:", cidade, end="!\n\n")
imprimir_informações("isadora", 20, "Rio")

#2.
def operação_desejada():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operação = str(input("Digite a operação desejada: "))
    if operação == "+":
        print(num1 + num2)
    elif operação == "-":
        print(num1 - num2)
    elif operação == "*":
        print(num1 * num2)
    elif operação == "/":
        print(num1/num2)
operação_desejada()

#3.
def itens_lista_de_compras():
    itens = input("Insira os itens de sua lista de compras, separados por vírgula: ").split(',')
    print("itens: ", itens)
itens_lista_de_compras()


#4.
def conersão_temperatura():
    grausc = float(input("Digite a temperatura em graus celsius: "))
    grausf = (grausc * 9/5) + 32
    print("A temperatura em graus farenheit é igual a ", grausf)
conersão_temperatura()

#5. 
def nomes():
    print("Digite nomes para adicionar à lista (digite 'sair' para terminar):")
    nomes = []
    while True:
        entrada = input()
        if entrada.lower() == 'sair':
            break
        else:
            nomes.append(entrada)
    for n in nomes:
        print("Nomes coletados:", n)
nomes()
