---
marp: true
theme: uncover-thiago
_class: invert
---

<title>Aula 3 — Slides</title>

# **SISB093 - Programação 3**

## Aula 3

Prof. Thiago Cavalcante

---

<!-- paginate: true -->
<!-- header: Capítulo 3: Funções -->

# Funções

> Uma função é uma **sequência nomeada de instruções** que executa uma operação de computação. Ao definir uma função, você especifica o nome e a sequência de instruções. Depois, **pode "chamar" a função** pelo nome.

---

# Chamada de função

`nome(argumentos)`

---

# Funções matemáticas

Módulo `math`

---

# Composição

> Uma das características mais úteis das linguagens de programação é a sua capacidade de usar pequenos blocos de montar para compor programas.

---

# <!-- fit --> Como acrescentar novas funções

```python
def nome():
    # corpo da função composto por
    # uma sequência de instruções

```

---

# Uso e definições

> A definição de função tem que ser executada antes que a função seja chamada.

---

# Fluxo de execução

[Python Tutor: Visualizador de fluxo de execução](http://www.pythontutor.com/)

---

# Parâmetros e argumentos

```python
# definição da função
def nome(parâmetros):
    # corpo da função composto por
    # uma sequência de instruções

# chamada da função
nome(argumentos)
```

---

# <!-- fit --> As variáveis e os parâmetros são locais

---

# <!-- fit --> Funções com resultado e funções nulas

---

# Por que funções?

* Nomear um grupo de instruções
* Eliminar código repetitivo
* Depurar (ou "Debugar") por partes
* Reusabilidade

---

<!-- _class: small-ol text-justify decrease-font -->

# Exercício 3.1

Escreva uma função chamada `alinhar_direita`, que receba uma string chamada s como parâmetro e exiba a string com espaços suficientes à frente para que a última letra da string esteja na coluna 70 da tela:

```python
>>> alinhar_direita('teste')
                                                          teste
```

Dica: Use concatenação de strings e repetição. Além disso, o Python oferece uma função chamada `len`, que apresenta o comprimento de uma string, então o valor de `len('teste')` é 5.

---

<!-- _class: small-ol text-justify decrease-font -->

# Exercício 3.2 (parte)

Um objeto de função é um valor que pode ser atribuído a uma variável ou passado como argumento. Por exemplo, `rodar_2x` é uma função que recebe um objeto de função e o chama 2 vezes:

```python
def rodar_2x(f):
    f()
    f()
```

Aqui está um exemplo que usa `rodar_2x`:

```python
def imprimir_texto():
    print('texto')
rodar_2x(imprimir_texto)
```
