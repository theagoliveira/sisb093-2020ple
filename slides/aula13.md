---
marp: true
theme: uncover-thiago
_class: invert
---

<title>Aula 13 — Slides</title>

# **SISB093 - Programação 3**

## Aula 13

Prof. Thiago Cavalcante

---

<!-- paginate: true -->

# Princípios da POO

* Herança
* Encapsulamento
* Abstração
* Polimorfismo
* Extra: *Modularidade, Composição*

---

<!-- _class: small-ul -->

# Herança

* Uma classe obtém parte de suas funcionalidades de outra classe
* Quem herda: **classe derivada**, **subclasse** ou **subtipo**
* Quem é herdada: **classe base** ou **superclasse**
* A subclasse **herda**, **deriva** ou **estende** a classe base
* Cria uma relação de **é um(a)** e estabelece uma hierarquia
* Permite a **reutilização ou substituição** de funcionalidades já implementadas e **adição** de novas funcionalidades independentes
* Objetos da subclasse possuem métodos e atributos da superclasse
* Criação de uma classe base genérica e subclasses específicas
* Python dá suporte a herança simples e múltipla
* :exclamation: *Para se aprofundar no assunto: Princípio da subsituição de **Liskov** e Princípios **SOLID***

---

# Herança em Python

```python
class ClasseBase1:
    # Corpo da classe base 1

class ClasseBase2:
    # Corpo da classe base 2

class Subclasse(ClasseBase1):
    # Corpo da subclasse com herança simples

class SubclasseMultipla(ClasseBase1, ClasseBase2):
    # Corpo da subclasse com herança múltipla
```

---

<!-- _class: small-ul -->

# Encapsulamento

* O comportamento (métodos) de um objeto é mantido escondido do lado externo do programa ***e/ou*** objetos mantém seu estado (propriedades, atributos) privado
* Interfaces **pública** (externa) e **privada** (interna)
* Divisão da classe em três seções: **pública**, **protegida**, **privada**
* Um utilizador da classe não pode alterar ou visualizar o estado de um objeto interagindo **diretamente** com as variáveis de instância, ele deve utilizar métodos expostos na interface (*getters e setters*)

---

<!-- _class: small-ul -->

# <!-- fit --> Vantagens do Encapsulamento

* O desenvolvedor tem a liberdade de modificar o código interno da classe sem se preocupar com outros programadores (contanto que a interface pública se mantenha constante e documentada) ➡ **otimização, correção de bugs**
* Adiciona segurança, pois o acesso aos dados é restrito
* Oferece proteção de propriedade intelectual (quando o utilizador da classe não tem acesso ao seu código-fonte)
* Esconde do usuário a complexidade da implementação

---

<!-- _class: small-ul -->

# <!-- fit --> Encapsulamento em Python

* Python não oferece suporte completo ao encapsulamento
* Não existem palavras-chave **public**, **protected** e **private**, como em outras linguagens
* Nenhum acesso é realmente restrito na implementação em Python
* O encapsulamento em Python é realizado através de convenções associadas aos usos do caractere underscore (`_`) na nomeação de variáveis e métodos

---

<!-- _class: small-ul -->

# Abstração

* Esconder (ou abstrair) a complexidade da classe, de forma que o usuário não precise se preocupar com a implementação interna
* Apresentar ao usuário uma interface simples, de alto nível
* Analogia: carro
* Exemplo de código: classe de equação do segundo grau

---

<!-- _class: small-ul -->

# Polimorfismo

* Chamadas de métodos são determinadas durante a execução do programa, de acordo com o tipo (classe) do objeto ➡ **Busca de métodos dinâmica**
* Permite que objetos de diferentes classes possam ser tratados da mesma forma, se a interface for adequada
* **Duck typing**: *"quando eu vejo um pássaro que caminha como um pato, nada como um pato e grasna como um pato, eu chamo aquele pássaro de pato"*

---

<!-- _class: small-ul -->

# <!-- fit --> Polimorfismo: possibilidades

* Um objeto possui várias implementações de um mesmo método, as quais se diferenciam pela quantidade de parâmetros ➡ **Sobrecarga de métodos**
* Um mesmo operador se comporta de forma diferente quando aplicado a diferentes objetos ➡ **Sobrecarga de operadores**
* Um objeto de uma subclasse possui uma implementação diferente de um método da classe base (o nome permance igual) ➡ **Sobrescrita de métodos** (*override*)
* Vários objetos de diferentes classes possuem um método de mesmo nome (mesma interface)

---

<!-- _class: small-ul -->

# <!-- fit --> Polimorfismo em Python

* Python não dá suporte à sobrecarga de métodos com definições múltiplas, mas ela pode ser realizada com a utilização valores padrão, instruções `if/else` ou bibliotecas externas
* Em Python, os operadores e algumas funções integradas estão atrelados a **métodos especiais** (*dunder methods*) que podem ser definidos/sobrescritos para fornecer a funcionalidade desejada

---

| Expressão | Método                  | Retorno |
| :-------- | :---------------------- | :------ |
| `x + y`   | `__add__(self, y)`      | objeto  |
| `x - y`   | `__sub__(self, y)`      | objeto  |
| `x * y`   | `__mul__(self, y)`      | objeto  |
| `x / y`   | `__truediv__(self, y)`  | objeto  |
| `x // y`  | `__floordiv__(self, y)` | objeto  |
| `x % y`   | `__mod__(self, y)`      | objeto  |
| `x ** y`  | `__pow__(self, y)`      | objeto  |

---

| Expressão | Método             | Retorno  |
| :-------- | :----------------- | :------- |
| `x == y`  | `__eq__(self, y)`  | booleano |
| `x != y`  | `__ne__(self, y)`  | booleano |
| `x < y`   | `__lt__(self, y)`  | booleano |
| `x <= y`  | `__le__(self, y)`  | booleano |
| `x > y`   | `__gt__(self, y)`  | booleano |
| `x >= y`  | `__ge__(self, y)`  | booleano |
| `-x`      | `__neg__(self, y)` | objeto   |

---

| Expressão              | Método               | Retorno |
| :--------------------- | :------------------- | :------ |
| `abs(x)`               | `__abs__(self, y)`   | objeto  |
| `float(x)`             | `__float__(self, y)` | float   |
| `int(x)`               | `__int__(self, y)`   | inteiro |
| `str(x)` ou `print(x)` | `__repr__(self, y)`  | string  |
| `x = NomeClasse()`     | `__init__(self, y)`  | objeto  |

---

<!-- _class: small-ul -->

# Modularidade

* Princípio de organização em que diferentes componentes de um programa são dividos em unidades funcionais separadas (módulos)
* Analogia: casa
* Em Python, os módulos são coleções de funções e classes intimamente relacionadas, os quais são definidas, geralmente, em um único arquivo de código (ex.: `math`)
* A utilização da modularidade facilita a correção de problemas no código (rastreamento)
* Permite também a reusabilidade do código em diferentes contextos onde o módulo se encaixa

---

<!-- _class: small-ul -->

# Composição

* Forma de combinar objetos e/ou classes para a criação de tipos de dados mais complexos
* Um método de uma determinada classe chama métodos de um objeto de uma outra classe, integrando sua funcionalidade sem a utilização de herança
* Cria uma relação de **tem um(a)**, sem a definição de uma hierarquia
* Exemplo: empregados e endereços

---

# Exercícios

1. Implemente uma superclasse `Pessoa`. Faça duas outras classes, `Estudante` e `Professor`, que herdam da superclasse `Pessoa`. Uma pessoa possui um nome e uma data de nascimento. Um estudante possui um curso e o professor possui um salário. Escreva as declarações de classe, os construtores e o método `__repr__` para todas as classes.

---

<!-- _class: small-ul -->

2. Criar uma classe para números racionais (frações) com as operações:

- Criar um número racional
- Acessar os valores de numerador e denominador individualmente
- Determinar se o número é negativo ou zero
- Fazer operações matemáticas em dois números racionais (soma, subtração, multiplicação, divisão e exponenciação)
- Comparar dois números racionais
- Criar uma representação em string de um número racional

---

<!-- _class: small-ul -->

# Referências

- GOODRICH, M. T.; TAMASSIA, R.; GOLDWASSER, M. H. **Data Structures and Algorithms in Python** (:us:)
- GIRIDHAR, C. **Learning Python Design Patterns** (:us:/:brazil:)
- HORSTMANN, C.; NECAISE, R. **Python for Everyone** (:us:)
- [**DAN BADER:** The Meaning of Underscores in Python](https://dbader.org/blog/meaning-of-underscores-in-python)
- [**EDUCATIVE.IO:** What is Object Oriented Programming?](https://www.educative.io/blog/object-oriented-programming)
- [**EDUCATIVE.IO:** How to Use OOP in Python](https://www.educative.io/blog/how-to-use-oop-in-python)
- [**PYTHON DOCS:** Classes > Private Variables](https://docs.python.org/3/tutorial/classes.html#private-variables)
- [**PYTHON DOCS:** Data Model > Special Method Names](https://docs.python.org/3/reference/datamodel.html#special-method-names)
- [**REAL PYTHON:** Inheritance and Composition: A Python OOP Guide](https://realpython.com/inheritance-composition-python/)
- [**REAL PYTHON:** Operator and Function Overloading in Custom Python Classes](https://realpython.com/operator-function-overloading/)
