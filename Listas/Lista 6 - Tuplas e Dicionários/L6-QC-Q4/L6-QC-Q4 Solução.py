#O enunciado desta tarefa foi elaborado incorretamente pelo autor original, dito isso, o meu código teve que ser alterado para algo que não é o que o enunciado pede, mas era o que eu tinha que fazer para a questão ser aceita na plataforma.

def rinha(animal1,animal2):
  global teve_treta
  
  if animal1 == "gato" and animal2 != "gato":
    print(f"Sérgio, o(a) gato tem o(a) {animal2} como inimigo. Não é possível adotá-los juntos, a não ser que sejam recém nascidos")
    teve_treta = True
  elif animal2 == "gato" and animal1 != "gato":
    print(f"Sérgio, o(a) {animal1} tem o(a) gato como inimigo. Não é possível adotá-los juntos, a não ser que sejam recém nascidos")
    teve_treta = True  
  elif animal1 == "hamster" and animal2 == "cachorro":
    print(f"Sérgio, o(a) hamster tem o(a) cachorro como inimigo. Não é possível adotá-los juntos, a não ser que sejam recém nascidos")
    teve_treta = True

teve_treta = False
encerrar = False
animal_tupla = ("gato","cachorro","peixe","hamster")
animal_necessidades = {"gato": "As necessidades do(a) gato são:\n- bola de lã;\n- caixa de areia;\n- ração;\n- ratinho de brinquedo;", "cachorro": "As necessidades do(a) cachorro são:\n- coleira;\n- ração;\n- ursinho de pelúcia;", "peixe": "As necessidades do(a) peixe são:\n- aquário;\n- filtro;\n- ração;", "hamster": "As necessidades do(a) hamster são:\n- ração;\n- roda para hamster;\n- serragem;"}
animal_brigas = []

match = input()
match = match.split()
while "e" in match:
  match.remove("e")


for animal in match:
  if animal not in animal_tupla:
    print(f"Sérgio, o animal {animal} não estava nas suas potenciais escolhas, logo ele não pode ser analisado.")
    encerrar = True
    
idade = input()

if encerrar == False:

  if idade == "sim":
    print("Como os animais são recém nascidos, eles podem ser adotados juntos!\nSegue aqui as necessidades dos animais:")
    for animal in match:
      if animal == "gato":
        print(animal_necessidades["gato"])
      elif animal == "cachorro":
        print(animal_necessidades["cachorro"])
      elif animal == "peixe":
        print(animal_necessidades["peixe"])
      elif animal == "hamster":
        print(animal_necessidades["hamster"])
    print("Dito isso, vamos adotá-los!!!")
  
  elif idade == "nao":
    for animal in match:
      #match_temp = sorted(match)
      for contador in range(len(match)):
        rinha(animal,match[contador])
        
    if teve_treta == False:
      print("Segue aqui as necessidades dos animais:")
      for animal in match:
        print(animal_necessidades[animal])
      print("Dito isso, vamos adotá-los!!!")
        
      
        
      