from asyncio.log import logger
import requests
import pandas as pd
import os

# Obtener el documento en excel
file_loc = "fotos.xlsx"

# Acceder a las columnas que tienen las imágenes en enlace con el key de la columna
Id = pd.read_excel(file_loc,  usecols="A")
im1 = pd.read_excel(file_loc,  usecols="DE")
im2 = pd.read_excel(file_loc,  usecols="DF")


# Nombre de las imágenes según la columna
nombreImagen = [
'imagen1',
'imagen2',
]

# Función que descarga y guarda las imágenes sí existen y de lo contrario no hace nada
def isNAN (value,path):
    # Evaluar que exista el link en la celda de excel
    if value != value:
        print('sin imagen ->'+path+'.jpeg')
    else:
        image = open(path+'.jpeg','wb')  
        response = requests.get(value)
        image.write(response.content)
        image.close() 
        print('imagen descargarda -> '+path+'.jpeg')

index = 0

while index < len(Id) :
    try:
        # Crear el directorio exist_ok=True sobrescribe los directorios sin borrar nada y no da error
        paths= '853/'+str(Id['PROYECTO_ID'][index])+'/images/'
        os.makedirs(paths, exist_ok=True)
        # Descargar las imágenes usando el nombre de la columna -> Image 1
        # Funciona bien sí el nombre de la columna es la fila 1 y los datos parten de la fila 2 en adelante
        print(":::::::::::::::::::: FILA "+str(index+1)+' ::::::::::::::::::::::::::')
        isNAN(im1['Image 1'][index],paths+nombreImagen[0])
        isNAN(im2['Image 2'][index],paths+nombreImagen[1])
        
            
    except Exception as e:
        
        logger.error('Error al descargar la imagen. Error tipo: '+str(e))

    index = index+1
print("Descarga completada")







