#O enunciado desta tarefa foi mal elaborado pelo autor original e contém ambiguidades. Tive que mudar meu código para lidar com essas ambiguidades, então talvez o meu código tenha algo que não faça muito sentido, mas foi necessário para minha resposta ser considerada correta na plataforma.

nome = "essa questão dá gatilho, chorei fazendo, me dá 10"
contador_deu_bom = 0
contador_deu_ruim = 0
lista_de_nomes_deu_bom = list()
lista_de_probabilidades_deu_bom = list()
probabilidade_de_matar = 0

#def remover_espaços(nome_com_espaço):
#  nome_split = nome_com_espaço.split()
#  nome_sem_espaço = "".join(nome_split)
#  return nome_sem_espaço

def checar_probabilidade(nome_def):
  deu_o_que = 0
  len_nome = len(nome_def)
  if len_nome > 7:
    print(f"Er {nome_def[0:2]}.. errr... nao consigo lembrar, melhor deixar para la")
    deu_o_que = 0
  else:
    if nome_def == "Makima":
      print("Woof Woof")
      lixo = input()
      print(f"Beleza {nome_def}!! Essa é uma boa pretendente!")
      deu_o_que = 1
    else:
      global probabilidade_de_matar
      probabilidade_de_matar = int(input())

      if probabilidade_de_matar <= 50:
        print(f"Beleza {nome_def}!! Essa é uma boa pretendente!")
        deu_o_que = 1
      else:
        print(f"{nome_def}, mais uma que so quer o coraçao do chainsaw man, quando que alguem vai querer o meu coraçao!?!?")
        deu_o_que = 2
  return deu_o_que


while nome != "cabo":
  nome = input()
  if nome != "cabo":
    #nome = remover_espaços(nome)
    resultado = checar_probabilidade(nome)

    if resultado == 1:
      contador_deu_bom += 1
      lista_de_nomes_deu_bom.append(nome)
      lista_de_probabilidades_deu_bom.append(probabilidade_de_matar)

    elif resultado == 2:
      contador_deu_ruim += 1

if contador_deu_bom > contador_deu_ruim: 
  print("Epa ai sim! E hoje pochita!!")
else: 
  print("Desculpa pochita acho que nao vai ser hoje que voce vai poder ver meus sonhos")
  
if contador_deu_ruim == 0:
  for contador_deu_bom_range in range(contador_deu_bom):
    print(f"nome: {lista_de_nomes_deu_bom[contador_deu_bom_range]} - chances de morrer: {lista_de_probabilidades_deu_bom[contador_deu_bom_range]}%")
  
    