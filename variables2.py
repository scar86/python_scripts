def cantidadvocales(cadena):
    cant=0
    for letra in cadena:
        if letra=='a':
            cant=cant+1
        if letra=='e':
            cant=cant+1
        if letra=='i':
            cant=cant+1
        if letra=='o':
            cant=cant+1
        if letra=='u':
            cant=cant+1
        if letra=='A':
            cant=cant+1
        if letra=='E':
            cant=cant+1
        if letra=='I':
            cant=cant+1
        if letra=='O':
            cant=cant+1
        if letra=='U':
            cant=cant+1
    return cant

print 'Cantidad de vocales en la palabra Hola:'
print cantidadvocales('Hola')
print '<br>'
print 'Cantidad de vocales en la palabra Computadora:'
print cantidadvocales('Computadora')

#listas, se hacen con corchetes y se pueden modificar usando su subindice


# si quieres saber si un elemento esta en una lista

lista1=[12,45,1,2,5,4,3,55]
if 1 in lista1:
    print 'El valor 1 esta contenido en la lista '
else:
    print 'El valor 1 no esta contenido en la lista '
print lista1


lista1=[2,4,6,8]
lista2=[10,12,14,16]
listatotal=lista1+lista2
print listatotal

#modificar variables
lista=[2,4,6]
lista[1]=10
print lista  #[2, 10, 6]
#Podemos borrar elementos de la lista utilizando la funcion del:
lista=[2,4,6]
del(lista[1])
print lista  #[2, 6]


#arrays

productos={'manzanas':23,'peras':50,'papas':120}

print productos['manzanas']

print productos
