nota1= float(input('Digite a primeira nota:'))
nota2=float(input('Digite a segunda nota:'))

n3=(nota1+nota2)/2

if n3 >=7.0:
    print('Parabéns, sua nota foi {}, está aprovado'.format(n3))
else:
    print('Sua nota foi {}, reprovado'.format(n3))


