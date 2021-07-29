'''
Universidad del valle de Guatemala
Cifrado de la informacion - laboratorio 2
Integrantes:
Bryann Alfaro
Diego Arredondo
Julio Herrera
'''
import converters
import xor

print('EJEMPLO 1 - BINARIO\n')
t = 'HOLA'
b =converters.text_to_bits(t)
print('Binario: ',b)
print('Traduccion: ',converters.text_from_bits(b))
print('\nEJEMPLO 2 - BINARIO\n')
t = 'Man is distinguished, not only by his reason'
b =converters.text_to_bits(t)
print('Binario: ',b)
print('Traduccion: ',converters.text_from_bits(b))
print('\nEJEMPLO 3 - BINARIO\n')
t = 'hoy es un gran dia'
b =converters.text_to_bits(t)
print('Binario: ',b)
print('Traduccion: ',converters.text_from_bits(b))

print('\nEJEMPLO 1 - BASE 64\n')
t2 = 'Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure.'
a = converters.encryptBase64(t2)
print('\nBase 64:\n',a)

print('\nDecodificacion Base 64:\n',converters.decryptBase64(a))
print('\nEJEMPLO 2 - BASE 64\n')
t2 = 'El covid 19 es una pandemia que afecto a todo el mundo'
a = converters.encryptBase64(t2)
print('\nBase 64:\n',a)
print('\nDecodificacion Base 64:\n',converters.decryptBase64(a))

print('\nEJEMPLO 3 - BASE 64\n')
t2 = 'Hoy es un dia nublado'
a = converters.encryptBase64(t2)
print('\nBase 64:\n',a)
print('\nDecodificacion Base 64:\n',converters.decryptBase64(a))

print('')

#Distribucion de solo la palabra
xor.properties(converters.text_to_bits('Homero Simpson'),1)
xor.properties(converters.text_to_bits('Homero Simpson'),2)
xor.properties(converters.text_to_bits('Homero Simmpson'),3)

#Haciendo XOR con bits random
xor.propertiesX(converters.text_to_bits('Homero Simpson'),1)
xor.propertiesX(converters.text_to_bits('Homero Simpson'),2)
xor.propertiesX(converters.text_to_bits('Homero Simpson'),3)
