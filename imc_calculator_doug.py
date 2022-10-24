# Programa que calcula o IMC (Índice de massa corporal) de uma pessoa.
import math
import time


print("""Olá! Esse programa tem como intuito calcular o seu índice de massa corporal (IMC)
e em seguida analísar se você está abaixo ou acima do peso!\n""")

# Interação com o usuário:
nome = str(input('Vamos começar com o seu nome: ')).strip().title()
print(f'É um prazer, {nome}!')
print(f'{nome}, para calcular o seu IMC, será necessário que informe sua altura e seu peso.\n')

#Dados de altura e peso do usuário:
peso = float(input(f'{nome}, digite o seu peso: '))
print(f'{peso:.0f} quilos.')
altura = float(input('Agora digite a sua altura: '))
print(f'{altura:.2f} metros.')

print(f'Ótimo! Você pesa {peso:.0f} quilos e possuí {altura:.2f} metros de altura.')

#Realizando o calculo do IMC:
imc = peso / pow(altura, 2)

print(f'{nome}, agora iremos calcular o seu IMC!')

print('\nCalculando...\n')
time.sleep(2)
print('Pronto!')
time.sleep(0.35)

print(f'O seu IMC é: {imc:.2f}')

time.sleep(1.5)
print(f'\n{nome}, agora veremos o que o seu IMC indica de acordo com a OMS!')

#O que o IMC do usuário indica: 
print('\nCarregando...\n')
time.sleep(1.5)
print('Pronto!')
time.sleep(0.35)

if imc <= 18.5:
    print(f'{nome}, o seu IMC ({imc:.2f}) indica que você está abaixo do peso normal!')

elif 18.6 <= imc <= 24.9:
    print(f'{nome}, o seu IMC ({imc:.2f}) indica que você está no peso ideal! Parabéns!')

elif 25 <= imc <= 29.9:
    print(f'{nome}, o seu IMC ({imc:.2f}) indica que você está levemente acima do peso!')

elif 30 <= imc <= 34.9:
    print(f'{nome}, o seu IMC ({imc:.2f}) indica obesidade de grau I!')

elif 35 <= imc <= 39.9:
    print(f'{nome}, o seu IMC ({imc:.2f}) indica obesidade de grau II (severa)!')

elif imc >= 40:
    print(f'{nome}, o seu IMC ({imc:.2f}) indica obesidade de grau III (mórbida)!')

#Fim do programa