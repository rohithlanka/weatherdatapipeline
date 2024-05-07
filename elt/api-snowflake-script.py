import requests
import json
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import pandas as pd
#place=input('Please give a place')
places=['london','chicago','aurora','tokyo','Greenland']
API_key='fdb1800c5ffd0f441c6a04e505ac7539'
col1=[]
col2=[]
col3=[]
col4=[]
col5=[]
for p in places:
    res = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={p}&appid={API_key}')
    if(res.status_code==200):
        json_data=res.json()
        for i in json_data['list']:
            col1.append(p)
            col2.append(i['dt_txt'])
            col3.append(i['weather'][0]['main'])
            col4.append(float(i['wind']['speed']))
            col5.append(float(i['main']['temp']))
datadict={'PLACE':col1,'DATE':col2,'WEATHER':col3,'WIND_SPEED':col4,'TEMP':col5}
df=pd.DataFrame(data=datadict)
ctx = snowflake.connector.connect(
    user='rohithlanka',
    password='Lanka@98',
    account='tmtbytu-ma17145',
)
database='PIPELINE1_DB'
cs = ctx.cursor()
query = f'CREATE OR REPLACE DATABASE {database};'
result=ctx.cursor().execute(query)
schema = 'PUBLIC'
table='WEATHERDATA'
fields = 'PLACE VARCHAR,DATE VARCHAR,WEATHER VARCHAR,WIND_SPEED FLOAT,TEMP FLOAT'
query=f'CREATE OR REPLACE TABLE {database}.{schema}.{table}({fields})'
result=ctx.cursor().execute(query)
query=f'use database {database};'
result=ctx.cursor().execute(query)
full_table=database+'.'+schema+'.'+table
print(f'fulll table name is {full_table}')
write_pandas(conn=ctx,df= df, table_name=table,database=database,schema=schema)
query = f'SELECT count(*) FROM {database}.{schema}.{table};'
count = ctx.cursor().execute(query).fetchone()
print(f'Snowflake table {table} has {count} rows')