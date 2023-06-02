# As motosserras de Denji

**Limite de tempo do código: 200ms**

O personagem principal do anime Chainsaw Man, Denji, é um jovem que faz parte de um grupo especial de caçadores de entidades do mal. Denji possui a habilidade única de se transformar em uma motosserra, e usa essa habilidade para lutar contra as forças do mal que ameaçam a humanidade.

![Denji](https://criticalhits.com.br/wp-content/uploads/2022/10/denji-chainsaw-man-3-1200x720-1-768x461.jpg)

Ajude Denji em sua missão para derrotar as 3 entidades **Makima**, **Reze**, **Santa Claus** (Denji irá enfrentar essas entidades nessa mesma ordem). Você decidiu criar um programa em Python que simula a transformação dele em uma motosserra, calcula sua força e verifica se ele irá ganhar a batalha.

- Energia → É um número inteiro que representa a quantidade de energia que Denji possui

- Controle → É um número inteiro entre 0 e 10 que representa o nível de controle que Denji tem sobre sua transformação em uma motosserra. Quanto maior o valor, mais controle ele tem sobre a transformação.

- Precisão → É um número inteiro entre 0 e 10 que representa a precisão de Denji ao usar sua motosserra. Quanto maior o valor, mais preciso ele é ao atacar.

Para avaliar a classificação da motosserra de Denji, utilize a seguinte tabela:

- Motosserra Suprema:

- - Energia →Maior ou igual a 750 unidades
- - Controle →Maior ou igual a 7
- - Precisão →Maior ou igual a 8

- Motosserra Avançada:

- - Energia →Maior ou igual a 500 unidades
- - Controle →Maior ou igual a 6
- - Precisão →Maior ou igual a 6

- Motosserra Normal:
- - Caso ele não esteja enquadrado nas condições de nenhuma das duas motosserras acima

Após calcular que tipo de motosserra Denji irá se transformar, é necessário que você calcule a força que ele terá para combater a entidade do mal. Esse calculo é dado pela seguinte fórmula

**Força Denji = Energia + (Controle * Precisão)**

Você irá receber o input da força da entidade para poder realizar a comparação.

Por fim, depois de calcular todas as batalhas, você deve “printar” o resultado final de todas as batalhas

## Input:

Em cada uma das três batalhas, você irá receber esses 4 inputs de inteiros

```
Energia do Denji
Controle do Denji
Precisão do Denji
Força do inimigo
```

## Output:

No inicio de cada rodada você irá “printar” a seguinte mensagem

```
### Rodada {Numero da rodada} - {vilão} ###
```
Após isso irá calcular em qual motosserra ele irá se transformar e printar a seguinte mensagem:

```
O Denji ira se transformar na {motosserra} para enfrentar o {vilao}
```

Depois, irá escrever a frase que informa se Denji ganhou, perdeu ou empatou aquela batalha:

Caso ele vença a batalha:

```
Denji saiu vitorioso nessa batalha contra o {vilao}
```

Caso ele perca a batalha:

```
Denji não conseguiu força o suficiente para derrotar o {vilao}
```

Caso a batalha der empate:

```
Como pode ser possível?? Denji possui a mesma força que o {vilao}
```

Após o final das 3 rodadas, será impressa a mensagem de resultado final, o log da batalha e uma mensagem final na seguinte ordem:

```
### Resultado Final ###
```

Após essa mensagem final, printar o histórico (Log) de batalhas da seguinte forma: (Em cada linha conterá uma batalha)

```
Rodada {x}: {motosserra} - {resultado da batalha}
```

**OBS: Os resultados das batalhas estão escritos da seguinte forma: Vitoria, Derrota, Empate (Cuidado com os prints)**

Por fim uma mensagem final:

- Caso ele ganhe as 3 batalhas:


Nenhum dos 3 inimigos foram capazes de derrotar o Denji!


- Caso ele perca as 3 batalhas:

```
Hoje não foi um dia bom para o Denji, perdeu todas as batalhas
```

- Caso ele Ganhe 1 batalha, Perca 1 batalha e Empate 1 batalha:

```
Hoje foi um dia equilibrado para o Denji, conseguiu ganhar, perder e empatar
```

- Caso o número de vitórias seja maior que o de derrotas e empates:

```
Denji conseguiu derrotar a maioria de seus inimigos
```

- Caso o número de derrotas seja maior que o de vitórias e empates:

```
Dia péssimo para o Denji, perdeu a maioria de suas batalhas
```

- Caso o número de empates seja maior que o de derrotas e vitorias:

```
Dia duro para o Denji, empatou de mais
```

**OBS 1: Os nomes das entidades estão escritos da seguinte forma: Makima, Reze, Santa Claus (Cuidado com os prints)**

**OBS 2: Caso tenha ficado em dúvida em relação aos outputs, se atentar aos casos teste**

**É obrigatório o uso de funções na resolução**

## Exemplos:

### Caso 1:

Input:
```
745
8
9
817
1356
10
10
1234
947
10
7
839
```

Output:
```
### Rodada 1 - Makima ###
O Denji ira se transformar na Motosserra Avançada para enfrentar o Makima
Como pode ser possível?? Denji possui a mesma força que o Makima
### Rodada 2 - Reze ###
O Denji ira se transformar na Motosserra Suprema para enfrentar o Reze
Denji saiu vitorioso nessa batalha contra o Reze
### Rodada 3 - Santa Claus ###
O Denji ira se transformar na Motosserra Avançada para enfrentar o Santa Claus
Denji saiu vitorioso nessa batalha contra o Santa Claus
### Resultado Final ###
Rodada 1: Motosserra Avançada - Empate
Rodada 2: Motosserra Suprema - Vitoria
Rodada 3: Motosserra Avançada - Vitoria
Denji conseguiu derrotar a maioria de seus inimigos
```

### Caso 2:

Input:
```
357
8
10
437
1000
8
8
957
677
6
9
731
```

Output:
```
### Rodada 1 - Makima ###
O Denji ira se transformar na Motosserra Normal para enfrentar o Makima
Como pode ser possível?? Denji possui a mesma força que o Makima
### Rodada 2 - Reze ###
O Denji ira se transformar na Motosserra Suprema para enfrentar o Reze
Denji saiu vitorioso nessa batalha contra o Reze
### Rodada 3 - Santa Claus ###
O Denji ira se transformar na Motosserra Avançada para enfrentar o Santa Claus
Como pode ser possível?? Denji possui a mesma força que o Santa Claus
### Resultado Final ###
Rodada 1: Motosserra Normal - Empate
Rodada 2: Motosserra Suprema - Vitoria
Rodada 3: Motosserra Avançada - Empate
Dia duro para o Denji, empatou de mais
```