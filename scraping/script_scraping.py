import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la página de Yahoo Finance que quieres scrapear
url = "https://finance.yahoo.com/markets/stocks/losers/"

# Enviar una solicitud GET a la página
response = requests.get(url)

# Comprobar que la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML de la página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar todos los spans con la clase 'yf-42jv6g'
    fin_streamers = soup.find_all('span', class_='yf-42jv6g')

    # Almacenar los datos en una lista
    organized_data = []
    data = []

    # Recorrer los elementos encontrados y organizar los datos
    for i, streamer in enumerate(fin_streamers):
        text = streamer.get_text(strip=True)  # Eliminar espacios en blanco extra

        # Almacenar temporalmente los datos de cada acción
        if i % 9 == 0:
            # Si ya tenemos datos en la lista, agregar el conjunto anterior
            if data:
                organized_data.append(data)
            # Iniciar un nuevo conjunto de datos
            data = [text]
        else:
            # Agregar los datos correspondientes al conjunto actual
            data.append(text)
    
    # Agregar el último conjunto de datos si existe
    if data:
        organized_data.append(data)

    # Mostrar los datos organizados
    for entry in organized_data:
        if len(entry) == 9:  # Asegurarse de que haya 9 elementos por entrada
            data_dict = {
                'Nombre': entry[0],
                'Último Precio': entry[1].split('-')[0],
                'Cambio': entry[2],
                '% Cambio': entry[3],
                'Volumen': entry[4],
                'Vol. Prom. (3 meses)': entry[5],
                'Cap. de Mercado': entry[6],
                'Ratio P/E (TTM)': entry[7],
                'Rango 52 semanas': entry[8]
            }
            print(data_dict)
        else:
            print(f"Entrada incompleta: {entry}")

else:
    print(f"Error al hacer la solicitud: {response.status_code}")
print(data_dict)

print('')


