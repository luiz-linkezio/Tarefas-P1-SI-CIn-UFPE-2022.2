numero = int(input())
contador = numero - 1
e_primo = True
lista_de_primos = list()

def verificar_se_e_primo(num):
    contador = num - 1
    e_primo = True
    while contador > 1:
        resto = num%contador
        if resto == 0:
            e_primo = False
        contador -= 1
    return e_primo

def listar_primos(num2):
    lista_de_primos = list()
    for contador2 in range(num2):
        num2 -= 1

        e_primo2 = verificar_se_e_primo(num2)
        if e_primo2 == True:
            lista_de_primos.append(num2)
    lista_de_primos.sort()
    lista_de_primos.remove(0)
    lista_de_primos.remove(1)        
    return lista_de_primos

if numero <= 1:
    print(f"O número {numero} não é primo.\nAlém disso, não temos primos no intervalo de 1 à {numero}.\nAGORA ESTOU PRONTO PARA MINHA NOVA VIDA!")

else:
    e_primo2 = verificar_se_e_primo(numero)
    if e_primo2 == True:
        print(f"O número {numero} é primo.\nAGORA ESTOU PRONTO PARA MINHA NOVA VIDA!")
    else:
        lista_final_de_primos = listar_primos(numero)   
        quantidade_de_primos_da_lista = len(lista_final_de_primos)

        print(f"O número {numero} não é primo.\nEntretanto, temos primos no intervalo de 1 à {numero}. Estes são:")
        for contador3 in range(quantidade_de_primos_da_lista):
            if contador3 == quantidade_de_primos_da_lista-1:
                print(f"{lista_final_de_primos[contador3]}")
            else:   
                print(f"{lista_final_de_primos[contador3]}, ", end="")   
        print("AGORA ESTOU PRONTO PARA MINHA NOVA VIDA!")
    
