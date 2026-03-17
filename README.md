##Apache Log Analysis using Spark

#Project Overview
This project analyzes Apache web server logs using PySpark to extract insights such as HTTP methods, status codes, request patterns, and overall traffic analysis.

#Project Structure
- data_sets/ --> Apache access log dataset
- spark_log_analysis/ --> PySpark analysis code
- output/ --> Parquet output files
- docs/ --> Project documentation and screenshots
- README.md --> Project details

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
