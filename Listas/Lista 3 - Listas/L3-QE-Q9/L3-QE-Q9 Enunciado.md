# Mensagens Criptografadas

- **(Este enunciado foi modificado para a melhor compreensão do leitor)**

**Limite de tempo do código: 3000ms**

O mundo de Gravity Falls está quase sendo destruído! Bill Cipher se cansou e decidiu acabar com tudo de uma vez por todas. Felizmente nós conseguimos rastrear suas ações e então roubar informações sobre seus planos futuros. Seu papel é nos ajudar agora a decodificar as mensagens obtidas e então ajudar a proteger o mundo!!!

Para tal, lembre-se de usar tudo que aprendeu até o momento!! É importante lutar e defender com todas as armas em mãos. (Livre uso de condicionais, loops e o que foi aprendido sobre lista 🙂)

**OBS:** É permitido APENAS o uso da função **append()** e **split()** na resolução da questão. Qualquer outra função de lista ou uso de assuntos não vistos resultará na ANULAÇÃO DA QUESTÃO.

![Bill Cipher Bravo](https://media.tenor.com/9NsGITXkts4AAAAM/bill-cipher-gravity-falls.gif)

## Input:

Primeiro de tudo você irá receber o nome do nosso inimigo!!

```
nomeInimigo
```

Depois, você receberá o nome do seu aliado que estará ali para lhe ajudar.

```
nomeAliado
```

Após o input dos nomes você receberá um relatório sobre o dia atual, de como está a situação climática...

```
climaAtual
```

Depois disso receberá 9 números em uma única linha correspondente a mensagem criptografada obtida do seu inimigo!! A quantidade de mensagens é indefinida e só parará com uma condição de parada.

```
mensagem1
mensagem2
mensagem3
…
mensagem_final
```

Exemplo 1: 1 2 3 4 5 6 7 8 9
Exemplo 2: 10 123 1345 0543 234 102 -1

Seu input só irá parar caso receba: **Cansado** finalizando o número de mensagens e terminando a contagem.

**DICA:** Organizar as mensagens em uma lista pode ajudar

## Output:

A primeira ação a ser feita é analisar o clima para a decodificação.

- Caso o clima NÃO seja **Ensolarado** ou **Nublado** ou **ChuvosoNormal** ou **ChuvosoComRaio**, printe:

```
Infelizmente esse clima não está bom. Não conseguimos decifrar a mensagem, o que será do mundo agora??
Tenho certeza que conseguiremos na próxima {nomeAliado}
```

Após as mensagens o programa deve ser ENCERRADO!!

- Caso o clima seja **Ensolarado**:

A ação a ser feita é realizar uma ORDENAÇÃO dos números de cada mensagem acima obtida. A ordenação deve ser feita do MENOR valor para o MAIOR.

Ao fim dessa etapa, você deve printar:

```
Caramba! Finalmente organizamos a mensagem secreta do {nomeInimigo} com esse clima Ensolarado! Vamos nessa {nomeAliado}!
```

- Caso o clima seja **Nublado**:

A ação a ser feita é realizar uma ORDENAÇÃO dos números de cada mensagem acima obtida. A ordenação deve ser feita do MAIOR valor para o MENOR.

Ao fim dessa etapa, você deve printar:

```
Ufa! Mesmo com o clima Nublado ainda desvendamos a mensagem do {nomeInimigo}! Vamos nessa {nomeAliado}!
```

**DICA:** Buscar qualquer tipo de ordenação para usar (procurem vídeos no Youtube). Algum exemplo de ordenações básicas: Bubble Sort e Selection Sort. Link rápido para explicação sobre Selection Sort: https://www.youtube.com/watch?v=g-PGLbMth_g

- Caso o clima seja ChuvosoNormal:

A ação a ser realizada é comparar os valores de cada posição de uma mensagem com os da mesma posição da mensagem seguinte. Caso o valor da posição X da primeira mensagem seja MENOR que o valor da posição X da segunda mensagem, deverá haver uma troca entre eles.

Exemplo: Valores da mensagem1 com Valores da mensagem2, Valores da mensagem2 com Valores da mensagem3, Valores da mensagem3 com Valores da mensagem4...

**OBS:** A última mensagem NÃO sofre troca com uma mensagem posterior por não haver continuação.

Ao fim dessa etapa, você deve printar:

```
Nem mesmo a chuva vai nos parar de salvar o mundo! Desvendamos a mensagem do {nomeInimigo}! Vamos nessa {nomeAliado}!
```

- Caso o clima seja **ChuvosoComRaio**:

A ação a ser feita é quase a mesma lógica do ChuvosoNormal mas agora a troca só ocorre caso o valor da posição X da primeira mensagem seja MAIOR que o valor da posição X da segunda mensagem.

**OBS:** A última mensagem NÃO sofre troca com uma mensagem posterior por não haver continuação.

Ao fim dessa etapa, você deve printar:

```
Eitaa! Até mesmo essa chuva com trovoadas não nos parou. Estamos indo até você, {nomeInimigo}! Vamos nessa {nomeAliado}!
```

Agora com todas as mensagens prontas para leitura podemos finalmente confirmar seu plano! Descobrimos que a quantidade de mensagens representa uma quantidade de ataques a ser feito. Portanto, a próxima ação é printar:

```
Agora decodificamos as {quantidade} mensagens do {nomeInimigo} e sabemos seus {quantidade} lugares de ataque.
Os lugares sao:
```

Após os prints acima, você deve mostrar o local do ataque que cada mensagem passou. Para isso, para CADA MENSAGEM você deve printar:

```
{posição} lugar:
```

Em que posição corresponde à numeração de cada lugar. A primeira mensagem é o primeiro lugar, a segunda mensagem é o segundo lugar, a terceira mensagem é o terceiro lugar, etc. e deve estar em número decimal , inciando do 1.

Exemplo: 1 lugar, 2 lugar...

Agora sabendo de qual lugar estamos falando devemos mostrar suas coordenadas, o horário do ataque e também a data! Para isso, basta olharmos nossa mensagem decodificada e pegar seus valores. A coordenada corresponde aos 3 primeiros valores obtidos, o horário corresponde aos próximos 3 valores e, por fim, a data corresponde aos últimos 3 valores.

**OBS:** Esses são os valores obtidos APÓS a ordenação ou a troca (depende do clima)

**OBS:** Cada local de ataque possui suas informações, então são os 9 valores do primeiro lugar, depois do segundo lugar, e assim por diante.

Então nossa próxima ação a ser feita é printar:

```
Coordenadas: {posição0 da msg}° {posição1 da msg}' {posição2 da msg}''
Horario: {posição3 da msg}h {posição4 da msg}m {posição5 da msg}s
Data: {posição6 da msg}/{posição7 da msg}/{posição8 da msg}
```

**OBS:** Para CADA MENSAGEM deve-se mostrar a numeração (qual número é o local) e também suas coordenadas, horários e datas.

**OBS:** Não se importar com coordenadas, horários e datas fora da realidade também.

Agora com tudo pronto nós temos que agir rápido!! Apenas finalize o programa com a seguinte ação, printar:

```
Vamos rapido {nomeAliado}!!
```

Obrigado por salvar o mundo!!!

## Exemplos:

### Caso 1:

Input:
```
Bill Cipher
Mabel Pines
Ensolarado
1 3 4 7 23 25 9 7 6
123 456 88 999 341 123 33 2 99
1 2 5 3 99 23 11 7 6
Cansado
```

Output:
```
Caramba! Finalmente organizamos a mensagem secreta do Bill Cipher com esse clima Ensolarado! Vamos nessa Mabel Pines!
Agora decodificamos as 3 mensagens do Bill Cipher e sabemos seus 3 lugares de ataque.
Os lugares sao:
1 lugar:
Coordenadas: 1° 3' 4''
Horario: 6h 7m 7s
Data: 9/23/25
2 lugar:
Coordenadas: 2° 33' 88''
Horario: 99h 123m 123s
Data: 341/456/999
3 lugar:
Coordenadas: 1° 2' 3''
Horario: 5h 6m 7s
Data: 11/23/99
Vamos rapido Mabel Pines!!
```

### Caso 2:

Input:
```
Bill Cipher
Stanley Pines
Nublado
9 9 9 9 9 9 9 9 9
23 11 234 435 6234 12341 153 44 7
1 2 5 3 99 23 11 7 6
1 2 3 4 5 6 7 8 9
Cansado
```

Output:
```
Ufa! Mesmo com o clima Nublado ainda desvendamos a mensagem do Bill Cipher! Vamos nessa Stanley Pines!
Agora decodificamos as 4 mensagens do Bill Cipher e sabemos seus 4 lugares de ataque.
Os lugares sao:
1 lugar:
Coordenadas: 9° 9' 9''
Horario: 9h 9m 9s
Data: 9/9/9
2 lugar:
Coordenadas: 12341° 6234' 435''
Horario: 234h 153m 44s
Data: 23/11/7
3 lugar:
Coordenadas: 99° 23' 11''
Horario: 7h 6m 5s
Data: 3/2/1
4 lugar:
Coordenadas: 9° 8' 7''
Horario: 6h 5m 4s
Data: 3/2/1
Vamos rapido Stanley Pines!!
```