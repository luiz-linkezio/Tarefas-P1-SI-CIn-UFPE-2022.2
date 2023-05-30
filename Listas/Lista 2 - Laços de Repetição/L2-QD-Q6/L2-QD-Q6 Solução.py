nome_da_invencao = str(input())
nome_da_etapa = ("")
etapas_realizadas = 0
custo_total = 0
tentativas_falhas = 0
while nome_da_etapa != ("concluir") and nome_da_etapa != ("desistir"):
  nome_da_etapa = str(input())
  contador_de_tentativas = 0
  if nome_da_etapa != ("concluir") and nome_da_etapa != ("desistir"):
    if nome_da_etapa == ("dar um plus"):
      custo_da_etapa = int(input())
      custo_total = (custo_total+custo_da_etapa)
      print(f"Agora o(a) {nome_da_invencao} ficou ainda mais legal! Pena que precisei gastar R${custo_da_etapa}")
    else:
      custo_da_etapa = int(input())
      tentativas_da_etapa = int(input())
      status_da_etapa = ("")
      while status_da_etapa != ("correto") and status_da_etapa != ("desistir") and status_da_etapa != ("concluir") and contador_de_tentativas < tentativas_da_etapa:
        status_da_etapa = str(input())
        contador_de_tentativas = (contador_de_tentativas+1)
        if status_da_etapa == ("incorreto"):
          print(f"Ainda não consegui {nome_da_etapa} corretamente, e essa tentativa me custou R${custo_da_etapa}")
          tentativas_falhas = (tentativas_falhas+1)
          custo_total = (custo_total+custo_da_etapa)
          if contador_de_tentativas == tentativas_da_etapa:
            print(f"ANDAMENTO DO PROJETO: Etapas realizadas - {etapas_realizadas} ; Tentativas falhas - {tentativas_falhas}")
        elif status_da_etapa == ("correto"):
          print(f"Oba! consegui {nome_da_etapa}, o que me custou R${custo_da_etapa}")
          etapas_realizadas = (etapas_realizadas+1)
          custo_total = (custo_total+custo_da_etapa)
          print(f"ANDAMENTO DO PROJETO: Etapas realizadas - {etapas_realizadas} ; Tentativas falhas - {tentativas_falhas}")
        elif status_da_etapa == ("desistir"):
          nome_da_etapa = ("desistir")
          print(f"ANDAMENTO DO PROJETO: Etapas realizadas - {etapas_realizadas} ; Tentativas falhas - {tentativas_falhas}")
        elif status_da_etapa == ("concluir"):
          nome_da_etapa = ("concluir")
          print(f"ANDAMENTO DO PROJETO: Etapas realizadas - {etapas_realizadas} ; Tentativas falhas - {tentativas_falhas}")
print(f"A jornada da construção do(a) {nome_da_invencao} acaba aqui.")
if nome_da_etapa == ("concluir"):
  print(f"Uhuuu, finalmente o(a) {nome_da_invencao} tá pronto(a)! Esse projeto me custou R${custo_total}")
elif nome_da_etapa == ("desistir"):
  print(f"Infelizmente, o sonho do(a) {nome_da_invencao} foi interrompido e levou junto com ele R${custo_total}")
  