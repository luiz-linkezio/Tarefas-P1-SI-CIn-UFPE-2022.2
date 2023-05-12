# Tamanho da caverna

**Limite de tempo do código: 1000ms**

Uma das formas de obter recursos minerais no Minecraft é cavando cavernas em baixo da terra e coletando todos os recursos encontrados.

Após escolher seu nickname, Tantan precisa juntar muitos recursos e decide ir minerar. Seu amigo Durval é especialista em mineração e, vendo o mapa, consegue escolher um bom tamanho para a caverna de mineração. Para melhores resultados, a base da caverna sempre é quadrada, com uma altura variante.

Sua tarefa é ajudar Tantan a saber qual o máximo de blocos que ele vai precisar quebrar para cavar a caverna, após Durval informar a dimensão da mesma.

## Input:

```
L
A
```

- L - número natural (1 <= L)
- A - número natural (2 <= A)

As duas linhas de entrada é composta pelo tamanho do lado da base da caverna e altura, respectivamente, que foram recomendados por Durval.

**Obs:** A entrada deve ser considerada amigável, ou seja, sempre estará no formato descrito.

## Output:

```
B
```

- B - número natural

A linha única de saída é composta pelo número máximo de blocos que precisam ser removidos por Tantan.

## Exemplos:

```
Input:
2
2

Output:
8
```

```
Input:
10
10

Output:
1000
```

```
Input:
5
10

Output:
250
```