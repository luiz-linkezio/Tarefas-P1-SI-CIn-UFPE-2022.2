x = str(input())
c = 1
while x != ("Por hoje já deu") and x != ("O relógio descarregou!"):
  x = str(input())
  c = (1+c)
c = (c-1)
if x == ("Por hoje já deu"):
  print(f"Muito Ben Ben! hehe você derrotou {c} aliens hoje")
elif x == ("O relógio descarregou!"):
  print(f"Corra Ben! Você já derrotou {c} aliens")