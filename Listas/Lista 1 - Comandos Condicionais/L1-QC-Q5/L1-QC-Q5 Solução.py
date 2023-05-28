selecao1 = str(input())
selecao2 = str(input())
g = ("Gol")
gt1 = 0
gt2 = 0
cc1 = 0
cc2 = 0
c1t1 = input()
cc1 = (cc1 + 1)
if c1t1 == g:
    gt1 = (gt1 + 1)
c1t2 = input()
cc2 = (cc2 + 1)
if c1t2 == g:
    gt2 = (gt2 + 1)
c2t1 = input()
cc1 = (cc1 + 1)
if c2t1 == g:
    gt1 = (gt1 + 1)
c2t2 = input()
cc2 = (cc2 + 1)
if c2t2 == g:
    gt2 = (gt2 + 1)
c3t1 = input()
cc1 = (cc1 + 1)
if c3t1 == g:
    gt1 = (gt1 + 1)
c3t2 = input()
cc2 = (cc2 + 1)
if c3t2 == g:
    gt2 = (gt2 + 1)
if (5 - cc2 + gt2) < gt1:
    print(f"{selecao1} vence a disputa de pênaltis por {gt1} a {gt2} e avança de fase!")
elif (5 - cc1 + gt1) < gt2:
    print(f"{selecao2} vence a disputa de pênaltis por {gt2} a {gt1} e avança de fase!")
else:
  c4t1 = input()
  cc1 = (cc1 + 1)
  if c4t1 == g:
      gt1 = (gt1 + 1)
  if (5 - cc2 + gt2) < gt1:
      print(f"{selecao1} vence a disputa de pênaltis por {gt1} a {gt2} e avança de fase!")
  elif (5 - cc1 + gt1) < gt2:
      print(f"{selecao2} vence a disputa de pênaltis por {gt2} a {gt1} e avança de fase!")
  else:
    c4t2 = input()
    cc2 = (cc2 + 1)
    if c4t2 == g:
        gt2 = (gt2 + 1)
    if (5 - cc2 + gt2) < gt1:
        print(f"{selecao1} vence a disputa de pênaltis por {gt1} a {gt2} e avança de fase!")
    elif (5 - cc1 + gt1) < gt2:
        print(f"{selecao2} vence a disputa de pênaltis por {gt2} a {gt1} e avança de fase!")
    else:
      c5t1 = input()
      cc1 = (cc1 + 1)
      if c5t1 == g:
          gt1 = (gt1 + 1)
      if (5 - cc2 + gt2) < gt1:
          print(f"{selecao1} vence a disputa de pênaltis por {gt1} a {gt2} e avança de fase!")
      elif (5 - cc1 + gt1) < gt2:
          print(f"{selecao2} vence a disputa de pênaltis por {gt2} a {gt1} e avança de fase!")
      else:
        c5t2 = input()
        cc2 = (cc2 + 1)
        if c5t2 == g:
            gt2 = (gt2 + 1)
        if (5 - cc2 + gt2) < gt1:
            print(f"{selecao1} vence a disputa de pênaltis por {gt1} a {gt2} e avança de fase!")
        elif (5 - cc1 + gt1) < gt2:
            print(f"{selecao2} vence a disputa de pênaltis por {gt2} a {gt1} e avança de fase!")
        elif gt1 == gt2:
            print(f"Ambas as seleções terminaram com {gt1} gols, mas o desempate vai ficar para outro dia.")
        
        
        
        
