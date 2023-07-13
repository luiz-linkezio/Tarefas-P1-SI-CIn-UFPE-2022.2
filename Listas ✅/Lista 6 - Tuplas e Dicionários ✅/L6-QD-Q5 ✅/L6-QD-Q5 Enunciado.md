# Passatempo Canino

- **(Este enunciado foi feito de forma incorreta e ruim pelo autor original, tentei modificar o enunciado para a melhor compreensão do leitor, porém, ainda há chances de estar incorreto, não sei se consegui consertar tudo. Além disso, talvez meu código fique difícil de compreender, pois tive que ir alterando algumas coisas até adivinhar os erros do autor do enunciado para que meu código fosse aceito pela plataforma como resposta correta)**

**Limite de tempo do código: 1000ms**

**PROIBIDO CONDICIONAIS E GLOBAIS** (ler abaixo)

Charlote é uma dog muito fofa e apaixonada por sua dona, minha mãe. Quando ela sai para trabalhar, Charlote sente muito sua falta, e fica a ter de se entreter com seus brinquedos e o que mais achar pela casa esperando ela retornar.

![Charlote](https://cdn.discordapp.com/attachments/848330741120106519/1089683796904910848/image.png)

Muito ocupado com minhas atribuições de monitoria, universidade e trabalho, peço ajuda de meus caros alunos para escrever um programa capaz de determinar o quão cansada minha dog cachorra fica após várias atividades.

Todo dia ela acorda com uma certa energia, que também é o máximo que ela pode atingir quando recuperar energia. Enquanto ainda tiver energia, isto é, acima de zero energia, e não tiver gasto mais que cem pontos de energia (caso gaste mais energia do que tem atualmente, a energia em excesso não é contabilizada) (o gasto de energia nunca é reduzido, apenas aumenta), ela vai achar algo pela casa e brincar, podendo ser uma das opções seguintes:

“Vaquinha” sempre é diversão, ela perde energia correspondente ao número de chacoalhadas que ela dá.

“Chupeta” é boa para correr e morder, por apertar muito a chupeta, nem sempre perde a mesma quantidade de energia. Sua energia vai diminuir para um valor que pode ser o número de vezes que morde a chupeta ou a energia atual menos 5, o que for maior entre esses. Ex. Charlote tinha 15 de energia quando achou a chupeta, e apertou ela 5 vezes. Devemos comparar 5 (vezes que apertou) com 10 (energia atual menos 5). Como 10 é maior, a nova energia será 10. Se o número de vezes que ela mordeu a chupeta fosse 12 em vez de 5, a nova energia seria 12, pois 12 é maior do que 10.

“Zé Gotinha” é um de seus favoritos, e ela brinca tanto com ele que sua energia se torna o resultado da divisão inteira da energia pelo número de vezes que ela aperta ele, mas se der zero apertos, sua energia permanece a mesma.

“Bolinha” é o que faz ela dar uma disparada, e chega a atingir velocidades absurdas, perdendo um ponto de energia a cada 4 km/h que ela atinge.

“Osso” é seu descanso, e recupera um adicional de energia equivalente ao dobro do número de vezes que rói ele.

“Comida” nem sempre é bom, pois ela gosta muito de roubar coisas da casa e tentar comer, perdendo ou ganhando a energia correspondente ao número de letras do que pegou, perdendo energia se o número de letras do que pegou for ímpar, e ganhando se for par.

**Obs.:** Você não deve se preocupar em tratar possíveis espaços em branco na contagem do len.

![Charlote 2](https://cdn.discordapp.com/attachments/848330741120106519/1089590880769409195/IMG_3404.jpg)

Ao final de tudo isso, sua dona chega, e ela vai direto para ela, receber muito carinho e amor.

OBS!!!!:

Por falar de amor, como o dela é incondicional, ESTÁ PROIBIDO USAR CONDICIONAIS PARA RESOLVER ESTA QUESTÃO, isto é, if elif else, e isso inclui usos inline, dentro de list comprehension, e quaisquer gambiarras usando loops, para os espertinhos. PROIBIDO USO DE VÁRIAVEIS GLOBAIS, se você for usar algo do resto do código em uma função, deve vir como argumento de sua execução, nada de referenciar variáveis fora do escopo. Todos os loops estão liberados, contanto que não sejam substituíveis por um condicional, e também é obrigatório o uso de dicionários.

**Dica:** Você pode passar uma função como item de dicionário, basta passá-la sem os () e usar ele com os devidos parâmetros no elemento do seu dicionário. Veja o exemplo abaixo.

```
def happy():
  print(":-)")

def sad():
  print(":-(")

dic = {"happy": happy, "sad": sad}

dic["sad"]()
dic["happy"]()
```

Você pode ler mais sobre aqui: [Store function as dictionary value](https://www.geeksforgeeks.org/python-store-function-as-dictionary-value/).

**Dica 2:** Usar as funções de max() e min() podem ajudar a contornar as restrições de condicional

## Input:

Uma linha de entrada, contendo um número, que será a energia inicial e máxima de Charlote.

```
INT
```

A seguir, um número indeterminado de linhas de comandos, que seguem enquanto sua energia for maior que 0, e enquanto ela não tiver gasto mais que ou exatos 100 pontos de energia.

```
{OBJETO}: {ADICIONAL}
```

Onde, para cada valor de OBJETO:

- Vaquinha → ADICIONAL é o número inteiro de chacoalhadas que ela dá

- Chupeta → ADICIONAL é o número inteiro de vezes que morde a chupeta

- Zé Gotinha → ADICIONAL é o número inteiro de vezes que aperta a gotinha

- Bolinha → ADICIONAL é o número inteiro da velocidade máxima atingida

- Osso → ADICIONAL é o número inteiro de vezes que rói o osso

- Comida → ADICIONAL é uma string do nome do que pegou para comer

## Output:

Para cada linha de entrada que receba referente ao que ela fez com sua energia, você vai imprimir correspondentemente:

- Vaquinha

```
Brinquedo da vaquinha! Vou chacoalhar
```

- Chupeta

```
Minha pipeta! Vou morder
```

- Zé Gotinha

```
Meu preferido! Faz barulho e mordo
```

- Bolinha

```
ZOOOOOOOOOOOOOOOOOM
```

- Osso 

```
Pausa para roer
```

- Comida

```
Uhh, {ADICIONAL} deve ser comestível
```

Ao final do programa, uma linha com a seguinte string:

```
Mamãe chegou! Gastei {X} pontos da minha energia e estou c{'a' * N}nsada, mas vou correr para seus braços!
```

Onde

X → 0 ≤ X ≤ 100, representando quantos pontos de energia foram gastos.

N → Uma string de n vezes a letra “a”, 0 < a ≤ 10, com um “a” para cada 10 energia gasta, minimo de 1 “a”.

## Exemplos:

### Caso 1:

Input:
```
20
Vaquinha: 5
Chupeta: 5
Zé Gotinha: 5
Vaquinha: 2
```

Output:
```
Brinquedo da vaquinha! Vou chacoalhar
Minha pipeta! Vou morder
Meu preferido! Faz barulho e mordo
Brinquedo da vaquinha! Vou chacoalhar
Mamãe chegou! Gastei 20 pontos da minha energia e estou caansada, mas vou correr para seus braços!
```

### Caso 2:

Input:
```
2023
Zé Gotinha: 2
```

Output:
```
Meu preferido! Faz barulho e mordo
Mamãe chegou! Gastei 100 pontos da minha energia e estou caaaaaaaaaansada, mas vou correr para seus braços!
```