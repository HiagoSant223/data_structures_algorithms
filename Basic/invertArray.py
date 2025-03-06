def invert_array(arr):
    i = 0
    f = len(arr) -1
    
    #Enquanto o indice i for menor que indice f:
    while i < f:
        
    #O indice do arr[i] e arr[f] será invertido = arr[f] e arr[i]
        arr[i], arr[f] = arr[f], arr[i]
    
    #Apos a inversão, o i deve adicionar +1 para que itere para direita e f -1 para que itere para esquerda
        i += 1
        f -= 1
    
    #Retorna o Array = arr
    return arr

#Definino meu array
arrayOriginal = [1, 2, 3, 4, 5, 6, 7]
print("Array original: ", arrayOriginal)

arrayOriginal.append(2)
print("Array original: ", arrayOriginal)

del arrayOriginal[7]
print("Array original: ", arrayOriginal)

#Defino uma variavel para armazenar o array invertido que recebe a função e seta o array original como parametro
arrayInvertido = invert_array(arrayOriginal)

print("Array invertido: ", arrayInvertido)

