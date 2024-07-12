from snowflake.connector.pandas_tools import write_pandas
import snowflake.connector
import pandas as pd

snowflake.connector._connection = snowflake.connector.connect(
                    user='matthew.clarke@fortescue.com',
                    account='wn74261.ap-southeast-2',
                    warehouse='WH_EDW_SELFSERVICE',
                    #password=config.password,
                    authenticator='externalbrowser',
                    role='EDW_MATTHEW.CLARKE',
                    database='AA_OPERATIONS_MANAGEMENT',
                    schema='SELFSERVICE',
)

def get_df(cur, sql):
    cur.execute(sql)  # executes the sql
    return cur.fetch_pandas_all()  # returns the pandas df

cur = snowflake.connector._connection.cursor()
sql = "select top 10 * from aa_operations_hiveanalytics.selfservice.iops_vw_OPF_TONNES_WTD"
cur.execute(sql)
df = cur.fetch_pandas_all()
print(df.head)