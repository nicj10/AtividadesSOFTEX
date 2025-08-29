# 1°)

livros = ['turma da monica', 'attack on titan', 'a cabana']
# print(livros)

# 2°)
# print(livros[0])
# print(livros[-1])

# 3°)
livros.append("Silêncio dos inocentes")
# print(livros)

# 4°)
livros.insert(1, "Duna")
# print(livros)

# 5°)
'''
if("Silêncio dos inocentes" in livros):
    livros.remove("Silêncio dos inocentes")
    print("Livro removido com sucesso")
    print(livros)
else:
    print("O livro não se encontra na lista")
    print(livros)
'''

# 7°)

for livro in livros:
    print(f"O livro {livro} é muito bom")