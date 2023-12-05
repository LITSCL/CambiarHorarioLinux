import subprocess

#Definir la nueva fecha y hora en el formato deseado (YYYY-MM-DD HH:MM:SS).
nueva_fecha: str = "2020-12-24 18:30:05"

#Ejecutar el comando para cambiar la fecha y hora (Se debe tener permisos de administrador)
comando: str = f"date -s '{nueva_fecha}'"
subprocess.call(["sudo", "bash", "-c", comando])

print("¡El horario fue cambiado con éxito!")