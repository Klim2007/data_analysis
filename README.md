# data_analysis
my personal idea of a small data analysis project 

if you are reading this: small project is not for complicated issues resolving. It was created just to show my basic python knowlages 

while doing this project i`d learn the following: 
-  create MySQL query via python 
-  connect simple API (which is done as a  separate module, in order to use it in upcoming projects, and lear how to create and use personal modules)
-  modify data taken from data base using pandas
-  drowing visual graf via matplotlib (as a final result)

what does this code doing
project consists of 2 files
1. yearly_sales_graf.py - main code (requst to data base via mysql, creating dataframe using data from sql query and data recived from API, drowing graff (in any currency)
2. currency_pick_module.py - module with API request to get last exchange rates of currencies (so we can get the latest currency rates automatically, if you have nothing to do with currencies just ignore it) 

Note: this project will not run on your PC because data base is local, you need to state you personal access setting
    host = "localhost",
    user = "root",          -- your username
    password = "Klim!2007", -- your password
    port = '3306', 
    database = 'sakila' -- your scheme
and you need to adjust query (columns and tables) in code 
"SELECT amount, DATE(payment_date) as PTDate FROM payment " 
YOU CAN ALSO USE THIS PROJECT FOR ANY GRAF/DATASET CREATION  WHERE IN  ACTUAL CURRENCY RATES AND/OR DATA FROM DATABASE SHOULD BE USED 
