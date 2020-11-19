# Trabalho Prático

1. Crie um projeto de um programa em Java e divida-o em três pacotes:

    a) Camada que linda com a interface com o usuário (view);
    
    b) Camada de negócio(business) com dois pacotes;
        
    - subcamada que possui regras (gerente de usuário) de negócio (control)

    - subcamad que possui entidades do negócio (model)

    c) camada que lida com a persistência/comunicação externa/etc (infra)

2. Implemente a ADIÇÃO DE USUÁRIOS no sistema e, na camada "business.control", algotirmos para validar os cadastros de usuários. Crie e utilize exceções próprias para representar os erros abaixo:

    **Login:**

        Máximo 20 caracteres
        Não pode ser vazio
        Não pode ter números// strWithNUmber.matches(".*\\d.*")

    **Senha:**

        Máximo 12 caracteres
        Mínimo de 8 caracteres
        Deve possuir letras e números e ao menos 2 números

    Dica: Pesquise o método "matches" da class "String" ou os métodos da classe Character.


3. Armazene os usuários numa coleção (deve ser atributo da classe que gerencia os usuários na camada "control") e implemente a persistência da lista utilizando arquivos binários na camada "infra".

4. Implemente a EXCLUSÃO DE UM USUÁRIO dado seu login.

5. Realize o tratamento de exceções em dois níveis: Capture as exceções java.io.IOException na camada "infra", relance-as para as camadas acima de modo que apresente uma mensagem para o usuário final amigável.

