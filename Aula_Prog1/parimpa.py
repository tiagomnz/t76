#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""parimpar.py: Faça um programa em Python onde o usuário digita um número e o programa exibe se ele
é par ou ímpar."""

__author__      = "Tiago Menezes"
__copyright__   = "Copyright 2019, Planet Earth"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Tiago Menezes"
__email__ = "tiagomnz@gmail.com"
__status__ = "Production"

numero=float(input("Digite um número : "))
resto = numero % 2
if resto == 0:
    print ( "Numero PAR !")
else:
    print ("Numero IMPAR !")