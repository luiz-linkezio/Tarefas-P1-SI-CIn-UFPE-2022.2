# As Mensagens de Bill Cipher

**Limite de tempo do código: 300ms**

![Bill Cipher](https://i.imgur.com/kc7Rccf.png)

Bill Cipher está tramando um plano maligno para destruir o universo de Gravity Falls. Para descobrir seu plano, Mabel e Dipper precisam decodificar uma mensagem e pediram a sua ajuda para escrever um script em Python para ajuda-los. A mensagem codificada é composta por símbolos especiais, números e letras.

Para decifrar a mensagem codificada, você receberá uma palavra decodificadora para cada palavra codificada, podendo ser **Portal**, **Experimento**, **Schembulock** e **Realidade**, cada uma representando uma ação diferente a ser realizada.

Caso receba **Portal**, você deve, para cada letra encontrada, descobrir a próxima letra no alfabeto [a-z]. A mensagem pode conter várias letras, você deve encontrar a próxima de cada uma e juntá-las para formar a palavra decodificada.

Se a palavra for **Experimento**, você deve pegar apenas os números pares e somá-los, essa soma é a palavra decodificada.

Já se for **Realidade**, os números ímpares são os que devem ser somados.

E, por último, caso sua palavra decodificadora seja **Schembulock**, você deve pegar todos os números e multiplicá-los, o resultado é a palavra decodificada.

Lembre-se que a mensagem codificada vai misturar símbolos especiais, letras e números. Os símbolos especiais devem ser ignorados [! @ $ % & #]. O que você deve manipular são os caracteres alfanuméricos que são esses [a-z , 0-9].

## Input:

Para decifrar a mensagem codificada você primeiro vai receber um número inteiro que é o total de palavras que você precisará decodificar:

```
n
```

Depois, por **n** vezes, você receberá a palavra decodificadora e a palavra codificada:

```
palavra_decodificadora
p a l a v r a _ c o d i f i c a d a
```

Em cada rodada, após decodificar a palavra codificada por meio das instruções da palavra decodificadora, você deve guardar essa palavra para compor a mensagem final.

💡 **Obs.:** Observe que existem quebras de linhas entre os inputs, e as letras na mensagem codificada são separadas por um espaço vazio

## Output:

O output final caso você consiga decodificar as palavras é uma mensagem com todas as palavras decodificadas separadas por espaço (lembre que cada conjunto de entrada com uma palavra decodificadora e uma palavra codificada gerava uma palavra):

```
Consegui! A mensagem decodificada de Bill Cipher é: {palavra1 palavra2 palavra3 ... palavraN}
```

Se a mensagem final não tiver letras ou números, você deve imprimir:

```
Esse formato de mensagem nem Bill Cipher entenderia!
```

## Exemplos:

### Caso 1:

Input:
```
4

Portal

g % ! % @ ! n $ % i % @ @ ! # d

Portal

c % ! % @ ! d $ % # % @ @ ! # @

Experimento

& % ! 8 @ ! 8 $ 3 & % @ @ ! # 5

Schembulock

@ d ! % k ! # $ % n % w @ 7 # 4
```

Output:
```
Consegui! A mensagem decodificada de Bill Cipher é: hoje de 16 28
```

### Caso 2:

Input:
```
2

Portal

l % z % @ ! a $ % d % @ @ ! # k

Portal

o % ! h @ ! m $ % # d @ @ r # @
```

Output:
```
Consegui! A mensagem decodificada de Bill Cipher é: mabel pines
```