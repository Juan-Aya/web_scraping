Automatización de la generación del informe de ocupación de RPA

Este proyecto automatiza la generación del informe de ocupación de RPA. El proceso se realiza de la siguiente manera:

Se descarga un archivo CSV de la base de datos de Notion que contiene la información de las solicitudes de RPA.
El archivo CSV se transforma en un DataFrame de Pandas.
Se calculan las horas de desarrollo para cada solicitud.
Se insertan los datos del DataFrame en la base de datos de RPA.
Requisitos

Python 3.8 o superior
Las bibliotecas pandas, mysql.connector, zipfile y selenium
Instalación

Instala las dependencias:
pip install -r requirements.txt
Uso

Ejecuta el script principal:
python Bot_Ocupacion_RPA.py
Explicación del código

El código se divide en las siguientes secciones:

Importación de librerías
Configuración de la conexión a la base de datos
Descarga del archivo CSV
Transformación del archivo CSV
Cálculo de las horas de desarrollo
Inserción de los datos en la base de datos
Configuración de la conexión a la base de datos

En esta sección se configura la conexión a la base de datos de RPA.

La variable cnx se utiliza para conectarse a la base de datos de RPA.
La variable cnx1 se utiliza para conectarse a la base de datos de Notion.
Descarga del archivo CSV

En esta sección se descarga un archivo CSV de la base de datos de Notion.

Se utiliza el navegador web Chrome para acceder a la base de datos de Notion.
Se seleccionan las opciones de exportación del archivo CSV.
Se descarga el archivo CSV en la carpeta Data.
Transformación del archivo CSV

En esta sección se transforma el archivo CSV en un DataFrame de Pandas.

Se leen los datos del archivo CSV.
Se convierten las fechas a formato datetime.
Se dividen las columnas Nombre Desarrollador y Observaciones.
Cálculo de las horas de desarrollo

En esta sección se calculan las horas de desarrollo para cada solicitud.

Se calcula la diferencia entre la fecha de inicio y la fecha de entrega.
Se divide el resultado entre 7 y se multiplica por 50.
Inserción de los datos en la base de datos

En esta sección se insertan los datos del DataFrame en la base de datos de RPA.

Se utiliza un bucle para insertar los datos del DataFrame en la base de datos.
Mejoras potenciales

Agregar más filtros para la descarga del archivo CSV.
Permitir la selección de la fecha de inicio y la fecha de entrega.
Enviar el informe de ocupación por correo electrónico.
Espero que este borrador sea útil. Por favor, no dudes en hacerme saber si tienes alguna pregunta o comentario.