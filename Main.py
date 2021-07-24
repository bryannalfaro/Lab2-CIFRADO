import converters
'''
print(converters.binary('hello'))
prueba = converters.binary('hello')
print(converters.binaryToText(prueba))'
'''
t = 'HOLA { QUE { TAL ('
print(converters.text_to_bits(t))
b =converters.text_to_bits(t)
print(converters.text_from_bits(b))