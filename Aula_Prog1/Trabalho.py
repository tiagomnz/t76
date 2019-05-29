#!/bin/env python

import os
import getpass   ## usado para esconder a senha
import glob      ## uso de globs


usuario = "root"
senha = "redes"

for x in usuario:
    print("##### Seja Bem vindo ###### ")
    x = input ("Usuario : ")
    y = getpass.getpass ("Senha : ", stream=None)
    if (x == usuario and y == senha):
        # Captura local
        lista_path = []
        path = os.getcwd()
        path = str(path)

        ## lista diretorio usando lista.
        print("Diretorio Atual = %s" % path)
        unidade_disco = path[0]
        print("Unidade de Disco = %s " % unidade_disco)

        ## lista arquivos
        print("-------------# Lista de arquivos #------------")

        files = [f for f in glob.glob(path + "**/*.*", recursive=True)]
        for f in files:
            print(f)
        print("-----------# Fim da lista #-----------")

        # Mostra diretorio

        p1, p2, p3, p4, p5  = path.split('/')

        #print do usuario
        print ("Nome do Usuário :", p3)

        # print pasta atual
        print ("Pasta Atual : ", p4)

    else:
        print ( "Usuário ou senha incorreta")












# while (usuario != "root") and (senha != "redes"):
#     print ("Senha errada")
#
#     print ("##### Seja Bem vindo ###### ")
#
#     usuario = input("Usuario : ")
#     senha = input("Senha: ")
#

###

#lista_path = []
#path = os.getcwd()

#path = str(path)
#lista_path = path.split("\\")
#print(lista_path)
#print("Diretorio Atual = %s" % path)
#unidade_disco = lista_path[0]
#ud = unidade_disco[:-1]
#print("Unidade de Disco = %s " % ud)
#print(lista_path)


