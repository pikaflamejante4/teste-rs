import os
os.system("clear")

#Solicite dois números e informe qual é o maior

primeiro_numero=float(input("digite seu numero: "))
segundo_numero=float(input("digite seu numero: "))

if primeiro_numero > segundo_numero:
    maior = primeiro_numero
    menor = segundo_numero
else:
    maior = segundo_numero
    menor = primeiro_numero

print(f"Menor: {menor}")
print(f"Maior: {maior}")




