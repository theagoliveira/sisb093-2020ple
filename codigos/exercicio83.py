def checar_palindromo(palavra):
    return palavra == palavra[::-1]


print(checar_palindromo("reviver"))
print(checar_palindromo("abcdefg"))
