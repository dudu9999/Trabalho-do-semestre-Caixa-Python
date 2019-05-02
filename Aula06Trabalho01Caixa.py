'''
Faca um algoritmo que leia um valor_digitado equivalente ao saque de um caixa automatico,
mostre quantas cedulas sao necessarias para pagar o valor_digitado solicitado.
Considerar notas de 100, 50, 20, 10 e 5 Reais.

Caso o valor_digitado solicitado nao seja possivel ser pago, mostre a seguinte mensagem:
"valor_digitado n√o pode ser pago"

Consideracoes:
Utilize um estoque de notas ao iniciar o programa de 20 notas de cada valor_digitado.
    Exemplo:
    Qt inicial de notas de 100= 20
    Qt inicial de notas de  50= 20
    Qt inicial de notas de  20= 20
    Qt inicial de notas de  10= 20
    Qt inicial de notas de   5= 20
Para cada saque realizado, subtraia do estoque as notas pagas.
Caso o usuario deseje sacar mais que o valor_digitado em estoque dar a seguinte
mensagem: "Este valor_digitado excede a capacidade deste terminal."
Caso a quantidade de notas de um dos valor_digitadoes termine, substitua por notas
menores.

Exemplo:

Digite o valor_digitado de saque: 270
Para pagar o valor_digitado solicitado s√£o necess√°rios:
2 notas de 100 Reais
1 nota de 50 Reais
1 nota de 20 Reais
'''

valor_digitado = -2 # tratamento para o usuario nao digitar valor_digitado negativo!
print("-----------------------------------------------------------")
print("--------------- CAIXA ECONOMICA FEDERAL -------------------")
print("-----------------------------------------------------------")
while valor_digitado<0:
    valor_digitado = int(input("Digite o valor que deseja sacar: "))
    print(" ")
    if valor_digitado<0:
        print("Erro - valor_digitadoes negativos digitados, digite valor_digitadoes positivos")    
    if valor_digitado >3701:
        print("Desculpe mas, o valor_digitado n„o pode ser pago")    
        valor_digitado = -2

print("Para pagar os ",valor_digitado," solicitado sao necesscarios:")
print('')

valor_100, valor_50, valor_20, valor_10, valor_5, disconto = 0, 0, 0, 0, 0, 0
resto_100, resto_50, resto_20, resto_10, resto_5, resto_sobra = 0, 0, 0, 0, 0, 0
    
#---------------------------------------------------------------------- 
if valor_digitado >=100:
    valor_100 = (valor_digitado//100)
    resto_100 = (valor_digitado%100)
    if valor_100>20:
        disconto = (valor_100-20) 
        valor_100=(valor_100-disconto) 
        resto_sobra = (disconto*100) 
        resto_100 = (resto_100+resto_sobra)
    print(valor_100," notas de 100 Reais")
else:
    print("Nenhuma nota de 100 Reais")
    resto_100 = valor_digitado
#---------------------------------------------------------------------- 
if resto_100 >=50:
    valor_50 = (resto_100//50)
    resto_50 = (resto_100%50)
    if valor_50>20:
        disconto = (valor_50-20) 
        valor_50=(valor_50-disconto) 
        resto_sobra = (disconto*50) 
        resto_50 = (resto_50+resto_sobra)
    print(valor_50," notas de 50 Reais")
else:
    print("Nenhuma nota de 50 Reais")
    resto_50 = resto_100
#----------------------------------------------------------------------
if resto_50>=20 and resto_50 != 0:
    valor_20 =(resto_50//20)
    resto_20=(resto_50%20)
    if valor_20>20:
        disconto = (valor_20-20)
        valor_20=(valor_20-disconto)
        resto_sobra = (disconto*20)
        resto_20 = (resto_20+resto_sobra)    
    print(valor_20," notas de 20 Reais")
else:
    print("Nenhuma nota de 20 Reais")
    resto_20 = resto_50
#----------------------------------------------------------------------
if resto_20>=10 and resto_20 != 0:
    valor_10 =(resto_20//10)
    resto_10=(resto_20%10)
    if valor_10>20:
        disconto = (valor_10-20)
        valor_10=(valor_10-disconto)
        resto_sobra = (disconto*10)
        resto_10 = (resto_10+resto_sobra)
    print(valor_10," notas de 10 Reais")
else:
    print("Nenhuma nota de 10 Reais")
    resto_10 = resto_20
#----------------------------------------------------------------------
if resto_10>=5 and resto_10!= 0:
    valor_5 =(resto_10//5)
    resto_5=(resto_10%5)
    if valor_5>20:
        disconto = (valor_5-20)
        valor_5=(valor_5-disconto)
        resto_sobra = (disconto*5)
        resto_5 = (resto_5+resto_sobra)
    print(valor_5," notas  de 5 Reais")
else:
    print("Nenhuma nota  de 5 Reais")
    resto_5 = resto_10
#----------------------------------------------------------------------  
if resto_5>0:
    if resto_5<10 and resto_5>0:
        print('')
        print('E ainda sobrou mais ',resto_5,'Reais mas')
        print("  a caixa nao possiu moedas de 1 Real")
    else:
        print("E ainda sobrou mais ",resto_5,"Reais mas")
        print("na caixa nao tem mais notas")
#----------------------------------------------------------------------
print(" ")
print("-----------------------------------------------------------")
print("A caixa agradece sua preferencia, ate logo!")
print("-----------------------------------------------------------")
print('')





