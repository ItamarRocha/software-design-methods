# Nivelamento POO

## Questão 1

### a) Explique com suas palavras uma vantagem da POO sobre a Programação Estruturada

> POO tem a vantagem de possibilitar uma organização melhor do código, com reaproveitamento dele através de classes e herança.

### b) O que é um objeto?

> são instâncias geradas a partir de moldes chamados classes, possuindo estrutura baseada nesse *blueprint*. Objetos podem apresentar atributos e métodos.

### c) O que é propriedade dinâmica e propriedade estática de um objeto? Dê exemplos concretos

> propriedade dinâmica pode ser alterada ao passo que a estática é algo fixo.
```C++
int main
{
    const int a = 10;
    const int b = a + 10; //funciona ok 
    i++;    // erro de compilação 
}
```

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

> Tudo em python é passado por referência, uma referência é o endereço desse objeto na memória.

### h) O que acontece quando atribuímos uma referência para um objeto a uma outra referência?

> Quando atribuímos uma referência para um objeto a uma outra referência, substituimos o valor antigo da referência, que passa a apontar para a referência do objeto.

### i) O que é uma classe? Paraque serve uma classe? Cite um exemplo em código.

> Uma classe é um *blueprint* para os objetos. a classe surfer abordada em cima serve como molde para criação de objetos.
```Python
john = surfer()
jonh.change_board("pranchinha", "5.11")
```

### j) Explique com suas palavras o significado de uma variável de classe e uma variável de instancia. Sabemos que uma mesma classe pode possuir vários métodos (ou construtores) com o mesmo nome. Qual o nome dado a esta situação? Neste caso, como Java consegue distinguir um método(ou construtor) de outro? (use um exemplo para explicar melhor).

> A variável de classe pertence à classe ao passo que a de instância é parte do objeto. Se uma mudança for feita em uma variável de classe, essa mesma mudança será percebida por todos os objetos feitos a partir dela. Overloading (sobrecarga) de classe/método. É possível distinguir um construtor de outro pois eles devem ter parâmetros diferentes, para o caso de métodos, são distinguíveis por ter parâmetros ou tipos diferentes. Não podem ser iguais.

```C++
int rotate(){
  return 90;
}

int rotate(int number){
  return 90 + number;
}
```

### k) Qual é a diferença entre this, super, this() e super()?

> o self em python seria equivalente ao this em C++. O self é uma referência à instância da classe e é usado pra acessar as variáveis que pertencem a classe.
> a função super é usada para dar acesso aos métodos e variáveis de uma classe, por meio de herança. Ele retorna um objeto que representa a classe pai.

### l) Quais são os três tipo de erros de execução que um programa pode gerar? Quais podemos tratar com exceções?

> runtime, Aritmético, resources. Todos eles.

### m) Qual a diferença entre a classe Exception e Error?

> Um erro é um problema que uma aplicação não deve tratar e é algo que deve ser consertado. Uma exceção é uma condição que uma aplicação queira tratar para continuar a execução normal do programa.

### n) Explique a utilização dos comandos try-catch, throw

> Try catch é utilizado para tratamento de exceções. Se houver uma exceção dentro do bloco, a execução dentro do bloco try terminará e o erro será tratado no catch e a execução do programa continuará normalmente. O throw é utilizado para lançar exceções quando algo fora do comum ocorrer no programa.

## Questão 2

Selecione 2 (dois) pacotes vistos na disciplina anterior de Java ou outro projeto de software O.O que você conhece para escolher 3 (três) classes para descrever (nome da classe, o que  a  classe  faz,  construtores,  principais  métodos,  atributos,  relacionamento  de  herança  com outras classes e que interfaces implementam a classe).

1. https://keras.io/api/models/sequential/
  > Se resume a uma classe que permite a criação de modelos de Redes neurais de camada por camada.
  ```python
  import tensorflow as tf
  model = tf.keras.Sequential()
  model.add(tf.keras.layers.Dense(1))
  ```
  > Os principais métodos da classe são:
  * .add() que adiciona uma camada ao modelo
  * .compile() que compila o modelo
  * .build() responsável por construir o modelo
  * .summary() retorna uma tabela com a distribuição
  
  > Principais atributos
  * .layers retorna a lista

2. https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html

  > se resume a uma classe que retorna uma estrutura de dados.
  ```python
  import pandas as pd
  dataset = pd.read_csv("dados.csv")
  print(dataset.head())
  ```
  
  > principais métodos:
  * .head() - retorna as 5 primeiras fileiras
  * .tail() - retorna as 5 últimas fileiras
  
  > principais atributos:
  * .columns - retorna os nomes das colunas
  * .rows - retorna os indices das linhas

3. https://keras.io/api/models/model/

  > *blueprint* para criação de modelos do keras
  ```python
  import tensorflow as tf
  inputs = tf.keras.Input(shape=(3,))
  x = tf.keras.layers.Dense(4, activation=tf.nn.relu)(inputs)
  outputs = tf.keras.layers.Dense(5, activation=tf.nn.softmax)(x)
  model = tf.keras.Model(inputs=inputs, outputs=outputs)
  ```
  
  > principais métodos:
  * .summary() retorna o sumário das redes
  * .get_layer() retorna a rede
