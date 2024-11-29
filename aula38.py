primeiro_numero = int(input("Qual o primeiro número??"))
segundo_numero = int(input("Qual o segundo número??"))

if primeiro_numero>segundo_numero:
    print(f"O {primeiro_numero=:.2f} é maior")
elif segundo_numero>primeiro_numero:
    print(f"O {segundo_numero=:.2f} é maior")
elif primeiro_numero==segundo_numero:
    print(f"Ambos são iguais")
else:
    print("Nenhum numero digitado ou os dois números são iguais!!")
