def somar_numeros(chat_comprimido_len):
  soma = 0
  lista_de_algarismos = ["0","1","2","3","4","5","6","7","8","9"]
  for contador_chat_comprimido_len in range(int(chat_comprimido_len)):
    if chat_comprimido[contador_chat_comprimido_len] in lista_de_algarismos:
      soma += int(chat_comprimido[contador_chat_comprimido_len])
    
  return soma
  
def resposta_GPT(soma_total):
  global chat_comprimido
  
  if 0 < soma_total and soma_total <= 5:
    print("ChatGPT:1t3a1 1f1a1c3i1n1h1o1 1n3e")
    chat_comprimido = "1t3a1 1f1a1c3i1n1h1o1 1n3e"
  elif 6 < soma_total and soma_total <= 20:
    print("ChatGPT:1c2o2m2p2r3e1 1u3m1 1t2e1c1l1a1d1o1 1n4o1v1o")
    chat_comprimido = "1c2o2m2p2r3e1 1u3m1 1t2e1c1l1a1d1o1 1n4o1v1o"
  elif 21 < soma_total and soma_total <= 30:
    print("ChatGPT:1s6o1 1n1a1 1v1i1d2a1 1m4a1n1s3a")
    chat_comprimido = "1s6o1 1n1a1 1v1i1d2a1 1m4a1n1s3a"
  elif 31 < soma_total and soma_total <= 40:
    print("ChatGPT:1v5a1 1e2s1t4u3d3a3r1 1r1a1p3a3z")
    chat_comprimido = "1v5a1 1e2s1t4u3d3a3r1 1r1a1p3a3z"
  elif 40 < soma_total:
    print("ChatGPT:3e1s1t5u1d1a1 1n2a1o1 1p1r3a1 1t2u1 1v4e1r")
    chat_comprimido = "3e1s1t5u1d1a1 1n2a1o1 1p1r3a1 1t2u1 1v4e1r"

def comprimir(chat_len=None, contador=None, caractere_atual=None, contador_repeticoes=None, indice_string_repeticao=None):
  global chat_comprimido
  
  if contador < chat_len:
    contador += 1
    if caractere_atual == chat[contador-1] and contador < chat_len:
      contador_repeticoes += 1
      comprimir(chat_len, contador, chat[contador-1], contador_repeticoes, indice_string_repeticao) # AQUI MADU
    else:
      if contador == chat_len:
        if chat[chat_len-1] != chat[chat_len-2]:
          indice_string_repeticao += f"{contador_repeticoes}{chat[contador-2]}"
          indice_string_repeticao += f"{1}{chat[chat_len-1]}"
        else:  
          indice_string_repeticao += f"{contador_repeticoes+1}{chat[contador-2]}"
      else:  
        indice_string_repeticao += f"{contador_repeticoes}{chat[contador-2]}"
        
      contador_repeticoes = 1
      comprimir(chat_len, contador, chat[contador-1], contador_repeticoes, indice_string_repeticao) #AQUI TAMBÉM
  
  elif contador >= chat_len:
      chat_comprimido = indice_string_repeticao
      print(f"usuário:{indice_string_repeticao}")
  
  

def descomprimir(chat_comprimido2="", chat_comprimido_len2=None, contador3=0, chat_descomprimido_def2=None, contador4=0):
  global chat_descomprimido
  
  if contador4 < chat_comprimido_len2:
    multiplicador_int = int(chat_comprimido2[contador3])
    chat_descomprimido_def2 += multiplicador_int*chat_comprimido2[contador3+1]
    contador3 += 2
    contador4 += 1
    descomprimir(chat_comprimido2, chat_comprimido_len2, contador3, chat_descomprimido_def2, contador4)
  else:
    chat_descomprimido = chat_descomprimido_def2
    print(f"Descobri! É: {chat_descomprimido}, tá de brincadeira né?")

existe_resposta = False

whileon = True
while whileon == True:

  ordem = input()
  
  chat = ""
  if ordem == "Vou pedir ajuda pro meu amigo ChatGPT":
    
    while chat != "Não tô entendendo nada":
    
      chat = input()
      
      if chat != "Não tô entendendo nada":
        
        chat_len = len(chat)
        
        comprimir(chat_len,0,chat[0],0,"")
        
        chat_comprimido_len = len(chat_comprimido)
        resposta_GPT(somar_numeros(chat_comprimido_len))
        
        existe_resposta = True
  
  elif ordem == "Qual era a tradução?":
    if existe_resposta == True:
      chat_comprimido_len = (len(chat_comprimido)/2)
      descomprimir(chat_comprimido, chat_comprimido_len, 0, "", 0)
    else:
      print("Não tem nada pra traduzir")
      
      
  else:
    whileon = False
    