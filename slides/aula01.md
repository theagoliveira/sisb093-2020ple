---
marp: true
theme: uncover-thiago
_class: invert
---

<title>Aula 1 — Slides</title>

# **SISB093 - Programação 3**

## Aula 1

Prof. Thiago Cavalcante

---

<!-- paginate: true -->

# Cronograma

| Semana | Data       | Evento        |
| :----- | :--------- | :------------ |
| 01     | 19/10/2020 | Aulas e Lista |
| 02     | 26/10/2020 | Aulas e Lista |
| 03     | 02/11/2020 | Aulas e Lista |
| 04     | 09/11/2020 | Encontro      |
| 05     | 16/11/2020 | AB1           |
| 06     | 23/11/2020 | Aulas e Lista |
| 07     | 30/11/2020 | Aulas e Lista |
| 08     | 07/12/2020 | Aulas e Lista |
| 09     | 14/12/2020 | Encontro      |
| 10     | 21/12/2020 | AB2           |
| 11     | 04/01/2021 | Reavaliação   |
| 12     | 11/01/2021 | Final         |

---

<!-- _class: large-ul -->

# Avaliação

- Listas: 30%
- Provas: 60%
- Participação: 10% (entregas)

---

<!-- _class: large-ul -->

# Google Classroom

- Aulas
- Atividades
- Materiais
- Dúvidas

---

# Programação Orientada a Objetos usando **Python**

<br>

[![Python Logo](https://www.python.org/static/community_logos/python-logo-generic.svg)](https://www.python.org)

---

# Introdução ao Python

Referência: [Pense em Python, 2ª Edição](https://penseallen.github.io/PensePython2e/)

---

<!-- header: Capítulo 1: A jornada do programa -->

# Execução do Python

1) Usar o Python na nuvem, no modo interativo ([PythonAnywhere](https://www.pythonanywhere.com/), [Repl.it](https://repl.it/))
2) Ainda na nuvem, criar arquivos de *scripts* com os códigos e rodá-los
3) Instalar o Python no seu dispositivo: Linux, [Windows](https://docs.microsoft.com/pt-br/windows/python/beginners), Android ([Pydroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3), [QPython 3L](https://play.google.com/store/apps/details?id=org.qpython.qpy3)) etc.

---

# Interpretador do Python

```text
Python 3.8.0 (default, Nov 11 2019, 13:27:35)
[GCC 9.2.0] on linux
Type "help", "copyright", "credits" or "license" for more
information.
>>>




```

---

# O Primeiro programa

`"Olá, Mundo!"`

---

# Operadores aritméticos

- Adição `+`
- Subtração `-`
- Multiplicação `*`
- Divisão `/`
- Exponenciação `**`

---

# Valores e tipos

---

<!-- _class: small-ol text-justify -->

# Exercício 1.1

1) Em uma instrução print, o que acontece se você omitir um dos parênteses ou ambos?
2) Se estiver tentando imprimir uma string, o que acontece se omitir uma das aspas ou ambas?
3) Você pode usar um sinal de menos para fazer um número negativo como -2. O que acontece se puser um sinal de mais antes de um número? E se escrever assim: 2++2?
4) Na notação matemática, zeros à esquerda são aceitáveis, como em 02. O que acontece se você tentar usar isso no Python?
5) O que acontece se você tiver dois valores sem nenhum operador entre eles?

---

<!-- _class: small-ol text-justify -->

# Exercício 1.2

Inicialize o interpretador do Python e use-o como uma calculadora.

1) Quantos segundos há em 42 minutos e 42 segundos?
2) Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.
3) Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?

---

<!-- header: Capítulo 2: Variáveis, expressões e instruções -->

# Instruções de atribuição

`variável = valor`

---

# Nomes de variáveis

* Devem ser **significativos**
* Podem ser **tão longos** quanto você queira
* Podem conter **letras e números**
* **Não podem começar com um número**
* Convenção: usar apenas **letras minúsculas**
* O caractere `_` pode aparecer em um nome
* Se você der um nome ilegal a uma variável, recebe um **erro de sintaxe**

---

# Nomes de variáveis (cont.)

Palavras-chave (ou reservadas)

```text
and         del         from        None        True
as          elif        global      nonlocal    try
assert      else        if          not         while
break       except      import      or          with
class       False       in          pass        yield
continue    finally     is          raise
def         for         lambda      return
```

---

# Expressões e instruções

* **Expressão:** combinação de **valores**, **variáveis** e **operadores** (pode ser um único valor ou variável, mas não um único operador). É **avaliada** e **tem um valor**.
* **Instrução:** unidade de código que tem um efeito, como criar uma variável ou imprimir um valor na tela. É **executada** e (geralmente) **não tem um valor**.
