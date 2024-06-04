a1 = float (input ("quanto vc ganha por hora: "))
a2 = float (input("num de horas trabalha no mes:"))
salario = (a1 * a2)
inss = salario * 0.11
ir = salario *0.08
sin = salario * 0.05
salario2 = (((salario - inss) - ir) - sin)
print ("salario bruto: "+str  (salario) )
print ("salario liquido: "+str (salario2))
print ("inss: "+str (inss))
print ("ir: "+ str(ir))
print ("sin: "+ str(sin ))
