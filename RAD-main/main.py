'''arquivo = open("texto.txt","r")
print(arquivo.read())'''
'''print(arquivo.readline())
print(arquivo.readline())
print(arquivo.seek(0))
print(arquivo.readlines())
#print(arquivo.seek(0))'''
'''print(arquivo.tell())
arquivo.close()
print(arquivo.closed)'''
'''print(arquivo.read())
print(arquivo.seek(0))
print(arquivo.read(8))'''
'''print(arquivo.name)
print(arquivo.mode)
print(arquivo.closed)'''

'''arquivo = open("novo.txt","w")
arquivo.write("Arquivo de escrita")
arquivo.close()
print(arquivo.closed)'''

'''arquivo = open("frutas.txt","w")
arquivo.write("banana")
arquivo.write("uva")
arquivo.write("mamao")
arquivo.close()'''

'''precos = [20,100,500,600]
with open("precos_roupas.txt","w") as arquivo:
 for preco in precos:
     arquivo.write(str(preco) + '\n')
print(arquivo.closed)'''

'''precos =  [8000]
with open("precos_roupas.txt","a") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + '\n')'''
'''precos = [100000]
with open("precos_roupas", "w") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + '\n')'''