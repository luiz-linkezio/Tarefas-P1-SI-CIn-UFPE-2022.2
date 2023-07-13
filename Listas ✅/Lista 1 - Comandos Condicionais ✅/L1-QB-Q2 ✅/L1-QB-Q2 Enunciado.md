# Zebrinha tá soltinha 🦓

**Limite de tempo do código: 2000ms**

![Zebra](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTs42Mok6Shb2coKOHSzO2TMcLixm2NBJvTMg&usqp=CAU)

Pedro Baptista, seu monitor de IP, está afundado em dívidas e decidiu pedir um empréstimo ao banco para apostar todo o seu dinheiro nas maiores zebras dos jogos da Copa do Mundo do Catar para ganhar a maior quantidade de dinheiro possível, mas ele não sabe como contabilizar o dinheiro que ganhou ou perdeu nas apostas.

Seu trabalho é informar o resultado do jogo que Pedro apostou e os ganhos que ele teve, além de impedir que ele aposte em resultados que não são zebra.

## Input:

Você receberá o nome das seleções que vão disputar a partida, a primeira seleção será sempre a que Pedro vai apostar:

```
seleção1 (String)
seleção2 (String)
```
**OBS.:** no caso de nome de países que tenha espaços, será colocado um traço para conectar as palavras, e não sera considerado acentos, por exemplo: “Coreia-do-Sul”, “Arabia-Saudita”

Você receberá o valor apostado no jogo:

```
aposta (Integer)
```
Você receberá a probabilidade “X” de vitória do país que Pedro vai apostar, tal que **0 < X < 1**:

```
probabilidade (Float)
```

Você também receberá se você acertou na aposta (Ganhou ou Perdeu):

```
resultado (String)
```

Ao todo, são 5 variáveis para serem armazenadas.

## Output:

Para Pedro apostar, a aposta precisa ser uma zebra, então caso a probabilidade do time que ele apostou ganhar seja maior ou igual a 0.5, acabe o código e imprima na tela:

```
Pedro, você está proibido de apostar nos favoritos, só em zebra, lembra?
```

Caso a probabilidade seja menor que 0.5, você deverá usar a seguinte fórmula para calcular o valor que receberá da aposta, sendo “p” a probabilidade do jogo em decimal:

![Fórmula](https://latex.codecogs.com/png.image?\LARGE&space;\dpi{110}\bg{white}valor&space;=&space;aposta*(1&space;+&space;(0.5-prob)^2*100))

**OBS.:** o valor deve ficar como um número inteiro, lembre-se de converter para int.

Caso acerte o palpite, você deverá imprimir: Caso a probabilidade seja menor que 0.5 e maior que 0.4:

```
Não foi um palpite tão arriscado, todos sabiam que {selecao1} não estava muito atrás de {selecao2}
Parabéns, você apostou R${aposta} e recebeu R${valor} nessa aposta
```

Caso a probabilidade seja menor ou igual a 0.4 e maior que 0.3:

```
Eu pensava que {selecao2} iria ganhar, mas nunca duvidei que a {selecao1} pudesse ganhar essa partida
Parabéns, você apostou R${aposta} e recebeu R${valor} nessa aposta
```

Caso a probabilidade seja menor ou igual que 0.3 e maior que 0.2:

```
Uau! que jogo foi esse?? {selecao1} surpreendeu a todos nós…
Parabéns, você apostou R${aposta} e recebeu R${valor} nessa aposta
```

Caso a probabilidade seja menor ou igual que 0.2 e maior que 0.1:

```
Essa é a copa das zebras?? O impossível aconteceu hoje nessa partida, como que {selecao1} ganhou de {selecao2}, alguém me explica?
Parabéns, você apostou R${aposta} e recebeu R${valor} nessa aposta
```

Caso a probabilidade seja menor ou igual que 0.1:

```
PEDROOOOO, você tá rico!! ninguém, absolutamente ninguém apostou na {selecao1}, somente você!
Parabéns, você apostou R${aposta} e recebeu R${valor} nessa aposta
```

Caso você erre o palpite:

```
Pedro, infelizmente você está no fundo do poço, se endividou completamente e não temos o que fazer…
Você poderia ter ganhado R${valor}, mas perdeu R${aposta}
```

## Exemplos:

### Caso 1:
Input:
```
Arabia-Saudita
Argentina
3500
0.06
Ganhou
```
Output:
```
PEDROOOOO, você tá rico!! ninguém, absolutamente ninguém apostou na Arabia-Saudita, somente você!
Parabéns, você apostou R$3500 e recebeu R$71260 nessa aposta
```
