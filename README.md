# Apache Log Analysis Using Spark

## 1. Project Introduction
This project analyzes Apache web server access logs using PySpark. The project processes the `access.log` file and extracts useful information such as HTTP methods, HTTP status codes, total request count, and overall web traffic patterns.

## 2. Problem Statement
Apache web server logs contain a large amount of request and response information. Analyzing these logs manually can be difficult and time-consuming.

The objective of this project is to use PySpark to process the Apache `access.log` file and perform log analysis efficiently.

## 3. Dataset
The dataset used in this project is an Apache web server access log file.

**Dataset file:**

```text
data_sets/Apache_web_log/access.log
```

The log contains web server request information such as:

* IP address
* HTTP request method
* Requested resource
* HTTP status code
* Request information

Additional dataset information is available in:

```text
docs/dataset_info.txt
```

## 4. Technologies Used
* Python
* PySpark
* Apache Spark
* Linux
* Regex
* Parquet

## 5. Project Architecture / Flow
```text
Apache access.log
       |
       v
   PySpark
       |
       v
Regex-based Log Parsing
       |
       v
Structured DataFrame
       |
       +----------------------+
       |                      |
       v                      v
HTTP Method Analysis    Status Code Analysis
       |                      |
       +----------+-----------+
                  |
                  v
          Total Records Count
                  |
                  v
          Save Data as Parquet
```

## 6. Implementation / Processing
The project is implemented using PySpark.

### Processing Steps
1. Read the Apache `access.log` file.
2. Parse the log records using regular expressions.
3. Extract relevant information from each log record.
4. Convert the parsed data into a structured DataFrame.
5. Analyze HTTP methods.
6. Analyze HTTP status codes.
7. Calculate the total number of records.
8. Save the processed data in Parquet format.

The main PySpark script is:

```text
spark_scripts/log_analysis.py
```
## 7. My Role
I worked on the complete log analysis pipeline, including:

- Read the Apache access log using PySpark.
- Parsed raw log records using regular expressions.
- Extracted relevant fields from log records.
- Created a structured Spark DataFrame.
- Performed HTTP method and status code analysis.
- Calculated the total number of log records.
- Saved the processed data in Parquet format.

## 8. Analysis Performed
The following analysis is performed on the Apache access log:

### HTTP Method Analysis
Counts the occurrences of HTTP request methods such as:

* GET
* POST
* HEAD

### Status Code Analysis
Analyzes HTTP response status codes returned by the web server.

Examples include:

* 200
* 404
* 500

### Total Records Count
Calculates the total number of processed log records.

## 9. Output / Results
The processed data is saved in Parquet format at:

```text
output/log_analysis_parquet/
```

The output directory contains Parquet part files and the Spark `_SUCCESS` marker.

Screenshots of the analysis and output are available in:

```text
docs/analysis_screenshots/
```

Available screenshots include:

* `method_count1.png`
* `parquet_save1.png`
* `spark_output1.png`
* `status_code_analysis1.png`
* `total_count1.png`

## 10. Challenges & Learning
### Challenges
* Apache log records are stored as raw text, so the required fields need to be extracted from the log format.
* Regular expressions are required to parse the log records correctly.
* Large log files can be difficult to process manually.

### Learning
Through this project, I gained practical experience in:

* Processing log data using PySpark
* Parsing unstructured text using regular expressions
* Working with Spark DataFrames
* Performing data analysis using PySpark
* Saving processed data in Parquet format
* Running PySpark applications using `spark-submit`

## 11. Project Structure
```text
.
├── data_sets
│   └── Apache_web_log
│       └── access.log
├── docs
│   ├── analysis_screenshots
│   │   ├── method_count1.png
│   │   ├── parquet_save1.png
│   │   ├── spark_output1.png
│   │   ├── status_code_analysis1.png
│   │   ├── total_count1.png
│   └── dataset_info.txt
├── output
│   └── log_analysis_parquet
│       ├── part-00000-*.snappy.parquet
│       ├── part-00001-*.snappy.parquet
│       ├── part-00002-*.snappy.parquet
│       ├── part-00003-*.snappy.parquet
│       └── _SUCCESS
├── README.md
└── spark_scripts
    └── log_analysis.py
```
## 12. Conclusion
This project demonstrates how PySpark can be used to process and analyze Apache web server logs.
The project provided practical experience in regular expression-based log parsing, Spark DataFrame processing, HTTP request and status code analysis, and Parquet-based data storage.

## 13. How to Run
```bash
spark-submit log_analysis.py
```
