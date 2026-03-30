#Estrutura de repetição
while True:
    usuario = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if (usuario == "admin" and senha == "123"):
        break
    else: 
        print("Falha ao realizar login")

print ("Bem vindo ao sistema")