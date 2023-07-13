# 

**Limite de tempo do código: 2000ms**

Para atrair novos clientes, a empresa de turismo CinTur decidiu promover uma ação e precisa da sua ajuda para concretizá-la.

Veja o anúncio da empresa: “Venha garantir seu pacote de viagem gratuito neste fim de ano! Basta visitar uma de nossas agências, sortear um número binário e converter mentalmente o número para decimal. Acertando a conversão de um de nossos bilhetes premiados, prepare as malas e venha conosco!”

![Avião](https://media.tenor.com/yZ7QWZvJ6-4AAAAi/party-travelling.gif)

O gerente da CinTur convocou você para desenvolver um programa que, ao receber o número sorteado e o palpite inicial do cliente, converta o número binário para decimal através de laços de repetição e verifique se o cliente acertou. O cliente possui até 03 chances para acertar, mas atenção: O cliente só irá falar um próximo palpite se realmente tiver errado o anterior.

Caso o palpite esteja correto, o programa deverá verificar qual será o destino premiado de acordo com a tabela abaixo, que foi divulgada pela a empresa:

![CIN Tour](https://i.postimg.cc/Rhbv7Bqr/Cin-Tour-2.png)

**Atenção:** A empresa também colocou no sorteio números inválidos, ou seja, que não correspondem a nenhum destino.

**OBS.1:** Sendo a entrada um valor em binário, trabalhe no formato de string.

**OBS.2 :** Todas as entradas serão amigáveis (Não precisa se preocupar com números negativos).

## Input:

Inicialmente, você receberá o número sorteado (em binário):

```
n_binario
```

Em seguida, será fornecido o primeiro palpite do cliente (em decimal):

```
palpite_01
```

Se, e somente se, o cliente errar, mais um palpite será recebido (também em decimal):

```
palpite_02
```

Se, e somente se, o cliente errar novamente, mais um palpite será recebido (também em decimal):

```
palpite_03
```

## Output:

Caso o cliente tenha **acertado**, imprima:

```
Parabéns!! Você acertou!
```

Em seguida, observe se era ou não um bilhete premiado e imprima:

- Caso o destino seja Porto de Galinhas:

```
Férias inesquecíveis estão te esperando!
Seu destino será Porto de Galinhas (BRA).
Prepare-se para viver dias incríveis desfrutando das riquezas naturais da nossa região!
```

- Caso o destino seja Fernando de Noronha:

```
Férias inesquecíveis estão te esperando!
Seu destino será Fernando de Noronha (BRA).
Belíssimas praias estão por vir.
Não esqueça o protetor solar.
```

- Caso o destino seja Gramado:

```
Férias inesquecíveis estão te esperando!
Seu destino será Gramado (BRA).
Aproveite passeios e paisagens espetaculares no sul do país!
```

- Caso o destino seja Berlim:

```
Férias inesquecíveis estão te esperando!
Seu destino será Berlim (ALE).
Desfrute de muita cultura e de experiências incríveis!
Prepare os casacos de frio!
```

- Caso o destino seja Tóquio:

```
Férias inesquecíveis estão te esperando!
Seu destino será Tóquio (JPN).
Viva uma experiência inesquecível explorando um país do outro lado do mundo.
Prepare-se para muitas horas de voo!
```

- Caso o número não corresponda a nenhum destino:

```
Mas, infelizmente, hoje não é o seu dia de sorte.
Apesar de ter dado a resposta correta, seu bilhete não oferece nenhum prêmio.
Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!
```

Porém, caso o cliente tenha informado a resposta incorreta, imprima:

- Se ele ainda possui chance(s) para adivinhar:

```
Resposta incorreta. Mas não desista! Você ainda tem { n_chances } chance(s).
```

e repita o processo.

- Ou se errou em todas as suas tentativas:

- - Caso o bilhete correspondesse a um destino:

```
Infelizmente mais uma resposta incorreta.
Agradecemos sua participação!
Seu bilhete era premiado. Que pena!
```

- - Ou caso o bilhete não correspondesse a um destino:

```
Infelizmente mais uma resposta incorreta.
Agradecemos sua participação!
Pelo menos seu bilhete não era premiado.
Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!
```

## Exemplos:

### Caso 1:

Input:
```
0001
1
```

Output:
```
Parabéns!! Você acertou!
Férias inesquecíveis estão te esperando!
Seu destino será Porto de Galinhas (BRA).
Prepare-se para viver dias incríveis desfrutando das riquezas naturais da nossa região!
```

### Caso 2:

Input:
```
11011
27
```

Output:
```
Parabéns!! Você acertou!
Mas, infelizmente, hoje não é o seu dia de sorte.
Apesar de ter dado a resposta correta, seu bilhete não oferece nenhum prêmio.
Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!
```

### Caso 3:

Input:
```
0001
3
5
1
```

Output:
```
Resposta incorreta. Mas não desista! Você ainda tem 2 chance(s).
Resposta incorreta. Mas não desista! Você ainda tem 1 chance(s).
Parabéns!! Você acertou!
Férias inesquecíveis estão te esperando!
Seu destino será Porto de Galinhas (BRA).
Prepare-se para viver dias incríveis desfrutando das riquezas naturais da nossa região!
```