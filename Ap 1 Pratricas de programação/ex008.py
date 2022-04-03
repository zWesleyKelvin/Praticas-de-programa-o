notas = []
olia = notas.sort()
print('Digite -1 para encerrar o programa')
while True:
    nota = float(input('Digite a nota: '))
    if nota < 0:
        print('O programa foi encerrado')
        break
    notas.append(nota)

media = sum(notas) / len(notas)
acima = 0
abaixo = 0
for n in notas:
    if n > media:
        acima += 1
    if n < 7:
        abaixo += 1
print('Foram lidos {} valores.'.format(len(notas)))
print('Os valores lidos foram: {}'.format(notas), end='\n')
print('A soma dos valores é: %.2f' % (sum(notas)))
print('Quantidade de valores acima da média %d' % acima)
print('Quantidade de valores abaixo de sete: %d' % abaixo)
