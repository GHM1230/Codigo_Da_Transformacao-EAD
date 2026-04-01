print('qual a sua idade?')
idade = int(input())

if idade <= 18:
    print('você é menor de idade')

elif idade <= 60:
    print('você é adulto')

else:
    print('você é idoso')