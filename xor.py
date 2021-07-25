import matplotlib.pyplot as plt
import numpy as np

#np.random.seed(25)

def xor(a, b):
    result = ''
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result

def p_occurancy(bits, type=1): # 1=monograma, 2=bigrama, 3=trigrama, 4=tetragrama, ...
    if type == 1:
        x, bins = np.histogram(bits, bins=np.arange(0, len(bits) + 1))
        plt.hist(x, density=True, bins=bins)
        plt.title('Probabilidade de bits monograma')
        plt.ylabel('Probabilid')
        plt.xlabel('Bits')
        plt.show()

def properties(bits):
    print(bits)
    p_occurancy(bits, 1)
    
# find repetitions of substring in string
def find_substring(string, substring):
    ocurrences = 0
    index = -1
    while True:
        index = string.find(substring, index + 1)
        if index == -1:
            break
        ocurrences += 1
    return ocurrences

print(find_substring('1111', '11'))