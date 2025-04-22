# Jogo de pedra, papel, tesoura
import random as rd

opcoes = ("Pedra", "Papel", "Tesoura")
relacao_vitorias = {
    "Pedra": "Tesoura",
    "Papel": "Pedra",
    "Tesoura": "Papel"
}

rodando = True

while rodando:
    cpu = rd.choice(opcoes)
    player = None
    
    while player not in opcoes:
        player = input("\nEscolha entre (Pedra, Papel, Tesoura): ").capitalize()
    
    print(f"\nPlayer: {player}")
    print(f"CPU: {cpu}")
    
    if player == cpu:
        print("Empate!")
    elif relacao_vitorias[player] == cpu:
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    
    if input("\nJogar novamente? (s/n): ").lower() != 's':
        rodando = False