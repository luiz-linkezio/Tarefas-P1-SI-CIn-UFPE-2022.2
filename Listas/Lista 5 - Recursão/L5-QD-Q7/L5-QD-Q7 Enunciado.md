# 🦇BatGPT

**Limite de tempo do código: 200ms**

![Batcomputer](https://media.tenor.com/q3usgo-LZEEAAAAC/batman-and-robin-bat.gif)

Mais uma vez a cidade de Gotham está sendo perturbada por algum vilão. O maior detetive do mundo, Batman, desconfia que quem está causando tudo isso seja o Charada, devido às pistas encontradas, porém o detetive teme que outro vilão esteja junto com o Charada.

De acordo com a sua experiência, ele tem 6 suspeitos além do próprio Charada, são eles: **Arlequina**, **Pinguim**, **Joker**, **Espantalho**, **Duas Caras** e o **Rei dos Condimentos**.

Ele chamou você para criar uma "inteligência artificial" que o auxilie a encontrar pistas em um caça-palavras em que as letras não precisam obrigatoriamente estar numa ordem, mas podem estar em várias direções distintas, como para frente, para atrás, para cima, para baixo ou até para as diagonais.

Exemplo:

[A L R Q U]
[R U E I A]
[Y T R N W]

Nesse exemplo, a partir do primeiro A, seguindo as direções ⬇️↗️↘️↗️➡️↙️⬇️↗️ você encontra ARLEQUINA

**OBS:** Só haverá um vilão no caça-palavras

## Input:

O primeiro input será um inteiro que terá quantas linhas e colunas terá o caça palavras.

```
N
```

Logo em seguida haverá N entradas com N caracteres em maiúsculo separados por um espaço em branco.

```
A B C ... E F G ... H I J ...
```

## Output:

Se você encontrar no caça palavras o Charada, o output será o seguinte:

```
Isso!!! Encontramos uma pista, mas somente o Charada está envolvido.
```

Caso você encontre outro vilão, a mensagem deverá ser a seguinte:

```
Isso!!! Encontramos uma pista, {Vilao} está junto com o Charada.
```

Mas caso não encontre nenhum vilão, a saída deverá ser a seguinte:

```
Poxa... acho que seguimos uma pista falsa.
```

**OBS:** O nome do vilão deverá ser sempre igual aos nomes do enunciado, mas no caça palavras estarão sempre maiúsculas e sem espaço vazio.

## Exemplos:

### Caso 1:

Input:
```
10
V B Z G O R R O F L
V P T C H X W F T G
V O G A R Q G M Y P
K U A N E U X Z N W
I Y U I P K X Y D G
M J Q W L U N O D I
N H R R P V H U O R
N T F I F Q H E S H
Z Y I O V B X N T L
H K J D W V K V X C
```

Output:
```
Isso!!! Encontramos uma pista, Pinguim está junto com o Charada.
```

### Caso 2:

Input:
```
7
D G I H M M H
Y O C L T G Q
B L O A Q D C
I H C N G G K
V A R A G Y Q
Z L A F A O M
V A D P P V H
```

Output:
```
Isso!!! Encontramos uma pista, mas somente o Charada está envolvido.
```

### Caso 3:

Input:
```
12
U O O L K M Y F H Y Q O
T X T I N F H Z F C J I
O L M O K D H C E W X V
K B Q C O S G A K J I W
U B Z K N R N C W N N I
B Z Z M W L N C F V T Z
T N I P K Y T J R C L S
Q Y M N X K N F P S B I
Y H F K K J Y H W Q E H
A P M Q T H R H R S C E
Z D U U E J Q N U W F K
S T Z G I Z Z U V M E W
```

Output:
```
Poxa... acho que seguimos uma pista falsa.
```