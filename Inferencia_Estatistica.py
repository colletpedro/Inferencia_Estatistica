import random

opcoes = ["Pedra", "Papel", "Tesoura"]
jogador = random.choice(opcoes)
computador = random.choice(opcoes)
#quem he quem
print(f"Jogador: {jogador}")
print(f"Computador: {computador}")

if jogador == computador:
    print("Empate!")
    #blablabla
elif (jogador == "Pedra" and computador == "Tesoura") or \
     (jogador == "Papel" and computador == "Pedra") or \
     (jogador == "Tesoura" and computador == "Papel"):
    print("Jogador venceu!")
else:
    print("Computador venceu!")
