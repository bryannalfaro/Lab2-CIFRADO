import matplotlib.pyplot as plt
import numpy as np
import itertools as it

#np.random.seed(25)

def xor(a, b):
    result = ''
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result

# find repetitions of substring in string
def find_substring(string, substring):
    if(substring!=1):
        return it.product(string,repeat=substring)

def p_occurancy(bits, type=1): # 1=monograma, 2=bigrama, 3=trigrama, 4=tetragrama, ...
    if type == 1:
        x, bins = np.histogram([int(x) for x in bits], bins=np.arange(0, 3))
        print('0: ', x[0]/len(bits) )
        print('1: ', x[1]/len(bits) )
        plt.hist([int(x) for x in bits], density=True, bins=[0,1,2])
        plt.title('Probabilidades de bits monograma')
        plt.ylabel('Probabilidad')
        plt.xlabel('Bits')
        plt.show()
    elif type == 2:
        bits = list(find_substring(bits,2))
        lista = []
        lista.append(bits.count(('0','0')))
        lista.append(bits.count(('0','1')))
        lista.append(bits.count(('1','0')))
        lista.append(bits.count(('1','1')))
        plt.bar(["00","01","10","11"],[y/len(bits) for y in lista])
        plt.title('Probabilidades de bits bigrama')
        plt.ylabel('Probabilidad')
        plt.xlabel('Bits')
        plt.show()
    elif type == 3:
        bits = list(find_substring(bits,3))
        lista = []
        lista.append(bits.count(('0','0','0')))
        lista.append(bits.count(('0','1','1')))
        lista.append(bits.count(('0','1','0')))
        lista.append(bits.count(('0','0','1')))
        lista.append(bits.count(('1','0','0')))
        lista.append(bits.count(('1','1','0')))
        lista.append(bits.count(('1','0','1')))
        lista.append(bits.count(('1','1','1')))

        plt.bar(["000","011","010","001","100","110","101","111"],[y/len(bits) for y in lista])
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

#print(find_substring('1111', '11'))