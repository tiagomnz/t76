#!/bin/python3
num = int(input("Insira o numero natural :"))
num2 = int(num) + 1
num3 = int(num) - 1

# Sequencia do exercicio
while num != 0 :
    if num < 10 :
        print ("String menor do que 10 caracteres !")
        num = int(input("Insira o novo numero natural :"))
    else :
        print ("O valor digitado foi : {0} // Somado a 1 = {1} // Subtraido 1 = {2}" .format(num,num2,num3))
        break
    


