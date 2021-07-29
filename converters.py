import base64;
'''
Universidad del valle de Guatemala
Cifrado de la informacion - laboratorio 2
Integrantes:
Bryann Alfaro
Diego Arredondo
Julio Herrera
'''
#GET FROM > https://www.it-swarm-es.com/es/python/convertir-binario-ascii-y-viceversa/940070781/
def text_to_bits(text):
    bits = bin(int.from_bytes(text.encode('utf-8'), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits):
    return int(bits,2).to_bytes((int(bits,2).bit_length() + 7) // 8, 'big').decode('utf-8')

#Using library base64
def text_b64(text):
    t = base64.b64encode(bytes(text_to_bits(text),'utf-8'))
    return t

def back_text_b64(b64):
    t = base64.b64decode(b64)
    t= text_from_bits(t)
    return t

# MANUAL ENCRYPTION

base64Table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

# get ascii code of char
def ascii_char(text):
    return ord(text)

# get ascii of text
def text_to_ascii(text):
    ascii = []
    for letra in text:
        ascii.append(str(ascii_char(letra)))
    return ascii

def ascii_to_bits(ascii):
    bits = [ bin(int(code))[2:].zfill(8) for code in ascii ]
    return bits

def bits_split_and_fill(bits):
    all_bits = ''.join(bits)
    new_bits = [ (all_bits[i:i+6].ljust(6, '0')) for i in range(0, len(all_bits), 6) ]
    octetos_left = len(''.join(new_bits)) - len(all_bits)
    return octetos_left, new_bits

def bin_to_number(bits):
    return int(bits,2)

def bits_to_indexes(bits):
    indexes = [ bin_to_number(x) for x in bits ]
    return indexes

def number_to_base64(number):
    return base64.b64encode(number.to_bytes((number.bit_length() + 7) // 8, 'big')).decode('utf-8')

def indexes_to_text(indexes):
    text = ''.join(base64Table[i] for i in indexes)
    return text

def encryptBase64(plainText):
    #print([ x for x in text ])
    t_a = text_to_ascii(plainText)
    #print(t_a)
    a_b = ascii_to_bits(t_a)
    #print(a_b)
    o_l, b_b = bits_split_and_fill(a_b)
    #print(b_b)
    b_i = bits_to_indexes(b_b)
    #print(b_i)
    i_t = indexes_to_text(b_i)
    return i_t.ljust(len(i_t) + o_l - 1, '=')

# MANUAL DECRYPTION

def base64_indexes(text):
    indexes = [ base64Table.index(i) for i in text ]
    return indexes

def numbers_to_bits(numbers):
    bits = [ bin(int(num))[2:].zfill(6) for num in numbers ]
    return bits

def bits_6_to_8(bits):
    all_bits = ''.join(bits)
    new_bits = [ (all_bits[i:i+8]) for i in range(0, len(all_bits), 8) ]
    if (len(new_bits[-1]) < 8):
        new_bits.pop(len(new_bits) - 1)
    return new_bits

def bits_to_ascii(bits):
    ascii = [ int(num, 2).to_bytes((int(num, 2).bit_length()+7) // 8, 'big').decode() for num in bits ]
    return ascii

def decryptBase64(cypher):
    cypher_enc = cypher.split('=')[0]
    b_i = base64_indexes(cypher_enc)
    #print(b_i)
    i_b = numbers_to_bits(b_i)
    #print(i_b)
    b_b = bits_6_to_8(i_b)
    #print(b_b)
    b_a = bits_to_ascii(b_b)
    return ''.join(b_a)
