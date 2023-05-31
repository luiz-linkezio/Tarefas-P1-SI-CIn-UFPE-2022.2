# Desventuras na mente do velho McGucket 

**Limite de tempo do código: 200ms**

![Memórias de McGucket](https://i.imgur.com/hiFwrXy_d.webp?maxwidth=760&fidelity=grand)

Algum tempo após a derrota do Bill Cipher e do Ford ter suas memórias apagadas, Ford vai recuperando sua memória aos poucos e, em uma solitária angústia, o velho McGucket teme que o grande vilão reapareça e pensa que a única solução para derrotá-lo de uma vez por todas seria recuperar as memórias do seu incidente com o portal, e, você, que estava passando o verão em Gravity Falls e andou espionando o velho maluco, decide ajudá-lo.

O que acontece de interessante é que o dispositivo de ler mentes mostra apenas uma série de números em vez de uma memória visual. A única coisa que o velho lembra e que não aparece no leitor de mentes são sequências gigantescas de números, pertencentes a sequência de fibonacci.

Juntos vocês descobriram que alguma entidade usava a sequência de fibonacci para se comunicar através das memórias do velho McGucket, a máquina de apagar memória codificou a mensagem para o formato que é visto na máquina. Quando vocês decodificaram, descobriram que a mensagem se dividia em duas partes:

- A primeira informava em qual índice da sequência de Fibonacci se encontra o número que iremos utilizar para decifrar nosso código.

- Na segunda parte, x-y são as posições de dois dígitos no número que foi encontrado na primeira parte. x = posição do primeiro dígito e y = posição do segundo dígito do código.

- Os dois dígitos encontrados são concatenados e formam um código ASCII.

**Utilize a função chr() para descobrir seu significado que fará parte da mensagem final.**

Exemplo:

Suponha que o número dado para o índice da sequência de fibonacci seja 32 e que x-y seja 2-3.
Na sequência de fibonacci, o número 32 da sequência é 2178309.
Os dígitos na posição 2 e 3 do número encontrado são, respectivamente, 7 e 8.
Portanto, devemos buscar na tabela ASCII o dígito de código ASCII 78.
Descobrimos, finalmente, que o dígito encontrado é a letra N.

Descoberto isso, o velho deixou você responsável por fazer o script que receberia as informações da máquina e encontrar qual é a mensagem sendo passada por cada memória.

**Obs.:** tanto a sequência de Fibonacci, quanto a contagem dos índices são iniciados em zero

## Input:

A primeira entrada indica a quantidade de decodificações que precisam ser realizadas

```
n
```

Em seguida, você receberá as n mensagens a serem decodificadas

```
z x-y
...
```

## Output:

A saída consiste na combinação de todas as decodificações:

```
{MENSAGEM DECODIFICADA}
```

## Exemplos:

### Caso 1:

Input:
```
10
23 1-2
42 2-3
20 0-1
31 5-6
30 1-2
35 3-4
56 3-4
94 13-14
42 2-3
56 3-4
```

Output:
```
VOCE JUROU
```

### Caso 2:

Input:
```
9
14 1-2
31 5-6
30 1-2
30 0-1
20 2-3
20 1-2
23 1-2
20 2-3
94 13-14
```

Output:
```
ME SALVAR
```

### Caso 3:

Input:
```
35
23 1-2
42 2-3
20 0-1
31 5-6
30 1-2
14 1-2
31 5-6
30 1-2
31 5-6
28 2-3
30 0-1
44 6-7
28 2-3
42 2-3
56 3-4
30 1-2
20 0-1
42 2-3
14 1-2
56 3-4
28 2-3
44 6-7
20 0-1
20 2-3
20 0-1
20 2-3
42 2-3
30 1-2
20 1-2
31 5-6
14 1-2
69 3-4
94 13-14
20 2-3
24 1-2
```

Output:
```
VOCE ME ENSINOU COMUNICACAO LEMBRA?
```