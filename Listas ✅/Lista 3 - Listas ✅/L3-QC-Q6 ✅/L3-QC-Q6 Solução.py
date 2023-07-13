quantidade_de_codificacoes = int(input())

for contador_de_codificacoes in range(quantidade_de_codificacoes):
  entrada_composta = str(input())
  sequencia_fibonacci = int(entrada_composta.split()[0])
  n1 = 0
  n2 = 1
  for contador_fibonacci in range(sequencia_fibonacci//2):
    n1 += n2
    n2 += n1
  if (sequencia_fibonacci%2) > 0:
    numero = str(n2)
  else:
    numero = str(n1)
    
  posicoes_dos_digitos = entrada_composta.split()[1]
  posicoes_dos_digitos_sem_traco = posicoes_dos_digitos.replace("-"," ")
  posicao_do_digito_1 = int(posicoes_dos_digitos_sem_traco.split()[0])
  posicao_do_digito_2 = int(posicoes_dos_digitos_sem_traco.split()[1])
  digito_1 = str(numero[posicao_do_digito_1])
  digito_2 = str(numero[posicao_do_digito_2])
  codigo = int(digito_1+digito_2)
  print(chr(codigo),end="")