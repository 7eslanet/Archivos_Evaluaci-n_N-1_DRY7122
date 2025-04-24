#!/bin/bash

ls -ltr * >  contenidoDirectorio.txt 
var2="$(find . -type f | wc -l)"
echo "La cantidad total de archivos contenidos en todos los directorios y subdirectorios es $var2" >>  contenidoDirectorio.txt
