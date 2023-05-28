# Mostra tua força Brasil! 

**Limite de tempo do código: 2000ms**

Depois de conseguir avançar na fase de grupos, a seleção de Tite chega como uma forte candidata a vencer o torneio, mas Tite não quis esperar o final da copa para saber se o brasil ia ser campeão ou não, então ele decidiu pedir para você fazer uma simulação com o mata-mata da seleção brasileira para ver o que ia acontecer.

Ele pediu para fazer de um jeito que o fator Favoritismo, sendo ele um numero inteiro, fosse ser algo muito presente na sua simulação.

Você vai receber os resultados que o brasil vai ter das fases do mata-mata, das oitavas até a semifinal (considerando que o Brasil vai chegar até lá). Nos resultados, o Brasil pode tanto avançar quanto ser eliminado em qualquer fase.

- Caso o brasil perca antes de chegar a final, ele será eliminado, e você não receberá as entradas das fases seguintes consequentemente.
- Caso ocorra um empate, aí é que o favoritismo começa a entrar em cena, porque ele é o fator de desempate nesse caso, ou seja, em caso de empate, passa a seleção com o maior favoritismo (caso elas empatem no favoritismo também, passa o Brasil porque Tite é clubista!).
- Caso o Brasil vença a partida (sem contar a final) o seu favoritismo aumenta dependendo do placar do jogo. Se o brasil vencer por 1 gol de diferença, seu favoritismo aumenta em 10 pontos, se vencer por 2 gols de diferença, aumenta em 20 pontos o favoritismo, e caso vença por 3 ou mais gols, aumenta em 30 pontos o favoritismo brasileiro.

A final já vai ser diferente, nela você não vai receber um resultado caso o brasil chegue nela, você só saberá o oponente do Brasil e o Favoritismo que ele chega, e só com o favoritismo, definir quem vai ser o campeão (caso haja empate no favoritismo, ganha quem tem mais copas do mundo ;) **Ps.** é o Brasil sempre).

**OBS:** Das oitavas até a final são 4 partidas, mas lembre-se que a última (final), possui uma entrada diferente, e que não necessariamente o Brasil jogará as 4 partidas.

**OBS:** As funções **exit()** e **quit()** não podem ser utilizadas nessa questão.

## Input:

Você primeiramente receberá um input, sendo ele um valor inteiro, que irá representar o favoritismo inicial da seleção brasileira.

```
FavoritismoBr
```

Depois, você receberá em uma sequência padronizada, o oponente que o brasil irá enfrentar, o seu favoritismo, e o resultado da partida entre os dois, sendo o primeiro número os gols do Brasil, e o 2º o do adversário, mantendo o padrão abaixo até a final:

```
NomeOponente1
FavoritismoOponente1
GolsBR1
GolsOPO1
NomeOponente2
FavoritismoOponente2
GolsBR2
GolsOPO2
.
.
.
```

Até chegar na final, onde você irá receber somente o nome e o favoritismo do oponente, como foi previamente dito.

```
NomeOponente
FavoritismoOponente
```

## Output:

Caso o Brasil seja eliminado em qualquer fase que não seja a final, por conta de uma derrota no resultado, imprima:

```
Infelizmente essa seleção dx {nome_adversario} era muito forte para o Brasil.
```

Caso o Brasil seja eliminado em qualquer fase que não seja a final, por conta de um empate no resultado, mas perdendo por causa do favoritismo, imprima:

```
Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...
```

Caso o Brasil avance de fase por conta de um empate no resultado, mas ganhando por causa do favoritismo, imprima:

```
No sufoco, o Brasil conseguiu ganhar!!!
```

Caso o Brasil avance de fase, por conta de uma vitória no resultado, imprima:

```
Quem é que segura o Brasil???
```

Caso o Brasil perca a final, imprima:

```
O nosso Brasil foi vice, não conseguindo bater a seleção dx {nome_adversario} na simulação
```

Caso o Brasil seja campeão, imprima:

```
O BRASIL VAI SER HEXAAAAAAAA
```

## Exemplos:

### Caso 1:

Input:
```
100
Coréia do Sul
25
4
1
Croácia
40
3
0
Argentina
110
2
2
França
115
```

Output:
```
Quem é que segura o Brasil???
Quem é que segura o Brasil???
No sufoco, o Brasil conseguiu ganhar!!!
O BRASIL VAI SER HEXAAAAAAAA
```

### Caso 2:

Input:
```
70
México
35
2
0
Bélgica
70
1
2
```

Output:
```
Quem é que segura o Brasil???
Infelizmente essa seleção dx Bélgica era muito forte para o Brasil.
```
