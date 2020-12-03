# Tarefa 9

* Identificar o uso do padrão de projeto Command no código abaixo (na tarefa indicar quais classes implementam: Executor, Comando, ComandoConcreto, Receptor e Cliente)

## Executor
O Executor está presente na classe Invoker. Ela chama o execute definido no Command. 

## Comando
O Comando foi implementado pela classe Command. Nela há a declaração de uma interface para a execução da
operação.

## Comando Concreto
O Comando Concreto foi implementado pelas classes DelCmd, UpdCmd, AddCmd e
GetCmd que herdam a classe AbstractCommand. Elas implementam a interface Command, dado que estabelecem um vínculo entre o Receptor Dao6 e uma ação, sendo elas Delete, Update, Add e Get, respectivamente.

## Receptor
O Receptor foi definido pela classe Dao6. Os comandos concretos recebem uma instância de Dao6 
para execução deles e a classe é a responsável por executar as operações associadas à uma solicitação, como exemplo.

## Cliente
O Cliente foi implementado pela classe Client2, pois a classe cria uma instância do Executor, o Invoker, e estabelece o seu Receptor, o Dao6.
