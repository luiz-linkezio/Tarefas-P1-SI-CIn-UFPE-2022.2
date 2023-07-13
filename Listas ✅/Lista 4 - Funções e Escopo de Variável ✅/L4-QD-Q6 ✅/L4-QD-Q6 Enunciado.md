# O Pentágono

**Limite de tempo do código: 2000ms**

O governo dos Estados Unidos da América solicitou ao Japão o envio de demônios para serem armazenados numa prisão especial localizada no Pentágono. Logo, a função de transferir e alocar foi designada para Makima, Líder da Divisão de Caçadores de Demônios da Defensoria Pública Japonesa. Por gostar de algoritmos, ela opta por fazer a prisão do Pentágono de Hash Table.

Hash Table ou Tabela de Dispersão é uma estrutura de dados que permite armazenar e acessar informações de forma rápida e eficiente. Funciona através da aplicação de uma função hash que transforma a chave de busca em um índice da tabela, onde o valor correspondente pode ser encontrado de forma direta.

![Hash Table](https://miro.medium.com/v2/resize:fit:720/1*IYmk2KnjtYu5gLihyDSTdg.gif)

Portanto, a fórmula para encontrar o índice das celas no Pentágono de cada demônio é dada por:

**x mod c**

**x** = soma dos valores correspondentes às letras no nome do demônio de acordo com a tabela ASCII;

**c** = quantidade de celas;

Se a cela que o demônio deveria ser alocado já estiver sendo ocupada, ele deve ser alocado na próxima cela vazia à direita de sua respectiva cela, estratégia chamada de Linear Probing.

![List](https://miro.medium.com/v2/resize:fit:720/1*TTNMxY5I27Ti3IbcyWIWTw.gif)

**obs.1:** O uso de funções é obrigatório na questão.

**obs.2:** Os nomes dos demônios conterão apenas letras de “a” a “z”.

**obs.3:** Use as funções ord e char de python para obter os valores dos caracteres na tabela ASCII”.

## Input:

Inicialmente serão fornecidos em uma linha, separados por um espaço, inteiros referentes ao número total de celas e quantas ordens você receberá:

```
quantidade_celas quantidade_ordens
```

depois, **n** linhas, contendo a ação a ser realizada (a ordem) e o nome do demônio com o qual a ação deve ser feita, também separados por um espaço:

```
ordem nome_demônio
```

Makima irá dar ordens para seu subordinado (você) "ADICIONAR" ou “REMOVER” demônios.

## Output:

Se Makima ordenar para "ADICIONAR" e a prisão estiver cheia você deve informá-la com “CHEIO”, e se ela ordenar para “REMOVER” e o demônio não existir você deve informá-la com “NAO EXISTE”.

**obs.4:** na hora de remover elementos, atente-se para a diferença de lugares vazios nunca ocupados e em que já foi removido algum elemento, caso não encontre o demônio na primeira cela acessada.

**obs.5:** as funções ADICIONAR e REMOVER devem ser criadas por você, de acordo com a lógica que foi explicada no enunciado.

No fim, informe a lista de demônios na ordem que foram alocados.

## Exemplos:

### Caso 1:

Input:
```
4 2
ADICIONAR lobo
ADICIONAR bolo
```

Output:
```
lobo bolo
```

### Caso 2:

Input:
```
11 7
ADICIONAR lobo
ADICIONAR bolo
ADICIONAR espada
ADICIONAR pistola
REMOVER espada
REMOVER controle
ADICIONAR bomba
```

Output:
```
NAO EXISTE
bolo pistola bomba lobo
```