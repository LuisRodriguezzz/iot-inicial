from torPublisher import publish_message
import time
from datos import capture_pe_ratios, get_falling_stocks
import schedule

publish_message('test/topic', get_falling_stocks(["AAPL", 'MSFT','GOOGL']))


# Publicar un mensaje cada 
""" while True:
    publish_message('test/topic', capture_pe_ratios(["AAPL", 'MSFT','GOOGL']))
    time.sleep(5)  # Esperar 60 segundos antes de volver a publicar """


# Programar la tarea para que se ejecute a las 4:00 PM hora del este (cierre del mercado en EE.UU.)
 
""" def job():
    publish_message('test/topic', get_falling_stocks(['MSFT', 'GOOGL', 'AAPL']))

# Programar la tarea para que se ejecute a las 4:00 PM hora del este (cierre del mercado en EE.UU.)
schedule.every().monday.at("16:00").do(job)
schedule.every().tuesday.at("16:00").do(job)
schedule.every().wednesday.at("16:00").do(job)
schedule.every().thursday.at("16:00").do(job)
schedule.every().friday.at("16:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)  # Esperar 1 segundo antes de verificar nuevamente """