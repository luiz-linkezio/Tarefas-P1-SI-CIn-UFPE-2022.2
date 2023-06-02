string_invertida = ""
contador = 0

def inverter_string(string, contador, string_len):
  global string_invertida
  string_invertida = string_invertida + string[string_len-contador]
  contador += 1
  if contador != string_len+1:
    inverter_string(string, contador, string_len)
  else:
    return string_invertida
  
string = input()

contador_len = 0
for caractere in string:
  contador_len += 1 

inverter_string(string, 0, contador_len-1)

print(string_invertida)