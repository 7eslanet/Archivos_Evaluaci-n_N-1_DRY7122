import requests
import time
seg = 60

def obtener_posicion_iss():
    url = "http://api.open-notify.org/iss-now.json"
    
    # Primera medición
    respuesta1 = requests.get(url)
    datos1 = respuesta1.json()
    latitud_1 = float(datos1['iss_position']['latitude'])
    longitud_1 = float(datos1['iss_position']['longitude'])

    print(f"Latitud_1: {latitud_1}")
    print(f"Longitud_1: {longitud_1}\n")

    time.sleep(seg)

    # Segunda medición
    respuesta2 = requests.get(url)
    datos2 = respuesta2.json()
    latitud_2 = float(datos2['iss_position']['latitude'])
    longitud_2 = float(datos2['iss_position']['longitude'])

    print(f"Latitud_2: {latitud_2}")
    print(f"Longitud_2: {longitud_2}\n")

    # Cálculo de diferencia (como estimación de velocidad)
    delta_lat = (latitud_2 - latitud_1) / seg
    delta_lon = (longitud_2 - longitud_1) /seg
    
    print(f"La velocidad estimada es {delta_lat}º de latidud y {delta_lon}º de longitud por minuto.\n")
 

# Ejecutar continuamente
while True:
    obtener_posicion_iss()