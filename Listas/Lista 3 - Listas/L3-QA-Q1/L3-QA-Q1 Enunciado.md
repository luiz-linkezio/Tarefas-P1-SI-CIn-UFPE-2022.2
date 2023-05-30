# Quem roubou o artefato misterioso?

- **(Este enunciado foi modificado para a melhor compreensão do leitor)**

**Limite de tempo do código: 2000ms**

![Mistério](https://uploads.jovemnerd.com.br/wp-content/uploads/2020/06/gravitu-falls-dica-de-desenho.jpg)

O artefato misterioso da Cabana do Mistério foi roubado e agora cabe a você, junto aos irmãos Pines, investigar a lista de frequentadores da cabana para descobrir o responsável pelo roubo e solucionar este mistério incômodo. Utilize sua astúcia e habilidades de dedução para ajudar a encontrar o culpado e recuperar o valioso artefato.

Para isso, você deverá receber entradas sem um fim determinado, e ir construindo a lista dos suspeitos. Pense com cuidado e ajude os irmãos Pines a resolver esse enigma!

## Input:

Para cada entrada abaixo, realize a determinada ação:

```
novo suspeito - altissima periculosidade
```

- receba como entrada um nome e o adicione no começo da lista.

```
novo suspeito - pouco perigoso
```

- receba como entrada um nome e o adicione no final da lista.

```
livre de suspeita, pode remover
```

- receba como entrada um nome e o remova da lista.

```
sujeito mais perigoso do que pensavamos
```

- receba duas entradas: uma com o índice atual do sujeito a partir de 0 e outra com o índice a ser atualizado. Troque a posição do indivíduo na lista com o indivíduo que está na nova posição dele a partir disso.

```
que estranho, esses dois meliantes… troque-os de lugar
```

- receba duas entradas, cada uma contendo um nome, e inverta a posição deles na lista.

```
essa posicao nao esta de acordo, ele nao e tao perigoso assim
```

- receba uma entrada contendo um nome, e atualize a lista levando o nome do sujeito para a última posição da lista.

```
como a lista esta ficando?
```

- não recebe entrada, apenas imprime todos os nomes da lista conforme especificado no output

```
ja temos nossa lista de suspeitos
```

- finaliza o recebimento de entradas, e imprime uma resposta de acordo como especificado no output

**OBS:** As entradas são amigáveis, sempre seguirão as especificações acima e não podem ter duas pessoas com o mesmo nome da lista.

## Output:

Caso a entrada seja:

```
como a lista esta ficando?
```

- Você deve imprimir:

```
suspeito1 suspeito2 suspeito3 ... suspeitoN
```

Caso a entrada seja:

```
ja temos nossa lista de suspeitos
```

- Você deve imprimir:

```
O resultado final ficou assim:
suspeito1 suspeito2 suspeito3 ... suspeitoN
```

**OBS:** É preciso imprimir todos os suspeitos separados por um espaço em branco.

**OBS2:** Cuidado com espaço em branco no fim da lista

## Exemplos:

### Caso 1:

Input:
```
novo suspeito - altissima periculosidade
João
novo suspeito - pouco perigoso
José
como a lista esta ficando?
novo suspeito - altissima periculosidade
Maria
como a lista esta ficando?
que estranho, esses dois meliantes… troque-os de lugar
João
Maria
como a lista esta ficando?
essa posicao nao esta de acordo, ele nao e tao perigoso assim
Maria
ja temos nossa lista de suspeitos
```

Output:
```
João José
Maria João José
João Maria José
O resultado final ficou assim:
João José Maria
```