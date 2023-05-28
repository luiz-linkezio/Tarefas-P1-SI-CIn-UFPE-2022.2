# Em busca do craque!

**Limite de tempo do código: 2000ms**

A Copa do Mundo da FIFA Catar 2022 está cada vez mais próxima e o técnico da seleção brasileira de futebol, Adenor Leonardo Bachi, mais conhecido como Tite, vem andando cada vez mais estressado e pressionado, pois ainda precisa recrutar um jogador para ocupar a posição de ponta-direita do time.

![Tite](https://cdn2.storyasset.link/ce41f424-ec63-46aa-9b8f-04a813db2f8c/pensando-tite-ms-msvugmzjfx.gif)

Tite está indeciso entre três atletas e, para fazer a escolha, resolveu fazer a análise do número de bolas colocadas na grande área por cada jogador em suas últimas partidas. Em caso de empate, o novo critério usado será o de aproveitamento, calculando a taxa de finalizações (chutes a gol) convertidas em gols, através da fórmula: **(gols/finalizações) * 100**.

Para elaborar esse complexo algoritmo, Tite resolveu contatar o Centro de Informática da UFPE e VOCÊ foi o programador escolhido para auxiliá-lo nessa tarefa!

**Obs:** não será permitido o uso das funções max(), min() ou qualquer outra semelhante.

## Input:

Você receberá 12 entradas, 4 para cada jogador, contendo os nomes dos jogadores, a quantidade de bolas colocadas na grande área por cada um, bem como o número de chutes a gol e o número de gols marcados, a fim de calcular suas respectivas taxas de aproveitamento.

- Nome do jogador (string)
- Bolas colocadas na grande área (inteiro)
- Finalizações (inteiro)
- Gols (inteiro)

## Output:

Inicialmente, caso os jogadores com maior número de bolas colocadas na grande área estejam empatados, você deverá imprimir:

```
Tite está mais indeciso do que nunca!
```

Em seguida, você deverá imprimir três linhas contendo os nomes de todos os jogadores em ordem do melhor para o pior, de acordo com os critérios discutidos anteriormente.

Após isso, você deverá imprimir:

```
Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…
```

Por fim, caso o número de bolas colocadas na grande área do jogador escolhido for menor ou igual a 10, imprima:

```
{melhor_jogador}?! Sei não hein Galvão…
```

Caso contrário, imprima:

```
{melhor_jogador}! Dessa vez o hexa vem pra casa!!
```

## Exemplos:

### Caso 1:

Input:
```
Rodrygo
10
5
2
Raphinha
13
8
3
Antony
11
6
1
```

Output:
```
Raphinha
Antony
Rodrygo
Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…
Raphinha! Dessa vez o hexa vem pra casa!!
```

### Caso 2:

Input:
```
Sergio
8
4
4
Ricardo Massa
10
5
2
Calegario
10
5
3
```

Output:
```
Tite está mais indeciso do que nunca!
Calegario
Ricardo Massa
Sergio
Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…
Calegario?! Sei não hein Galvão…
```