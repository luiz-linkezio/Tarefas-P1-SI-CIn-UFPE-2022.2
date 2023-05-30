numero_binario = str(input())
len_numero_binario = len(numero_binario)
numero_decimal = 0

for len in range(len_numero_binario):
    algarismo = int(numero_binario[len])
    if algarismo == 1:
        valor_do_algarismo = 2**(len_numero_binario-len-1)
        numero_decimal = (numero_decimal+valor_do_algarismo)

acertou = 0 
chances = 3
while chances > 0 and acertou == 0:
  palpite1 = int(input())
  if palpite1 == numero_decimal:
    acertou = 1
    print("Parabéns!! Você acertou!")
  else:
    chances = (chances-1)
    print(f"Resposta incorreta. Mas não desista! Você ainda tem {chances} chance(s).")
    palpite2 = int(input())
    if palpite2 == numero_decimal:
      acertou = 1
      print("Parabéns!! Você acertou!")
    else:
      chances = (chances-1)
      print(f"Resposta incorreta. Mas não desista! Você ainda tem {chances} chance(s).")
      palpite3 = int(input())
      if palpite3 == numero_decimal:
        acertou = 1
        print("Parabéns!! Você acertou!")
      else:
        chances = (chances-1)
        if numero_decimal == 1 or numero_decimal == 2 or numero_decimal == 3 or numero_decimal == 4 or numero_decimal == 5:
          print("Infelizmente mais uma resposta incorreta.")
          print("Agradecemos sua participação!")
          print("Seu bilhete era premiado. Que pena!")
        else:
          print("Infelizmente mais uma resposta incorreta.")
          print("Agradecemos sua participação!")
          print("Pelo menos seu bilhete não era premiado.")
          print("Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!")

if acertou == 1:
  if numero_decimal == 1:
    print("Férias inesquecíveis estão te esperando!")
    print("Seu destino será Porto de Galinhas (BRA).")
    print("Prepare-se para viver dias incríveis desfrutando das riquezas naturais da nossa região!")
  elif numero_decimal == 2:
    print("Férias inesquecíveis estão te esperando!")
    print("Seu destino será Fernando de Noronha (BRA).")
    print("Belíssimas praias estão por vir.")
    print("Não esqueça o protetor solar.")
  elif numero_decimal == 3:
    print("Férias inesquecíveis estão te esperando!")
    print("Seu destino será Gramado (BRA).")
    print("Aproveite passeios e paisagens espetaculares no sul do país!")
  elif numero_decimal == 4:
    print("Férias inesquecíveis estão te esperando!")
    print("Seu destino será Berlim (ALE).")
    print("Desfrute de muita cultura e de experiências incríveis!")
    print("Prepare os casacos de frio!")
  elif numero_decimal == 5:
    print("Férias inesquecíveis estão te esperando!")
    print("Seu destino será Tóquio (JPN).")
    print("Viva uma experiência inesquecível explorando um país do outro lado do mundo.")  
    print("Prepare-se para muitas horas de voo!")
  else:
    print("Mas, infelizmente, hoje não é o seu dia de sorte.")
    print("Apesar de ter dado a resposta correta, seu bilhete não oferece nenhum prêmio.")
    print("Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!")