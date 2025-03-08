import os
os.system ("clear")

#Faça um algoritmo que solicite ao usuário dois números e um
#caractere que calcula as operações básicas (+ - * /).  
#Mostre os números informados pelo usuário,o operador escolhido e
#o resultado.

primeiro_numero = float(input("Digite o numero: "))
operador = input("Digite seu operador (+ - * /): ")
segundo_numero = float(input("Digite o numero: "))

match operador:
    case "+": 
       resultado = primeiro_numero + segundo_numero
    case "-": 
       resultado = primeiro_numero - segundo_numero
    case "*": 
        resultado = primeiro_numero * segundo_numero
    case "/": 
        resultado = primeiro_numero / segundo_numero
    case _:
        "Operação inválida"
print (f"\nPrimeiro número: {primeiro_numero}  ")
print (f"Operador: {primeiro_numero}  ")
print (f"Segundo_numero: {segundo_numero}  ")
print (f"Resultado: {resultado}")

