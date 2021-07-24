'''def binary(text):
    binario = ''
    for letra in text:
        byte = (letra.encode('ascii'))

        binario += bin(int.from_bytes(byte,'big'))[2:]
    return binario.zfill(8 * ((len(binario) + 7) // 8))

def binaryToText(bits):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode('utf-8', 'surrogatepass') or '\0'
    '''
#GET FROM > https://www.it-swarm-es.com/es/python/convertir-binario-ascii-y-viceversa/940070781/
def text_to_bits(text):
    bits = bin(int.from_bytes(text.encode('utf-8'), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits):
    return int(bits,2).to_bytes((int(bits,2).bit_length() + 7) // 8, 'big').decode('utf-8')


