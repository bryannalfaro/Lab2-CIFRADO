import converters
'''
print(converters.binary('hello'))
prueba = converters.binary('hello')
print(converters.binaryToText(prueba))'
'''
t = 'HOLA'
b =converters.text_to_bits(t)
print('Binario: ',b)

print('Traduccion: ',converters.text_from_bits(b))

t2 = 'Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure'
a = converters.text_b64(t2)
print('Base 64: ',a)

print('Decodificacion Base 64',converters.back_text_b64(a))