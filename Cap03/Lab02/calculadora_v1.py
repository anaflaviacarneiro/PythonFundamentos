# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print ("\nSelecione o número da operção desejada: \n")

print("1 - Soma\n")
print("2 - Subtração\n")
print("3 - Multiplicação\n")
print("4 - Divisão\n")

opcao = input("Digite a sua opção (1/2/3/4): ")
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
numA = int(num1)
numB = int(num2)

    
if opcao == '1':
    resultado = numA + numB
    print( numA, ' + ', numB, ' = ',resultado )
    
elif opcao =='2':
    resultado = numA - numB
    print( numA, ' - ', numB, ' = ',resultado )

elif opcao =='3':
    resultado = numA * numB
    print( numA, ' * ', numB, ' = ',resultado )

elif opcao =='4':
    resultado = numA / numB
    print( numA, ' / ', numB, ' = ',resultado )
    
else:
    print("\n\n Opção inválida")