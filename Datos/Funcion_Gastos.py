import requests
import pandas as pd

def obtencion_datos():
    # Endpoint para Financial Summaries (déficit/superávit fiscal)
    url_financial_summaries = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service//v1/accounting/mts/mts_table_1"

    # Parámteros para filtrar por fecha reciente (por ejemplo, datos de 2023)
    params = {
        'filter': 'record_date:gte:2010-01-01',  # 'gte' significa "greater than or equal"
        'sort': '-record_date',  # Ordenar los resultados por fecha descendente (más recientes primero)
        'page[size]': 10000  # Limitar el número de resultados
    }

    # Hacemos la solicitud a la API
    financial_data = requests.get(url_financial_summaries, params=params).json()

    financial_df = pd.DataFrame(financial_data['data'])

    # Convertir las columnas de interés a numérico
    financial_df['current_month_gross_rcpt_amt'] = pd.to_numeric(financial_df['current_month_gross_rcpt_amt'], errors='coerce')
    financial_df['current_month_gross_outly_amt'] = pd.to_numeric(financial_df['current_month_gross_outly_amt'], errors='coerce')

    # Convertir 'record_date' a formato de fecha
    financial_df['record_date'] = pd.to_datetime(financial_df['record_date'])

    # Intentamos convertir 'print_order_nbr' a numérico
    financial_df['print_order_nbr'] = pd.to_numeric(financial_df['print_order_nbr'], errors='coerce')


    # Creamos columnas de año y mes
    financial_df['year'] = financial_df['record_date'].dt.year
    financial_df['month'] = financial_df['record_date'].dt.month

    # Función para obtener la fila con el segundo valor más alto de 'print_order_nbr'
    def second_highest(group):
        return group.nlargest(2, 'print_order_nbr').iloc[-1]

    # Agrupamos por año y mes, y aplicamos la función
    result = financial_df.groupby(['year', 'month']).apply(second_highest).reset_index(drop=True)

    # Ordenamos el resultado por fecha (más reciente primero)
    Recaudacion_year_month = result.sort_values(['year', 'month'], ascending=False)

    # Mostramos el resultado
    return(Recaudacion_year_month)



