# O lugar ideal

**Limite de tempo do código: 2000ms**

Finalmente, férias! Depois de tanto estudo, você e seus amigos decidem que merecem descansar e relaxar. Ou talvez viajar. Quem sabe vocês devessem ir ao museu? Ou seria melhor pegar um cinema?

![Homer comendo pipoca](https://media.tenor.com/VYc0eKXOtioAAAAC/the-simpsons-homer-simpson.gif)

Foi tanta indecisão que após uma semana de férias, vocês ainda não fizeram nada!

Decididos a escolher um lugar de uma vez por todas, vocês resolvem colocar seu conhecimento de programação em prática para escrever um código que lhe dirá onde aproveitar esse tempinho livre.

Ficou estabelecido que decisão acontecerá em forma de votação. O melhor lugar será aquele que possuir o maior total de pontos, enquanto o pior lugar, o que possuir o menor total.

## Input:

A primeira entrada é um inteiro N ≥ 2 que representa o total de lugares que serão sugeridos.

```
N
```

Em seguida, o programa receberá uma string contendo o nome do lugar sugerido.

```
nome_lugar
```

A sugestão então receberá um número indefinido de notas, parando quando uma das notas tiver um valor menor que 0 (o valor negativo não deve contar para o total de pontos que uma sugestão recebeu).

```
nota1
nota2
nota3
…
nota < 0
```

Esse processo se repetirá N vezes.

## Output:

- Se não ocorrer empate para o melhor_lugar

```
{melhor_lugar} ganhou de lavada de {pior_lugar}, com {maior_nota} vs {pior_nota}
```

- Se ocorrer empate para melhor_lugar

```
{melhor_lugar1}, {melhor_lugar2}, (…) , {melhor_lugarN}
Tantas opções
```

**OBS:** Não existem casos onde seja preciso imprimir mais que um pior_lugar

**OBS2:** Em caso de empate, os lugares vão ser mostrados separados por vírgula e em ordem de entrada. **Lembrem-se que vocês ainda não podem usar listas, pensem em uma outra maneira de armazenar a informação dos melhores lugares**

## Exemplos:

### Caso 1:

Input:
```
2
Disney
10
10
-2
Cinema
4
3
2
-1
```

Output:
```
Disney ganhou de lavada de Cinema, com 20 vs 9
```

### Caso 2:

Input:
```
3
Praia
8
6
-1
Museu
9
5
-2
Viajar
7
7
-4 
```

Output:
```
Praia, Museu, Viajar
Tantas opções
```

