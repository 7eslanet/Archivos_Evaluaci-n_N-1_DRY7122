# Script para identificar el tipo de ACL IPv4

# Solicita al usuario que ingrese el número de ACL
acl_num = int(input("Introduce el número de ACL IPv4: "))

# Determina el tipo de ACL
if 1 <= acl_num <= 99 or 1300 <= acl_num <= 1999:
    print("La ACL es de tipo Estándar.")
elif 100 <= acl_num <= 199 or 2000 <= acl_num <= 2699:
    print("La ACL es de tipo Extendida.")
else:
    print("El número no corresponde a una lista de acceso.")
