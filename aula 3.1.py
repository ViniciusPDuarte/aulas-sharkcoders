naqr = input('Digite o nome do arquivo que desejas criar: ')
carq = input('\nDigite o que queres por lá dentro: ')

with open(f'{naqr}', 'w') as file:
    file.write(carq)

print(f'\nO arquivo "{naqr}.txt" foi criado com sucesso. Verifique as pastas.')