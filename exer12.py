alt=float(input("Digite a altura de uma parede "))
largura=float(input("Digite a largura de uma parede "))
tt =float(((largura*alt)/3))
dd = float((((tt*3.6)*107)))
print("O tanto de tinta necessária é{:.3f}\nE a área será de {} e o dinherio gasto com tinta será de {}".format(tt,((largura*alt)),dd))