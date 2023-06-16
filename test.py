import sqlalchemy
import pandas as pd
import pyodbc

engine = sqlalchemy.create_engine("mssql+pyodbc://IVELIN-IVANOV\SQLEXPRESS/AdventureWorksDW2019?driver=SQL+Server&integrated+security=true")

table = pd.read_sql('select * from [Books DW].dbo.DimBook', engine)

print(table)
