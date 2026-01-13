largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))  
area = largura * altura #o valor e multiplicado para calcular a area da parede
print ("a sua parede tem a dimensao de {}x{} e sua area e de {}m²".format(largura, altura, area))
tinta = area /2 
print ("para pintar essa parede, voce precisara de {}l de tinta".format(tinta))