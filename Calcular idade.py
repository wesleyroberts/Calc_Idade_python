import datetime                 #Módulo da Biblioteca
from datetime import date       #classe Date
#cabeçalho
print('='*20)
print('CALCULADORA DE IDADE')
print('='*20)
 
def leiaInt(msg):
 ok= False
 valor=0
 while True:
   n=str(input(msg))
   if n.isnumeric():
    valor=int(n)
    ok=True
   else:
     print('Erro, só pode digitar numeros')
   if ok:
     break
 return valor         
 
#entrada de dados
nome=(input('Digite seu Nome:'))
 
print('Nas perguntas a seguir adicionar somente números')
dia=leiaInt('Digite o dia em que você nasceu:')
mes=leiaInt('Digite o mês em que você nasceu:')
ano =leiaInt('Digite o ano em que você nasceu:')
 
#Diferença entre data atual e data de Nascimento
data_nasc=datetime.date(ano, mes, dia)
diferenca=(date.today()-data_nasc)
 
#CAlculo do resultado
resultado= (diferenca.days/365.25)
#formata string onde o %d torna o número inteiro
print('%s tem %d anos'%(nome,resultado))
