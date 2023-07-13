nome_do_inimigo = str(input())
nome_do_aliado = str(input())
clime_hoje = str(input())
primeira_vez_clima = 0
lista_total = list()
numeros = ""
quantidade_de_ataques = 0
clima_ruim = 0

if clime_hoje == "Ensolarado" or clime_hoje == "Nublado" or clime_hoje == "ChuvosoNormal" or clime_hoje == "ChuvosoComRaio":

  while numeros != "Cansado":
    numeros = str(input())
    
    if numeros != "Cansado":
      quantidade_de_ataques += 1
      numeros_split = numeros.split()
      len_numeros_split = len(numeros_split)
      
      if clime_hoje == "Ensolarado":
        for contador_len_ensolarado in range(len_numeros_split):
          for contador_len_ensolarado_2 in range(len_numeros_split):
            if int(numeros_split[contador_len_ensolarado]) < int(numeros_split[contador_len_ensolarado_2]):
              numeros_split[contador_len_ensolarado], numeros_split[contador_len_ensolarado_2] = numeros_split[contador_len_ensolarado_2], numeros_split[contador_len_ensolarado]
        lista_total.append(numeros_split[:])
        if primeira_vez_clima == 0:
          primeira_vez_clima = 1
          print(f"Caramba! Finalmente organizamos a mensagem secreta do {nome_do_inimigo} com esse clima Ensolarado! Vamos nessa {nome_do_aliado}!")
      
      elif clime_hoje == "Nublado":
        for contador_len_nublado in range(len_numeros_split):
          for contador_len_nublado_2 in range(len_numeros_split):
            if int(numeros_split[contador_len_nublado]) > int(numeros_split[contador_len_nublado_2]):
              numeros_split[contador_len_nublado], numeros_split[contador_len_nublado_2] = numeros_split[contador_len_nublado_2], numeros_split[contador_len_nublado]
        lista_total.append(numeros_split[:])
        if primeira_vez_clima == 0:
          primeira_vez_clima = 1
          print(f"Ufa! Mesmo com o clima Nublado ainda desvendamos a mensagem do {nome_do_inimigo}! Vamos nessa {nome_do_aliado}!")
        
      elif clime_hoje == "ChuvosoNormal":
        if primeira_vez_clima == 0:
          primeira_vez_clima = 1
          lista_anterior = list()
          print(f"Nem mesmo a chuva vai nos parar de salvar o mundo! Desvendamos a mensagem do {nome_do_inimigo}! Vamos nessa {nome_do_aliado}!")
        else:  
          for contador_chuvoso in range(len_numeros_split):
            if int(lista_anterior[contador_chuvoso]) < int(numeros_split[contador_chuvoso]):
              numeros_split[contador_chuvoso], lista_anterior[contador_chuvoso] = lista_anterior[contador_chuvoso], numeros_split[contador_chuvoso]
          lista_total.append(lista_anterior[:])  
          lista_anterior = list()    
        for contador_chuvoso_2 in range(len_numeros_split):
          lista_anterior.append(numeros_split[contador_chuvoso_2])
          
      elif clime_hoje == "ChuvosoComRaio":
        if primeira_vez_clima == 0:
          primeira_vez_clima = 1
          lista_anterior = list()
          print(f"Eitaa! Até mesmo essa chuva com trovoadas não nos parou. Estamos indo até você, {nome_do_inimigo}! Vamos nessa {nome_do_aliado}!")
        else:  
          for contador_raio in range(len_numeros_split):
            if int(lista_anterior[contador_raio]) > int(numeros_split[contador_raio]):
              numeros_split[contador_raio], lista_anterior[contador_raio] = lista_anterior[contador_raio], numeros_split[contador_raio]
          lista_total.append(lista_anterior[:])  
          lista_anterior = list()    
        for contador_raio_2 in range(len_numeros_split):
          lista_anterior.append(numeros_split[contador_raio_2])
  
  if clime_hoje == "ChuvosoNormal" or clime_hoje == "ChuvosoComRaio":
    lista_total.append(numeros_split[:])
  
  print(f"Agora decodificamos as {quantidade_de_ataques} mensagens do {nome_do_inimigo} e sabemos seus {quantidade_de_ataques} lugares de ataque.\nOs lugares sao:")
  
  for contador_de_ataques in range(quantidade_de_ataques):
    print(f"{contador_de_ataques+1} lugar:")
    
    primeira_vez_coordenadas = 0
    primeira_vez_horario = 0
    primeira_vez_data = 0
    
    if primeira_vez_coordenadas == 0:
      primeira_vez_coordenadas = 1
      print(f"Coordenadas: {lista_total[contador_de_ataques][0]}° {lista_total[contador_de_ataques][1]}' {lista_total[contador_de_ataques][2]}''")
    if primeira_vez_horario == 0:
      primeira_vez_horario = 1
      print(f"Horario: {lista_total[contador_de_ataques][3]}h {lista_total[contador_de_ataques][4]}m {lista_total[contador_de_ataques][5]}s")
    if primeira_vez_data == 0:
      primeira_vez_data = 1
      print(f"Data: {lista_total[contador_de_ataques][6]}/{lista_total[contador_de_ataques][7]}/{lista_total[contador_de_ataques][8]}")
      
  
  print(f"Vamos rapido {nome_do_aliado}!!")
  
else:
  print(f"Infelizmente esse clima não está bom. Não conseguimos decifrar a mensagem, o que será do mundo agora??\nTenho certeza que conseguiremos na próxima {nome_do_aliado}")
  