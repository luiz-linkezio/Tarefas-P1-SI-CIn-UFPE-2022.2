contador_vitorias = 0
contador_derrotas = 0
contador_empates = 0
viloes = ["Makima", "Reze", "Santa Claus"]
resultado_batalhas = list()

def definir_motosserra():
  global energia
  global controle
  global precisao
  energia = int(input())
  controle = int(input())
  precisao = int(input())
  
  if energia >= 750 and controle >= 7 and precisao >= 8:
    motosserra_definida = "Motosserra Suprema"
  
  elif energia >= 500 and controle >= 6 and precisao >= 6:
    motosserra_definida = "Motosserra Avançada"
    
  else:
    motosserra_definida = "Motosserra Normal"
    
  return motosserra_definida

def batalhar(vilao, rodada):
  
  motosserra = definir_motosserra()
  
  forca_vilao = int(input())
  
  print(f"### Rodada {rodada} - {vilao} ###")
  print(f"O Denji ira se transformar na {motosserra} para enfrentar o {vilao}")
  
  forca_denji = energia + controle * precisao
  
  if forca_denji > forca_vilao:
    print(f"Denji saiu vitorioso nessa batalha contra o {vilao}")
    global contador_vitorias
    contador_vitorias += 1
    resultado_batalha = "Vitoria"
  elif forca_denji < forca_vilao:
    print(f"Denji não conseguiu força o suficiente para derrotar o {vilao}")
    global contador_derrotas
    contador_derrotas += 1
    resultado_batalha = "Derrota"
  else: 
    print(f"Como pode ser possível?? Denji possui a mesma força que o {vilao}")
    global contador_empates
    contador_empates += 1
    resultado_batalha = "Empate"
    
  resultado_batalha_texto = (f"Rodada {(contador_de_batalhas+1)}: {motosserra} - {resultado_batalha}")  
  global resultado_batalhas
  resultado_batalhas.append(resultado_batalha_texto)

def resultado_final():
  print("### Resultado Final ###")
  print(f"{resultado_batalhas[0]}\n{resultado_batalhas[1]}\n{resultado_batalhas[2]}")
  
  if contador_vitorias == 3:
    print("Nenhum dos 3 inimigos foram capazes de derrotar o Denji!")
  
  elif contador_vitorias == 2:  
    print("Denji conseguiu derrotar a maioria de seus inimigos")
    
  elif contador_derrotas == 3:
    print("Hoje não foi um dia bom para o Denji, perdeu todas as batalhas")
    
  elif contador_derrotas == 2:
    print("Dia péssimo para o Denji, perdeu a maioria de suas batalhas")
    
  elif contador_empates >= 2:
    print("Dia duro para o Denji, empatou de mais")
  else:
    print("Hoje foi um dia equilibrado para o Denji, conseguiu ganhar, perder e empatar")
  
for contador_de_batalhas in range(3):
  batalhar(viloes[contador_de_batalhas], (contador_de_batalhas+1))
  
resultado_final()
  
  
  
  