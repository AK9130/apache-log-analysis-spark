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

**Approximate size:** ~168 MB
**Total records:** 1,568,097 parsed log records (1,801 additional lines did not match the log format and were removed)

The log contains web server request information such as:

* IP address
* Timestamp
* HTTP request method
* Requested resource (URL)
* HTTP status code
* Response size (bytes)

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
       v
Remove Unparsed Lines
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
3. Extract relevant information from each log record (IP, timestamp, method, URL, status, bytes).
4. Convert the parsed data into a structured DataFrame.
5. Remove log lines that did not match the regex pattern.
6. Analyze HTTP methods.
7. Analyze HTTP status codes.
8. Calculate the total number of records.
9. Save the processed data in Parquet format.

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
- Removed log lines that did not match the expected format.
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

The log file (~168 MB) was parsed with regex and analyzed in PySpark. Lines that did not match the log pattern (1,801 lines, about 0.1%) were removed.

### Key Results

- **Total log records processed:** 1,568,097
- **HTTP methods:** GET 1,564,021 (99.7%), HEAD 3,965, POST 111
- **HTTP status codes:**

| Status | Count | Share |
|---|---|---|
| 200 (OK) | 1,397,254 | 89.1% |
| 304 (Not Modified) | 134,146 | 8.6% |
| 302 (Redirect) | 26,482 | 1.7% |
| 404 (Not Found) | 10,014 | 0.6% |
| 403 (Forbidden) | 171 | <0.1% |
| 501 | 27 | <0.1% |
| 500 | 3 | <0.1% |

### Insights

- Almost all traffic is GET requests, so this server mostly serves pages and files.
- About 89% of requests succeeded (200), and about 8.6% were served from browser cache (304).
- About 10,000 requests returned 404, which points to broken or missing links.
- Server errors (500/501) are very rare (30 requests).

### Output Location
The processed data is saved in Parquet format at:

```text
output/log_analysis_parquet/
```

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
* Some log lines did not match the regex (1,801 lines), and some lines had "-" instead of a byte count. The regex was updated to accept "-", and unparsed lines were filtered out.
* Large log files can be difficult to process manually.

### Learning
Through this project, I gained practical experience in:

* Processing log data using PySpark
* Parsing unstructured text using regular expressions
* Handling unmatched records, since `regexp_extract` returns an empty string instead of an error
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
│       ├── part-0000*.snappy.parquet
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
cd spark_scripts
spark-submit log_analysis.py
```

> **Note:** The input and output paths in `log_analysis.py` are absolute paths on the local machine. Update them to match your own setup before running.
