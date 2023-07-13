# PAC - Programa de aprovação de cãezinhos

**Limite de tempo do código: 2000ms**

![Cachorro Reprovado](https://i.imgur.com/hspAi7L.png)

Nas últimas semanas uma história sobre o doguinho Bob Afonso, reprovado na avaliação de uma creche para cãezinhos bombou no twitter. A mãe pet estava revoltada pois acreditava que seu amigão tinha sido injustiçado e que era perfeitamente capaz de atender às expectativas da equipe de professores, responsáveis pelo bom convívio entre os demais cachorros na creche.

Você, vendo esse caso, e sendo um grande ativista da causa animal e educacional, decide criar um programa simples que ajudaria uma creche a ter um controle mais sistematizado - embora ainda com certo teor de subjetividade - para definir se um sujeito canino foi comportado o suficiente para continuar no convívio com seus colegas e professores.

Utilizando as características únicas dos dicionários (e das tuplas também, se necessário), o programa deve possibilitar que se cadastrem doguinhos, junto de suas respectivas raças e de suas notas em certos critérios (critérios esses que juntos formarão a nota que definirá sua aprovação, reprovação ou recuperação). Ele fará o cálculo da média de três características: Atividade (o nível de ‘agitação’ e de exercício físico do cãozinho), Obediência (o quão sucetível a comandos e a atenção dos cuidadores responsáveis o cão é) e Socialização (o quão amigável e enturmado o bichinho é com seus colegas).

Em seguida ele mostrará o nome de cada um dos doguinhos aprovados, reprovados e em recuperação, seguindo a ordem de inserção no cadastro juntos de sua respectiva raça e sua média.

Todos esses critérios (notas) vão de 0 a 5 estrelas. A média para a aprovação é de 3 ou mais estrelas, para a reprovação direta é de menos de 2 estrelas e para a recuperação (uma nova chance) a média deve ser maior ou igual a 2 estrelas e menor que 3 estrelas.

## Input:

A entrada inicia com um inteiro M, que definirá o número de cachorros a serem cadastrados. Em seguida virão as M entradas do tipo string com os nomes, seguidos da raça, nota de atividade, nota de obediência e nota de socialização, separados por vírgula seguida de espaço.

Exemplo:

```
M
Nome_1, Raça_1, Atividade_1, Obediencia_1, Socializacao_1
Nome_2, Raça_2, Atividade_2, Obediencia_2, Socializacao_2
...
Nome_M, Raça_M, Atividade_M, Obediencia_M, Socializacao_M
```

**As notas são do tipo float e contém duas casas decimais.**

## Output:

A saída mostrará os nomes, raças e médias dos N aprovados, seguidos dos N reprovados e por fim, os N que ficaram de recuperação:

```
Estao aprovados e de parabens os seguintes coleguinhas:
{Nome_aprovado_1} - {Raça_aprovado_1} - media: {Media_aprovado_1}
...
{Nome_aprovado_N} - {Raça_aprovado_N} - media: {Media_aprovado_N}
Os colegas a seguir nao se comportaram bem e precisam de ajuda profissional (entrar em contato urgente):
{Nome_reprovado_1} - {Raça_reprovado_1} - media: {Media_reprovado_1}
...
{Nome_reprovado_N} - {Raça_reprovado_N} - media: {Media_reprovado_N}
Esses queridos terao uma nova chance e prometem melhorar:
{Nome_recuperacao_1} - {Raça_recuperacao_1} - media: {Media_recuperacao_1}
...
{Nome_recuperacao_N} - {Raça_recuperacao_N} - media: {Media_recuperacao_N}
```

**As médias devem ser do tipo float e conter 2 casas decimais.**

**OBS:** Podem existir casos em que não há reprovações, ou cachorros em recuperação, o mesmo pode ocorrer para as aprovações, mas sempre existirá pelo menos uma dessas classificações presentes no output.

## Exemplos:

### Caso 1:

Input:
```
4
Scooby Doo, Dogue Alemao, 4.75, 3.25, 4.50
Lassie, Collie, 3.00, 4.25, 3.75
Pluto, Cao de Caça, 3.50, 3.75, 3.25
Hachiko, Akita Inu, 4.25, 4.00, 4.50
```

Output:
```
Estao aprovados e de parabens os seguintes coleguinhas:
Scooby Doo - Dogue Alemao - media: 4.17
Lassie - Collie - media: 3.67
Pluto - Cao de Caça - media: 3.50
Hachiko - Akita Inu - media: 4.25
```

### Caso 2:

Input:
```
7
Snoopy, Beagle, 3.4, 4.1, 2.8
Rex, Pastor Alemao, 4.9, 3.3, 4.2
Toto, Cairn Terrier, 3.1, 3.8, 3.7
Bolt, Pastor Australiano, 2.7, 2.5, 2.8
Pongo, Dalmata, 3.6, 3.3, 3.5
Perdita, Dalmata, 2.9, 2.8, 2.6
Droopy, Bloodhound, 2.6, 2.8, 3.3
```

Output:
```
Estao aprovados e de parabens os seguintes coleguinhas:
Snoopy - Beagle - media: 3.43
Rex - Pastor Alemao - media: 4.13
Toto - Cairn Terrier - media: 3.53
Pongo - Dalmata - media: 3.47
Esses queridos terao uma nova chance e prometem melhorar:
Bolt - Pastor Australiano - media: 2.67
Perdita - Dalmata - media: 2.77
Droopy - Bloodhound - media: 2.90
```

### Caso 3:

Input:
```
6
Buddy, Golden Retriever, 2.5, 3.0, 2.0
Max, Poodle, 1.5, 2.0, 1.0
Lola, Bulldog Frances, 2.0, 1.5, 2.0
Rocky, Pastor Alemao, 3.0, 2.5, 2.5
Charlie, Yorkshire Terrier, 3.5, 3.5, 3.0
Daisy, Shih Tzu, 1.5, 1.0, 1.5
```

Output:
```
Estao aprovados e de parabens os seguintes coleguinhas:
Charlie - Yorkshire Terrier - media: 3.33
Os colegas a seguir nao se comportaram bem e precisam de ajuda profissional (entrar em contato urgente):
Max - Poodle - media: 1.50
Lola - Bulldog Frances - media: 1.83
Daisy - Shih Tzu - media: 1.33
Esses queridos terao uma nova chance e prometem melhorar:
Buddy - Golden Retriever - media: 2.50
Rocky - Pastor Alemao - media: 2.67
```