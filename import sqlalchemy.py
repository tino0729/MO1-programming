import sqlalchemy
import pandas as pd

data=sqlalchemy.create_engine('sqlite:////path/books.db')  


df=pd.read_sql('select title from book',data)

print(df)