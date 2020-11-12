# Revisão dos termos SOLID

## Single Responsibility Principle

* Uma classe deve ter um, e somente um, motivo para mudar. Ou seja, a classe deve ter apenas uma responsabilidade dentro do software.

Ex do que seria não utilizar o SRP:
```php

class Order
{
    public function calculateTotalSum(){/*...*/}
    public function getItems(){/*...*/}xx
    public function getItemCount(){/*...*/}
    public function addItem($item){/*...*/}
    public function deleteItem($item){/*...*/}

    public function printOrder(){/*...*/}
    public function showOrder(){/*...*/}

    public function load(){/*...*/}
    public function save(){/*...*/}
    public function update(){/*...*/}
    public function delete(){/*...*/}
}
```
No exemplo assima, realizamos 3 tipos de tarefas diferentes

Agora usando o SRP:

```php
class Order
{
    public function calculateTotalSum(){/*...*/}
    public function getItems(){/*...*/}
    public function getItemCount(){/*...*/}
    public function addItem($item){/*...*/}
    public function deleteItem($item){/*...*/}
}

class OrderRepository
{
    public function load($orderID){/*...*/}
    public function save($order){/*...*/}
    public function update($order){/*...*/}
    public function delete($order){/*...*/}
}

class OrderViewer
{
    public function printOrder($order){/*...*/}
    public function showOrder($order){/*...*/}
}
```

Problemas decorrentes de não usar o Single Responsibility Principle:
* Falta de coesão
* Alto acoplamento
* Dificuldades na implementação de testes automatizados
* Dificuldade para reaproveitar o código

Outro exemplo:

```php
//Ruim:
function emailClients(array $clients): void
{
    foreach ($clients as $client) {
        $clientRecord = $db->find($client);
        if ($clientRecord->isActive()) {
            email($client);
        }
    }
}



// Bom:
function emailClients(array $clients): void
{
    $activeClients = activeClients($clients);
    array_walk($activeClients, 'email');
}

function activeClients(array $clients): array
{
    return array_filter($clients, 'isClientActive');
}

function isClientActive(int $client): bool
{
    $clientRecord = $db->find($client);

    return $clientRecord->isActive();
}
```

## Open-Closed Principle

* Objetos ou entidades devem estar abertos para extensão, mas fechados para modificação. Quando novos comportamentos e recursos precisam ser adicionados no software, devemos estender o código e não alterar o original.

Ex do que não fazer:
```php
class ContratoClt
{
    public function salario()
    {
        //...
    }
}

class Estagio
{
    public function bolsaAuxilio()
    {
        //...
    }
}

class FolhaDePagamento
{
    protected $saldo;
    
    public function calcular($funcionario)
    {
        if ( $funcionario instanceof ContratoClt ) {
            $this->saldo = $funcionario->salario();
        } else if ( $funcionario instanceof Estagio) {
            $this->saldo = $funcionario->bolsaAuxilio();
        }
    }
}
```
Aqui teríamos que alterar o original modificando a classe folha de pagamento, podendo possivelmente criar um if grande e desnecessário.

Problemas de não utilizar o **Open-Closed principle**:
* Alterar uma classe já existente para adicionar um novo comportamento, corremos um sério risco de introduzir bugs em algo que já estava funcionando.

OCP preza que uma classe deve estar fechada para alteração e aberta para extensão.

Uma correção para o exemplo anterior seria :

```php
interface Remuneravel
{
    public function remuneracao();
}

class ContratoClt implements Remuneravel
{
    public function remuneracao()
    {
        //...
    }
}

class Estagio implements Remuneravel
{
    public function remuneracao()
    {
        //...
    }
}

class FolhaDePagamento
{
    protected $saldo;
    
    public function calcular(Remuneravel $funcionario)
    {
        $this->saldo = $funcionario->remuneracao();
    }
}
```

## Liskov Substitution Principle
Uma classe derivada deve ser substituível por sua classe base.

se S é um subtipo de T, então os objetos do tipo T, em um programa, podem ser substituídos pelos objetos de tipo S sem que seja necessário alterar as propriedades deste programa.

```php
class A 
{
    public function getNome()
    {
        echo 'Meu nome é A';
    }
}

class B extends A 
{ 
    public function getNome()
    {
        echo 'Meu nome é B';
    }
}

$objeto1 = new A;
$objeto2 = new B;

function imprimeNome(A $objeto)
{
    return $objeto->getNome();
}

imprimeNome($objeto1); // Meu nome é A
imprimeNome($objeto2); // Meu nome é B
```

Violação do Liskov Substitution Principle
* Sobrescrever/implementar um método que não faz nada
* Lançar uma exceção inesperada
* Retornar valores de tipos diferentes da classe base

## Interface Segregation Principle

Uma classe não deve ser forçada a implementar interfaces e métodos que não irão utilizar.
Esse princípio basicamente diz que é melhor criar interfaces mais específicas ao invés de termos uma única interface genérica.

Ex: Ave penguim voar

## Dependency Inversion Principle

## Referências

https://medium.com/desenvolvendo-com-paixao/o-que-%C3%A9-solid-o-guia-completo-para-voc%C3%AA-entender-os-5-princ%C3%ADpios-da-poo-2b937b3fc530

## Lista 3

### Jogo da velha [Tabuleiro.java]

Problemas:
1. Violação do Single Responsibility Principle.
    * A classe Tabuleiro é responsável por diversas coisas. Poderíamos separar em classes diferentes. Uma responsável pela construção do tabuleiro, uma para checar quem ganhou e outra para mostrar os resultados. Além disso, poderíamos enxugar o pouco o código com coisas que não são importantes.
2. Violação do Open Closed Principle.
    * Neste caso, precisaríamos fazer modificações no código atual ao invés de extensões no caso da checagem do vencedor, o que vai contra o OCP. Como estão faltando algumas checagens para determinar o vencedor, teríamos que adicionar ao if mais condições.
 
### Saudação [Saudacao.java]

Problemas:
1. Violação Open Closed Principle.
    * Neste caso, se quiséssemos adicionar alguma variável teríamos que modificar a função saudar. Uma possível solução seria criar uma interface para formalidade e classes criadas para cada formalidade a partir dessa interface, que seriam passadas como parâmetro pela função saudar, que executaria uma função saudar. Assim, só precisaríamos extender o código caso quiséssemos adicionar alguma saudação/formalidade e não mais modificar o já existente.

### Apartamento

Problemas:
1. Violação Open Closed Principle.
    * Os valores de número de quartos na cobertura estão setados no código. Além disso, o upgrade do apartamento está fixado em 40 e o numero de quartos em 1. Esses valores deveriam ser passados como parâmetro. Do contrário, precisaríamos mudar o código caso quiséssemos colocar valores diferentes.
2. Violação Dependency Inversion Principle
    * Um modelo de alto nível não deve depender de um de baixo nível. Ambos devem depender da abstração. Isso é violado na classe UpgradeApartemento, que precisa da existência da Studio.class

### Ave

Problemas:
1. Violação Liskov Substitution Problem
    * Lança uma exceção inesperada na função voa()
2. Violação Interface Segregation Problem
    * Há a implementação de uma função que não faz nada na classe pinguim (a função voa). O **ISP** diz que uma classe não deve ser forçada a implementar interfaces e métodos que não irão utilizar. Uma possível solução seria criar uma interface que extende aves, mas se chama avesQueVoam. Assim, deixaríamos a interface Ave apenas com o método trocaplumagem() e a interface avesQueVoam teria o método voa().
    
### 
