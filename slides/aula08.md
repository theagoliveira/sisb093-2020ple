---
marp: true
theme: uncover-thiago
_class: invert
---

<title>Aula 8 — Slides</title>

# **SISB093 - Programação 3**

## Aula 8

Prof. Thiago Cavalcante

---

<!-- paginate: true -->
<!-- header: Capítulo 8: Strings -->

# Operador in

> Operador booleano que recebe duas strings e retorna `True` se a primeira aparecer como uma substring da segunda.

---

# Comparação de strings

> Os operadores relacionais funcionam em strings.

---

<!-- _class: small-ol text-justify decrease-font -->

# Exercício 8.1

Leia a documentação dos métodos de strings em http://docs.python.org/3/library/stdtypes.html#string-methods. Pode ser uma boa ideia experimentar alguns deles para entender como funcionam. strip e replace são especialmente úteis.

A documentação usa uma sintaxe que pode ser confusa. Por exemplo, em `find(sub[, start[, end]])`, os colchetes indicam argumentos opcionais. Então `sub` é exigido, mas `start` é opcional, e se você incluir `start`, então `end` é opcional.

---

<!-- _class: small-ol text-justify decrease-font -->

# Exercício 8.3

Uma fatia de string pode receber um terceiro índice que especifique o "tamanho do passo"; isto é, o número de espaços entre caracteres sucessivos. Um tamanho de passo 2 significa tomar um caractere e outro não; 3 significa tomar um e dois não etc.

Um tamanho de passo -1 atravessa a palavra de trás para a frente, então a fatia `[::-1]` gera uma string invertida.

Use isso para escrever uma versão de uma linha de `checar_palindromo` do Exercício 6.3.
