# 🔊CInexa

**Limite de tempo do código: 200ms**

CInexa é uma famosa assistente virtual que faz parte da vida de diversas pessoas na atualidade. Tal situação pode ser explicada porque a CInexa é construída por meio de uma inteligência artificial baseada em um sistema de processamento de linguagem natural (NLP). Assim, ela consegue interpretar comandos de voz e responder aos usuários, possibilitando que eles ouçam notícias, marquem lembretes, escutem músicas e até mesmo obtenham o resultado de cálculos complexos.

![CInexa](https://codesrevolvewordpress.s3.us-west-2.amazonaws.com/revolveai/2022/05/15110810/natural-language-processing-techniques.png)

Certo dia, um usuário resolveu perguntar à CInexa qual é o 24º termo de uma progressão aritmética em que o primeiro número é 32, o segundo é 38 e o terceiro é 44. Ela, por sua vez, realizou uma recursão e informou que o resultado é 170.

Hoje, o seu trabalho será escrever um código que simule o cálculo feito pela CInexa, recebendo as seguintes entradas e retornando as seguintes saídas:

## Input:

Primeiro, você receberá os três primeiros números INTEIROS da progressão aritmética em uma string:

```
numero1 numero2 numero3
```

Por fim, você receberá um inteiro N, que representa a posição do elemento a ser buscado na progressão aritmética:

```
N
```

## Output:

Após realizar o cálculo, a saída deverá ser a seguinte:

```
Na progressão aritmética cujos três primeiros números são {numero1}, {numero2} e {numero3}, o {N}º elemento é {numero} e a razão da progressão é {razao}.
```

## Exemplos:

### Caso 1:

Input:
```
2 5 8
6
```

Output:
```
Na progressão aritmética cujos três primeiros números são 2, 5 e 8, o 6º elemento é 17 e a razão da progressão é 3.
```