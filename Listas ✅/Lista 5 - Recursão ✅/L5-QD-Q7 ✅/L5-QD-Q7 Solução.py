def mapeamento(linhas_colunas):
  global lista
  
  if linhas_colunas > 0:
    
    linha = list(input())
    while " " in linha:
      linha.remove(" ")
  
    lista.append(linha)  
    mapeamento(linhas_colunas-1) #RECURSÃO

def minusculo_string(string):
  nova_string = string[0] 
  for letra in string[1:]:
    nova_string += letra.lower()
  return nova_string
  
def encontrar_primeira_letra(nome_vilao, len_nome_vilao, indices_iniciais):
  
  for linha in lista:
    for i in range(linhas_colunas):
      if linha[i] == nome_vilao[0]:
        indices_iniciais.append([lista.index(linha), i])
  return indices_iniciais



def encontrar_vilao(nome_vilao, indices, contador):
  global encontrou
  
  if contador < len(nome_vilao):
  
    #esquerda superior
    if indices[0]-1 != linhas_colunas and indices[1]-1 != linhas_colunas:
      if lista[indices[0]-1][indices[1]-1] == nome_vilao[contador]:
        indices_temp = [indices[0]-1,indices[1]-1]
      
        encontrar_vilao(nome_vilao, indices_temp, contador+1)
      
    #cima
    if indices[0]-1 != -1: 
      if lista[indices[0]-1][indices[1]] == nome_vilao[contador]:
        indices_temp = [indices[0]-1,indices[1]]
      
        encontrar_vilao(nome_vilao, indices_temp, contador+1)
    
    #direita superior
    if indices[0]-1 != -1 and indices[1]+1 != linhas_colunas:
      if lista[indices[0]-1][indices[1]+1] == nome_vilao[contador]:
        indices_temp = [indices[0]-1,indices[1]+1]
      
        encontrar_vilao(nome_vilao, indices_temp, contador+1)
     
    #esquerda
    if indices[1]-1 != -1:
      if lista[indices[0]][indices[1]-1] == nome_vilao[contador]:
        indices_temp = [indices[0],indices[1]-1]
        
        encontrar_vilao(nome_vilao, indices_temp, contador+1)
      
    #direita
    if indices[1]+1 != linhas_colunas:
      if lista[indices[0]][indices[1]+1] == nome_vilao[contador]:
        indices_temp = [indices[0],indices[1]+1]
      
        encontrar_vilao(nome_vilao, indices_temp, contador+1)
      
    #esquerda inferior
    if indices[0]+1 != linhas_colunas and indices[1]-1 != -1:
      if lista[indices[0]+1][indices[1]-1] == nome_vilao[contador]:
        indices_temp = [indices[0]+1,indices[1]-1]
        
        encontrar_vilao(nome_vilao, indices_temp, contador+1)
      
    #baixo
    if indices[0]+1 != linhas_colunas:
      if lista[indices[0]+1][indices[1]] == nome_vilao[contador]:
        indices_temp = [indices[0]+1,indices[1]]
      
        encontrar_vilao(nome_vilao, indices_temp, contador+1)
      
    #direita inferior
    if indices[0]+1 != linhas_colunas and indices[1]+1 != linhas_colunas:
      if lista[indices[0]+1][indices[1]+1] == nome_vilao[contador]:
        indices_temp = [indices[0]+1,indices[1]+1]
      
        encontrar_vilao(nome_vilao, indices_temp, contador+1)
  
  else:
    if encontrou == False:
      encontrou = True
      if nome_vilao == "CHARADA":
        print("Isso!!! Encontramos uma pista, mas somente o Charada está envolvido.")
      else:
        if nome_vilao == "DUASCARAS":
          print(f"Isso!!! Encontramos uma pista, Duas Caras está junto com o Charada.")
        elif nome_vilao == "REIDOSCONDIMENTOS":
          print(f"Isso!!! Encontramos uma pista, Rei dos Condimentos está junto com o Charada.")
        else:
          print(f"Isso!!! Encontramos uma pista, {minusculo_string(nome_vilao)} está junto com o Charada.")

lista_de_viloes = ["CHARADA","PINGUIM","ARLEQUINA","JOKER","ESPANTALHO","DUASCARAS", "REIDOSCONDIMENTOS"]
encontrou = False    
lista = list()
linhas_colunas = int(input())
mapeamento(linhas_colunas)

for vilao in lista_de_viloes:
  for par_ordenado in encontrar_primeira_letra(vilao, len(vilao), []):
    encontrar_vilao(vilao, par_ordenado, 1)
    
if encontrou == False:
  print("Poxa... acho que seguimos uma pista falsa.")
  