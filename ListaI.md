# Nivelamento POO

## Questão 1

### a) Explique com suas palavras uma vantagem da POO sobre a Programação Estruturada

> POO tem a vantagem de possibilitar uma organização melhor do código, com reaproveitamento dele através de classes e herança.

### b) O que é um objeto?

> são instâncias geradas a partir de moldes chamados classes, possuindo estrutura baseada nesse *blueprint*. Objetos podem apresentar atributos e métodos.

### c) O que é propriedade dinâmica e propriedade estática de um objeto? Dê exemplos concretos



### d) O que é encapsulamento? Por que ele é importante na Programação Orientada a Objetos?

> Encapsulamento é uma forma de privar o acesso a certas variáveis e métodos de uma classe. Ele é importante para esconder certas habilidades dos usuários e para dar uma maior robustez ao código.

### e) Para que serve o estado de um objeto? E o comportamento de um objeto?

> O estado corresponde as variáveis de um objeto (os atributos), responsáveis por armazenar informação desses objetos, ao passo que o comportamento define o que o objeto pode fazer (são os métodos).

### f) De que forma implementamos o estado e o comportamento de um objeto? Dê exemplos usando código
```python
class surfer():
  def __init__():
    self.board = "fishboard"
    self.size = "6.10"
    self.is_broken = False
   
   def change_board(board, size):
    self.board = board
    self.size = size
   
   def break_board():
    self.is_broken = True
```

> No caso acima, quando criado um objeto apartir dessa classe, o estado seria *board, size e is_broken*, ao passo que os comportamentos seriam change_board e break_board.

### g) O que é uma referência para um objeto?

### h) O que acontece quando atribuímos uma referência para um objeto a uma outra referência?

### i) O que é uma classe? Paraque serve uma classe? Cite um exemplo em código.

### j) Explique com suas palavras o significado de uma variável de classe e uma variável de instancia. Sabemos que uma mesma classe pode possuir vários métodos (ou construtores) com o mesmo nome. Qual o nome dado a esta situação? Neste caso, como Java consegue distinguir um método(ou construtor) de outro? (use um exemplo para explicar melhor).

### k) Qual é a diferença entre this, super, this() e super()?

### l) Quais são os três tipo de erros de execução que um programa pode gerar? Quais podemos tratar com exceções?

### m) Qual a diferença entre a classe Exception e Error?

### n) Explique a utilização dos comandos try-catch, throw, throws e finally

## Questão 2

Selecione 2 (dois) pacotes vistos na disciplina anterior de Java ou outro projeto de software O.O que você conhece para escolher 3 (três) classes para descrever (nome da classe, o que  a  classe  faz,  construtores,  principais  métodos,  atributos,  relacionamento  de  herança  com outras classese que interfaces implementam a classe).
