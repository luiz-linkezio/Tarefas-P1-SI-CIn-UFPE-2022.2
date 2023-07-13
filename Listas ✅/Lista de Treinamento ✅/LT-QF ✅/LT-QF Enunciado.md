# Quantas ticks?

**Limite de tempo do código: 1000ms**

Quase todo jogo é controlado por um grande loop e toda tarefa é executada dentro de um ciclo desse loop. No Minecraft esse ciclo é chamado de tick. Em situações ideais, são executadas 20 ticks por segundo e um dia dentro do jogo tem 24000 ticks (ou 20 minutos).

Um dia dentro do jogo, assim como na vida real, tem um ciclo de dia e noite. O dia se inicia em 0 ticks e acaba as 12000 ticks, dando inicio ao por do sol, seguido pela noite e, posteriormente, o nascer do sol.

Monstros como zumbis, esqueletos e aranhas não são um perigo durante o dia, pois queimam com a luz do sol ou ficam passivos. Consequentemente, é mais seguro andar durante o dia.

Depois de minerar bastante e coletar vários outros tipos de recurso, Tantan decidiu que estava na hora de construir suas vilas com casas muito legais. Porém, por ser muito estudioso, Tantan só pode jogar 3 horas por dia e deseja utilizar todas essas horas para construir. Por curiosidade, ele estava interessado em quantas ticks ele gastava construindo cada casa, sendo que todas seguem o mesmo padrão e levam o mesmo tempo para ser construídas.

Tantan definiu que cada vila deveria ter 10, 100 ou 1000 casas.

Sua tarefa é fazer um programa que ajude Tantan a descobrir quantos ticks ele levou para construir cada casa, considerando que, por ele ter medo de monstros, ele só pode construir durante o dia do tempo do jogo.

## Input:

```
D
C
```

- D - número natural (1 <= D)
- C - número natural ( { 10, 100, 1000} )

As duas linhas de entrada é composta pelo número de dias da vida real que Tantan passou construindo e pela quantidade de casas na vila, respectivamente.

**Obs:** A entrada deve ser considerada amigável, ou seja, sempre estará no formato descrito.

## Output:

```
T
```

- T - número natural

A linha única de saída é composta pela quantidade de ticks gastas construindo cada casa.

## Exemplos:

### Caso 1:

Input:
```
2
100
```

Output:
```
2160
```

### Caso 2:

Input:
```
50
1000
```

Output:
```
5400
```

### Caso 3:

Input:
```
1
10
```

Output:
```
10800
```
