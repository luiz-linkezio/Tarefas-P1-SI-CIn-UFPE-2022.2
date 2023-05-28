# Disputa de Pênaltis

**Limite de tempo do código: 2000ms**

![Pênalti](https://www.lance.com.br/files/article_main/uploads/2022/12/05/638e2d9d64ef4.jpeg)

Com fim da fase de grupos e o início do mata-mata, vem junto com ele a possível etapa que testa o coração do brasileiro, a disputa de pênaltis. Nela, cada seleção bate pênaltis alternadamente e vence aquela que tiver mais gols que a adversária após ambas chutarem 5 pênaltis OU não ter mais como a outra seleção vencer a disputa, terminando instantaneamente a partida.

**Exemplo:** Na partida entre Croácia e Japão, a disputa terminou em 3 a 1 para Croácia, pois o Japão iria para o quinto e último chute e já não tinha mais chance virar o placar.

Sua missão será fazer a contagem de gols de uma disputa de pênaltis da copa e definir qual das seleções passa para próxima fase.

**OBS:** Caso as duas seleções façam seus 5 chutes e o resultado termine empatado, a disputa não continua nessa questão e considera-se apenas que ocorreu um empate.

## Input:

A entrada será formada primeiro pelo nome das duas seleções que estão disputando os pênaltis.

```
Nome1
Nome2
```

Depois, virão 10 entradas, no máximo, já que podem vir menos se a disputa acabar antes, mas nunca mais que 10 entradas. As possibilidades de entradas são: “Gol”, “Errou”, “Na trave” e “Defendeu”, sendo que apenas a entrada “Gol” conta como gol para a seleção que bateu o pênalti. Além disso, as entradas de número ímpar são batidas pela seleção Nome1 e as entradas de número par batidas pela seleção Nome2.

```
Entrada1
Entrada2
Entrada3
Entrada4
…
```

## Output:

Haverá apenas 2 possibilidades de saída. Caso uma das seleções vença a disputa, você imprimirá na tela:

```
{vencedor} vence a disputa de pênaltis por {gols_vencedor} a {gols_perdedor} e avança de fase!
```
Porém, caso haja um empate, a saída abaixo deverá ser mostrada:

```
Ambas as seleções terminaram com {numero_de_gols} gols, mas o desempate vai ficar para outro dia.
```

## Exemplos:

### Caso 1:

Input:
```
Brasil
Argentina
Gol
Gol
Gol
Gol
Gol
Na trave
Errou
Gol
Gol
Defendeu
```

Output:
```
Brasil vence a disputa de pênaltis por 4 a 3 e avança de fase!
```

### Caso 2:

Input:
```
Argentina
Holanda
Errou
Gol
Defendeu
Gol
Gol
Gol
Errou
```

Output:
```
Holanda vence a disputa de pênaltis por 3 a 1 e avança de fase!
```

### Caso 3:

Input:
```
Brasil
Croácia
Gol
Errou
Gol
Gol
Na trave
Gol
Gol
Gol
Gol
Gol
```

Output:
```
Ambas as seleções terminaram com 4 gols, mas o desempate vai ficar para outro dia.
```