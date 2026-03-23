#lista de nomes

nomes = ["Giovanna", "Mateus", "Goão", "Pietro", "Julia", "Vitória"]

for indice, nome in enumerate(nomes):
    print(f"Estou no {indice} que possui o nome {nome}")
    if nome == "Goão":
        nome = "João"
        break
print(nomes)