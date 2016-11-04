edad=18


if edad<18:
	print "es menor de edad"
else:
	print "es mayor de edad"

print 'termine'

import random

x=random.randint(1,20)
print x
print '<br>'
if x<10:
    print 'El valor generado tiene un digito'
else:
    print 'El valor generado tiene dos digitos'

num=5

num2=random.randint(1,10)


if num==num2:
	print "el numero es igual"
else:
	print "el numero no es igual es "
	print num2


#Elif

x=random.randint(1,1000)
print x
if x<10:
    print 'Tiene 1 dgito'
elif x<100:
    print 'Tiene 2 dgitos'
elif x<1000:
    print 'Tiene 3 dgitos'
else:
    print 'Tiene 4 dgitos'


#numeros

#x=random.randint(100,200)
#print 'Numero final:'
#print x
#print '<br>'
#cont=1
#while cont<=x:
#    print cont
#    print '-'
#    cont=cont+1

def presentacion():
    print 'Primer mensaje.<br>'
    print 'Segundo mensaje.<br>'

def fin():
    print 'Ultimo mensaje.'

presentacion()
fin()



print ""

def imprimirmayor(valor1,valor2):
    if valor1>valor2:
        print valor1
    else:
        print valor2

imprimirmayor(4,5)
print '<br>'
x1=20
x2=30
imprimirmayor(x1,x2)
