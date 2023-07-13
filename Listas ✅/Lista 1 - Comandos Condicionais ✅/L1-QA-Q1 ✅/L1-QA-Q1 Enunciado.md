# Fulaninho joga em qual posição?

**Limite de tempo do código: 2000ms**

A convocação dos 26 jogadores que compõem a seleção brasileira foi muito aguardada por vários apaixonados por futebol, até apostas foram feitas. Essa foi a lista dos jogadores convocados pelo técnico Tite:

![Tabela de escalação](https://cdn6.campograndenews.com.br/uploads/noticias/2022/11/07/ea941c97b7eaecb0b9972a50877ae08282306056.jpg)

Você tem um amigo chamado João que nunca lembra a posição dos jogadores e passa o tempo todo perguntando **“Fulaninho joga em qual posição?”**. Para facilitar sua vida, você decide escrever um código que responde a essa pergunta.

## Input:

A entrada será constituída de um nome:

```
nome_jogador
```


## Output:

A saída será da seguinte forma:

```
[nome_jogador] foi convocado e jogará como [posicao]!
```

As posições são:

- goleiro
- lateral
- zagueiro
- meia
- atacante

Caso o nome informado não seja de nenhum jogador convocado, você deverá responder o seguinte:

```
[nome_jogador] não foi convocado, mas quem sabe na próxima?
```

**PS: Deverá ser considerado apenas os nomes da forma escrita EXATAMENTE como na imagem e deve ser respondida a posição que ele joga de acordo com a imagem.**

## Exemplos:

### Caso 1:

Input:
```
Alisson
```

Output:
```
Alisson foi convocado e jogará como goleiro!
```

### Caso 2:

Input:
```
Vini Jr.
```

Output:
```
Vini Jr. foi convocado e jogará como atacante!
```
