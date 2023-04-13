
## Spider


## 


## Librerias:

Tragajando en Python se utilizan las librerias:
 - Beautiful Soup (BSS4)
 - Exifread para lectura de metadatos


 Las imagenes se pueden descargar en una carpeta comun.



### En Python
 Para leer los metadatos de una imagen utilizando ExifRead en Python, puedes seguir los siguientes pasos:

Instala la biblioteca ExifRead utilizando el comando pip install exifread.
Abre la imagen utilizando la función open() de Python y luego lee sus metadatos utilizando la función exifread.process_file().
Accede a los metadatos utilizando el diccionario devuelto por la función exifread.process_file().
Aquí hay un ejemplo de cómo puedes leer los metadatos de una imagen utilizando ExifRead:

import exifread

image_path = "ruta/a/la/imagen.jpg"
with open(image_path, "rb") as image_file:
    tags = exifread.process_file(image_file)
    for tag in tags.keys():
        if tag not in ("JPEGThumbnail", "TIFFThumbnail", "Filename", "EXIF MakerNote"):
            print(f"{tag}: {tags[tag]}")
Espero que esto te ayude!