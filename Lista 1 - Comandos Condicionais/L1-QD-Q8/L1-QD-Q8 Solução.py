jog1 = str(input())
ga1 = int(input())
f1 = int(input())
g1 = int(input())
jog2 = str(input())
ga2 = int(input())
f2 = int(input())
g2 = int(input())
jog3 = str(input())
ga3 = int(input())
f3 = int(input())
g3 = int(input())
ap1 = g1/f1
ap2 = g2/f2
ap3 = g3/f3
gaescolhido = 0
escolhido = 0
if ga1 == ga2 and ga1 > ga3:
  print("Tite está mais indeciso do que nunca!")
  if ap1 > ap2:
    print(jog1)
    print(jog2)
    escolhido = jog1
    gaescolhido = ga1
  elif ap2 > ap1:
    print(jog2)
    print(jog1)
    escolhido = jog2
    gaescolhido = ga2
  print(jog3)
elif ga1 == ga3 and ga1 > ga2:
  print("Tite está mais indeciso do que nunca!")
  if ap1 > ap3:
    print(jog1)
    print(jog3)
    escolhido = jog1
    gaescolhido = ga1
  elif ap3 > ap1:
    print(jog3)
    print(jog1)
    escolhido = jog3
    gaescolhido = ga3
  print(jog2)
elif ga2 == ga3 and ga2 > ga1:
  print("Tite está mais indeciso do que nunca!")
  if ap2 > ap3:
    print(jog2)
    print(jog3)
    escolhido = jog2
    gaescolhido = ga2
  elif ap3 > ap2:
    print(jog3)
    print(jog2)
    escolhido = jog3
    gaescolhido = ga3
  print(jog1)
elif ga1 > ga2 and ga1 > ga3:
  escolhido = jog1
  gaescolhido = ga1
  print(jog1)
  if ga2 > ga3:
    print(jog2)
    print(jog3)
  elif ga3 > ga2:
    print(jog3)
    print(jog2)
  elif ga3 == ga2:
    if ap3 > ap2:
      print(jog3)
      print(jog2)
    elif ap2 > ap3:
      print(jog2)
      print(jog3)  
elif ga2 > ga1 and ga2 > ga3:
  print(jog2)
  escolhido = jog2
  gaescolhido = ga2
  if ga1 > ga3:
    print(jog1)
    print(jog3)
  elif ga3 > ga1:
    print(jog3)
    print(jog1)
  elif ga1 == ga3:
    if ap1 > ap3:
      print(jog1)
      print(jog3)
    elif ap3 > ap1:
      print(jog3)
      print(jog1)
elif ga3 > ga1 and ga3 > ga2:
  print(jog3)
  escolhido = jog3
  gaescolhido = ga3
  if ga1 > ga2:
    print(jog1)
    print(jog2)
  elif ga2 > ga1:
    print(jog2)
    print(jog1)
  elif ga1 == ga2:
    if ap1 > ap2:
      print(jog1)
      print(jog2)
    elif ap2 > ap1:
      print(jog2)
      print(jog1)
elif ga1 == ga2 and ga2 == ga3:
  print("Tite está mais indeciso do que nunca!")
  if ap1 > ap2 and ap1 > ap3:
    if ap2 > ap3:
      print(jog1)
      print(jog2)
      print(jog3)
      escolhido = jog1
      gaescolhido = ga1
    elif ap3 > ap2:
      print(jog1)
      print(jog3)
      print(jog2)
      escolhido = jog1
      gaescolhido = ga1
  elif ap2 > ap1 and ap2 > ap3:
    if ap1 > ap3:
      print(jog2)
      print(jog1)
      print(jog3)
      escolhido = jog2
      gaescolhido = ga2
    elif ap3 > ap1:
      print(jog2)
      print(jog3)
      print(jog1)
      escolhido = jog2
      gaescolhido = ga2
  if ap3 > ap2 and ap3 > ap1:
    if ap2 > ap1:
      print(jog3)
      print(jog2)
      print(jog1)
      escolhido = jog3
      gaescolhido = ga3
    elif ap1 > ap2:
      print(jog3)
      print(jog1)
      print(jog2)
      escolhido = jog3
      gaescolhido = ga3
print("Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…")
if gaescolhido <= 10:
    print(f"{escolhido}?! Sei não hein Galvão…")
elif gaescolhido > 10:
    print(f"{escolhido}! Dessa vez o hexa vem pra casa!!")