# Adoção de pets

- **(Este enunciado foi elaborado incorretamente pelo autor original, dito isso, o meu código teve que ser alterado para algo que não é o que o enunciado pede, mas era o que eu tinha que fazer para a questão ser aceita na plataforma como resposta correta.)**

**Limite de tempo do código: 2000ms**

![Gato vs Cachorro](https://thumbs.gfycat.com/HauntingHorribleAmericansaddlebred-max-1mb.gif)

Sérgio, o monitor de IP, está pensando em adotar pets. Como ele nunca teve um e sua intenção é ter mais de um, ele sabe que precisa analisar muitas variáveis como: quais pets podem ficar juntos, o que precisa ser mudado na casa dele, dentre outras variáveis. Para lidar com toda essa situação, ele decidiu usar dicionários para organizar tudo isso e poder tomar as melhores decisões para que tudo dê certo.

A primeira coisa que ele fez foi fazer uma lista das potenciais escolhas de pets que ele queria. Ele pensou em gato, cachorro, peixe e hamster. Depois, ele partiu para o modo pesquisa e aprendeu tudo que precisava saber sobre cada um deles. O que ele concluiu foi o seguinte:

- O gato tem todos os outros citados como inimigos;
- O hamster tem como inimigo o cachorro, mas o cachorro não tem como um inimigo o hamster;
- Exceto o caso acima, todas as outras relações de inimigos são mútuas. Exemplo, o gato é inimigo do cachorro, assim como o cachorro é inimigo do gato;
- Todo animal é amigo do animal da mesma espécie;
- Para um gato é preciso das seguintes necessidades: ração, bola de lã, ratinho de brinquedo e caixa de areia;
- Para um cachorro é preciso das seguintes necessidades: ração, coleira, ursinho de pelúcia;
- Para um peixe é preciso das seguintes necessidades: aquário, ração e filtro;
- Para um hamster é preciso das seguintes necessidades: serragem, ração e roda para hamster

Outra coisa muito importante que ele concluiu com suas pesquisas também foi o fato de que se os animais são recém nascidos, eles nunca vão ser inimigos.

**Atenção:** Como Sérgio tem o mínimo de organização, quando os animais e suas características (quem são seus amigos, inimigos e quais são suas necessidades) forem cadastrados, tudo terá que ser feito em ordem alfabética.

**Obs:** É obrigatório o uso de dicionários na resolução.

**Obs2:** Copie o nome das necessidades dos animais exatamente como está escrito na questão.

## Input:

A primeira linha de entrada representa quais são os animais que ele quer consultar, usando o ‘e’ para ir dizendo quais são os animais, exemplos:

```
cachorro e gato
```

```
cachorro e gato e hamster
```

A segunda linha de entrada corresponde se eles são recém nascidos ou não:

```
sim
```

ou

```
nao
```

## Output:

Caso seja um nome de um animal que não esteja na lista que Sérgio preparou, imprima a seguinte mensagem:

```
Sérgio, o animal {animal} não estava nas suas potenciais escolhas, logo ele não pode ser analisado.
```

**OBS:** Você deve imprimir essa mensagem para todo animal contido na entrada que não estiver na lista de Sérgio e os outros tipos outputs serão desconsiderados

Caso os animais sejam recém nascidos, imprima:

```
Como os animais são recém nascidos, eles podem ser adotados juntos!
Segue aqui as necessidades dos animais:
As necessidades do(a) {animal} são:
- {necessidade_1};
- {necessidade _2};
- ...
Dito isso, vamos adotá-los!!!
```

Caso eles não sejam recém nascidos, mas ainda assim possam ser adotados juntos:

```
Segue aqui as necessidades dos animais:
As necessidades do(a) {animal} são:
- {necessidade_1};
- {necessidade _2};
- ...
Dito isso, vamos adotá-los!!!
```

Caso os animais não possam ficar juntos:

```
Sérgio, o(a) {animal1} tem o(a) {animal2} como inimigo. Não é possível adotá-los juntos, a não ser que sejam recém nascidos
```

**OBS:** Você deve imprimir essa mensagem para toda combinação entre dois animais em que houver alguma relação de inimizade

## Exemplos:

### Caso 1:

Input:
```
gato e cachorro
nao
```

Output:
```
Sérgio, o(a) gato tem o(a) cachorro como inimigo. Não é possível adotá-los juntos, a não ser que sejam recém nascidos
Sérgio, o(a) cachorro tem o(a) gato como inimigo. Não é possível adotá-los juntos, a não ser que sejam recém nascidos
```

### Caso 2:

Input:
```
gato e cachorro
sim
```

Output:
```
Como os animais são recém nascidos, eles podem ser adotados juntos!
Segue aqui as necessidades dos animais:
As necessidades do(a) gato são:
- bola de lã;
- caixa de areia;
- ração;
- ratinho de brinquedo;
As necessidades do(a) cachorro são:
- coleira;
- ração;
- ursinho de pelúcia;
Dito isso, vamos adotá-los!!!
```

### Caso 3:

Input:
```
coelho e peixe
sim
```

Output:
```
Sérgio, o animal coelho não estava nas suas potenciais escolhas, logo ele não pode ser analisado.
```

### Caso 4:

Input:
```
peixe e cachorro
nao
```

Output:
```
Segue aqui as necessidades dos animais:
As necessidades do(a) peixe são:
- aquário;
- filtro;
- ração;
As necessidades do(a) cachorro são:
- coleira;
- ração;
- ursinho de pelúcia;
Dito isso, vamos adotá-los!!!
```
