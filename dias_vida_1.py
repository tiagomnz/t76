#!/bin/python
import datetime
date_entry = input("Informe a data de nascimento  :  ")
## ----
## Conversão de data --- analisar
##date_object = datetime.strptime(date_entry, '%d/%m/%y')
##print (date_object)
## ----
year, month, day = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day)
hj = datetime.date.today()
## ---
# idade
if date1.month > hj.month:
    byear = (hj.year - date1.year) - 1
else :
    byear = hj.year - date1.year
## - Convertendo
hj_num = hj.toordinal()
date2 = date1.toordinal()
days_live = hj_num - date2
print ("Dias vividos : {0} dias".format (days_live))
print ("Idade : {0} anos".format(byear))

