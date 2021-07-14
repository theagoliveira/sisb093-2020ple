---
marp: true
theme: uncover-thiago
_class: invert
---

<title>Aula 2 — Slides</title>

# **SISB093 - Programação 3**

## Aula 2

Prof. Thiago Cavalcante

---

<!-- paginate: true -->
<!-- header: Capítulo 2: Variáveis, expressões e instruções -->

# Modo script

---

<!-- _class: decrease-font text-justify -->

# Modo script (cont.)

Para verificar sua compreensão, digite as seguintes instruções no interpretador do Python e veja o que fazem:

```python
5
x = 5
x + 1
```

Agora ponha as mesmas instruções em um script e o execute. Qual é a saída? Altere o script transformando cada expressão em uma instrução de exibição e então o execute novamente.

---

# Ordem das operações

- Parênteses > Exponenciação > Multiplicação e Divisão > Adição e Subtração
- Operadores com a mesma precedência são avaliados da *esquerda para a direita*

---

# Operações com strings

- Em geral, não é possível executar operações matemáticas com strings, mesmo se elas parecerem números
- Duas exceções: **+** (concatenação) e **\*** (repetição)

---

# Comentários

* Notas que **explicam** o que o programa está fazendo
* Começam com o símbolo **#**
* Pode ficar **sozinho em uma linha** ou **ao final de uma linha de comando**
* Tudo **do # ao fim da linha** é ignorado pelo interpretador
* Evitar comentários **redundantes**
* Equilíbrio: nomes de variáveis $\times$ comentários

---

<!-- _class: small-ol text-justify -->

# Exercício 2.1

1) Vimos que n = 42 é legal. E 42 = n?
2) Ou x = y = 1?
3) Em algumas linguagens, cada instrução termina em um ponto e vírgula ;. O que acontece se você puser um ponto e vírgula no fim de uma instrução no Python?
4) E se puser um ponto no fim de uma instrução?
5) Em notação matemática é possível multiplicar x e y desta forma: xy. O que acontece se você tentar fazer o mesmo no Python?


---

<!-- _class: small-ol text-justify -->

# Exercício 2.2

Pratique o uso do interpretador como uma calculadora:

1) O volume de uma esfera com raio r é $\frac{4}{3}\pi r^3$. Qual é o volume de uma esfera com raio 5?
2) Suponha que o preço de capa de um livro seja R\$24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R\$3,00 para o 1º exemplar e R\$0,75 para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?
3) Se eu sair da minha casa às 6:52 e correr 1 km a um certo passo (8min15s por km), então 3 kms a um passo mais rápido (7min12s por km) e 1 km no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?
