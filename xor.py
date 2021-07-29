'''
Universidad del valle de Guatemala
Cifrado de la informacion - laboratorio 2
Integrantes:
Bryann Alfaro
Diego Arredondo
Julio Herrera
'''
import matplotlib.pyplot as plt
import numpy as np
import itertools as it

def xor(a, b):
    result = ''
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result

# find repetitions of substring in string
def find_substring(string, substring):
    if(substring!=1):
        return it.product(string,repeat=substring)

def p_occurancy(bits, type=1): # 1=monograma, 2=bigrama, 3=trigrama
    if type == 1:
        x, bins = np.histogram([int(x) for x in bits], bins=np.arange(0, 3))
        print('\nDistribución de monogramas')
        print('0: ', x[0]/len(bits) )
        print('1: ', x[1]/len(bits) )
        plt.hist([int(x) for x in bits], density=True, bins=[0,1,2])
        plt.title('Probabilidades de bits monograma')
        plt.ylabel('Probabilidad')
        plt.xlabel('Bits')
        plt.show()
    elif type == 2:
        bits = list(find_substring(bits,2))
        bigramas = [('0', '0'), ('0', '1'), ('1', '0'), ('1', '1')]
        lista = []
        print('\nDistribución de bigramas')
        for bigrama in bigramas:
            lista.append(bits.count(bigrama))
            print(f'{bigrama}: {bits.count(bigrama)/len(bits)}''')
        plt.bar([ str(bi) for bi in bigramas ],[y/len(bits) for y in lista])
        plt.title('Probabilidades de bits bigrama')
        plt.ylabel('Probabilidad')
        plt.xlabel('Bits')
        plt.show()
    elif type == 3:
        bits = list(find_substring(bits,3))
        trigramas = [('0','0','0'), ('0','0','1'), ('0','1','0'), ('0','1','1'), ('1','0','0'), ('1','0','1'), ('1','1','0'), ('1','1','1')]
        lista = []
        print('\nDistribución de trigramas')
        for trigrama in trigramas:
            lista.append(bits.count(trigrama))
            print(f'{trigrama}: {bits.count(trigrama)/len(bits)}''')
        plt.bar([ str(tri) for tri in trigramas ],[y/len(bits) for y in lista])
        plt.title('Probabilidades de bits trigrama')
        plt.ylabel('Probabilidad')
        plt.xlabel('Bits')
        plt.show()

def propertiesX(bits,type):
    y = lengthBits(len(bits))
    xor(bits,y) #XOR entre random y teorico
    p_occurancy(bits, type)

def properties(bits,type):
    p_occurancy(bits, type)

def lengthBits(lenBits):
    return ''.join(str(np.random.randint(0, 2)) for _ in range(lenBits))
