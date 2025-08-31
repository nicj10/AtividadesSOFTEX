# 6°)
'''
num = [1, 2, 3, 2, 4, 2, 5]
print(num.count(2))
'''

# 8°)
'''
lista = [12, 18, 25, 14, 30]

for i in lista:
    if(i >= 18):
        print(i)
'''

# 9°)
'''
lista = [10, 20, 30, 40]
soma = 0

for i in lista:
    soma += i 

print(soma)
'''

# 10°)
notas = [] 

for i in range(2):  
    aluno_notas = []  
    print(f"\nDigite as notas do aluno {i+1}:")
    for j in range(3): 
        nota = float(input(f"Nota {j+1}: "))
        aluno_notas.append(nota)
    notas.append(aluno_notas)  


for i in range(2):
    media = sum(notas[i]) / len(notas[i])
    print(f"Média do aluno {i+1}: {media:.2f}")
