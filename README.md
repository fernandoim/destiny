# destiny

## English

#### Description
Python module to create the filename of the next file to generate. 

Generate filenames when many files are automatically generated, for example, the frames of a scene or a series of text files that you want to order successively but without using the creation date, instead, they want to be saved as file_0.png, file_1.png...

Accepts the following parameters:
- **src**: The source file from which it will be extracted, in case the destination is a directory, the name of the file and the extension to generate the new names. If a file name is not specified for the destination, it will be generated from this.
- **dst**: The destination file or directory.
- **ext**: The extension for the destination files, in case you want to change the extension. For example, if a video is generated from an image, the extension of the source file can be .png and the extension of the destination file can be .mp4.
- **mkdir**: If True, if the destination directory does not exist, it generates it. By default, its value is *True*.
- **forced**: If the destination file exists, it deletes it and returns its name. It's *forced* to overwrite that file. By default, its value is False.
- **pattern**: Pattern to append to the name of the file that is indicated as destination. For example, to generate town_photography_0001.png, it will be indicated as destination 'town' and as pattern, 'photograph'. By default it does not generate patterned file names. 
- **underline**: If its value is True, between the filename and the pattern and the pattern and the numeral (in case the pattern exists) or between the filename and the numbering, it will add a '\_'. By default, its value is *True*.
- **digits**: The number of digits the numbering will contain. By default, its value is 4. If 0 or '' is indicated, it will number consecutively with the corresponding number: file_0.png, file_1.png, \[...], file_8.png, file_9.png, file_10 .png, file_11.png, \[...], file_98.png, file_99.png, file_100.png, file_101.png ...

#### Usage examples
Create a video file name with an .mp4 extension from a png image to store inside the home, in the ~/videoframes/video/ directory::
~~~
filename = destiny('./image.png', '~/videoframes/video/', ext='.mp4')
~~~
Returns:
~~~
/home/fernando/videoframes/video/image_0000.mp4
~~~

Create the filename of an image in a directory where there are already a series of saved images:
~~~
filename = destiny('./image.png', '~/videoframes/')
~~~
Returns:
~~~
/home/fernando/videoframes/image_0172.png
~~~
**Note**: 0172 changes according to the number of images stored in that directory.


~~~
filename = destiny('./image.png', '~/videoframes/video/', ext='.mp4')
~~~

## Español

#### Descripción
Módulo para establecer el siguiente nombre de fichero cuando se generan automáticamente una sucesión de ficheros. 

Cuando se generan automáticamente muchos ficheros, por ejemplo, los fotogramas de una escena o una serie de ficheros de texto que se desean ordenar sucesivamente pero sin usar la fecha de creación, sino:
- fichero_0001.png
- fichero_0002.png
- fichero_0003.png
- ...
destiny devuelve el siguiente nombre de fichero en la secuencia. 

Acepta los siguientes parámetros:
- **src**: El fichero de origen del que se extraerá, en caso de que el destino sea un directorio, el nombre del fichero y la extensión para generar los nuevos nombres. En caso de que no se indique un nombre de fichero para el destino, se generará a partir de este. 
- **dst**: El fichero o directorio de destino. 
- **ext**: La extensión para los ficheros de destino, en caso de que se quiera cambiar de extensión. Por ejemplo, si, a partir de una imagen, se genera un vídeo, la extensión del fichero de origen puede ser .png y la extensión del fichero de destino, puede ser .mp4.
- **mkdir**: En caso de ser True, si el directorio de destino no existe, lo genera. Por defecto, su valor es *True*.
- **forced**: En caso de existir el fichero de destino, lo borra y devuelve su nombre. *Fuerza* a sobreescribir ese fichero. Por defecto, su valor es False.
- **pattern**: Patrón para anexar al nombre del fichero que se le indica como destino. Por ejemplo, para generar pueblo_fotografia_0001.png se le indicará como destino 'pueblo' y como patrón, 'fotografía'. Por defecto no genera nombres de fichero con patrón. 
- **underline**: Si su valor es True, entre el nombre de fichero y el patrón y el patrón y el numeral (en caso de que exista el patrón) o entre el nombre del fichero y la numeración, añadirá un '\_'. Por defecto, su valor es *True*.
- **digits**: El número de dígitos que contendrá la numeración. Por defecto, su valor es 4. En caso de indicar 0 o '', numerará correlativamente con el número que le corresponda: fichero_0.png, fichero_1.png, \[...], fichero_8.png, fichero_9.png, fichero_10.png, fichero_11.png, \[...], fichero_98.png, fichero_99.png, fichero_100.png, fichero_101.png...

#### Ejemplos

Crear un nombre de fichero de vídeo con extensión .mp4 a partir de una imagen en png para almacenar dentro de la home, en el directorio ~/videoframes/video/:
~~~
filename = destiny('./image.png', '~/videoframes/video/', ext='.mp4')
~~~
Devuelve:
~~~
/home/fernando/videoframes/video/image_0000.mp4
~~~

Crear el nombre de fichero de una imagen en un directorio donde ya hay una serie de imágenes guardadas:
~~~
filename = destiny('./image.png', '~/videoframes/')
~~~
Devuelve:
~~~
/home/fernando/videoframes/image_0172.png
~~~
**Ojo**: la numeración *0172* cambia según el número de imágenes guardadas en ese directorio.
