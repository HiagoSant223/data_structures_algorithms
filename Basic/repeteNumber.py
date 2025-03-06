def most_freq(arr):
    contagem = {}
    
    for num in arr:
        if num in contagem:
            contagem[num] += 1
        else:
            contagem[num] = 0
        
    mais_frequente = None
    maior_numero = 0
    
    for num, qtd in contagem.items():
        if qtd > maior_numero:
            maior_numero = qtd
            mais_frequente = num
            
    return mais_frequente

primeroArray = [1, 2, 3, 3, 3, 5]
print(primeroArray)

maiorNummero = most_freq(primeroArray)

print(maiorNummero)