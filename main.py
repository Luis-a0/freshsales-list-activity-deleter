import csv
import requests

def delete_sales_activities(csv_file, token, url):
    # Leer los IDs de actividades desde el archivo CSV
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        activity_ids = [row[0] for row in reader]

    # Eliminar cada actividad de venta
    for activity_id in activity_ids[1:]:
        print(f"{url}/api/sales_activities/{activity_id}")
        """response = requests.delete(f"{url}/api/sales_activities/{activity_id}", 
                                   headers={"Authorization": f"Token token={token}"})
        if response.status_code == 200:
            print(f"Actividad de venta {activity_id} eliminada con éxito.")
        else:
            print(f"Error al eliminar la actividad de venta {activity_id}: {response.text}")"""

if __name__ == "__main__":
    # Solicitar nombre del archivo CSV
    csv_file = input("Ingrese el nombre del archivo CSV que contiene los IDs de las actividades de venta: ")

    # Solicitar token de acceso
    token = input("Ingrese el token de acceso: ")

    # Solicitar URL de la aplicación
    url = input("Ingrese la URL de la aplicación: ")

    # Llamar a la función para eliminar las actividades de venta
    delete_sales_activities(csv_file, token, url)
