#Este pedo va con   zipfile    shutil

import zipfile

# dentro de los parametros va name archivo que le pondra al new archivo  y su apertura w r ...
mi_zip = zipfile.ZipFile("44_ArchivoComprimido.zip",'w')  

mi_zip.write('42_PruebaZip.txt')
mi_zip.write('43_PruebaZip2.txt')

mi_zip.close()
