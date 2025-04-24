#!/bin/bash

#se genera la variable
nombre_archivo="$1"
#permisos root
sudo chmod 700 "$nombre_archivo"
#cambio de propiedad
sudo chown root "$nombre_archivo"



