from time import sleep
import pygame
import os
import questionary

pygame.init()

def musica(musica):
    pygame.mixer.music.load(f"{musica}.mp3")
    pygame.mixer.music.play()
def iniciar():
    print("A Venum's Game...")
    sleep(2)
    pygame.mixer.music.load("tema.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.3)
    sleep(1)
    os.system("cls")
    print("As Aventuras das")
    sleep(1.15)
    print("\033[32m/------    /------\\    /----\\    ■   |          |    /------\\    /-----\\    ■   |\\     |    |     |    /------\\    -----      |")
    for c in range(3):
        sleep(0.7)
        if c == 0:
            print("|          |      |    |    |    |   |          |    |      |    |     |    |   | \\    |    |     |    |      |   |           |")
        elif c == 1:
            print("|          |------|    |----/    |   |          |    |------|    |\\----|    |   |  \\   |    |-----|    |------|    _____      |")
        else:
            print('|          |      |    |         |    \\        /     |      |    |  \\       |   |   \\  |    |     |    |      |         |     |')
    sleep(0.7)
    print("\\------    |      |    |         |     \\______/      |      |    |    \\     |   |    \\ |    |     |    |      |    -----      ■")
    sleep(3)
def menu():
    opcao = questionary.select("\nMenu Principal",
                               choices = ["Começar jogo",
                                        "Configurações",
                                        "Sair do jogo"]).ask()
    if opcao == "Começar jogo":
        return 1
    elif opcao == "Configurações":
        return 2
    elif opcao == "Sair do jogo":
        return 3
def jogo():
    barra = ''
    for c in range(101):
        print(f"\rCarregando {c}%: |{barra}|", end='')
        if c%2 == 0:
            barra+="■"
        sleep(0.05)
    pygame.mixer.music.stop()
    os.system("cls")
    sleep(1)
    nome = str(input("Qual o seu nome, capivara?\n")).strip()
    inicio = f"bem, {nome}, essa jornada será mais que lendária..."
    anima1 = ""
    pygame.mixer.music.load("teclado.mp3")
    pygame.mixer.music.play()
    sleep(0.8)
    for letra in inicio:
        anima1 += letra
        print(f"\r{anima1}",end='')
        sleep(0.08)
        if len(anima1) == 5 + len(nome):
            pygame.mixer.music.stop()
            sleep(1.2)
            pygame.mixer.music.load("teclado.mp3")
            pygame.mixer.music.play()
            sleep(0.8)
    pygame.mixer.music.stop()
    sleep(2)
    os.system("cls")
    
    input()



while True:
    iniciar()
    if menu() == 1:
        jogo()
    elif menu() == 2:
        pygame.mixer.music.stop()
        os.system("cls")
