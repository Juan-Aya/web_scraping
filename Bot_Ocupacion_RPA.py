# Importar las librerias nesesarias para la ejecución del bot
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import shutil
import zipfile
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine, inspect
from datetime import datetime
import calendar
import locale
import builtins


# Lista para almacenar los mensajes
mensajes = []

# Redefinir la función print() para guardar los mensajes
def print(*args, **kwargs):
    mensaje = ' '.join(map(str, args))
    mensajes.append(mensaje)
    builtins.print(*args, **kwargs)  # Imprimir en la consola si es necesario

# Guardar los mensajes en un archivo CSV
def guardar_mensajes_en_csv(filename):
    df = pd.DataFrame({'Mensajes': mensajes})
    df.to_csv(filename, index=False)


# Establecer la configuración regional en español
locale.setlocale(locale.LC_TIME, 'es_ES')


# ---------- Primer inserción  encuesta de satisfacion ------------------------------------------------\

# Configuración de la conexión a la base de datos
cnx = mysql.connector.connect(user='juanaya6582', password='gZ%vsFWmf6%ANuU8',
                              host='172.17.8.68', database='bbdd_groupcos_bog_rpa')

cnx1 = mysql.connector.connect(user='juanaya6582', password='gZ%vsFWmf6%ANuU8',
                              host='172.70.7.60', database='bbdd_groupcos_repositorio_rpa')



# Abrir el navegador  webdriver
driver = webdriver.Chrome()

#Abrir el enlace de nition.so/login 
driver.get("https://www.notion.so/login")

# Tiempo de espera de para que cargue la pagina
time.sleep(4)

# "ID_DEL_ELEMENTO" de ingreso de correo como Usuario  se adiciona el correo y se da continuar con un ENTER
paso2 = driver.find_element(By.ID, "notion-email-input-2")
paso2.send_keys("juan.aya@groupcos.com.co")
paso2.send_keys(Keys.ENTER)

# Tiempo de espera de para que cargue la siguiente opción
time.sleep(2)

# "ID_DEL_ELEMENTO" de el ingreso de contraseña, se ingrsa la contraseña y se le indica selecionar Enter para continuar 
paso3 = driver.find_element(By.ID, "notion-password-input-1")
paso3.send_keys("Cos2023*")
time.sleep(2)
paso3.send_keys(Keys.ENTER)

print("Termino Loguin Satisfactoriamente")
# Tiempo de espera de para que cargue la la pgina de notión y sus opciones 
time.sleep(5)

# Selección de boton para selecionara el area de trabajo   
paso4 = driver.find_element(By.CLASS_NAME, "notion-sidebar-switcher")
paso4.click()

# Tiempo de espera de para que cargue la pgina de notión y sus opciones 
time.sleep(2)

# Selecciona la area de trabajo de RPA
paso4.send_keys(Keys.ARROW_DOWN)
paso4.send_keys(Keys.ARROW_DOWN)
paso4.send_keys(Keys.ARROW_DOWN)
paso4.send_keys(Keys.ENTER)
time.sleep(10)

# Seleciona la opción de estiñlos exportacion y mas 
paso6 = driver.find_element(By.CLASS_NAME, "dots")
paso6.click()

# Slecciona la opcion de exportar 
paso7 = driver.find_element(By.CLASS_NAME, "file")
paso7.click()

# Tiempo de espera de para que cargue la ventana emergente de exportación 
time.sleep(3)

# Seleciona la opción de incluir base de datos todo 
driver.switch_to.active_element.send_keys(Keys.TAB)
driver.switch_to.active_element.send_keys(Keys.TAB)
driver.switch_to.active_element.click()
driver.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
driver.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
driver.switch_to.active_element.send_keys(Keys.ENTER)

# Seleciona el el primer checkbox y lo activa 
driver.switch_to.active_element.send_keys(Keys.TAB)
driver.switch_to.active_element.send_keys(Keys.TAB)
driver.switch_to.active_element.click()

# Seleciona el el sugundo checkbox y lo activa 
driver.switch_to.active_element.send_keys(Keys.TAB)
ActionChains(driver).send_keys(Keys.SPACE).perform()
driver.switch_to.active_element.click()

# Seleciona el boton de exportar y exporta la informacion que se nesecita para el informe de ocupación
driver.switch_to.active_element.send_keys(Keys.TAB)
driver.switch_to.active_element.send_keys(Keys.TAB)
driver.switch_to.active_element.click()
time.sleep(30)

#Cerrar la pagina que se Abrio 
driver.close()

print("Termino Satisfactoriamente la descaraga")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# PROCESO DE OBTENCIO DEL ARCHIVO DESCARGADO DESCOMPRIMARI Y GUARDAR EL LA CARPETA DESEADA

# Ruta de la carpeta de descargas
carpeta_descargas = "C:\\Users\\Juan.Aya\\Downloads"

# Obtener la lista de archivos en la carpeta de descargas
archivos_descargas = os.listdir(carpeta_descargas)

# Filtrar solo los archivos comprimidos (ZIP)
archivos_zip = [archivo for archivo in archivos_descargas if archivo.endswith(".zip")]

# Ordenar la lista de archivos ZIP por fecha de modificación descendente
archivos_zip.sort(key=lambda x: os.path.getmtime(os.path.join(carpeta_descargas, x)), reverse=True)

if len(archivos_zip) > 0:
    # Obtener la ruta completa del archivo ZIP más reciente
    archivo_zip_mas_reciente = os.path.join(carpeta_descargas, archivos_zip[0])

    # Crear una carpeta para la extracción
    carpeta_destino = "C:\\Users\\Juan.Aya\\Documents\\Proyectos\\Ocupacion\\Data"
    os.makedirs(carpeta_destino, exist_ok=True)

    # Descomprimir el archivo ZIP en la carpeta de destino
    with zipfile.ZipFile(archivo_zip_mas_reciente, 'r') as archivo_zip:
        archivo_zip.extractall(carpeta_destino)
else:
    print("No se encontraron archivos ZIP en la carpeta de descargas.")

print('Actualizacion de la info local satisfactoria')


# Obtener la fecha final del mes actual
fecha_actual = datetime.now()

# Obtener el último día del mes actual
ultimo_dia_mes_actual = calendar.monthrange(fecha_actual.year, fecha_actual.month)[1]

# Crear una nueva fecha con el último día del mes actual
fecha_final_mes_actual = fecha_actual.replace(day=ultimo_dia_mes_actual)

# Formatear la fecha en el formato deseado
fecha_final_formateada = fecha_final_mes_actual.strftime('%Y-%m-%d')

print(fecha_actual)

# ------------TRANSFORMACION DE LA INFORMACIÓN EN UN DF ----------------------------------------


# Ruta del archivo CSV
csv_path = 'C:\\Users\\Juan.Aya\\Documents\\Proyectos\\Ocupacion\\Data\\CONTROL RPA 02ea76e2bedd4a6da97cce873f3f74f3\\Historial Solicitudes 2023 b7f46579a9aa4dd5963c95f35649eeb3_all.csv'
print('obtencion de la informacion satisfactoria')
# Leer el archivo CSV
if os.path.isfile(csv_path):
    df = pd.read_csv(csv_path)
else:
    print('El archivo CSV no existe en la ruta especificada')

df['Last edited time'] = pd.to_datetime(df['Last edited time'], format="%d de %B de %Y %H:%M")
df['Created time'] = pd.to_datetime(df['Created time'], format="%d de %B de %Y %H:%M")
df['FECHA DE ENTREGA'] = pd.to_datetime(df['FECHA DE ENTREGA'], format="%d de %B de %Y")
df['FECHA DE INICIO'] = pd.to_datetime(df['FECHA DE INICIO'], format="%d de %B de %Y")
df['FECHA DE APROBADO'] = pd.to_datetime(df['FECHA DE APROBADO'], format="%d de %B de %Y")    


# Dividir la columna "nombre_desarrollador" en varias columnas
df[['Desarrollador_1', 'Desarrollador_2', 'Desarrollador_3']] = df['Nombre Desarrollador'].str.split(',', expand=True)


# Llenar las fechas vacías con la fecha final del mes actual
df['FECHA DE ENTREGA'].fillna(fecha_final_formateada, inplace=True)
df['Dias']=(df['FECHA DE ENTREGA']-df['FECHA DE INICIO']).dt.days
df['HORAS_DESARROLLO'] = (df['Dias']/7)*50
df['HORAS_DESARROLLO'] = df['HORAS_DESARROLLO'].round(decimals=0)

df= df.drop('HORAS DE DESARROLLO',axis=1)
df=df.rename(columns={'HORAS_DESARROLLO':'HORAS DE DESARROLLO'})




# Guardar el dataframe en un archivo CSV
df.to_csv('C:\\Users\\Juan.Aya\\Documents\\Proyectos\\Ocupacion\\Data\\CONTROL RPA 02ea76e2bedd4a6da97cce873f3f74f3\\Historial Solicitudes 2023 b7f46579a9aa4dd5963c95f35649eeb3_all.csv', index=False)
print("Conversion de la onformacion satisfactoria")

# ------------------segunda inserción base de datos rendimiento del agente ------------------------------------------------------------------

# SQL para borrar los registros existentes
sql1 = "TRUNCATE TABLE tb_ocupacion_rpa;"

# Ejecutar la consulta en la primera conexión
cursor = cnx.cursor()
cursor.execute(sql1)
cnx.commit()

# Ejecutar la consulta en la segunda conexión
cursor1 = cnx1.cursor()
cursor1.execute(sql1)
cnx1.commit()


# Derección de donde se encuentra el archivo "csv" 
df1 = pd.read_csv('C:\\Users\\Juan.Aya\\Documents\\Proyectos\\Ocupacion\\Data\\CONTROL RPA 02ea76e2bedd4a6da97cce873f3f74f3\\Historial Solicitudes 2023 b7f46579a9aa4dd5963c95f35649eeb3_all.csv')

df1 = df1.fillna(0)  # Reemplazar NaN con 0

# Condición para el cargue de la base "csv" a la base de datos  "bbdd_cos_bog_hikvision"
for index, row in df1.iterrows():

    # Construcción de la consulta SQL utilizando la cláusula \"INSERT INTO\" para insertar siempre un nuevo registro
    sql2 = """
        INSERT IGNORE INTO tb_ocupacion_rpa (ID_PROYECTO,NOMBRE_SOLICITUD,Nombre_Coodinardor,Nombre_Desarrollador,TEAM_DESARROLLADOR,COORDINADOR,DESARROLLADOR,ESTADO,FECHA_APROBADO,FECHA_INICIO,FECHA_ENTREGA,TIPO_SOLUCION,TIPO_SOLICITUD,CLIENTE,SERVIDOR,HORAS_DESARROLLO,OBSERVACIONES,ANOTACIONES,HORAS_CALCULO,Created_time,Created_by,Last_edited_time,Desarrollador_1,Desarrollador_2,Desarrollador_3,Motivo_Tardanza,MPV_1,MPV_2,MPV_3,MPV_4,MPV_5)
        VALUES (%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,%s,%s,%s,%s,%s,%s)
    """

    # Ejecución de la consulta
    cursor = cnx.cursor()
    cursor.execute(sql2, (row['ID PROYECTO '], row['NOMBRE SOLICITUD'], row['Nombre_Coodinardor '], row['Nombre Desarrollador'], row['TEAM DESARROLLADOR'], row['COORDINADOR'], row['DESARROLLADOR'], row['ESTADO'], row['FECHA DE APROBADO'], row['FECHA DE INICIO'], row['FECHA DE ENTREGA'], row['TIPO SOLUCION'], row['TIPO SOLICITUD'], row['CLIENTE'], row['SERVIDOR'], row['HORAS DE DESARROLLO'], row['OBSERVACIONES'], row['ANOTACIONES'], row['HORAS CALCULO'],row['Created time'],row['Created by'],row['Last edited time'],row['Desarrollador_1'],row['Desarrollador_2'],row['Desarrollador_3'],row['Motivo de Tardanza '],row['MPV_1'],row['MPV_2'],row['MPV_3'],row['MPV_4'],row['MPV_5']))
    cnx.commit()


    cursor1=cnx1.cursor()
    cursor1.execute(sql2,(row['ID PROYECTO '], row['NOMBRE SOLICITUD'], row['Nombre_Coodinardor '], row['Nombre Desarrollador'], row['TEAM DESARROLLADOR'], row['COORDINADOR'], row['DESARROLLADOR'], row['ESTADO'], row['FECHA DE APROBADO'], row['FECHA DE INICIO'], row['FECHA DE ENTREGA'], row['TIPO SOLUCION'], row['TIPO SOLICITUD'], row['CLIENTE'], row['SERVIDOR'], row['HORAS DE DESARROLLO'], row['OBSERVACIONES'], row['ANOTACIONES'], row['HORAS CALCULO'],row['Created time'],row['Created by'],row['Last edited time'],row['Desarrollador_1'],row['Desarrollador_2'],row['Desarrollador_3'],row['Motivo de Tardanza '],row['MPV_1'],row['MPV_2'],row['MPV_3'],row['MPV_4'],row['MPV_5']))
    cnx1.commit()

print('Cargue de la información satisfactorio')

# Cerrar el cursor y la conexión a la base de datos
cursor.close()
cnx.close()

print("finalizo")
# Guardar los mensajes en un archivo CSV
guardar_mensajes_en_csv('output.csv')