def classificar_cela(nome):
  len_nome = len(nome)
  global soma_total
  soma_total = 0
  
  for contador_len in range(len_nome):
    letra_atual = nome[contador_len]
    numero_ASCII = ord(letra_atual)
    soma_total += numero_ASCII
  
  return soma_total  

def adicionar(nome):
  global cadeia
  if cadeia[indice_da_cela] == "":
    cadeia[indice_da_cela] = nome
  else:
    foi_preso = False
    for mudancas_de_cela in range(int(len(cadeia) - indice_da_cela)):
      if foi_preso == False:
        if cadeia[indice_da_cela+mudancas_de_cela] != "":
          None
        else:
          cadeia[indice_da_cela+mudancas_de_cela] = nome
          foi_preso = True
    if indice_da_cela+mudancas_de_cela+2 > quantidade_de_celas and foi_preso == False:
      foi_preso2 = False
      for mudancas_de_cela2 in range(len(cadeia)):
        if foi_preso2 == False:
          if cadeia[mudancas_de_cela2] != "":
            None
          else:
            cadeia[mudancas_de_cela2] = nome
            foi_preso2 = True
  
      if foi_preso2 == False and mudancas_de_cela2+1 == quantidade_de_celas:
        print("CHEIO")

def remover(nome):
  global cadeia
  if nome in cadeia:
    indice_removido = cadeia.index(nome)
    cadeia[indice_removido] = ""
  else: 
    print("NAO EXISTE")


quantidade_de_celas = 0
quantidades = input()
quantidades_separadas = quantidades.split()
quantidade_de_celas = int(quantidades_separadas[0])
quantidade_de_ordens = int(quantidades_separadas[1])

cadeia = [""] * quantidade_de_celas

for ordens in range(quantidade_de_ordens):
  ordem_nome = input()
  ordem_nome_separados = ordem_nome.split()
  ordem = ordem_nome_separados[0]
  nome = ordem_nome_separados[1]
  
  indice_da_cela = int((classificar_cela(nome) % quantidade_de_celas))
  
  if ordem == "ADICIONAR":
    adicionar(nome)
    
  elif ordem == "REMOVER":
    remover(nome)

cadeia_temporaria2 = list()
quantidade_de_celas_temporaria = len(cadeia)
for celas_verificadas in range(quantidade_de_celas_temporaria):
  if cadeia[celas_verificadas] != "":
    cadeia_temporaria2.append(cadeia[celas_verificadas])
cadeia = cadeia_temporaria2
    

print(*cadeia)  