'''
1 - Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
'''
# lista: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for numero in lista:
#     print(numero)

'''
2 - Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
'''
# lista_linguagem: list = ["Python", "Java", "C++", "JavaScript"]
# # lista_linguagem.remove('C++') 
# lista_linguagem.pop(2)
# lista_linguagem.append('Ruby')
# print(lista_linguagem)

'''
3 - Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
'''
dicionario_livro: dict = {
    'Autor': 'Napoleon Hill',
    'Título': 'Mais Espero que o Diabo',
    'Ano': 2020
}
# print(dicionario_livro)

for item in dicionario_livro.items():
    print(item)

'''
4 - Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
'''

'''
5 - Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
'''