# Vamos solicitar como entrada dois númeors
# e depois vamos realizar uma operacao simples
# entre eles 

primeiro_numero = int(input("Digite o primeiro número"))
segundo_numero = int(input("Digite o segundo número"))

def soma():
    return f"O valor da soma é {primeiro_numero + segundo_numero}"

def subtracao():
    return f"O valor da subtração é {primeiro_numero - segundo_numero}"

def multiplicacao():
    return f"O valor da multiplicação é {primeiro_numero * segundo_numero}"

def divisao():
    return f"O valor da divisão é {primeiro_numero / segundo_numero}"

operacoes = {
    "1": multiplicacao(), "2":divisao(), 
    "3":soma(), "4":subtracao()
}

opcao = input("""Operações:
      [1]: Multiplicação
      [2]: Divisão
      [3]: Soma
      [4]: Subtração""")

print(f"O valor da operacao é : {operacoes.get(opcao, "opcão invalida")}")
