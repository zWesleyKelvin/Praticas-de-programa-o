print(' Questão 3 ')
      
sexo = int(input('Escolha: 1- Sexo Masculino / 2- Sexo Feminino: '))
h = float(input('Altura:'))
peso = float(input('Peso:'))

peso_ideal = (72.7*h) - 58 if sexo == 1 else (62.1*h) - 44.7

if peso < peso_ideal:
	print('Abaixo do peso ideal!')
elif peso == peso_ideal:
	print('Dentro do peso ideal!')
else:
	print('Acima do peso ideal!')
print ('Peso: %.2f / Peso ideal: %.2f' %(peso, peso_ideal))


#exemplo de código da condição da linha 11 mais detalhado
'''if sexo == 1:
	peso_ideal = (72.7*h) - 58
else:
	peso_ideal = (62.1*h) - 44.7'''
