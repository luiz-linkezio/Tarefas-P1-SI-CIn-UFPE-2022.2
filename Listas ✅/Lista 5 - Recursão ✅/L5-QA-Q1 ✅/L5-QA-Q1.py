ultimo_termo = 0
def termo_n(ordem, razao, termo_atual):
  global ultimo_termo
  global termo_x
  termo_x = termo_atual + razao
  if termo_x != (termo_0+(razao*ordem)-razao):
    termo_n(ordem, razao, termo_x)
  else:
    ultimo_termo = termo_x


numeros = input()
ordem = int(input())
numeros_split = numeros.split()
len_numeros_split = len(numeros_split)
termo_0 = int(numeros_split[0])
termo_1 = int(numeros_split[1])
termo_2 = int(numeros_split[2])
razao = termo_1 - termo_0

termo_n(ordem, razao, termo_0)

print(f"Na progressão aritmética cujos três primeiros números são {termo_0}, {termo_1} e {termo_2}, o {ordem}º elemento é {ultimo_termo} e a razão da progressão é {razao}.")