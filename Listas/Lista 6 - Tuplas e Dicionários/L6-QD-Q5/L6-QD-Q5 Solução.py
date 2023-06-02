#O enunciado desta tarefa foi feito de forma incorreta e ruim pelo autor original, tentei modificar o enunciado para a melhor compreensão do leitor, porém, ainda há chances de estar incorreto, não sei se consegui consertar tudo. Além disso, talvez meu código fique difícil de compreender, pois tive que ir alterando algumas coisas até adivinhar os erros do autor do enunciado para que meu código fosse aceito pela plataforma como resposta correta

def vaquinha(energia, atividade_vezes, energia_gasta, energia_primaria):
  energia_inicial = energia
  
  energia = energia - int(atividade_vezes)
  
  energia_gasta = min((energia_gasta + energia_inicial - energia), (energia_gasta + energia_inicial))
  
  print("Brinquedo da vaquinha! Vou chacoalhar")
  return energia, energia_gasta

def chupeta(energia, atividade_vezes, energia_gasta, energia_primaria):
  energia_inicial = energia
  
  energia = min(max((energia-5), (int(atividade_vezes))), energia_primaria)
  
  energia_gasta = energia_gasta + energia_inicial - energia
  
  print("Minha pipeta! Vou morder")
  return energia, energia_gasta

def zegotinha(energia, atividade_vezes, energia_gasta, energia_primaria):
  energia_inicial = energia
  
  atividade_vezes = max(int(atividade_vezes), 1)
  energia = int(energia/int(atividade_vezes))
  
  energia_gasta = energia_gasta + energia_inicial - energia
  
  print("Meu preferido! Faz barulho e mordo")
  return energia, energia_gasta
  
def bolinha(energia, atividade_vezes, energia_gasta, energia_primaria):
  energia_inicial = energia
  
  energia -= int(int(atividade_vezes)/4)
  
  energia_gasta = min((energia_gasta + energia_inicial - energia), (energia_gasta + energia_inicial))
  
  print("ZOOOOOOOOOOOOOOOOOM")
  return energia, energia_gasta
  
def osso(energia, atividade_vezes, energia_gasta, energia_primaria):
  
  energia += (int(atividade_vezes)*2)
  
  print("Pausa para roer")
  return energia, energia_gasta
 
def comida(energia, atividade_vezes, energia_gasta, energia_primaria):
  
  energia_inicial = energia
  
  energia_comida = (-len(atividade_vezes))
  for letra in atividade_vezes:
    energia_comida = (energia_comida*(-len(atividade_vezes))) / len(atividade_vezes)
    
  energia =   energia + energia_comida*(-1)
  
  energia_gasta = min((energia_gasta + max((energia_inicial - energia),0)), (energia_gasta + energia_inicial))
  
  print(f"Uhh, {atividade_vezes} deve ser comestível")
  return energia, energia_gasta
  
energia = int(input())
energia_primaria = energia
energia_gasta = 0


while energia > 0 and energia_gasta <= 100:
  atividade = input()
  atividade = atividade.split(":")
  atividade_nome = atividade[0]
  atividade_vezes = atividade[1].split(' ', 1)
  atividade_vezes = ''.join(atividade_vezes)
  
  atividades_dict = {"Vaquinha": vaquinha, "Chupeta": chupeta, "Zé Gotinha": zegotinha, "Bolinha": bolinha, "Osso": osso, "Comida": comida}
  energia, energia_gasta = atividades_dict[atividade_nome](int(energia), atividade_vezes, int(energia_gasta), energia_primaria)

  energia = min(energia, energia_primaria)

energia_gasta = min(energia_gasta, 100)  
energia_gasta_decimal = max((int(energia_gasta/10)),1)
  
print(f"Mamãe chegou! Gastei {int(energia_gasta)} pontos da minha energia e estou c{'a' * energia_gasta_decimal}nsada, mas vou correr para seus braços!")