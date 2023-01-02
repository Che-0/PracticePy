import os 

# r = os.getcwd()  <-- directorio actual

r = os.chdir('D:\\Che\\invest')

archivo = open('format.txt','r')
print(archivo.readlines())

archivo.close()
