# Digitalizando os Diários

**Limite de tempo do código: 2000ms**

Com a grande quantidade de informações espalhadas nos diferentes diários, encontrar um registro específico pode ser um desafio.

Para ajudar a solucionar esse problema, você foi convidado a criar um programa capaz de indicar em qual dos três cadernos se encontra determinado conteúdo buscado.

![Livros](https://i.imgur.com/HrBfcEo.png)

Para tanto, o seu programa deve ser capaz de receber os nomes de determinada quantidade de registros e o diário onde cada um se encontra, armazená-los no diário correspondente, e, depois, permitir que o usuário busque-os, indicando o diário referente.

## Input:

O primeiro input consiste em um inteiro **n >= 1**, indicando o número de entradas subsequentes, que consistirão nas informações a registrar.

```
n
```

Esses **n** inputs sempre terão o formato abaixo, em que {conteudo} pode ser uma string qualquer e {numero_do_diario} pode ser o número 1, 2 ou 3 separados por vírgula e um espaço:

```
{conteudo}, {numero_do_diario}
...

```

Depois, será recebido um inteiro **m >= 1**, referente ao número de informações que queremos buscar:

```
m
```

Seguido de **m** strings a buscar, cada uma referenciando, ou não, a algum dos **n** nomes recebidos anteriormente:

```
{conteudo_buscado}
...
```

## Output:

Para cada uma das **m** buscas, será printada uma dessas frases, dependendo do seu resultado:

- No caso da informação buscada ser encontrada:

```
Informacoes sobre {conteudo_buscado} estao no Diario {numero_do_diario}
```

- Caso o conteúdo buscado não exista em nenhum dos diários:

```
Nenhum dos diarios possui informacoes sobre {conteudo_buscado}
```

## Exemplos:

### Caso 1:

Input:
```
3
Olho-Morcego, 1
Gnomos, 3
Cycloptopus, 2
3
Gnomos
Olho-Morcego
Diabretes
```

Output:
```
Informacoes sobre Gnomos estao no Diario 3
Informacoes sobre Olho-Morcego estao no Diario 1
Nenhum dos diarios possui informacoes sobre Diabretes
```

### Caso 2:

Input:
```
6
Fonte da Juventude, 1
Doppelgangers, 2
Bill Cipher, 3
Unicornios, 1
O Olho Cego, 3
Gremloblin, 3
4
Doppelgangers
Halflings
Bill Cipher
Unicornios
```

Output:
```
Informacoes sobre Doppelgangers estao no Diario 2
Nenhum dos diarios possui informacoes sobre Halflings
Informacoes sobre Bill Cipher estao no Diario 3
Informacoes sobre Unicornios estao no Diario 1
```