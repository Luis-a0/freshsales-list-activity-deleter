# Freshsales List Activity Deleter

Este repositorio contiene un script en Python que permite eliminar actividades de venta en Freshsales utilizando la API proporcionada por Freshworks.

## Descripción

El script facilita la eliminación masiva de actividades de venta en Freshsales utilizando un archivo .CSV que contiene una lista de IDs de actividades a eliminar. Utiliza la API de Freshsales para enviar solicitudes DELETE a la URL correspondiente con los IDs de las actividades a eliminar.

## Funcionalidades

- Eliminación masiva de actividades de venta en Freshsales.
- Interfaz de línea de comandos (CLI) para ingresar el nombre del archivo .CSV, el token de acceso y la URL de la aplicación.
- Proceso seguro que solicita confirmación antes de la eliminación de actividades.
- Manejo de errores para identificar y manejar posibles problemas durante el proceso de eliminación.

## Requisitos

- Python 3.x instalado.
- Acceso a la API de Freshsales.
- Archivo .CSV con la lista de IDs de actividades a eliminar.

## Uso

- Ejecutar el script main.py.
- Ingresar el nombre del archivo .CSV que contiene la lista de IDs.
- Ingresar el token de acceso a la API de Freshsales.
- Ingresar la URL de la aplicación de Freshsales.
- Confirmar la eliminación de actividades cuando se solicite.