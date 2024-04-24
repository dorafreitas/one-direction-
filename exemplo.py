print("Olá", "Isadora", sep="-")

print("Olá", "Isadora", end="!\n")

print("20", "05", "2003", sep="/")

print("isadora", "freitas", "email", sep="; ")

# Continuando impressões na mesma linha
print("Loading", end=" ")
print("[OK]") # Saída: Loading [OK]

nome = input("Entre com o seu nome: ")

print("Olá", nome)

itens = input("Digite itens separados por vírgula: ").split(',')

print("Itens: ", itens)

# Convertendo a entrada para inteiro
idade = input("Me diga sua idade: ")
idade = int(idade)
print("Daqui a cinco anos, você terá", idade + 5, "anos.")
