# Denji quer uma namorada 

- **(Este enunciado foi mal elaborado pelo autor original e contém ambiguidades. Tive que mudar meu código para lidar com essas ambiguidades, então talvez o meu código tenha algo que não faça muito sentido, mas foi necessário para minha resposta ser considerada correta na plataforma.)**

**Limite de tempo do código: 200ms**

O menino-serra é só um adolescente, e como qualquer outro pivete de 16 anos, só quer saber de uma coisa: sim, batman, eles estão falando daquilo. Mas Denji tem um pequeno azar e todas as mulheres que ele conhece querem matar ele.

![Makima alimentando Denji](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi59gSYJlHMCu5NufI5X_IJNSnJqVlIaHUGZz8zDcJkoqg_Vxd0BAaoFXANJECW3S_qDFa0VKEAFjVIgysdDzUEVeT9K8qY3aLuvOCvUNekbRcKhmdqtvt1lVUveitXlOYDE7r4jHa41mNyBu_L--wk_2u4ZZDzh6lSacUdG6TDDdRYnmCvCQ/s1600/Chainsaw%20Man%20-%20Episode%202%20-%20Makima%20Feeds%20Denji.gif)

Ele precisa da sua ajuda para fazer um código que armazene o nome das garotas que ele conhece e a chance em % que elas têm de querer matar ele, armazenadas de 0% a 100%, em uma lista com as possíveis candidatas. Denji já está acostumado com essa situação, então, caso a chance seja menor ou igual 50%, ela é um bom partido, do contrário ela deve ser melhor evitar. Existe outro problema, Denji não só é ruim em matemática como também tem dificuldade de memorizar nomes, por isso caso o nome da garota passe de 7 letras, ele não será capaz de decorar o nome e não colocará ela na lista. Além disso, caso o nome da garota seja "Makima" ele ignora as possibilidades de ser assasinado e a considera um bom partido.

![Denji](https://pbs.twimg.com/media/D1jvK-HX4AEk-7c.jpg)

**VOCÊ DEVE UTILIZAR FUNÇÕES PARA REALIZAR CADA ETAPA DO CÓDIGO, CRIE MAIS DE UMA FUNÇÃO PARA NÃO REPETIR O MESMO PROCEDIMENTO VÁRIAS VEZES**

## Input:

Primeiro, você receberá um input contendo o nome de uma mulher ou a string "cabo" para encerrar o código

```
nome
```

Em seguida, você receberá um número inteiro representando a probabilidade entre 0 e 100 de Denji ser morto por ela.

```
probabilidade
```

**OBS:** Caso a entrada seja o nome de uma garota com mais do que 7 letras, você deve descartá-la sem receber a probabilidade de ser morto por ela.

## Output:

Ao receber o nome da garota, você deverá imprimir:

Caso o nome dela tenha mais do que 7 letras:

```
Er {as duas primeiras letras do nome dela}.. errr... nao consigo lembrar, melhor deixar para la
```

**OBS:** você não deve se preocupar com espaços em branco no nome das garotas.

Caso o nome dela seja "Makima":

```
Woof Woof
```

Após ver a chance, Denji dirá:

Caso a probabilidade seja favorável (menor ou igual a 50) ou o nome seja "Makima":

```
Beleza {nome}!! Essa é uma boa pretendente!
```

Do contrário, a probabilidade será muito alta, então você deve imprimir:

```
{nome}, mais uma que so quer o coraçao do chainsaw man, quando que alguem vai querer o meu coraçao!?!?
```

Ao receber a string "cabo", você deverá imprimir uma linha:

Caso o número de relacionamentos que dão certo seja maior do que o de relacionamentos onde a mulher tem altas chances de matar Denji, imprima:

```
Epa ai sim! E hoje pochita!!
```

Caso o contrário (não existe chance de empate):

```
Desculpa pochita acho que nao vai ser hoje que voce vai poder ver meus sonhos
```

Por fim, caso a lista seja totalmente favorável, você deverá imprimi-la no seguinte modelo:

```
nome: {nome 1} - chances de morrer: {chance 1}%
...
nome: {nome n} - chances de morrer: {chance n}%
```

## Exemplos:

### Caso 1:

Input:
```
Reze
45
Power
90
Asa
5
cabo
```

Output:
```
Beleza Reze!! Essa é uma boa pretendente!
Power, mais uma que so quer o coraçao do chainsaw man, quando que alguem vai querer o meu coraçao!?!?
Beleza Asa!! Essa é uma boa pretendente!
Epa ai sim! E hoje pochita!!
```

### Caso 2:

Input:
```
Kobeni
50
Himeno
20
Reze
45
cabo
```

Output:
```
Beleza Kobeni!! Essa é uma boa pretendente!
Beleza Himeno!! Essa é uma boa pretendente!
Beleza Reze!! Essa é uma boa pretendente!
Epa ai sim! E hoje pochita!!
nome: Kobeni - chances de morrer: 50%
nome: Himeno - chances de morrer: 20%
nome: Reze - chances de morrer: 45%
```