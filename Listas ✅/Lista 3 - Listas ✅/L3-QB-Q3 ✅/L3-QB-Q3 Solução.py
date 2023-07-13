lista_de_diarios = list()
lista_de_numero_dos_diarios = list()

numero_de_diarios = int(input())
for contador_diarios in range(numero_de_diarios):
  diario = str(input())
  len_diario = int(len(diario))
  lista_de_numero_dos_diarios.append(diario[len_diario-1])
  lista_de_diarios.append(diario[0:(len_diario-3)])
  
numero_de_buscas = int(input())
for contador_de_buscas in range(numero_de_buscas):
  diario = str(input())
  if diario in lista_de_diarios:
    indice_diario = lista_de_diarios.index(diario)
    numero_do_diario = lista_de_numero_dos_diarios[indice_diario]
    print(f"Informacoes sobre {diario} estao no Diario {lista_de_numero_dos_diarios[indice_diario]}")
  else:
    print(f"Nenhum dos diarios possui informacoes sobre {diario}")
  