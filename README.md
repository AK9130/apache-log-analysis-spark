##Apache Log Analysis using Spark

#Project Overview
This project analyzes Apache web server logs using PySpark to extract insights such as HTTP methods, status codes, request patterns, and overall traffic analysis.

#Project Structure

.
├── data_sets

│   └── Apache_web_log

│       └── access.

├── docs

│   ├── analysis_screenshots

│   │   ├── method_count1.png

│   │   ├── parquet_save1.png

│   │   ├── spark_output1.png
│   │   ├── status_code_analysis1.png
│   │   └── total_count1.png
│   ├── dataset_info.txt
│   └── results_summary.txt
├── output
│   └── log_analysis_parquet
│       ├── part-00000-0ae17b30-5a69-42d8-b278-24affb4f117d-c000.snappy.parquet
│       ├── part-00001-0ae17b30-5a69-42d8-b278-24affb4f117d-c000.snappy.parquet
│       ├── part-00002-0ae17b30-5a69-42d8-b278-24affb4f117d-c000.snappy.parquet
│       ├── part-00003-0ae17b30-5a69-42d8-b278-24affb4f117d-c000.snappy.parquet
│       └── _SUCCESS
├── README.md
└── spark_scripts
    └── log_analysis.py
    

#Technologies Used
- Python
- PySpark
- Apache Spark
- Linux

#Analysis Performed
- Log parsing using regex
- HTTP method analysis
- Status code analysis
- Total records count
- Data saved in Parquet format

#How to Run

```bash
cd spark_scripts
spark-submit log_analysis.py
