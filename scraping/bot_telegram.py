import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time
from telegram import Bot

# Configuración del bot de Telegram
TELEGRAM_TOKEN = '7505196905:AAFrQhr9A3R4aqfDMhuGSzQWM7dVbP7ZXmo'
CHAT_ID = '1732985833'
bot = Bot(token=TELEGRAM_TOKEN)

def scrape_data():
    url = "https://finance.yahoo.com/markets/stocks/losers/"

    # Enviar una solicitud GET a la página
    response = requests.get(url)

    # Comprobar que la solicitud fue exitosa
    if response.status_code == 200:
        # Parsear el contenido HTML de la página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar todos los spans con la clase 'yf-42jv6g'
        spans = soup.find_all('span', class_='yf-42jv6g')

        # Almacenar los valores data-value en una lista
        data_values = []
        for span in spans:
            fin_streamer = span.find('fin-streamer')
            if fin_streamer and 'data-value' in fin_streamer.attrs:
                data_value = fin_streamer['data-value']
                data_values.append(data_value)

        # Convertir la lista a un array y luego reshaping
        data_array = np.array(data_values).reshape(-1, 5)

        # Crear el DataFrame
        Valores = pd.DataFrame(data_array, columns=['Precio', 'Change_value', 'Change_porc', 'Volumen', 'MarketCap'])

        # Obtener símbolos
        data_symbols = []
        symbols = soup.find_all('span', class_='symbol yf-ravs5v')
        if symbols:
            for symbol in symbols:
                data_symbols.append(symbol.get_text())

        # Agregar la columna de símbolos al DataFrame
        Valores.insert(0, 'Símbolos', data_symbols)

        # Convertir el DataFrame a un formato legible
        message = Valores.to_string(index=False)

        # Enviar el DataFrame como mensaje en Telegram
        bot.send_message(chat_id=CHAT_ID, text=message)

    else:
        print(f"Error al hacer la solicitud: {response.status_code}")

# Ejecutar el scraping cada 20 segundos
while True:
    scrape_data()
    time.sleep(20)  # Espera 20 segundos antes de volver a ejecutar
    import requests

    TELEGRAM_TOKEN = '7505196905:AAFrQhr9A3R4aqfDMhuGSzQWM7dVbP7ZXmo'
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"

    response = requests.get(url)
    updates = response.json()

    print(updates)

    import requests

    payload = {
        'chat_id': CHAT_ID,
        'text': 'Este es un mensaje de prueba desde el bot.'
    }

    response = requests.post(url, data=payload)
    print(response.json())



    

