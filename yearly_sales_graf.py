#from openexchangerate import OpenExchangeRates
import mysql.connector  #
import pandas as pd
import currency_pick_module as cpm

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Klim!2007",
    port = '3306',
    database = 'sakila')                                                # connection to DB

extract = "SELECT amount, DATE(payment_date) as PTDate FROM payment "    # putting our query to variable
cursor = mydb.cursor()                                                  # getting needly object
cursor.execute(extract)                                                 # executing our query
query = cursor.fetchall()                                               # fetchall method for getting all data we need
data_set = [set for set in query]                                       # fill in data from query to
df = pd.DataFrame(data_set, columns=['amount', 'pmtdate']) #index=[1]   # creating data frame and naming colums
#print(df.info)
get = cpm.get_last_rate(1, 'USD', 'KZT', 10)                           # getting needly rate as int using module / 3th value state currency u need 4th value is days back from current date
cdf = df.assign(amount_in_cur = lambda x: x.amount * get)              # creating new DF and new column  amount_in_cur
print(cdf.head(3))                                                     # checking result (taking first 3 rows)






