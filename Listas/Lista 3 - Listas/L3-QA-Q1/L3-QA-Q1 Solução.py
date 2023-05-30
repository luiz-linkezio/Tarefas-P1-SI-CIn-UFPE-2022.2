lista_de_criminosos = list()
situação_criminosidade = ""
while situação_criminosidade != "ja temos nossa lista de suspeitos":
  situação_criminosidade = str(input())
  if situação_criminosidade == "novo suspeito - altissima periculosidade":
    criminoso = str(input())
    lista_de_criminosos.insert(0,criminoso)
  elif situação_criminosidade == "novo suspeito - pouco perigoso":
    criminoso = str(input())
    lista_de_criminosos.append(criminoso)
  elif situação_criminosidade == "livre de suspeita, pode remover":
    inocente = str(input())
    lista_de_criminosos.remove(inocente)
  elif situação_criminosidade == "sujeito mais perigoso do que pensavamos":
    indice_atual_criminoso = int(input())
    indice_novo_criminoso = int(input())
    lista_de_criminosos[indice_atual_criminoso], lista_de_criminosos[indice_novo_criminoso] = lista_de_criminosos[indice_novo_criminoso], lista_de_criminosos[indice_atual_criminoso]
  elif situação_criminosidade == "que estranho, esses dois meliantes… troque-os de lugar":
    criminoso = str(input())
    criminoso2 = str(input())
    indice_criminoso = lista_de_criminosos.index(criminoso)
    indice_criminoso2 = lista_de_criminosos.index(criminoso2)
    lista_de_criminosos[indice_criminoso], lista_de_criminosos[indice_criminoso2] = lista_de_criminosos[indice_criminoso2], lista_de_criminosos[indice_criminoso]
  elif situação_criminosidade == "essa posicao nao esta de acordo, ele nao e tao perigoso assim":
    criminoso = str(input())
    lista_de_criminosos.remove(criminoso)
    lista_de_criminosos.append(criminoso)
  elif situação_criminosidade == "como a lista esta ficando?":
    len_lista_de_criminosos = len(lista_de_criminosos)
    for n in range(len_lista_de_criminosos):
      if n < len_lista_de_criminosos-1:
        print(lista_de_criminosos[n],end=" ")
      if n == len_lista_de_criminosos-1:
        print(lista_de_criminosos[n])
        break

print(f"O resultado final ficou assim:")
len_lista_de_criminosos = len(lista_de_criminosos)
for n in range(len_lista_de_criminosos):
    if n < len_lista_de_criminosos-1:
      print(lista_de_criminosos[n],end=" ")
    if n == len_lista_de_criminosos-1:
      print(lista_de_criminosos[n])



