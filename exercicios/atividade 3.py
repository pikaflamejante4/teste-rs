import os
os.system("clear")

#Solicite dois números. Se forem iguais, mostre o produto; caso contrário, mostre a soma.

primeiro_numero=float(input("Digite seu numero: "))
segundo_numero=float(input("Digite seu numero: "))
produto= primeiro_numero * segundo_numero
soma= primeiro_numero + segundo_numero


if primeiro_numero == segundo_numero:
    print(f"Produto: {produto}")
    
else:
    print(f"Soma: {soma}")



