#Laço de repetição for

repetir = 's'
fatura = []
total = 0

while repetir =='s':
    produto = input('Type the product name: ')
    preco = float(input('Type the price: '))

    fatura.append([produto, preco])
    total += preco

    repetir = input('Add more product? (S/N)').lower()

#for i in fatura:
    #print(i[0], ':', i[1])
    print(fatura)

print('O tatal da fatura é: ', total)