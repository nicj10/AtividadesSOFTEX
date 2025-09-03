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

def calculadora(a, b):
    def soma(a, b):
        return a + b
    def subt(a, b):
        return a - b
    def mult(a, b):
        return a * b
    def divi(a, b):
        return a / b

num = float(input("Digite um número:"))
num1 = float(input("Digite o segundo número:"))
oper = int(input("SELECIONE A OPERAÇÃO\n " \
                "1 - SOMA\n " \
                "2 - SUBTRAÇÃO\n" \
                "3 - MULTIPLICAÇÃO\n" \
                "4 - DIVISÃO"))

match oper:
    case 1:
        print(calculadora().soma(num, num1))