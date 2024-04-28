from datetime import datetime

def transformar_fecha(fecha):
    fecha_obj = datetime.strptime(fecha, "%d/%m/%y %H:%M:%S.%f")
    fecha_formateada = fecha_obj.strftime("%Y-%m-%d %H:%M:%S.%f")
    return fecha_formateada

fecha = "20/01/24 14:35:46.830122000"
fecha_transformada = transformar_fecha(fecha)

print(fecha_transformada)  