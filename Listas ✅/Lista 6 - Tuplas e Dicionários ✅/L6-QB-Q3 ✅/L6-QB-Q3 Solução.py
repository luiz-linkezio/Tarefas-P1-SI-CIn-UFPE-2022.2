quantidade_de_pets = int(input())
lista_de_pets = list()


for contador in range(quantidade_de_pets):
  dicionario_animal = dict()
  
  animal = input()
  animal2 = animal
  
  animal = animal.replace(" ", "")
  animal = animal.replace(",", " ")
  animal = animal.split()
  
  animal_media = (float(animal[2])+float(animal[3])+float(animal[4]))/3
  animal_media = "{:.2f}".format(animal_media)
  
  animal.pop(2)
  animal.pop(2)
  animal.pop(2)
  
  animal.append(animal_media)
  
  animal2 = animal2.replace(" ","*")
  animal2 = animal2.replace(","," ")
  animal2 = animal2.split()
  animal_etnia = animal2[1]
  animal_etnia = animal_etnia.replace("*", " ")
  animal_nome = animal2[0]
  animal_nome = animal_nome.replace("*", " ")
  
  dicionario_animal = {"Nome": animal_nome, "Etnia": animal_etnia, "Média": animal[2]}
  lista_de_pets.append(dicionario_animal)


lista_de_aprovados = list()
lista_de_recuperacao = list()
lista_de_reprovados = list()
for dic in lista_de_pets:
  if float(dic["Média"]) >= 3:
    lista_de_aprovados.append(dic)
  elif 3 > float(dic["Média"]) >= 2:
    lista_de_recuperacao.append(dic)
  elif float(dic["Média"]) < 2:
    lista_de_reprovados.append(dic)

    
if len(lista_de_aprovados) > 0:
  print("Estao aprovados e de parabens os seguintes coleguinhas:")
  for bixo in lista_de_aprovados:
    print(bixo["Nome"],"-"+bixo["Etnia"],"-","media:",bixo["Média"])

if len(lista_de_reprovados) > 0:
  print("Os colegas a seguir nao se comportaram bem e precisam de ajuda profissional (entrar em contato urgente):")
  for bixo in lista_de_reprovados:
    print(bixo["Nome"],"-"+bixo["Etnia"],"-","media:",bixo["Média"])
  
if len(lista_de_recuperacao) > 0:
  print("Esses queridos terao uma nova chance e prometem melhorar:")
  for bixo in lista_de_recuperacao:
    print(bixo["Nome"],"-"+bixo["Etnia"],"-","media:",bixo["Média"])  