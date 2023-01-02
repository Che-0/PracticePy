import zipfile


zip_abierto = zipfile.ZipFile('44_ArchivoComprimido.zip','r')

zip_abierto.extractall()
print(zip_abierto)