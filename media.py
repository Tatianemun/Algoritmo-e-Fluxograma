# Programa Média

print("Digite a sua nota do 1º Bimestre:")
nota1 = input() 
nota1_real = float (nota1)
print("Digite a sua nota do 2º Bimestre:")
nota2 = input()
nota2_real = float (nota2)
print("Digite a sua nota do 3º Bimestre:")
nota3 = input()
nota3_real = float (nota3)
print("Digite a sua nota do 4º Bimestre:")
nota4 = input()
nota4_real = float (nota4)
media = (nota1_real+nota2_real+nota3_real+nota4_real)/4
print (f"Sua média é: {media}")
if media >= 6:
    print ("Parabéns, você foi aprovado")
else:
    print ("Sinto muito, você está reprovado")