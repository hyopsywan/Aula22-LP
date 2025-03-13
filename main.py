from operacoes import soma,subtracao,multiplicacao,divisao
from utils import exibir_resultado
operacao= input("escolha uma operacao (+,-,*,/)")
a = int (input ("Digite um valor:"))
b = int (input ("Digite um segundo valor:"))

if operacao == "+":
    resultado = soma (a,b)

elif operacao == "+":
    resultado = soma (a,b)

elif operacao == "-":
    resultado = subtracao (a,b)

elif operacao == "*":
    resultado = multiplicacao (a,b)

elif operacao == "/": 
    resltado = divisao (a,b)   

exibir_resultado (operacao, resultado)
