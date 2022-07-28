#importando funções do sistema operacional
import os
#importando lib de criptografia
import pyaes

#abrindo arquivo criptografado
file_name = "foto.jpg.pyransom"
file = open(file_name, "rb")
file_data = file.read()
file.close()

#chave para descriptografar
key = "0143256789fravtr"
#descriptografando o arquivo
aes = pyaes.AESModeOfOperationCTR(key.encode())
decrypt_data = aes.decrypt(file_data)

#para remover o arquivo
os.remove(file_name)

#gerando novo arquivo descriptografado
new_file_name = "foto.jpg"
new_file = open(new_file_name, "wb")
new_file.write(decrypt_data)
new_file.close()
