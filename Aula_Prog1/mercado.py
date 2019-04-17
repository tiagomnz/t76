#!/bin/python3
merc = input ("Informe o nome da mercadoria : ")
prec = int(input ("Informe o preço da mercadoria : "))
quan = int(input ("Informe a quantidade vendida : "))
fatu = prec * quan
esto = [merc, prec, quan, fatu]
ultm = esto[-1]
print (ultm)


while True:
    resp = input("Cadastrar outra mercadoria (s/n) ?")
    if resp == 'sim' or resp == 's' or resp == 'yes' or resp =="y" :

        merc = input ("Informe o nome da nova mercadoria : ")
        prec = int(input ("Informe o preço da nova mercadoria : "))
        quan = int(input ("Informe a quantidade vendida : "))
        esto.append(merc)
        esto.append(prec)
        esto.append(quan)
        fatu = prec * quan
        esto.append(fatu)
        ultm = fatu + ultm
        
        
    elif resp == "não" or resp == "n" or resp == "no" or resp == "n" :
        print (esto)
        print ("Faturmanto : {0}".format(ultm))
        break
    else:
        print ("Responder s/n")
        pass



