import pyarrow.parquet as pq 

table = pq.read_table('taxi.parquet')

df = table.to_pandas()

df.dtypes

df.head()