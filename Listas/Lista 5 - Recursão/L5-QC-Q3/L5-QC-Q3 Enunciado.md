# Viciado em ChatGPT

**Limite de tempo do código: 2000ms**

Um aluno novato do CIn anda usando bastante o ChatGPT, usou tanto que seu teclado quebrou!!! Letras estão se repetindo. Agora o ChatGPT está comprimindo as respostas, mostrando do lado esquerdo a quantidade de vezes que a letra se repete, e nosso aluno não consegue mais copiar como antes, agora ele vai ter que criar um código para entender as mensagens do ChatGPT.

![Compressão e Descompressão](https://imgur.com/IXn7djF)

## Input:

Você pode receber 3 entradas diferentes, sendo elas:

```
Vou pedir ajuda pro meu amigo ChatGPT
Qual era a tradução?
Preciso parar de usar o ChatGPT
```

## Output:

Se a entrada for "Vou pedir ajuda pro meu amigo ChatGPT”, você irá receber várias frases com letras repetidas, parando quando receber a entrada “Não tô entendendo nada”. Para cada frase, você deverá mostrar como ChatGPT comprimiu a mensagem e sua resposta.

```
usuário:{mensagem_comprimida}
ChatGPT:{resposta_comprimida}
```

A resposta do ChatGPT vai depender da soma de todos os números contidos na mensagem comprimida, sendo:

- 0 < soma <= 5, resposta:

```
1t3a1 1f1a1c3i1n1h1o1 1n3e
```

- 6 < soma <= 20, resposta:

```
1c2o2m2p2r3e1 1u3m1 1t2e1c1l1a1d1o1 1n4o1v1o
```

- 21 < soma <= 30, resposta:

```
1s6o1 1n1a1 1v1i1d2a1 1m4a1n1s3a
```

- 31 < soma <= 40, resposta:

```
1v5a1 1e2s1t4u3d3a3r1 1r1a1p3a3z
```

- 40 < soma, resposta:

```
3e1s1t5u1d1a1 1n2a1o1 1p1r3a1 1t2u1 1v4e1r
```

Se a entrada for “Qual era a tradução?”, você deve mostrar a versão descomprimida da última resposta que ChatGPT deu:

```
Descobri! É: {resposta_descomprimida}, tá de brincadeira né?
```

Se não tiver última resposta, mostre:

```
Não tem nada pra traduzir
```

Por fim, se a entrada for "Preciso parar de usar o ChatGPT", o programa é encerrado.

**OBS:** A quantidade de cada letra repetida não vai ultrapassar 9

**OBS:** as funções de comprimir e descomprimir devem ser obrigatoriamente recursivas

## Exemplos:

### Caso 1:

Input:
```
Vou pedir ajuda pro meu amigo ChatGPT
lllisssttta 44
mmeee ajjudda aii
Não tô entendendo nada
Qual era a tradução?
Preciso parar de usar o ChatGPT
```

Output:
```
usuário:3l1i3s3t1a1 24
ChatGPT:1c2o2m2p2r3e1 1u3m1 1t2e1c1l1a1d1o1 1n4o1v1o
usuário:2m3e1 1a2j1u2d1a1 1a2i
ChatGPT:1c2o2m2p2r3e1 1u3m1 1t2e1c1l1a1d1o1 1n4o1v1o
Descobri! É: coommpprreee ummm teeclado noooovo, tá de brincadeira né?
```