# Welcome to Spark for Data Engineers

After watching this video, you'll be able to define Spark and list its key features and identify the uses of Spark by data engineers.

## What is Spark?

Spark is a distributed computing system that processes large-scale datasets. It overcomes the drawbacks of the Hadoop MapReduce framework, which was slow and ineffective for specific data processing jobs. Spark provides a unified computing engine that supports a variety of data processing tasks, such as batch processing, stream processing, machine learning, and graph processing. It uses a distributed computing model for distributing data and processing tasks across a cluster of machines.

## Key Features of Spark

1. **In-Memory Processing Capability**
   - This feature of Spark enables caching of data in the memory and eliminates the high I/O costs associated with traditional disk-based processing systems.

2. **Support for Several Programming Languages**
   - Spark supports Java, Scala, Python, and R. It offers an easy-to-use API that allows developers to construct data processing applications efficiently.
   - Additionally, Spark has built-in support for widely-used data sources like Hadoop Distributed File System (HDFS), Cassandra, and Amazon S3, further streamlining the development process.

3. **Scalability and Efficiency**
   - Spark allows the building of scalable and efficient data processing systems. Data engineers can use Spark to build data pipelines, process and analyze large datasets, and integrate with other big data technologies such as Hadoop and Apache Kafka.

## Uses of Spark by Data Engineers

Data engineers who use Spark perform the following tasks:

1. **Data Ingestion**
   - Data engineers use Spark to intake large volumes of data from sources like HDFS, cloud-based storage, databases, and streaming sources like Apache Kafka.
   - They design and implement efficient data ingestion pipelines to handle complex data structures and file formats.

2. **Data Transformation**
   - To make valuable data for analysis, engineers transform it after data intake. They use Spark's robust APIs and libraries to clean, filter, change, and aggregate data.
   - Data transformation tasks may include joining different datasets, pivoting, and aggregating data by groupings.

3. **Data Storage**
   - Data engineers design and implement data storage strategies using Spark. They leverage Spark's distributed storage system and build efficient data storage layers capable of handling petabytes of data.
   - They may use different data storage systems like HDFS, Amazon S3, or a distributed database like Apache Cassandra.

4. **Complex Data Processing**
   - Data engineers use Spark to perform complex data processing tasks like graph processing, stream processing, and machine learning.
   - They design and build data processing pipelines that handle real-time data streams and large-scale batch processing.

5. **Performance Optimization**
   - Data engineers optimize Spark performance by tuning parameters like partitioning, memory usage, and caching.
   - They may also optimize the code and data structures to boost performance and reduce resource consumption.

6. **Cluster Monitoring**
   - Data engineers monitor the Spark cluster to ensure it's running efficiently and troubleshoot any issues that may arise.
   - They employ Spark's built-in monitoring and third-party tools to track the cluster's performance, resource usage, and overall health.

In this video, you learned that Spark is a distributed computing system that processes large-scale datasets. Spark provides three main key features to data engineers. Spark assists in creating scalable and efficient data processing pipelines. It handles massive datasets and complex data structures, and data engineers can create solutions using Spark's distributed computing approach, in-memory processing, and APIs.

# Welcome to GraphFrames on Apache Spark

After watching this video, you'll be able to:

- Define graph theory.
- Define GraphFrames.
- Explore data suitable for use with GraphFrames.

## What is Graph Theory?

Graph theory is the mathematical study of modeling relationships between objects. A graph is a construct that contains a set of vertices with pairwise edges that connect one vertex to another. Graphs can be directed or undirected.

- **Directed Graph:** Contains edges with a single direction between two vertices indicating a one-way relationship, illustrated here by the use of lines with arrows. Examples include manufacturing optimization, project scheduling, train and airline route analysis, traffic recommendations, and others.
- **Undirected Graph:** Has edges that represent a relationship without a direction, illustrated here by the use of lines without arrows. Examples include social relationship analysis, marketing analysis, genomics analysis, knowledge repositories, and others.

## What are GraphFrames?

GraphFrames is an extension to Apache Spark that enables Spark to perform graph processing, run computations, and analyze standard graphs.

- **Based on Spark DataFrames:** Uses the same APIs and represents data as a DataFrame.
- **Main Difference from GraphX:** GraphFrames use DataFrames, while GraphX is based on RDDs.
- **Standard Algorithms:** Contains standard graph-based algorithms capable of covering most use cases.

## Using GraphFrames

GraphFrames is not currently included in the Spark installation and must be downloaded as a separate package. You can download and use GraphFrames with Spark automatically using the package framework. Use the Spark-packages.org website to locate the correct available versions, otherwise, the package might be unusable.

### Installation

When submitting your Spark application with `spark-submit`, include the argument `--packages` followed by the package group, name, and version as shown in the onscreen example. Remember to select the correct identifiers for your version of Spark. This onscreen example will download and use GraphFrames version 0.8.1 for Spark 3.0 with Scala version 2.12.

### Features

- **Spark SQL Integration:** Since GraphFrames is based on Spark SQL, you can use the same APIs to run SQL queries directly on the provided vertex and edge DataFrames.
- **Checkpoint Directory:** GraphFrames requires that you set a directory for checkpoints.
- **Motif Finding:** Supports motif finding, which is the search for structural patterns or a subgraph that repeats itself. The `find` method uses domain-specific language (DSL) to specify the search query in terms of edges and vertices.

### Supported Algorithms

GraphFrames currently supports the following widely used algorithms:

- Breadth-first search (BFS)
- Connected components
- Label Propagation Algorithm (LPA)
- PageRank
- Shortest paths
- Triangle count

#### Example: PageRank

A notable everyday use of an algorithm is PageRank. As reported by Wikipedia, PageRank, originally developed by Google, is the algorithm used to measure importance and rank web pages for their search engine. For more details on how Google currently returns search results, visit the Google Search blog pages for algorithm descriptions in nontechnical but interesting detail.

## Data Suitable for GraphFrames

Generally speaking, the type of data suited for GraphFrames is any data that can be modeled with connecting relationships. You can use GraphFrames to compute the strength and direction of the relationship.

### Example

In this example, a graph where people are vertices and the relationship between people is represented by an edge with a property indicating if they are friends with a person or follow another person on a social media site. In this example, we can see that Alice and Esther are friends.

GraphFrames produces two DataFrames from this data:

- **Vertices DataFrame:** Lists the people.
- **Edges DataFrame:** Displays the relationships among the people.

You can query these DataFrames individually with Spark SQL or use any of the GraphFrames provided algorithms.

## Summary

In this video, you learned that GraphFrames allows for graph processing within Apache Spark using DataFrames. GraphFrames provides one DataFrame for graph vertices and one DataFrame for edges that can be used with Spark SQL for analysis. GraphFrames come with popular built-in graph algorithms for use with the edge and vertex DataFrames.

# Welcome to ETL Workloads with Apache Spark

After watching this video, you'll be able to:

- Define ETL: extract, transform, and load.
- Describe how to extract, transform, and load data using Apache Spark.

## What is ETL?

Extract, transform, load, abbreviated as ETL, is a common big data paradigm. ETL describes the process of moving data from a source to another destination that has a different data format or structure.

### Steps in ETL

1. **Extract:** Obtains the data from a source and reads the data into an application.
2. **Transform:** Cleans the data and changes it into a suitable format for the destination.
3. **Load:** Takes the transformed data and loads it into a data warehouse, database, or other data sink for further transformation and analysis as needed.

## Using Apache Spark for ETL

Apache Spark directly integrates the standard Big Data Ecosystem with support for native HDFS and file formats like Parquet and other data sources.

### Benefits of Spark

- **Data Cleaning and Transformation:** Easily clean and transform data after extraction using the Spark SQL framework.
- **Scalability:** Handles small to large ETL workloads with ease, allowing you to use the same application as the data sizes increase.
- **Data Source Support:** Supports HDFS data extraction from Parquet, Apache ORC, Hive, and JDBC.

### Extract Step

During the extract step, data can originate from more than one data source, such as a Parquet dataset and a Hive table. Spark has built-in support for many of the most popular data sources and an extendable data source API for extracting data from custom sources.

Here is an example of how to load a Parquet file named `People` into a DataFrame:

```python
people_df = spark.read.parquet("path/to/people.parquet")
```

### Transform Step

The goal of transformation is to clean the data after extraction, making the data more accessible and removing the need for additional cleaning and formatting. You can join DataFrames, group, and aggregate data for later ease of use.

For example, eliminating unneeded columns or trimming whitespace from strings can result in clean data in the required format and ready for loading into the new data sink. The sample below uses Spark SQL to create a view of the people dataset and then uses the select operation to transform the data to people between ages 13 and 19:

```python
people_df.createOrReplaceTempView("people")
teenagers_df = spark.sql("SELECT * FROM people WHERE age BETWEEN 13 AND 19")
```

### Load Step

The load step places your transformed data in its next repository for use, such as a data warehouse, database, or other data sinks. You can use the same Spark data sources for this process as in the extract step. For example, the load process could write the transformed DataFrame using a JDBC driver.

In this example, you first add the PostgreSQL driver to the application class path for use in the cluster. Next, you write the transformed DataFrame to a database using the supplied PostgreSQL driver and the provided username and password:

```python
teenagers_df.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://database_server:5432/dbname") \
    .option("dbtable", "teenagers") \
    .option("user", "username") \
    .option("password", "password") \
    .save()
```

### Example ETL Workflow

1. **Extract:** A Parquet file is extracted to create a DataFrame with a name column. Another data source extracts information such as age from a database into a second DataFrame.
2. **Transform:** Data stored in the name column is cleaned and transformed into two columns to separate first and last names.
3. **Load:** These two DataFrames are then joined and loaded into the data warehouse for further analysis using the new format.

# Welcome to Apache Spark Structured Streaming

After watching this video, you'll be able to:

- Define streaming data.
- Describe structured streaming.
- Identify structured streaming data sources, streaming output modes, and supported data sinks.
- Describe streaming data operations.
- Describe streaming listeners and checkpointing.

## What is Streaming Data?

Streaming data is data that is continuously generated and often originates from more than one source. Data is unavailable as a complete data set because it is continuously created. Thus, past data is often unavailable due to the volume being too large to store. As data is processed, new data arrives, requiring incremental processing.

## Apache Spark Structured Streaming

Apache Spark Structured Streaming supports the processing of streaming data using Spark SQL. It uses the same DataFrame and Dataset APIs. Spark processes the data in micro-batches or, more recently, using continuous processing. Spark Structured Streaming optimizes queries using the same Spark SQL engine.

## Structured Streaming Terms

- **Source:** Defines where data comes from, the data origination location.
- **Sink:** Specifies where to output the structured streaming data results.
- **Event Time:** The record creation time and is the timestamp at which a data point is created. It is not the same as arrival time or processing time.
- **End-to-End Latency:** The amount of time needed for the data to process from source to sink.
- **Watermarking:** Manages late data. It enables the inclusion of late-arriving data stream processing and updates results after initial data processing.

### Data Sources

Spark Structured Streaming allows for many different data sources, including:

- Files
- Kafka
- IP sockets
- Rate sources

### Data Operations

Spark Structured Streaming runs on top of the Spark SQL engine, which supports standard SQL operations, including:

- **Select**
- **Projection**
- **Aggregation on sliding windows over event time**

It supports aggregations within each window. You can also join your streams with persistent data on DataFrames or other streams.

### Output Modes

While writing data, you can specify the output mode:

- **Append:** Only add new rows of data.
- **Complete:** Deletes the existing targeted data and starts the output from the beginning.
- **Update:** Updates existing rows. This mode is especially helpful to manage late-arriving data points.

### Data Sinks

Structured Streaming supports various sinks, including:

- **File:** Outputs files to a directory.
- **Kafka:** Outputs to Kafka topics.
- **Foreach and ForeachBatch:** Apply a function to each record or batch.
- **Console and Memory:** Recommended for debugging only as these sinks are not fault-tolerant.

### Advanced Features

- **External Listeners:** Work through external frameworks or programmatically act as monitors on data streams to trigger events.
- **Checkpointing:** Compensates for node failures, recovers query progress on failure, and enables writing streams to disk.

# Welcome to Feature Extraction and Transformation

After watching this video, you'll be able to:

- Define data preprocessing.
- Describe feature extraction and list the steps for performing feature extraction using Spark.
- Describe feature transformation and list the steps required to perform feature transformation using Spark.
- Identify the importance of feature extraction and transformation.

## Data Preprocessing

Data preprocessing is a process that involves cleaning, transforming, and preparing raw data for various analytics and machine learning tasks. This process consists of several crucial steps, with feature extraction and transformation being two of the most important components.

## Feature Extraction

Feature extraction is the process of selecting or deriving relevant features from the raw data that are useful for further analysis or modeling tasks. The selected features should have a strong correlation with the target variable or capture important patterns and relationships in the data. There are several techniques available for feature extraction, including Principal Component Analysis (PCA), factor analysis, and feature engineering.

### Feature Extraction using Spark

Apache Spark, an open-source big data processing framework, supports distributed computing on large datasets. Within Spark's Machine Learning Library (MLlib), a collection of tools and algorithms is dedicated to feature extraction. MLlib offers the following feature extraction techniques:

- **Tokenization:** Splitting text data into individual words or tokens using the `Tokenizer` class.
- **TF-IDF (Term Frequency - Inverse Document Frequency):** Identifies important words in a text document using the `TF-IDF` class.
- **Word2Vec:** Represents words in a text document as vectors using the `Word2Vec` class.
- **PCA (Principal Component Analysis):** A dimensionality reduction technique that transforms high-dimensional data into a lower-dimensional space using the `PCA` class.

### Steps to Perform Feature Extraction using Apache Spark

1. Import the necessary Spark libraries such as Spark SQL and Spark ML.
2. Load the data into a Spark RDD or DataFrame.
3. Define the feature extraction technique that you want to use.
4. Convert the extracted features into a format suitable for further analysis or machine learning tasks.

## Feature Transformation

Feature transformation is the process of converting the extracted features into a suitable format for further analysis. It involves modifying or manipulating the original features to create new representations that are more suitable for analysis or modeling tasks. This step aims to improve the features' quality, distribution, or relationship, making them more informative.

### Feature Transformation Techniques in Spark

Spark provides a variety of functions and libraries for performing feature transformation on large datasets:

- **Scaling and Normalization:** Transforms numerical features into a common scale using functions like `StandardScaler`, `MinMaxScaler`, and `MaxAbsScaler`.
- **One-Hot Encoding:** Converts categorical features to numerical features using the `OneHotEncoder` function.
- **StringIndexer:** Converts categorical strings into numerical indices using the `StringIndexer` function.
- **PCA:** Reduces the dimensionality of a dataset using the `PCA` function.

### Steps to Perform Feature Transformation using Spark

1. Load the data into a Spark RDD or DataFrame.
2. Define the feature transformation technique that you want to perform.
3. Apply the transformation to the data.
4. Convert the transformed data into a format suitable for further analysis or machine learning tasks.

## Importance of Feature Extraction and Transformation

The combination of feature extraction and transformation techniques is critical for achieving reliable and meaningful results in data analysis and machine learning tasks. By appropriately selecting and transforming features, analysts can remove irrelevant information that could adversely affect the model's performance. These preprocessing steps improve the accuracy of the model and contribute to fast and efficient training and inference processes.

# Welcome to Machine Learning Pipelines Using Spark

After watching this video, you'll be able to:

- Describe machine learning pipelines and list the steps involved.
- Determine the advantages of machine learning pipelines.
- Explain machine learning pipelines using Spark and its advantages.

## Machine Learning Pipelines

Machine learning pipelines are a systematic approach to building and deploying machine learning models. A pipeline provides a structured way to organize and automate the end-to-end machine learning process from the preparation of data to the deployment of models. Machine learning pipelines involve the following steps:

1. **Data Collection and Ingestion:**
   - Acquiring data from various sources such as databases, files, APIs, and streams.

2. **Data Preprocessing:**
   - Cleaning and processing the raw data, dealing with outliers, scaling, and transforming the data into a format suitable for machine learning algorithms.

3. **Feature Extraction:**
   - Selecting the most important features from the data relevant to the machine learning task, including creating new features derived from the existing ones.

4. **Model Selection and Training:**
   - Selecting and training the appropriate machine learning model using the preprocessed data.

5. **Model Evaluation:**
   - Determining the performance of the model using various metrics such as accuracy, precision, recall, and F1-score.

6. **Model Deployment:**
   - Deploying the trained model to a production environment, creating APIs, integrating the model with other systems, and monitoring the model's performance in production.

## Advantages of Machine Learning Pipelines

- **Reproducibility:** Documenting the entire machine learning process makes it easier to reproduce and share results with others.
- **Scalability:** Pipelines can handle large volumes of data and are capable of scaling.
- **Automation:** Automating routine tasks in machine learning, such as cleaning data, extracting features, selecting models, and tuning hyperparameters, allows data scientists to focus on more complex projects.
- **Modularity and Flexibility:** Allowing data scientists to experiment with different algorithms and hyperparameters without rewriting the entire pipeline.
- **Consistency:** Ensuring consistent data preparation and modeling practices by following the same steps each time the pipeline runs.
- **Ease of Deployment:** Facilitating easy integration with deployment environments.

## Machine Learning Pipelines Using Spark

Spark MLlib is a library for machine learning in Spark that provides a set of high-level APIs for building scalable machine learning pipelines. Here are some of the key components that Spark provides at each step of the machine learning pipeline process:

### Data Ingestion

- Spark provides various data sources and APIs to ingest data from diverse sources, such as Hadoop Distributed File System (HDFS), Amazon S3, and Apache Cassandra.
- Spark's unified data processing engine allows seamless integration and parallel processing of data from different sources.

### Data Cleaning and Preprocessing

- Spark offers a wide variety of transformation functions that enable data cleaning and preprocessing operations.
- Spark efficiently handles large-scale data cleaning tasks, including handling missing values, filtering outliers, and performing data transformations with its distributed computing capabilities.

### Feature Extraction

- Spark provides a comprehensive set of feature extraction techniques and libraries for feature extraction tasks, including tokenization, TF-IDF, and word embedding.

### Model Selection and Training

- Spark provides a variety of machine learning algorithms and model training functionalities such as decision trees, random forests, and logistic regression.
- Spark enables efficient model selection and training on large datasets.

### Model Evaluation

- Spark provides evaluation metrics and tools to evaluate the performance of trained models.
- Spark's APIs allow for the calculation of various evaluation metrics, performing cross-validation, and generating performance reports.
- Spark's distributed computing capabilities facilitate efficient evaluation even on large-scale datasets.

### Model Deployment

- Spark provides various options for deploying the trained model, including exporting the model as a Java Archive (JAR) or as a Portable Format for Analytics (PFA) file.
- Spark enables seamless model deployment by allowing you to save trained models and load them for inference on new data.

## Advantages of Machine Learning Pipelines Using Spark

- **Scalability:** Spark's distributed computing framework scales to handle large volumes of data.
- **Performance:** Spark's in-memory processing and parallel execution result in quick data processing and machine learning algorithms.
- **Integration:** Spark seamlessly integrates with various big data tools and platforms, simplifying data ingestion and integration tasks.
- **Rich Ecosystem:** Spark has a rich ecosystem of libraries and tools making it easy to use.
- **Unified Interface:** Spark provides a unified programming interface that allows data scientists to work with different sources of data and machine learning algorithms in a seamless and integrated way.
