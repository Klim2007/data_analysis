import requests
import pandas as pd
import matplotlib.pyplot as plt
import datetime
def get_last_rate(amount,currency,converted_currency,days_back):
    today_date = datetime.datetime.now()
    last_date = today_date-datetime.timedelta(days_back)
    url = f'https://api.exchangerate.host/timeseries'
    payload = {'base':currency,'amount':amount,'start_date':last_date.date(),'end_date':today_date.date()}
    response = requests.get(url, params=payload)
    data = response.json()
    #- create dict to stroe values
    currency_history = {}
    rate_history_array = []
    # fill in dicts
    for item in data['rates']:
        current_date = item
        currency_rate = data['rates'][item][converted_currency]
        currency_history[current_date] = [currency_rate]
        rate_history_array.append(currency_rate)
    # getting needly value using pandas
    pd_data = pd.DataFrame(currency_history).transpose()
    pd_data.columns = ['rate']
    pd.set_option('display.max_rows',None)
    y = int(pd_data['rate'].values[0])
    return y

