 #adicao +
#subtracao -
#multiplicacao *
#divisao /
#exponenciacao **
#modulo %
 
real = float(input("converter real: "))
print("Escolha a moeda para conversão:")
print("1 - Dólar")
print("2 - Euro")
print("3 - Libra Esterlina")
print("4 - Dólar Canadense")
opcao = int(input("Digite o número da opção desejada: "))
if opcao == 1:
    dolar = real / 5.37
    print("O valor de R${:.2f} em dólares é: $ {:.2f}".format(real, dolar))
elif opcao == 2:
    euro = real / 6.35
    print("O valor de R${:.2f} em euros é: € {:.2f}".format(real, euro))
elif opcao == 3:
    libra_esterlina = real / 7.30
    print("O valor de R${:.2f} em libras esterlinas é de: £ {:.2f}".format(real, libra_esterlina))
elif opcao == 4:
    dolar_canadense = real / 2.90
    print("O valor de R${:.2f} em dólares canadenses é: C$ {:.2f}".format(real, dolar_canadense))
else:
    print("Opção inválida. Exibindo valor em reais.")
