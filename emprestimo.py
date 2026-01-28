salario = float(input("digite seu salario: "))
casa = float(input("digite o valor da casa: "))
anos = int(input("digite a quantidade de anos: "))
m = salario * 30 /  100 #calul para obter o numero de 30 por cento do salario
P = casa / (anos*12) # valor da casa divido pelo tempo * 12
if P <= m: # se o valor da prestacao for menor que 30 por cento do salario print empresitmo aprovado
    print("emprestimo aprovado")
else: # caso contrario negado
    print("emprestimo reprovado")

