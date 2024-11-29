texto_padrao1 = "Qual o "
texto_padrao2 = " numero que gostaria de "
valorAcumulado = 0
def calculador():
    print(
        f"Temos as opções disponiveis na calculadora atual:\n"
        "\n"
        f"Soma (Digite +)\n"
        f"Subtração (Digite -)\n"
        f"Multiplicação (Digite *)\n"
        f"Divisão (Digite /)\n"
        f"Caso queira sair (Digite Sair)\n "
        )
    selecao = input("Qual operação gostaria de fazer?? ").lower()
    if selecao == "+":
        operador = "somar: "
        print("Você irá realizar uma soma")
        sequencia = "primeiro"
        numero1 = int(input(f"{texto_padrao1}{sequencia}{texto_padrao2}{operador}"))
        sequencia = "segundo"
        numero2 = int(input(f"{texto_padrao1}{sequencia}{texto_padrao2}{operador}"))
        resultado = numero1 + numero2
        print(f"{resultado}")
        calculador()
    elif selecao == "-":
        operador = "subtrair: "
        print("Você irá realizar uma subtração")
        sequencia = "primeiro"
        numero1 = int(input(f"{texto_padrao1}{sequencia}{texto_padrao2}{operador}"))
        sequencia = "segundo"
        numero2 = int(input(f"{texto_padrao1}{sequencia}{texto_padrao2}{operador}"))
        resultado = numero1 + numero2
        print(f"{resultado}")
        calculador() 
    elif selecao == "*":
        operador = "multiplicar: "
        print("Você irá realizar uma multiplicação")
        sequencia = "primeiro"
        numero1 = int(input(f"{texto_padrao1}{sequencia}{texto_padrao2}{operador}"))
        sequencia = "segundo"
        numero2 = int(input(f"{texto_padrao1}{sequencia}{texto_padrao2}{operador}"))
        resultado = numero1 + numero2
        print(f"{resultado}")
        calculador()
    elif selecao == "/":
        operador = "dividir: "
        print("Você irá realizar uma divisão")
        sequencia = "primeiro"
        numero1 = int(input(f"{texto_padrao1}{sequencia}{texto_padrao2}{operador}"))
        sequencia = "segundo"
        numero2 = int(input(f"{texto_padrao1}{sequencia}{texto_padrao2}{operador}"))
        resultado = numero1 + numero2
        print(f"{resultado}")
        calculador()
    elif selecao == "sair":
        exit()
    else:
        print("Não reconheci o operador")
        calculador()

calculador()