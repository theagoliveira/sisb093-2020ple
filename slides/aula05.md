---
marp: true
theme: uncover-thiago
_class: invert
---

<title>Aula 5 — Slides</title>

# **SISB093 - Programação 3**

## Aula 5

Prof. Thiago Cavalcante

---

<!-- paginate: true -->
<!-- header: Capítulo 6: Funções com resultado -->

# Valores de retorno

Instrução `return`

---

# <!-- fit --> Desenvolvimento incremental

> A meta do desenvolvimento incremental é evitar longas sessões de depuração (ou *debugging*), acrescentando e testando pequenas partes do código de cada vez.

---

# Funções booleanas

Funções que retornam `True` ou `False`

---

# Verificação de tipos

Função `isinstance`

---

<!-- _class: small-ol text-justify decrease-font -->

# Exercício 6.3

Um palíndromo é uma palavra que se soletra da mesma forma nos dois sentidos, como "osso" e "reviver".
As funções seguintes recebem uma string como argumento e retornam as letras iniciais, finais e do meio das palavras:

```python
def primeira_letra(palavra):
    return palavra[0]
def ultima_letra(palavra):
    return palavra[-1]
def meio(palavra):
    return palavra[1:-1]
```

---

<!-- _class: small-ol text-justify decrease-font -->

# Exercício 6.3 (cont.)

1. Digite essas funções em um arquivo chamado palindromo.py e teste-as. O que acontece se chamar middle com uma string de duas letras? Uma letra? E se a string estiver vazia, escrita com `''` e não contiver nenhuma letra?

2. Escreva uma função chamada `checar_palindromo` que receba uma string como argumento e retorne True se for um palíndromo e False se não for. Lembre-se de que você pode usar a função integrada `len` para verificar o comprimento de uma string.
