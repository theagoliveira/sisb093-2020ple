---
marp: true
theme: uncover-thiago
_class: invert
---

<title>Aula 10 — Slides</title>

# **SISB093 - Programação 3**

## Aula 10

Prof. Thiago Cavalcante

---

<!-- paginate: true -->
<!-- header: Capítulo 10: Listas -->

# Objetos e valores

> Se dois objetos forem idênticos, eles também são equivalentes, mas se eles forem equivalentes, não são necessariamente idênticos.

---

# Alias

> Se a se refere a um objeto e você atribui b = a, então ambas as variáveis se referem ao mesmo objeto.

---

# Argumentos de listas

> Ao passar uma lista a uma função, a função recebe uma referência à lista. Se a função alterar a lista, quem faz a chamada vê a mudança.
> (...)
> É importante distinguir entre operações que alteram listas e operações que criam novas listas.

---

<!-- _class: small-ol text-justify decrease-font -->

# Exercício 10.1

Escreva uma função chamada `soma_listas` que receba uma lista de listas de números inteiros e adicione os elementos de todas as listas aninhadas. Por exemplo:

```python
>>> t = [[1, 2], [3], [4, 5, 6]]
>>> soma_listas(t)
21
```

---

<!-- _class: small-ol text-justify decrease-font -->

# Exercício 10.4

Escreva uma função chamada `cortar` que tome uma lista alterando-a para remover o primeiro e o último elementos, e retorne `None`. Por exemplo:

```python
>>> t = [1, 2, 3, 4]
>>> cortar(t)
>>> t
[2, 3]
```

---

<!-- _class: small-ol text-justify decrease-font -->

# Exercício 10.6

Duas palavras são anagramas se você puder soletrar uma rearranjando as letras da outra. Escreva uma função chamada `checar_anagrama` que tome duas strings e retorne `True` se forem anagramas.
