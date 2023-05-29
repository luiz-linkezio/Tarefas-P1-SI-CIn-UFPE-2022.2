# Um belo dia de praia 🏝️

- **(Este enunciado foi modificado para a melhor compreensão do leitor)**

**Limite de tempo do código: 2000ms**

![Praia](https://www.cin.ufpe.br/~jmsm3/barragrande.jpg)

É verão e você quer curtir um dia nas belíssimas praias de Maragogi, o Caribe brasileiro. Você acabou de tomar seu café da manhã, e quer se preparar para tomar o tão esperado banho de mar. Para ter o dia perfeito de praia, você deve passar seu filtro solar e separar um dinheiro para tomar aquela água de coco de lei. **Se estiver chovendo, você não poderá ir à praia.**

No início do dia, você se encontra:
- Sem protetor solar
- 0 reais na carteira
- Clima ensolarado

## Input:

Você receberá inúmeras entradas contendo ações realizadas por você ou uma mudança do clima, até receber a entrada “ir para a praia”. As ações podem ser as seguintes:

- separar dinheiro → Pede uma nova entrada, em float, que representa a quantia adicionada à carteira

- passar protetor → Passa o protetor ¯_(ツ)_/¯

- choveu → Muda o clima para "chuvoso"

- parou de chover → Muda o clima para "ensolarado"

- ir para a praia → Finaliza os acontecimentos

**Obs.:** Caso apareça uma entrada diferente dessas ações, seu programa deverá ignorar.

## Output:

Você deve se preparar para dois tipos de saídas: uma para se você vai à praia ou não, e outra para como você chegou da praia.

Se o clima estiver chuvoso:

```
Hoje não vai dar pra ir, chuvinha barrou
```

Se o clima estiver ensolarado:

```
Hoje tem sol e mar!
```

Se você foi à praia e:
- não passou protetor e está com menos de 10 reais:

```
Você não chegou muito bem, chame um médico!
```

- não passou protetor e está com 10 ou mais reais:

```
O novo camarão do CIn foi criado
```

- passou protetor e está com menos de 10 reais:

```
Só faltou uma aguinha de coco...
```

- passou protetor e está com 10 ou mais reais:

```
Aí sim! Hoje rendeu!
```

## Exemplos:

### Caso 1:

Input:
```
passar protetor
separar dinheiro
20
choveu
estiou
ir para a praia
```

Output:
```
Hoje não vai dar pra ir, chuvinha barrou
```

### Caso 2:

Input:
```
separar dinheiro
2
choveu
separar dinheiro
30
parou de chover
ir para a praia
```

Output:
```
Hoje tem sol e mar!
O novo camarão do CIn foi criado
```