import json
from datetime import datetime

# Abrir y cargar el JSON en una variable llamada json_file
with open("myfile.json", "r") as json_file:
    ourjson = json.load(json_file)

# Extraer valores
token = ourjson["token"]
expira_en = ourjson["expira_en"]

# Calcular tiempo restante
fecha_expiracion = datetime.fromisoformat(expira_en)
ahora = datetime.now()
tiempo_restante = fecha_expiracion - ahora

# Mostrar resultados
print(f"Token: {token}")
print(f"Tiempo restante antes de que caduque: {tiempo_restante}")