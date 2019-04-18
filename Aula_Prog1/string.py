#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""string.py:  Faça um programa em Python que leia uma String do teclado e exiba: o tamanho, o primeiro
e último caractere da mesma (considere que com tamanho >=1 e <=10).."""

__author__      = "Tiago Menezes"
__copyright__   = "Copyright 2019, Planet Earth"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Tiago Menezes"
__email__ = "tiagomnz@gmail.com"
__status__ = "Production"

entrada = input ("Insira uma string : ")
tamanho = int(len(entrada))
print ("Primeiro caracter : {0} ".format(entrada[0]))
print ("Ultimo caracter : {0}".format(entrada[-1]))
print ("Tamanho total : {0}".format(tamanho))
