---
marp: true
theme: uncover-thiago
_class: invert
---

<title>Aula 6 — Slides</title>

# **SISB093 - Programação 3**

## Aula 6

Prof. Thiago Cavalcante

---

<!-- paginate: true -->
<!-- header: Capítulo 7: Iteração -->

# Reatribuição

```python
>>> x = 5
>>> x
5
>>> x = 7
>>> x
7
```

---

# Atualização de variáveis

> Um tipo comum de reatribuição, onde o novo valor da variável depende do velho.

---

# Instrução while

> 1. Determine se a condição é verdadeira ou falsa.
> 2. Se for falsa, saia da instrução `while` e continue a execução da próxima instrução.
> 3. Se a condição for verdadeira, execute o corpo e então volte ao passo 1.

---

# break

Saindo do *loop*

---

<!-- _header: Capítulo 6: Funções com resultado -->
<!-- _class: small-ol text-justify decrease-font -->

# Exercício 6.3 (cont.)

1. Digite essas funções em um arquivo chamado palindromo.py e teste-as. O que acontece se chamar middle com uma string de duas letras? Uma letra? E se a string estiver vazia, escrita com `''` e não contiver nenhuma letra?

2. Escreva uma função chamada `checar_palindromo` que receba uma string como argumento e retorne True se for um palíndromo e False se não for. Lembre-se de que você pode usar a função integrada `len` para verificar o comprimento de uma string.

---

<!-- _class: small-ol text-justify decrease-font -->

# Exercício 7.3

O matemático S. Ramanujan encontrou uma série infinita que pode ser usada para gerar uma aproximação numérica de $1/\pi$:

$$ \frac{1}{\pi} = \frac{2\sqrt{2}}{9801}\sum_{k=0}^\infty \frac{(4k)!(1103 + 26390k)}{(k!)^4396^{4k}} $$

Escreva uma função chamada `estimar_pi` que use esta fórmula para computar e devolver uma estimativa de $\pi$. Você deve usar o loop `while` para calcular os termos da adição até que o último termo seja menor que $1\times10^{-15}$. Você pode verificar o resultado comparando-o com `math.pi`.
