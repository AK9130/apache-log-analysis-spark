from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_extract

# 1. Start Spark 
spark = SparkSession.builder.appName("Apache Log Analysis").getOrCreate()

# 2. Read the log file 
log_file = "file:///home/aaqib/PROJECTS/1_Apache_Log_Analysis_Using_Spark/data_sets/Apache_web_log/access.log"
df = spark.read.text(log_file)

# 3. Extract columns using regex 
pattern = r'(\S+) - - \[(.*?)\] "(\S+) (.*?) .*?" (\d+) (\d+|-)'

df_parsed = df.select(
    regexp_extract('value', pattern, 1).alias('ip'),
    regexp_extract('value', pattern, 2).alias('timestamp'),
    regexp_extract('value', pattern, 3).alias('method'),
    regexp_extract('value', pattern, 4).alias('url'),
    regexp_extract('value', pattern, 5).alias('status'),
    regexp_extract('value', pattern, 6).alias('bytes')
)

# 4. Remove bad rows
print("Empty IP rows:", df_parsed.filter(df_parsed.ip == "").count())
df_parsed = df_parsed.filter(df_parsed.ip != "")

# 5. Preview the data 
df_parsed.show(5, False)
print("Total Records:", df_parsed.count())

# 6. Count by HTTP method
df_parsed.groupBy("method").count().show()

# 7. Count by status code (high to low) 
df_parsed.groupBy("status").count().orderBy("count", ascending=False).show()

# 8. Save as Parquet 
df_parsed.write.mode("overwrite").parquet(
    "file:///home/aaqib/PROJECTS/1_Apache_Log_Analysis_Using_Spark/output/log_analysis_parquet"
)

# 9. Stop Spark 
spark.stop()

# Run:                    spark-submit log_analysis.py
# Save output to file:    spark-submit log_analysis.py > output.txt
# Screen + file both:     spark-submit log_analysis.py | tee run_output.txt
