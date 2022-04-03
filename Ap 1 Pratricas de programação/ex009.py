sal = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0, len(sal)):
    venda = float(input('Digite o valor das vendas: '))
    salario = ((venda * 9) / 100) + 200
    contador = int(salario / 100) - 1
    if contador > 9:
        contador = 9
    else:
        contador = 1
        sal[contador - 1] += 1
for func in range(0, 9):
    print ('''
    %d - %d : %d
    ''' % (func * 100 + 200, (func + 1) * 100 + 199, sal[func]))
