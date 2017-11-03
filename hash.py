import hashlib

def readFile(dir):
    arq = open(dir)
    cont = arq.read()
    arq.close()
    return cont

def isEqual(hashA,hashB):
    if hashA == hashB:
        return True
    return False    

def getHashMd5(file):
     h = hashlib.md5()
     h.update(file) 
     return h.hexdigest() #Retorna o hash em hexadecimal

if __name__ == "__main__":
    arqA = raw_input('\nDigite o arquivo A: ')
    hashA = getHashMd5( readFile(arqA) )
    print("Hash do arquivo A:" + hashA + "\n")

    arqB = raw_input('Digite o arquivo B: ')
    hashB = getHashMd5( readFile(arqB) )
    print("Hash do arquivo B:" + hashB + "\n")
    

    print( "Hash iguais? " + str( isEqual(hashA,hashB) ) + "!\n")