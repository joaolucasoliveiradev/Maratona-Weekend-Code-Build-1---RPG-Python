from time import sleep
import pygame
import os
import questionary


pygame.init()
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
    os.system("cls")
    print("Carregando")
    for c in range(100):
        sleep(1)
        print(c)
        os.system("cls")


iniciar()
menu()
if menu == 1:
    jogo()