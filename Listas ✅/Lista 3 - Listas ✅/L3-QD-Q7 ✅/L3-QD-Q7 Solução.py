alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
algarismos = ["0","1","2","3","4","5","6","7","8","9"]
mensagem_final = 0
numero_de_palavras = int(input())
espaco = input()

for decodificacoes in range(numero_de_palavras):
  palavra_decodificadora = str(input())
  espaco = input()
  palavra_codificada = str(input())
  palavra_codificada = palavra_codificada.replace(" ","")
  len_palavra_codificada = len(palavra_codificada)
  palavra_codificada_lista = list()
  for contador_len in range(len_palavra_codificada):
    palavra_codificada_lista.append(palavra_codificada[contador_len])
  
  letras_portal = ""
  soma_experimento = 0
  soma_realidade = 0
  multiplicacao_schembulock = 1
  if palavra_decodificadora == "Portal":
    len_palavra_codificada_lista = len(palavra_codificada_lista)
    for contador_len_portal in range(len_palavra_codificada_lista):
      elemento_portal = palavra_codificada_lista[contador_len_portal]
      if elemento_portal in alfabeto:
        indice_alfabeto = alfabeto.index(elemento_portal)
        if indice_alfabeto == 25:
          letras_portal += alfabeto[0]
        else:
          letras_portal += alfabeto[indice_alfabeto+1]
        if mensagem_final == 0:
          print("Consegui! A mensagem decodificada de Bill Cipher é: ", end="")
          mensagem_final = 1
    if decodificacoes == (numero_de_palavras-1) and (mensagem_final == 1) and (letras_portal != ""):
      print(letras_portal)
    elif decodificacoes < (numero_de_palavras-1) and (mensagem_final == 1) and (letras_portal != ""):  
      print(letras_portal, end=" ")

  elif palavra_decodificadora == "Experimento":
    len_palavra_codificada_lista = len(palavra_codificada_lista)
    for contador_len_experimento in range(len_palavra_codificada_lista):
      elemento_experimento = palavra_codificada_lista[contador_len_experimento]
      if elemento_experimento in algarismos:
        elemento_experimento = int(elemento_experimento)
        if (elemento_experimento%2) == 0:
          soma_experimento = soma_experimento+elemento_experimento
          if mensagem_final == 0:
            print("Consegui! A mensagem decodificada de Bill Cipher é: ", end="")
            mensagem_final = 1
    if decodificacoes == (numero_de_palavras-1) and (mensagem_final == 1) and (soma_experimento != 0):
      print(soma_experimento)
    elif decodificacoes < (numero_de_palavras-1) and (mensagem_final == 1) and (soma_experimento != 0):        
      print(soma_experimento, end=" ")
          
  elif palavra_decodificadora == "Realidade":
    len_palavra_codificada_lista = len(palavra_codificada_lista)
    for contador_len_schembulock in range(len_palavra_codificada_lista):
      elemento_realidade = palavra_codificada_lista[contador_len_schembulock]
      if elemento_realidade in algarismos:
        elemento_realidade = int(elemento_realidade)
        if (elemento_realidade%2) > 0:
          soma_realidade = soma_realidade+elemento_realidade
          if mensagem_final == 0:
            print("Consegui! A mensagem decodificada de Bill Cipher é: ", end="")
            mensagem_final = 1
    if decodificacoes == (numero_de_palavras-1) and (mensagem_final == 1) and (soma_realidade != 0):
      print(soma_realidade)
    elif decodificacoes < (numero_de_palavras-1) and (mensagem_final == 1) and (soma_realidade != 0):        
      print(soma_realidade, end=" ")
          
  elif palavra_decodificadora == "Schembulock":
    len_palavra_codificada_lista = len(palavra_codificada_lista)
    for contador_len_schembulock in range(len_palavra_codificada_lista):
      elemento_schembulock = palavra_codificada_lista[contador_len_schembulock]
      if elemento_schembulock in algarismos:
        elemento_schembulock = int(elemento_schembulock)
        multiplicacao_schembulock = multiplicacao_schembulock*elemento_schembulock
        if mensagem_final == 0:
            print("Consegui! A mensagem decodificada de Bill Cipher é: ", end="")
            mensagem_final = 1
    if decodificacoes == (numero_de_palavras-1) and (mensagem_final == 1) and (multiplicacao_schembulock != 1):
      print(multiplicacao_schembulock)
    elif decodificacoes < (numero_de_palavras-1) and (mensagem_final == 1) and (multiplicacao_schembulock != 1):        
      print(multiplicacao_schembulock, end=" ")
  
  if decodificacoes < (numero_de_palavras-1):
    espaco = input()
    
if mensagem_final == 0:
  print("Esse formato de mensagem nem Bill Cipher entenderia!")