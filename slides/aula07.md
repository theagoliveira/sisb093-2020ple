---
marp: true
theme: uncover-thiago
_class: invert
---

<title>Aula 7 — Slides</title>

# **SISB093 - Programação 3**

## Aula 7

Prof. Thiago Cavalcante

---

<!-- paginate: true -->
<!-- header: Capítulo 8: Strings -->

# Uma string é uma sequência

> Uma string é uma sequência de caracteres. Você pode acessar um caractere de cada vez com o operador de colchete `[]`.

---

# len

> Função integrada que devolve o número de caracteres em uma string

---

# Travessia com loop for

---

# Fatiamento de strings

Operador `[n:m]`

---

# Strings são imutáveis

> Você não pode alterar uma string existente.

---

# Buscando

```python
# O que faz a seguinte função?

def buscar(palavra, letra):
    indice = 0
    while indice < len(palavra):
        if palavra[indice] == letra:
            return indice
        indice = indice + 1
    return - 1
```

---

# Loop e contagem

---

# Métodos de strings

`upper`, `lower` e `find`
