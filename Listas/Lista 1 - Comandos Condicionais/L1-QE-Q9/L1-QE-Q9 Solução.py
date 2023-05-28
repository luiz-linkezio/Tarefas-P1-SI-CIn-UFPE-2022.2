favbr = float(input())
adv = input()
favadv = float(input())
golsbr = int(input())
golsadv = int(input())
if golsadv > golsbr:
  print(f"Infelizmente essa seleção dx {adv} era muito forte para o Brasil.")
elif golsadv == golsbr and favadv > favbr:
  print("Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...")
else:
  if golsadv == golsbr:
    print("No sufoco, o Brasil conseguiu ganhar!!!")
  elif golsadv < golsbr:
    difgols = golsbr-golsadv
    if difgols < 3:
      favbr = (favbr + (difgols*10))
    elif difgols >= 3:
      favbr = (favbr + 30)
    print("Quem é que segura o Brasil???")
  adv = input()
  favadv = float(input())
  golsbr = int(input())
  golsadv = int(input())
  if golsadv > golsbr:
    print(f"Infelizmente essa seleção dx {adv} era muito forte para o Brasil.")
  elif golsadv == golsbr and favadv > favbr:
    print("Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...")
  else:
    if golsadv == golsbr:
      print("No sufoco, o Brasil conseguiu ganhar!!!")
    elif golsadv < golsbr:
      difgols = golsbr-golsadv
      if difgols < 3:
        favbr = (favbr + (difgols*10))
      elif difgols >= 3:
        favbr = (favbr + 30)
      print("Quem é que segura o Brasil???")
    adv = input()
    favadv = float(input())
    golsbr = int(input())
    golsadv = int(input())
    if golsadv > golsbr:
      print(f"Infelizmente essa seleção dx {adv} era muito forte para o Brasil.")
    elif golsadv == golsbr and favadv > favbr:
      print("Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...")
    else:
      if golsadv == golsbr:
        print("No sufoco, o Brasil conseguiu ganhar!!!")
      elif golsadv < golsbr:
        difgols = golsbr-golsadv
        if difgols < 3:
          favbr = (favbr + (difgols*10))
        elif difgols >= 3:
          favbr = (favbr + 30)
        print("Quem é que segura o Brasil???")
      adv = input()
      favadv = float(input())
      if favadv > favbr:
        print(f"O nosso Brasil foi vice, não conseguindo bater a seleção dx {adv} na simulação")
      else:
        print("O BRASIL VAI SER HEXAAAAAAAA")