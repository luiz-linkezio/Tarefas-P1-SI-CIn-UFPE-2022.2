carteira=0
protsol=0
clima=0
x=0
while x!=("ir para a praia"):
  x=input()
  if x==("separar dinheiro"):
    x=float(input())
    carteira=(carteira+x)
  elif x==("passar protetor"):
    protsol=1
  elif x==("choveu"):
    clima=1
  elif x==("parou de chover"):
    clima=0
if clima==1:
  print("Hoje não vai dar pra ir, chuvinha barrou")
elif clima==0:
  print("Hoje tem sol e mar!")
  if carteira<10 and protsol==0:
    print("Você não chegou muito bem, chame um médico!")
  elif carteira>=10 and protsol==0:
    print("O novo camarão do CIn foi criado")
  elif carteira<10 and protsol==1:
    print("Só faltou uma aguinha de coco...")
  elif carteira>=10 and protsol==1:
    print("Aí sim! Hoje rendeu!")