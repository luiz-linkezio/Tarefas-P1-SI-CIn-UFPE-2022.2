# "Ferb, já sei o que vamos fazer hoje!"

**Limite de tempo do código: 1000ms**

Depois de um início de período atípico, os Cinners estão entrando de férias e irão aproveitar a oportunidade para desopilar! Enquanto esperava por esse momento, você utilizou seu tempo livre para assistir um episódio de Phineas e Ferb e os irmãos acabaram te inspirando a aproveitar o recesso pra realizar várias invenções!

![Phineas and Ferb](http://3.bp.blogspot.com/-8Z2wysb2rkY/T-ty2kvHKoI/AAAAAAAAFro/ZlC6EB1KVZ8/s1600/gif_animado_phineas-ferb.gif)

Para colocar a ideia em prática, você decidiu que deveria começar organizando as etapas e os gastos para garantir que seu projeto conseguisse ser executado.

## Input:

Inicialmente, você receberá o nome da invenção:

```
nome_invencao
```

Em seguida, serão fornecidas n vezes as informações acerca de cada etapa:

```
nome_etapa
custo_etapa
tentativas_etapa
```

**OBS.1:** Há casos em que nem todas as entradas sobre a etapa serão necessárias; nessas situações, elas não serão fornecidas. As etapas "concluir" e "desistir" não possuem custo nem tentativas, a entrada "dar um plus" possui custo mas não tentativas, todas outras etapas possuem custo E tentantivas

**OBS.2:** Para uma mesma etapa, todas as tentativas têm o mesmo custo.

Para cada tentativa, você receberá uma entrada que indicará o status dessa etapa, o qual será "correto" ou "incorreto":

```
status_etapa
```

**OBS.3:** No máximo um dos status será "correto". Após recebê-lo, você não deverá continuar realizando as tentativas restantes.

## Output:

Enquanto você recebe as entradas das etapas, você deve imprimir:

- Caso a etapa seja "desistir" ou "concluir":

```
A jornada da construção do(a) {invencao} acaba aqui.
```

Nesse caso, não serão fornecidas as entrada de custo nem de tentativas e deve-se interromper a chamada de novas etapas.

- Caso a entrada seja "dar um plus":

```
Agora o(a) {invencao} ficou ainda mais legal! Pena que precisei gastar R${custo}
```

Nesse caso, será fornecida apenas a entrada de custo, a entrada de tentativas não será fornecida.

Ambos os casos citados acima não serão contabilizados no andamento do projeto como etapas realizadas.

Para os outros casos, você imprimirá:

- Se o status for "incorreto" :

```
Ainda não consegui {etapa} corretamente, e essa tentativa me custou R${custo}
```

- Se o status for "correto":

```
Oba! consegui {etapa}, o que me custou R${custo}
```

Em que, {custo} é um valor inteiro referente à realização daquela única etapa.

Após realizar todas as tentativas necessárias de cada etapa, você deve imprimir:

```
ANDAMENTO DO PROJETO: Etapas realizadas - {etapas_REALIZADAS} ; Tentativas falhas - {total_falhas}
```

Por fim, você deve imprimir:

- Se você desistiu:

```
Infelizmente, o sonho do(a) {invencao} foi interrompido e levou junto com ele R${despesa_total}
```

- Se você concluiu:

```
Uhuuu, finalmente o(a) {invencao} tá pronto(a)! Esse projeto me custou R${despesa_total}
```

## Exemplos:

### Caso 1:

Input:
```
Chalé de Gelo
encontrar gelo suficiente
200
4
incorreto
incorreto
incorreto
incorreto
desistir
```

Output:
```
Ainda não consegui encontrar gelo suficiente corretamente, e essa tentativa me custou R$200
Ainda não consegui encontrar gelo suficiente corretamente, e essa tentativa me custou R$200
Ainda não consegui encontrar gelo suficiente corretamente, e essa tentativa me custou R$200
Ainda não consegui encontrar gelo suficiente corretamente, e essa tentativa me custou R$200
ANDAMENTO DO PROJETO: Etapas realizadas - 0 ; Tentativas falhas - 4
A jornada da construção do(a) Chalé de Gelo acaba aqui.
Infelizmente, o sonho do(a) Chalé de Gelo foi interrompido e levou junto com ele R$800
```

### Caso 2:

Input:
```
Piões Gigantes
comprar material
150
1
correto
fazer o controle de energia
30
4
incorreto
incorreto
correto
dar um plus
45
definir velocidades
10
2
incorreto
correto
concluir
```

Output:
```
Oba! consegui comprar material, o que me custou R$150
ANDAMENTO DO PROJETO: Etapas realizadas - 1 ; Tentativas falhas - 0
Ainda não consegui fazer o controle de energia corretamente, e essa tentativa me custou R$30
Ainda não consegui fazer o controle de energia corretamente, e essa tentativa me custou R$30
Oba! consegui fazer o controle de energia, o que me custou R$30
ANDAMENTO DO PROJETO: Etapas realizadas - 2 ; Tentativas falhas - 2
Agora o(a) Piões Gigantes ficou ainda mais legal! Pena que precisei gastar R$45
Ainda não consegui definir velocidades corretamente, e essa tentativa me custou R$10
Oba! consegui definir velocidades, o que me custou R$10
ANDAMENTO DO PROJETO: Etapas realizadas - 3 ; Tentativas falhas - 3
A jornada da construção do(a) Piões Gigantes acaba aqui.
Uhuuu, finalmente o(a) Piões Gigantes tá pronto(a)! Esse projeto me custou R$305
```