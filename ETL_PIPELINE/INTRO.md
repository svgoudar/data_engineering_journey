
# ETL Fundamentals

## Introduction

Welcome to ETL Fundamentals.

## Learning Objectives

After watching this video, you will be able to:

- Describe what an ETL process is
- Describe what data extraction means
- Describe what data transformation means
- Describe what data loading means
- List use cases for ETL processes

## What is an ETL process?

ETL stands for **Extract, Transform, and Load**. It's a methodology used to curate data from multiple sources, transform it into a unified format, and load it into a new environment for analytics purposes.

### Extraction

- Extracting data involves reading data from one or more sources.
- Common methods include web scraping and using APIs.

### Transformation

- Data transformation involves processing data to conform to the needs of the target system and use case.
- This includes cleaning, filtering, joining, feature engineering, and formatting.

### Loading

- Data loading is the process of writing data to a new destination such as databases or data warehouses.
- The goal is to make data available for analytics applications.

## Use Cases for ETL

ETL processes are vital for:

- Digitizing analog data like documents and tapes.
- Capturing transaction history from OLTP systems for analysis in OLAP systems.
- Preparing data for ingestion by dashboards and machine learning models.

# ELT Basics

## What is an ELT process?

ELT stands for **Extract, Load, and Transform**. It's a methodology for automated data pipeline engineering. Unlike ETL, ELT involves loading data directly into the destination before transforming it.

### Extraction

- Data is obtained from all sources.
- The extraction process reads data into an application, often asynchronously.

### Loading

- Raw data is loaded as-is into the destination, such as a data lake.

### Transformation

- Data is transformed on demand within the modern analytics platform, enabling dynamic and interactive data handling.

## Use Cases for ELT

ELT is well-suited for:

- Managing large-scale Big Data implementations.
- Performing real-time analytics on streaming data.
- Integrating highly distributed data sources globally.

## Why is ELT emerging?

- **Cloud Computing:** Rapid evolution to meet Big Data demands, offering scalable and cost-efficient resources.
- **Speed and Flexibility:** Less data movement means better performance; ELT provides flexibility for building various data products.
- **No Information Loss:** Working with a replica of source data in the cloud ensures that all information is retained.

# Comparing ETL and ELT

## Differences between ETL and ELT

- **Transformation Order**: ETL processes transform data before loading, while ELT transformations occur after data is loaded into the destination.
- **Flexibility**: ETL is typically a fixed process, whereas ELT allows for more self-serve analytics flexibility.
- **Big Data Handling**: ETL is suited for structured, relational data and can struggle with scalability. ELT can handle all data types and scales better with cloud services.
- **Time-to-Insight**: ETL requires changes to be implemented by development teams, delaying insights. ELT empowers end users to directly access and analyze raw data.

## ELT as an Evolution of ETL

- **Democratizing Data**: ELT meets the demand for making raw data accessible to a wider enterprise user base.
- **From Staging to Data Lakes**: Traditional ETL staging areas resemble data lakes but are not typically shared across a company. ELT leverages data lakes for broader access and manipulation.
- **Tools and Accessibility**: Modern analytics tools have made data sources accessible to less technical users, supporting the shift to self-service data platforms.

## The Trend from ETL to ELT

- **Meeting Modern Demands**: ELT addresses challenges like long time-to-insight and scalability issues presented by Big Data.
- **Breaking Down Silos**: ELT moves away from the siloed nature of conventional ETL.
- While ETL still plays a role in data product development, the trend favors the modern, flexible ELT approach for real-time, ad-hoc analytics.

# Data Extraction Techniques

## Examples of Raw Data Sources

- Archived text and images from paper documents and PDFs
- Web pages, including text, tables, images, and links
- Analog audio and video on media or streaming in real time
- Survey, statistical, and economic data
- Transactional data from various industries
- Event-based data like social media streams
- Weather data from station networks
- IoT sensor streams
- Medical records, including treatments and images
- Personal genetic data from DNA and RNA samples

## Data Extraction Techniques

- **OCR**: Converts scanned text into a computer-readable format.
- **ADCs**: Digitizes analog audio recordings and signals.
- **CCDs**: Captures and digitizes images.
- **Polling and Census**: Gathers opinions and vital data.
- **Behavioral Tracking**: Uses cookies and logs to track activities.
- **Web Scraping**: Searches for content on web pages.
- **APIs**: Accesses online data repositories and feeds.
- **SQL/NoSQL**: Queries structured and non-structured data.
- **Edge Computing**: Processes raw data on the device to extract features.
- **Biomedical Devices**: Extracts DNA sequences and medical data.

## Use Cases with Data Sources and Extraction Techniques

- **Central Repository Integration**: Using APIs to integrate structured data from multiple sources.
- **History Archiving**: Capturing events via APIs for a historical record.
- **IoT Data Optimization**: Employing edge computing to minimize data redundancy from devices.
- **Medical Diagnostics**: Utilizing imaging devices and sensors for health data acquisition.

# Introduction to Data Transformation Techniques

## Data Transformation Techniques

Data transformation adjusts data to fit the needs of an application, involving operations such as:

- **Data Typing**: Casting data to types like integer, float, string, object, and category.
- **Data Structuring**: Converting data formats (e.g., JSON, XML, CSV) to database tables.
- **Anonymizing and Encrypting**: Transformations for privacy and security.
- **Cleaning**: Removing duplicates and filling missing values.
- **Normalizing**: Ensuring comparable units (e.g., standardizing currency).
- **Filtering, Sorting, Aggregating, Binning**: Preparing data for access and analysis.
- **Joining/Merging**: Combining data from different sources.

## Schema-on-Write vs. Schema-on-Read

- **Schema-on-Write**: Traditional ETL method requiring data to conform to a pre-defined schema before loading. It offers stability and quick queries but limits data versatility.
- **Schema-on-Read**: Modern ELT approach applying schema after data is read from storage. It provides versatility and access to more data without rigorous pre-processing.

## Information Loss in Transformation

Information can be "lost in transformation" either intentionally or accidentally. Examples include:

- **Lossy Data Compression**: Reducing data precision or bitrate can lead to loss.
- **Filtering**: Permanent filtering may discard valuable data subsets.
- **Aggregation**: Summarizing data (e.g., yearly averages) can remove finer details.
- **Edge Computing Devices**: Devices streaming only alarm signals instead of raw data could miss information.

# Data Loading Techniques

## Data Loading Techniques

- **Full Loading**: Loading all data at once, often used to initialize a new database.
- **Incremental Loading**: Appending new or updated data to an existing dataset.
- **Scheduled Loading**: Loading data based on a predefined schedule.
- **On-Demand Loading**: Triggered by specific events or conditions.

## Batch vs. Stream Loading

- **Batch Loading**: Data is loaded in chunks at regular intervals, suitable for non-real-time needs.
- **Stream Loading**: Continuously loads data in real time as it becomes available.
- **Micro-Batch Loading**: A middle ground, providing recent data for imminent processes.

## Push vs. Pull

- **Pull**: Clients request data from a server (e.g., RSS feeds, email retrieval).
- **Push**: Server sends data to clients as it becomes available (e.g., push notifications, instant messaging).

## Parallel Loading

- Utilizes multiple streams to load data simultaneously, enhancing efficiency for large datasets or distant transfers.
- Splits files into smaller chunks for concurrent loading to speed up the process.

# ETL USing shell scripting

Extraction:

Write a Bash script to call the get_temp API to extract the current temperature and append it to temperature.log.
Ensure that only the last 60 readings are kept in temperature.log by overwriting the file with the most recent hour of data.
Transformation:

Use a Python script named get_stats.py that takes the temperature.log file as input, calculates hourly average, minimum, and maximum temperatures, and outputs these stats to a file, such as temp_stats.csv.
Loading:

Include in your Bash script a step that calls the load_stats API with temp_stats.csv to load the temperature stats into the reporting system.
Scheduling:

Make the Bash script executable using chmod.
Schedule the Bash script to run every minute by creating a cron job.

```shell

#!/bin/bash

# Extract the temperature reading and append to temperature.log
get_temp >> temperature.log

# Keep only the last 60 readings (most recent hour) in temperature.log
tail -n 60 temperature.log > temp_buffer.log
mv temp_buffer.log temperature.log

# Transform the data by calculating stats and writing them to temp_stats.csv
python3 get_stats.py temperature.log temp_stats.csv

# Load the stats into the reporting system
load_stats temp_stats.csv



* * * * * /path/to/Temperature_ETL.sh

```

![img.png](dags_with_cron.png)
