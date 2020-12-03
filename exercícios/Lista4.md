# Diferenças entre padrões Strategy e State

Os padrões Strategy e State são bem parecidos. A diferença está em apenas alguns detalhes:

1. O padrão State armazena uma referência aos objetos.
2. O padrão State pode se substituir, como por exemplo: alterar o estado do objeto de contexto para outra coisa, enquanto o padrão Strategy não.
3. O padrão Strategy é passado para o objeto como parâmetro, enquanto o padrão State é criado pelo próprio objeto.
4. O padrão Strategy trata apenas de uma única tarefa específica, enquanto o padrão State fornece a implementação para tudo (ou quase tudo) que o objeto faz.
