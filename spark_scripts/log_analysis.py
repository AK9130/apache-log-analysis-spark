from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_extract

spark = SparkSession.builder \
    .appName("Apache Log Analysis") \
    .getOrCreate()

log_file = "file:///home/aaqib/PROJECTS/1_Apache_Log_Analysis_Using_Spark/data_sets/access.log"

df = spark.read.text(log_file)

pattern = r'(\S+) - - \[(.*?)\] "(\S+) (.*?) .*?" (\d+) (\d+)'

df_parsed = df.select(
    regexp_extract('value', pattern, 1).alias('ip'),
    regexp_extract('value', pattern, 2).alias('timestamp'),
    regexp_extract('value', pattern, 3).alias('method'),
    regexp_extract('value', pattern, 4).alias('url'),
    regexp_extract('value', pattern, 5).alias('status'),
    regexp_extract('value', pattern, 6).alias('bytes')
)

df_parsed.show(5, False)
print("Total Records:", df_parsed.count())

df_parsed.groupBy("method") \
    .count() \
    .show()

df_parsed.groupBy("status") \
    .count() \
    .orderBy("count", ascending=False) \
    .show()

df_parsed.write.mode("overwrite").parquet("file:///home/aaqib/PROJECTS/1_Apache_Log_Analysis_Using_Spark/output/log_analysis_parquet"
)

spark.stop()

#spark-submit log_analysis.py
#spark-submit log_analysis2.py > output.txt
#spark-submit log_analysis2.py | tee run_output.txt
