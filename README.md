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

---

## Espa??ol

#### Descripci??n
M??dulo para establecer el siguiente nombre de fichero cuando se generan autom??ticamente una sucesi??n de ficheros. 

Cuando se generan autom??ticamente muchos ficheros, por ejemplo, los fotogramas de una escena o una serie de ficheros de texto que se desean ordenar sucesivamente pero sin usar la fecha de creaci??n, sino:
- fichero_0001.png
- fichero_0002.png
- fichero_0003.png
- ...
destiny devuelve el siguiente nombre de fichero en la secuencia. 

Acepta los siguientes par??metros:
- **src**: El fichero de origen del que se extraer??, en caso de que el destino sea un directorio, el nombre del fichero y la extensi??n para generar los nuevos nombres. En caso de que no se indique un nombre de fichero para el destino, se generar?? a partir de este. 
- **dst**: El fichero o directorio de destino. 
- **ext**: La extensi??n para los ficheros de destino, en caso de que se quiera cambiar de extensi??n. Por ejemplo, si, a partir de una imagen, se genera un v??deo, la extensi??n del fichero de origen puede ser .png y la extensi??n del fichero de destino, puede ser .mp4.
- **mkdir**: En caso de ser True, si el directorio de destino no existe, lo genera. Por defecto, su valor es *True*.
- **forced**: En caso de existir el fichero de destino, lo borra y devuelve su nombre. *Fuerza* a sobreescribir ese fichero. Por defecto, su valor es False.
- **pattern**: Patr??n para anexar al nombre del fichero que se le indica como destino. Por ejemplo, para generar pueblo_fotografia_0001.png se le indicar?? como destino 'pueblo' y como patr??n, 'fotograf??a'. Por defecto no genera nombres de fichero con patr??n. 
- **underline**: Si su valor es True, entre el nombre de fichero y el patr??n y el patr??n y el numeral (en caso de que exista el patr??n) o entre el nombre del fichero y la numeraci??n, a??adir?? un '\_'. Por defecto, su valor es *True*.
- **digits**: El n??mero de d??gitos que contendr?? la numeraci??n. Por defecto, su valor es 4. En caso de indicar 0 o '', numerar?? correlativamente con el n??mero que le corresponda: fichero_0.png, fichero_1.png, \[...], fichero_8.png, fichero_9.png, fichero_10.png, fichero_11.png, \[...], fichero_98.png, fichero_99.png, fichero_100.png, fichero_101.png...

#### Ejemplos

Crear un nombre de fichero de v??deo con extensi??n .mp4 a partir de una imagen en png para almacenar dentro de la home, en el directorio ~/videoframes/video/:
~~~
filename = destiny('./image.png', '~/videoframes/video/', ext='.mp4')
~~~
Devuelve:
~~~
/home/fernando/videoframes/video/image_0000.mp4
~~~

Crear el nombre de fichero de una imagen en un directorio donde ya hay una serie de im??genes guardadas:
~~~
filename = destiny('./image.png', '~/videoframes/')
~~~
Devuelve:
~~~
/home/fernando/videoframes/image_0172.png
~~~
**Ojo**: la numeraci??n *0172* cambia seg??n el n??mero de im??genes guardadas en ese directorio.
