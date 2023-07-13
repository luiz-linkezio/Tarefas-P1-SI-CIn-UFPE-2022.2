# Aniversariantes do Mês

**Limite de tempo do código: 200ms**

Seu Anselmo é um amante de pets e dono do petshop mais famoso do bairro. Ele acredita que nada é mais importante do que celebrar a vida dos nossos amigos de quatro patas e decidiu começar a dar festas de aniversário conjuntas para seus clientes. Com direito a petiscos especiais para cada espécie, é claro!

![Mickey e Pluto](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjRmOTYzY2Y3ZDMzYzMzMDFkN2NlMjU1NDg4NDJlMDJiYTViZTI2YiZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/2fWbBASfuz63Ser5oC/giphy.gif)

Como ele sabe que você tem grandes habilidades de programação, ele decidiu te contratar para ajudá-lo a organizar os aniversariantes do mês. Seu trabalho é criar um programa que registre as informações de cada animal e, dado um determinado mês, retorne os nomes e espécies dos bichinhos que fazem aniversário naquele mês para que ele possa organizar a festa.

**É obrigatório o uso de dicionários na resolução da questão.**

## Input:

O programa deverá receber um inteiro inicial que representa a quantidadede bichinhos a serem cadastrados.

```
N
```

Seguido de N linhas no formato:

```
nome_animal especie data_nascimento
```

E, por ultimo, mais um inteiro, representando o mês a ser consultado:

```
M
```

- data_nascimento é uma string no formato "DD/MM/AAAA".
- (1 ≤ M ≤ 12)

## Output:

Se houver bichinhos que fazem aniversário no mês consultado, imprima:

```
E os donos da festa do mes sao:
```

Seguido de x linhas, cada uma com o formato:

```
{nome_animal} - {especie}
```

- Os bichinhos devem ser listados em ordem alfabética pelo nome.

Caso não haja bichinhos que fazem aniversário no mês consultado, imprima:

```
Sem festa esse mes. :(
```

## Exemplos:

### Caso 1:

Input:
```
4
Luna Cachorro 14/03/2016
Simba Gato 25/08/2017
Pingo Coelho 12/02/2019
Arya Cachorro 04/03/2015
3
```

Output:
```
E os donos da festa do mes sao:
Arya - Cachorro
Luna - Cachorro
```

### Caso 2:

Input:
```
2
Bella Hamster 10/06/2020
Fred Cachorro 20/08/2018
7
```

Output:
```
Sem festa esse mes. :(
```