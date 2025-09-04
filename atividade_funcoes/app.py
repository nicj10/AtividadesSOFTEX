# 1.
'''
def saudacao():
    return "Olá, bem-vindo ao Python"

print(saudacao())
'''

# 2.
'''
def dobro(numero):
    return numero * 2

num = float(input("Digite um número: "))
print(dobro(num))
'''

# 3.
'''
def soma(a, b):
    return a + b

num = 10 # Posso fazer com input também, professor? KKKKKKKKK
num1 = 20

print(soma(num, num1))
'''

# 4.
'''
def mensagem(nome):
    if(nome == ""):
        return "Olá, visitante"
    else:
        return "Olá, " + nome;

lindo = input("Digite seu nome: ")

print(mensagem(lindo))
'''

# 5.
'''
def operacoes(a, b):
    soma = a + b
    subt = a - b
    mult = a * b
    return(soma, subt, mult)

num = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print(operacoes(num, num2))
'''

# 6.
'''
def media(*args):
    soma = sum(args)
    return soma / len(args)

notas = []
while True:
    num = float(input("Digite sua nota (0 para sair do loop): "))
    if num == 0:
        break
    notas.append(num)

if notas:
    resultado = media(*notas)
    print(f"A méida é: {resultado}")
else:
    print(f"Bote nota meu filho")    
    
# Professor, usei input dnv pra dificultar um pouco, se tiver algum erro me diz por favor! :)
'''

# 7.
'''
def dados_pessoais(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
cidade = input("Digite sua cidade: ")
dados_pessoais(nome=nome,idade=idade, cidade=cidade) 
# Eu fiz com os dados que o senhor passou mas depois coloquei o input
'''

# 8.
'''
def calculadora(a, b, oper):
    def soma(x, y):
        return x + y

    def subt(x, y):
        return x - y

    def mult(x, y):
        return x * y

    def divi(x, y):
        return x / y

    match oper:
        case 1:
            return soma(a, b)
        case 2:
            return subt(a, b)
        case 3:
            return mult(a, b)
        case 4:
            if b != 0:
                return divi(a, b)
            else:
                return "Erro: divisão por zero"
        case _:
            return "Operação inválida"


# Entrada do usuário
num = float(input("Digite um número: "))
num1 = float(input("Digite o segundo número: "))
oper = int(input("SELECIONE A OPERAÇÃO\n"
                 "1 - SOMA\n"
                 "2 - SUBTRAÇÃO\n"
                 "3 - MULTIPLICAÇÃO\n"
                 "4 - DIVISÃO\n"))

resultado = calculadora(num, num1, oper)
print("Resultado:", resultado)
'''

# 9.
def calculadora(a, b, oper):
    def soma(x, y):
        return x + y

    def subt(x, y):
        return x - y

    def mult(x, y):
        return x * y

    def divi(x, y):
        return x / y

    match oper:
        case 1:
            return soma(a, b)
        case 2:
            return subt(a, b)
        case 3:
            return mult(a, b)
        case 4:
            if b != 0:
                return divi(a, b)
            else:
                return "Erro: divisão por zero"
        case _:
            return "Operação inválida"


num = 10
num1 = 5
oper = 3  # 1 - SOMA, 2 - SUBTRAÇÃO, 3 - MULTIPLICAÇÃO, 4 - DIVISÃO

resultado = calculadora(num, num1, oper)
print("Resultado:", resultado)

