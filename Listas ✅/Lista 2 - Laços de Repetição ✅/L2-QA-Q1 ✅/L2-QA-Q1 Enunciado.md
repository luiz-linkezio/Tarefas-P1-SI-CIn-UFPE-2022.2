# Férias derrotando aliens

**Limite de tempo do código: 200ms**

Chegando as tão esperadas férias, Ben Tenysson se prepara para virar herói e pede a sua ajuda para saber quantos alienígenas ele consegue derrotar por dia.

![Alien](https://media.tenor.com/TmbNLu_okcUAAAAM/grey-matter-ben10.gif)

Para isso, você precisa criar um código que recebe frases, indicando se ele derrotou algum alienígena e, caso ele receba a mensagem que o dia acabou ou que o relógio descarregou, a contagem para.

💡 **OBS:** é obrigatório o uso de algum laço de repetição.

## Input:

Você vai receber um número indeterminado de inputs, que devem ser contabilizados como alienígenas derrotados, até receber o input: ‘O relógio descarregou!', ou ‘Por hoje já deu', que finalizam a contagem.

```
frase_1
frase_2
…
frase_final
```


## Output:

Ao receber algum dos inputs finais, deve-se imprimir as seguintes frases:

Caso a frase seja: 'O relógio descarregou!':

```
Corra Ben! Você já derrotou {contador} aliens
```

Caso a frase seja: 'Por hoje já deu':

```
Muito Ben Ben! hehe você derrotou {contador} aliens hoje
```

## Exemplos:

### Caso 1:

Input:
```
Derrotei um alien com o diamente
O XLR8 levou mais um
Fantasmático botou mais um pra correr
Por hoje já deu
```

Output:
```
Muito Ben Ben! hehe você derrotou 3 aliens hoje
```