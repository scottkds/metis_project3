import sqlite3
import pandas as pd
from pprint import pprint

con = sqlite3.connect("customer.db")
con
df = pd.read_csv('~/p3/data/raw/telecom_churn_named.csv')
df.head()
pprint(df.columns)

df.columns = df.columns.str.replace(' ', '_')
df.head()

df.to_sql('customers', con, if_exists='append', index=False)



print("Database opened successfully")
con.execute("""create table customers (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        first_name TEXT NOT NULL,
                                        last_name TEXT NOT NULL,
                                        state TEXT DEFAULT NULL,
                                        account_length INT,
                                        area_code INT,
                                        phone_number TEXT,
                                        international_plan TEXT,
                                        voice_mail_plan TEXT,
                                        number_vmail_messages INT,
                                        total_day_minutes REAL,
                                        total_day_calls INT,
                                        total_day_charge REAL,
                                        total_eve_minutes REAL,
                                        total_eve_calls INT,
                                        total_eve_charge REAL,
                                        total_night_minutes REAL,
                                        total_night_calls INT,
                                        total_night_charge REAL,
                                        total_intl_minutes REAL,
                                        total_intl_calls INT,
                                        total_intl_charge REAL,
                                        customer_service_calls,
                                        churn INT)""")
print("Table created successfully")

sqlite3.

con.close()
