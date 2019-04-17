#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""moeda.py: calcular o valor em reais que existe em um cofre
automatizado ."""

__author__      = "Tiago Menezes"
__copyright__   = "Copyright 2019, Planet Earth"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Tiago Menezes"
__email__ = "tiagomnz@gmail.com"
__status__ = "Production"



ummreal = int(input("Informe o valor de 1,00   real : "))
cinqcen = int(input("Informe o valor de 50 centavos : "))
vintcen = int(input("Informe o valor de 20 centavos : "))
dezzcen = int(input("Informe o valor de 10 centavos : "))
cinccen = int(input("Informe o valor de 5  centavos : "))

rcinqcen = cinqcen * 0.20
rvintcen = vintcen * 0.5
rdezzcen = dezzcen * 0.10
rcinccen = cinccen * 0.05


print ("Total de 1 real : {0} reais ".format(ummreal))
print ("Total de 50 centavos : {0} reais".format(rcinccen))
print ("Total de 20 centavos : {0} reais ".format(rvintcen))
print ("Total de 10 centavos : {0} reais".format(rdezzcen))
print ("Total de 5  centavos : {0} reais".format(rcinccen))


