inscricoes = int(input())
infos = list()
alfabeto_M = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for contador in range(inscricoes):
  info_atual = input()
  
  info_atual = info_atual.replace("/"," ")
  
  info_atual = info_atual.split()
  
  animal_dicionario = dict()
  animal_dicionario = {"Nome": info_atual[0], "Espécie": info_atual[1], "Mês_Anv": info_atual[3]}
  
  infos.append(animal_dicionario)


mes = input()
if len(mes) == 1:
  mes = "0"+mes

exibicao = list()
primeira_vez = True
for info in infos:
  if info["Mês_Anv"] == mes:
    
    if primeira_vez == True:
      primeira_vez = False
      print("E os donos da festa do mes sao:")
      
    exibicao.append(info["Nome"]+" - "+info["Espécie"])
    
exibicao.sort()
for resultado in exibicao:
  print(resultado)
  


    
if primeira_vez == True:
  print("Sem festa esse mes. :(")
