nulu=int(input())
ml=("")
mlno=0
pl=("")
plno=999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
empatenomes=("")
empatou=0
mq=0
for x in range(nulu):
  nomelu=str(input())
  nota=0
  snota=0
  while nota>=0:
    nota=int(input())
    if nota>=0:
      snota=snota+nota
  if snota>mlno:
    mq=1
    mlno=snota
    ml=nomelu
    empatou=0
  elif snota==mlno:
    empatou=1
    mlno=snota
    if mq==1:
      empatenomes=(ml)
      mq=2
    empatenomes=(f"{empatenomes}, {nomelu}")
  elif snota<mlno and snota<plno:
    plno=snota
    pl=nomelu
  if plno == 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
    plno = mlno
if empatou==1:
  print(f"{empatenomes}")
  print("Tantas opções")
else:
  print(f"{ml} ganhou de lavada de {pl}, com {mlno} vs {plno}")