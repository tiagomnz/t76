#!/usr/env python

aeronaves = []
aeroportos = []


def menu(titulo, opcoes):
    while True:
        print("=" * len(titulo), titulo, "=" * len(titulo), sep="\n")
        for i, (opcao, funcao) in enumerate(opcoes, 1):
            print("[{}] - {}".format(i, opcao))
        print("[{}] - Retornar/Sair".format(i+1))
        op = input("Opção: ")
        if op.isdigit():
            if int(op) == i + 1:
                # Encerra este menu e retorna a função anterior
                break
            if int(op) < len(opcoes):
                # Chama a função do menu:
                opcoes[int(op) - 1][1]()
                continue
        print("Opção inválida. \n\n")

def principal():
    opcoes = [
        ("Adicionar", adicionar),
        ("Listar", listar),
        ("Procurar", procurar)
    ]
    return menu("Menu  principal", opcoes)

def adicionar():
    opcoes = [
        ("Aeronaves", adicionar_aeronave),
        ("Aeroportos", adicionar_aeroporto),
        # ...
    ]
    return menu("Adicionar", opcoes)

def adicionar_aeronave():
    aeronaves.append(input("Nova aeronave: "))


def adicionar_aeroporto():
    aeroportos.append(input("Nova aeronave: "))

    #...

def listar():
   ...

def procurar():
   ...

def systeminfo():
    ...

def ping ():
    ...

def 
principal()