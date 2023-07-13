# A sobrevivência de Denji

**Limite de tempo do código: 2000ms**

Entre os muitos desafios enfrentados por Denji, um dos piores foi lidar com a traição de seu parceiro Yakuza. Este com quem contava com a sua ajuda pra quitar a dívida deixada por seu falecido pai, na verdade queria que Denji fosse de arrasta pra cima igualmente seu pai. Contudo, ele conseguiria sobreviver, caso fizesse um pacto de forma correta com seu amigo Ponchita.

![Denji e Pochita](https://cdn.discordapp.com/attachments/893547371491893248/1080628832421281843/perai_minino.png)

O pacto se daria da seguinte forma: Ponchita diria um número positivo N, maior que zero e Denji deveria dizer se tal número é primo ou não. Caso não fosse, Denji deveria dizer quais números primos existem no intervalo de 1 à N.

Se Denji acertar a resposta, ele obtverá sucesso no pacto e conseguirá sobreviver. Ajude-o nessa missão!

## Input:

Você receberá um número N positivo, sendo N>0

## Output:

Para o output, temos os seguintes casos:

- Caso1: Caso o número digitado seja primo, você deve imprimir a seguinte mensagem:

```
O número {N} é primo.
```

- Caso 2: Caso o número digitado não seja primo, você deve imprimir as seguintes mensagens:

```
O número {N} não é primo.
```

Além disso, se houverem número primos de 1 à N, você imprimir na tela dessa maneira:

```
Entretanto, temos primos no intervalo de 1 à {N}. Estes são:
{primo1}, {primo2}, {primoN}
```

Caso não tenha números primos no intervalo citado. Imprima juntamente com o print B:

```
Além disso, não temos primos no intervalo de 1 à {N}.
```

Ao final, independente do caso, você deve exibir na tela::

```
AGORA ESTOU PRONTO PARA MINHA NOVA VIDA!
```

## Exemplos:

### Caso 1:

Input:
```
5
```

Output:
```
O número 5 é primo.
AGORA ESTOU PRONTO PARA MINHA NOVA VIDA!
```

### Caso 2:

Input:
```
4
```

Output:
```
O número 4 não é primo.
Entretanto, temos primos no intervalo de 1 à 4. Estes são:
2, 3
AGORA ESTOU PRONTO PARA MINHA NOVA VIDA!
```