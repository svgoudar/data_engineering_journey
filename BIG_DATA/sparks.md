
# Why Use Apache Spark

Welcome to "Why Use Apache Spark." After watching this video, you will be able to:

- Describe Apache Spark attributes
- Describe distributed computing
- List the benefits of Apache Spark and distributed computing
- Compare and contrast Apache Spark to MapReduce

## Overview of Apache Spark

- **Open-Source**: Spark is available under the Apache Foundation.
- **In-Memory**: All operations happen within the memory (RAM).
- **Distributed Data Processing**: Spark processes data across multiple machines.
- **Scalability**: Spark scales well with large datasets.
- **Programming Language**: Spark is primarily written in Scala and runs on Java virtual machines.

## What is Distributed Computing?

- **Definition**: A group of computers or processors working together.
- **Parallel vs. Distributed Computing**: 
  - Parallel computing shares all memory.
  - Distributed computing has each processor access its own memory.
![alt text](image-26.png)

## Benefits of Distributed Computing
![alt text](image-27.png)
1. **Scalability and Modular Growth**: 
   - Distributed systems can scale horizontally by adding more machines.
2. **Fault Tolerance and Redundancy**: 
   - Systems continue to function even if some nodes fail, ensuring business continuity.

## Spark and Distributed Computing

- **Spark Advantages**:
  - Large-scale data processing and analysis.
  - Parallel distributed data processing.
  - Scalability and fault-tolerance on commodity hardware.
  - In-memory processing for efficiency.
  - Flexible programming with Python, Scala, and Java APIs.

## Comparing Apache Spark to MapReduce
![alt text](image-28.png)
![alt text](image-29.png)

- **MapReduce**:
  - Iterative jobs require reads and writes to disk or HDFS.
  - Disk I/O operations are time-consuming and expensive.
- **Apache Spark**:
  - Keeps much of the data in-memory.
  - Avoids expensive disk I/O.
  - Reduces overall processing time significantly.

## Spark's Applications

- **Data Engineering**:
  - Core Spark engine, cluster management, SparkSQL, and DataFrames.
- **Data Science and Machine Learning**:
  - Libraries like SparkML and Streaming for advanced analytics.
![alt text](image-30.png)


# Functional Programming Basics

Welcome to "Functional Programming Basics!" After watching this video, you will be able to:

- Explain the term functional programming
- Explain Lambda functions
- Relate functional programming with Apache Spark

## What is Functional Programming?

Functional Programming (FP) is a style of programming that follows the mathematical function format. Think of an algebra class with the f(x) notation. 
![alt text](image-31.png)

### Key Characteristics of Functional Programming:

- **Declarative Nature**: Emphasis on the "what" of the solution rather than the "how to."
- **Expressions**: Use expressions like f(x).

### Historical Background:

- **LISP**: The first functional programming language, starting in the 1950s.
- **Modern Languages**: Scala, Python, R, and Java are some of the modern options.

## Functional Programming in Scala
![alt text](image-33.png)
![alt text](image-34.png)
- **Scala**: The most recent representative in the family of functional programming languages.
- **First-Class Functions**: Functions can be passed as arguments, returned by other functions, and used as variables.

### Example:
![alt text](image-32.png)
```scala
val increment = (x: Int) => x + 1
val numbers = List(1, 2, 3, 4)
val incrementedNumbers = numbers.map(increment)
```

This program increments each element in the list by one.

## Imperative vs. Functional Programming

### Imperative Paradigm:

- Uses explicit steps to perform tasks.
- Example: Using a "for-loop" to increment each element in an array.

### Functional Paradigm:

- Emphasizes the "what" part of the solution.
- Directly applies functions to entire lists or arrays.

## Benefits of Functional Programming

### Parallelization:

- Functional programming allows tasks to be split into multiple computing chunks (nodes) and run in parallel.
- No need to change function definitions or code to parallelize.

### Example:

- Incrementing a large array from 1 to 9 by splitting the task into three nodes running in parallel.

## Lambda Calculus

- **Lambda Calculus**: A mathematical concept where every computation is expressed as an anonymous function applied to a data set.
- **Lambda Functions**: Anonymous functions used to write functional programming code.

### Example in Scala and Python:

#### Scala:

```scala
val add = (a: Int, b: Int) => a + b
```

#### Python:

```python
add = lambda a, b: a + b
```

Both examples abstract the result directly, a hallmark of the declarative paradigm.

## Functional Programming and Apache Spark
![alt text](image-35.png)
- **Parallelization**: Spark parallelizes computations using lambda functions.
- **Scalability**: Spark programs are inherently parallel, capable of scaling from one kilobyte to one petabyte by adding more resources to the Spark cluster.

## Key Takeaways

- Functional programming follows a declarative model emphasizing "What" instead of "how to" and uses expressions.
- Lambda functions are anonymous functions that enable functional programming.
- Spark parallelizes computations using lambda calculus, making all functional Spark programs inherently parallel.



# Parallel Programming Using Resilient Distributed Datasets (RDDs)

Welcome to parallel programming using resilient distributed datasets. After watching this video, you'll be able to:

- Define resilient distributed datasets (RDDs)
- Define parallel programming
- Explain resilience in Apache Spark
- Relate RDDs and parallel programming with Apache Spark

## What is an RDD?

A resilient distributed dataset (RDD) is Spark's primary data abstraction. It is a collection of fault-tolerant elements partitioned across a cluster's nodes capable of receiving parallel operations. RDDs are immutable, meaning they cannot be changed once created.

### Key Features of RDDs:

- **Fault Tolerant**: RDDs can recover from node failures.
- **Partitioned**: Data is split across multiple nodes for parallel processing.
- **Immutable**: Data cannot be altered once created.

### Spark Applications:

Every Spark application consists of a driver program that runs the user's main functions and executes multiple parallel operations on a cluster.

### Supported File Types:

RDDs support various file types, including:
- Text
- Sequence files
- Avro
- Parquet
- Hadoop input formats

### Supported Storage Systems:

RDDs can work with:
- Local file systems
- Cassandra
- HBase
- HDFS
- Amazon S3
- Many relational and NoSQL databases

## Creating RDDs
![alt text](image-36.png)
### Methods to Create RDDs:

1. **Using External or Local Files**: 
   - From Hadoop-supported file systems like HDFS, Cassandra, HBase, or Amazon S3.

2. **Using the Parallelize Function**: 
   - Apply the parallelize function to an existing collection in the driver program.
   - This can be done in Python, Java, or Scala.

   ```scala
   // Scala example
   val data = List(1, 2, 3, 4)
   val rdd = sc.parallelize(data)
   ```

   ```python
   # Python example
   data = [1, 2, 3, 4]
   rdd = sc.parallelize(data)
   ```

   - Important: Specify the number of partitions to optimize parallel processing.

3. **Using Transformations**: 
   - Create a new RDD by applying a transformation to an existing RDD.

## Parallel Programming
![alt text](image-37.png)
### Definition:

Parallel programming is the simultaneous use of multiple compute resources to solve a computational task. It involves:

- Parsing tasks into discrete parts.
- Solving these parts concurrently using multiple processors.
- Processors accessing a shared pool of memory.

### RDDs and Parallel Programming:

RDDs enable parallel programming by distributing partitions across nodes. Spark runs one task per partition, allowing RDDs to be operated on in parallel.

## Resilience in Spark

### How RDDs Provide Resilience:

- **Immutability**: Data is always recoverable because RDDs are immutable.
- **Caching**: 
  - Persisting or caching data in memory makes future actions much faster.
  - Each node stores the partitions it computes, allowing for reuse in future actions.

### Benefits of Caching:

- **Fault Tolerance**: Cached data is fault-tolerant and recoverable.
- **Performance**: Iterative operations are significantly faster, often by more than 10 times.

## Key Takeaways

- You can create RDDs from external or local files, collections, or other RDDs.
- RDDs are immutable and always recoverable.
- Parallel programming uses multiple compute resources to solve tasks concurrently.
- RDDs can persist or cache datasets in memory, enhancing iterative operations.



# Scale Out and Data Parallelism in Apache Spark

Welcome to "Scale out and Data Parallelism in Apache Spark." After watching this video, you will be able to:

- Describe Apache Spark components.
- Describe how Apache Spark scales with big data.

## Apache Spark Architecture

Apache Spark architecture consists of three main components:

1. **Data Storage**:
   - Datasets load from data storage into memory.
   - Any Hadoop-compatible data source is acceptable.

2. **High-Level Programming APIs**:
   - Spark has APIs in Scala, Python, and Java.

3. **Cluster Management Framework**:
   - Handles the distributed computing aspects of Spark.
   - Can exist as a stand-alone server, Mesos, or YARN (Yet Another Resource Negotiator).

### Visualization of Spark Architecture

- **Data Flow**: Data from a Hadoop file system flows into the compute interface (API), which then distributes tasks across different nodes.

## Spark Core
![alt text](image-40.png)
- **Spark Core**: The base engine for large-scale parallel and distributed data processing.
  - **Functions**:
    - Manages memory and task scheduling.
    - Contains APIs used to define RDDs and other data types.
    - Parallelizes a distributed collection of elements across the cluster.
![alt text](image-38.png)
## Scaling with Big Data: Spark Application Architecture

### Components:

1. **Driver Program**:
   - Manages the Spark jobs and splits them into tasks.
   - Communicates with executors and receives task results.

2. **Executor Programs**:
   - Run on worker nodes.
   - Perform tasks assigned by the driver.
   - Can start additional processes if there is enough memory and cores available.
   - Can use multiple cores for multithreaded calculations.

### Communication:

- **Driver and Executors**: The driver submits tasks to executors and receives results upon completion.

### Organizational Analogy:

- **Driver Code**: Executive management making decisions and allocating work.
- **Executors**: Junior employees executing tasks.
- **Worker Nodes**: Physical office space where tasks are performed.

### Scaling:

- Add additional worker nodes to scale big data processing incrementally.

## Key Takeaways

- **Apache Spark Architecture**: Consists of data storage, compute input (APIs), and management (cluster framework).
- **Spark Core**: Performs large-scale parallel and distributed data processing, manages memory, schedules tasks, and houses APIs for defining RDDs.
- **Driver Program**: Communicates with the cluster and distributes RDDs among worker nodes.

![alt text](image-39.png)


# SparkSQL and DataFrames

In this video, you'll learn about SparkSQL and DataFrames. By the end, you'll be able to:

- Define SparkSQL and understand its components and benefits.
- Understand what DataFrames are, their components, and why they are beneficial.
- Explore how DataFrames work with Spark SQL.

## SparkSQL

SparkSQL is a module in Apache Spark for structured data processing. It allows interaction through SQL queries and the DataFrame API. Key points:

- Supports Java, Scala, Python, and R APIs.
- Utilizes the same execution engine for processing.
- Offers flexibility to choose the most natural API for transformations.

Example of a Spark SQL query using Python:

```sql
SELECT * FROM people;
```

- DataFrames are built on top of the Spark SQL RDD API.
- Provide optimizations like a cost-based optimizer, columnar storage, and code generation.

## DataFrames

DataFrames are collections of data organized into named columns, similar to tables in databases or data frames in R/Python. Key features:

- Conceptually equivalent to a table in a relational database.
- Built on top of Spark SQL RDD API.
- Highly scalable and support various data formats and storage systems.
- Offer optimization and code generation through a Catalyst optimizer.
- Developer-friendly, with integration across big data tooling via Spark and APIs.

Example Python code snippet to create a DataFrame from a JSON file:

```python
# Read from JSON file and create DataFrame
df = spark.read.json("file.json")
```

- Supports relational queries using RDDs.
- Enables running SQL queries on the data.

### Benefits of DataFrames:
![alt text](image-41.png)
- Highly scalable, from small to large datasets.
- Support various data formats and storage systems.
- Offer optimization through Catalyst.
- Developer-friendly with broad API support.

## Query Examples

### Example 1: Retrieving Names Column

```sql
-- SQL Query
SELECT names FROM people;
```

### Example 2: DataFrame API

```python
# DataFrame API
df.select("names")
```
![alt text](image-42.png)
### Filtering Data

To locate people above the age of 21:

```sql
-- SQL Query
SELECT * FROM people WHERE age > 21;
```

```python
# DataFrame API
df.filter(df["age"] > 21)
```

## Summary

- SparkSQL is a module for structured data processing, providing DataFrames and a SQL query engine.
- DataFrames offer similar functionality to tables in databases or data frames in R/Python, with optimizations for big data processing.


Here's the information organized in a tabular format:

| Package/Method       | Description                                                                                                                           | Code Example                                                                                               |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| `appName()`          | A name for your job to display on the cluster web UI.                                                                                 | ```python\nfrom pyspark.sql import SparkSession\nspark = SparkSession.builder.appName("MyApp").getOrCreate()\n``` |
| `cache()`            | An Apache Spark transformation often used on a DataFrame, dataset, or RDD when you want to perform multiple actions. `cache()` caches the specified DataFrame, dataset, or RDD in the memory of your cluster's workers. Since `cache()` is a transformation, the caching operation takes place only when a Spark action (for example, `count()`, `show()`, `take()`, or `write()`) is also used on the same DataFrame, dataset, or RDD in a single action. | ```python\ndf = spark.read.csv("customer.csv")\ndf.cache()\n```                                               |
| `count()`            | Returns the number of elements with the specified value.                                                                              | ```python\ncount = df.count()\nprint(count)\n```                                                             |
| `createTempView()`   | Creates a temporary view that can later be used to query the data. The only required parameter is the name of the view.               | ```python\ndf.createOrReplaceTempView("cust_tbl")\n```                                                       |
| `filter()`           | Returns an iterator where the items are filtered through a function to test if the item is accepted or not.                           | ```python\nfiltered_df = df.filter(df['age'] > 30)\n```                                                      |
| `getOrCreate()`      | Get or instantiate a SparkContext and register it as a singleton object.                                                              | ```python\nspark = SparkSession.builder.getOrCreate()\n```                                                   |
| `import`             | Used to make code from one module accessible in another. Python imports are crucial for a successful code structure. You may reuse code and keep your projects manageable by using imports effectively, which can increase your productivity. | ```python\nfrom pyspark.sql import SparkSession\n```                                                         |
| `len()`              | Returns the number of items in an object. When the object is a string, the `len()` function returns the number of characters in the string. | ```python\nrow_count = len(df.collect())\nprint(row_count)\n```                                              |
| `map()`              | Returns a map object (an iterator) of the results after applying the given function to each item of a given iterable (list, tuple, etc.) | ```python\nrdd = df.rdd.map(lambda row: (row['name'], row['age']))\n```                                      |
| `pip`                | To ensure that requests will function, the pip program searches for the package in the Python Package Index (PyPI), resolves any dependencies, and installs everything in your current Python environment. | ```python\npip list\n```                                                                                     |
| `pip install`        | The `pip install <package>` command looks for the latest version of the package and installs it.                                      | ```python\npip install pyspark\n```                                                                          |
| `print()`            | Prints the specified message to the screen or other standard output device. The message can be a string or any other object; the object will be converted into a string before being written to the screen. | ```python\nprint("Hello, PySpark!")\n```                                                                     |
| `printSchema()`      | Used to print or display the schema of the DataFrame or dataset in tree format along with the column name and data type. If you have a DataFrame or dataset with a nested structure, it displays the schema in a nested tree format. | ```python\ndf.printSchema()\n```                                                                             |
| `sc.parallelize()`   | Creates a parallelized collection. Distributes a local Python collection to form an RDD. Using range is recommended if the input represents a range for performance. | ```python\nrdd = sc.parallelize([1, 2, 3, 4, 5])\n```                                                        |
| `select()`           | Used to select one or multiple columns, nested columns, column by index, all columns from the list, by regular expression from a DataFrame. `select()` is a transformation function in Spark and returns a new DataFrame with the selected columns. | ```python\nselected_df = df.select('name', 'age')\n```                                                       |
| `show()`             | Spark DataFrame `show()` is used to display the contents of the DataFrame in a table row and column format. By default, it shows only twenty rows, and the column values are truncated at twenty characters. | ```python\ndf.show()\n```                                                                                    |
| `spark.read.json`    | Spark SQL can automatically infer the schema of a JSON dataset and load it as a DataFrame. The `read.json()` function loads data from a directory of JSON files where each line of the files is a JSON object. Note that the file offered as a JSON file is not a typical JSON file. | ```python\njson_df = spark.read.json("customer.json")\n```                                                   |
| `spark.sql()`        | To issue any SQL query, use the `sql()` method on the SparkSession instance. All `spark.sql` queries executed in this manner return a DataFrame on which you may perform further Spark operations if required. | ```python\nresult = spark.sql("SELECT name, age FROM cust_tbl WHERE age > 30")\nresult.show()\n```           |
| `time()`             | Returns the current time in the number of seconds since the Unix Epoch.                                                              | ```python\nfrom pyspark.sql.functions import current_timestamp\ncurrent_time = df.select(current_timestamp().alias("current_time"))\ncurrent_time.show()\n``` |

# Glossary

Here's the information organized in a tabular format:

| Term                                           | Definition                                                                                                                                                                                                                   |
|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Amazon Simple Storage Service (Amazon S3)      | An object store interface protocol that Amazon invented. It is a Hadoop component that understands the S3 protocol. S3 provides an interface for Hadoop services, such as IBM Db2 Big SQL, to consume S3-hosted data.          |
| Apache Spark                                   | An in-memory and open-source application framework for distributed data processing and iterative analysis of enormous data volumes.                                                                                           |
| Application programming interface (API)        | Set of well-defined rules that help applications communicate with each other. It functions as an intermediary layer for processing data transfer between systems, allowing companies to open their application data and functionality to business partners, third-party developers, and other internal departments. |
| Big data                                       | Data sets whose type or size supersedes the ability of traditional relational databases to manage, capture, and process the data with low latency. Big data characteristics include high volume, velocity, and variety.         |
| Classification algorithms                      | A type of machine learning algorithm that helps computers learn how to categorize things into different groups based on patterns they find in data.                                                                            |
| Cluster management framework                   | It handles the distributed computing aspects of Spark. It can exist as a stand-alone server, Apache Mesos, or Yet Another Resource Network (YARN). A cluster management framework is essential for scaling big data.             |
| Commodity hardware                             | Consists of low-cost workstations or desktop computers that are IBM-compatible and run multiple operating systems such as Microsoft Windows, Linux, and DOS without additional adaptations or software.                         |
| Compute interface                              | A shared boundary in computing against which two or more different computer system components exchange information.                                                                                                             |
| Data engineering                               | A prominent practice that entails designing and building systems for collecting, storing, and analyzing data at scale. It is a discipline with applications in different industries. Data engineers use Spark tools, including the core Spark engine, clusters, executors and their management, Spark SQL, and DataFrames. |
| Data science                                   | Discipline that combines math and statistics, specialized programming, advanced analytics, artificial intelligence (AI), and machine learning with specific subject matter expertise to unveil actionable insights hidden in the organization's data. These insights can be used in decision-making and strategic planning. |
| DataFrames                                     | Data collection categorically organized into named columns. DataFrames are conceptually equivalent to a table in a relational database and similar to a dataframe in R or Python, but with greater optimizations. They are built on top of the Spark SQL RDD API. They use RDDs to perform relational queries. Also, they are highly scalable and support many data formats and storage systems. They are developer-friendly, offering integration with most big data tools via Spark and APIs for Python, Java, Scala, and R. |
| Declarative programming                        | A programming paradigm that a programmer uses to define the program's accomplishment without defining how it needs to be implemented. The approach primarily focuses on what needs to be achieved, rather than advocating how to achieve it. |
| Distributed computing                          | A group of computers or processors working together behind the scenes. It is often used interchangeably with parallel computing. Each processor accesses its own memory.                                                        |
| Fault tolerance                                | A system is fault-tolerant if it can continue performing despite parts failing. Fault tolerance helps to make your remote-boot infrastructure more robust. In the case of OS deployment servers, the whole system is fault-tolerant if the OS deployment servers back up each other. |
| For-loop                                       | Extends from a FOR statement to an END FOR statement and executes for a specified number of iterations, defined in the FOR statement.                                                                                           |
| Functional programming (FP)                    | A style of programming that follows the mathematical function format. Declarative implies that the emphasis of the code or program is on the "what" of the solution as opposed to the "how to" of the solution. Declarative syntax abstracts out the implementation details and only emphasizes the final output, restating "the what." We use expressions in functional programming, such as the expression f of x, as mentioned earlier. |
| Hadoop                                         | An open-source software framework offering reliable distributed processing of large data sets by using simplified programming models.                                                                                           |
| Hadoop Common                                  | Fundamental part of the Apache Hadoop framework. It refers to a collection of primary utilities and libraries that support other Hadoop modules.                                                                                |
| Hadoop Distributed File System (HDFS)          | A file system distributed on multiple file servers, allowing programmers to access or store files from any network or computer. It is the storage layer of Hadoop. It works by splitting the files into blocks, creating replicas of the blocks, and storing them on different machines. It is built to access streaming data seamlessly. It uses a command-line interface to interact with Hadoop. |
| HBase                                          | A column-oriented, non-relational database system that runs on top of Hadoop Distributed File System (HDFS). It provides real-time wrangling access to the Hadoop file system. It uses hash tables to store data in indexes, allowing for random data access and making lookups faster. |
| Immutable                                      | This type of object storage allows users to set indefinite retention on the object if they are unsure of the final duration of the retention period or want to use event-based retention. Once set to indefinite, user applications can change the object retention to a finite value. |
| Imperative programming paradigm                | In this software development paradigm, functions are implicitly coded in every step used in solving a problem. Every operation is coded, specifying how the problem will be solved. This implies that pre-coded models are not called on. |
| In-memory processing                           | The practice of storing and manipulating data directly in a computer's main memory (RAM), allowing for faster and more efficient data operations compared to traditional disk-based storage.                                     |
| Iterative process                              | An approach to continuously improving a concept, design, or product. Creators produce a prototype, test it, tweak it, and repeat the cycle to get closer to the solution.                                                        |
| Java                                           | A technology equipped with a programming language and a software platform.                                                                                                                                                     |
| Java virtual machines (JVMs)                   | The platform-specific component that runs a Java program. At runtime, the VM interprets the Java bytecode compiled by the Java compiler. The VM is a translator between the language and the underlying operating system and hardware. |
| JavaScript Object Notation (JSON)              | A simplified data-interchange format based on a subset of the JavaScript programming language. IBM Integration Bus provides support for a JSON domain. The JSON parser and serializer process messages in the JSON domain.       |
| Lambda calculus                                | A mathematical concept that implies every computation can be expressed as an anonymous function that is applied to a data set.                                                                                                   |
| Lambda functions                               | Calculus functions, or operators. These are anonymous functions that enable functional programming. They are used to write functional programming code.                                                                          |
| List processing language (Lisp)                | The functional programming language that was initially used in the 1950s. Today, there are many functional programming language options, including Scala, Python, R, and Java.                                                    |
| Machine learning                               | A full-service cloud offering that allows developers and data scientists to collaborate and integrate predictive capabilities with their applications.                                                                           |
| MapReduce                                      | A program model and processing technique used in distributed computing based on Java. It splits the data into smaller units and processes big data. It is the first method used to query data stored in HDFS. It allows massive scalability across hundreds or thousands of servers in a Hadoop cluster. |
| Modular development                            | Techniques used in job designs to maximize the reuse of parallel jobs and components and save user time.                                                                                                                        |
| Parallel computing                             | A computing architecture in which multiple processors execute different small calculations fragmented from a large, complex problem simultaneously.                                                                              |
| Parallel programming                           | It resembles distributed programming. It is the simultaneous use of multiple compute resources to solve a computational task. Parallel programming parses tasks into discrete parts solved concurrently using multiple processors. The processors access a shared pool of memory, which has control and coordination mechanisms in place. |
| Parallelization                                | Parallel regions of program code executed by multiple threads, possibly running on multiple processors. Environment variables determine the number of threads created and calls to library functions.                          |
| Persistent cache                               | Information is stored in "permanent" memory. Therefore, data is not lost after a system crash or restart, as if it were stored in cache memory.                                                                                 |
| Python                                         | Easy-to-learn, high-level, interpreted, and general-purpose dynamic programming language focusing on code readability. It provides a robust framework for building fast and scalable applications for z/OS, with a rich ecosystem of modules to develop new applications like any other platform. |
| R                                              | An open-source, optimized programming language for statistical analysis and data visualization. Developed in 1992, it has a rich ecosystem with complex data models and elegant tools for data reporting.                       |
| Redundancy                                     | Duplication of data across multiple partitions or nodes in a cluster. This duplication is implemented to enhance fault tolerance and reliability. If one partition or node fails, the duplicated data on other partitions or nodes can still be used to ensure that the computation continues without interruption. Redundancy is critical in maintaining data availability and preventing data loss in distributed computing environments like Spark clusters. |
| Resilient Distributed Datasets (RDDs)          | A fundamental abstraction in Apache Spark that represents distributed collections of data. RDDs allow you to perform parallel and fault-tolerant data processing across a cluster of computers. RDDs can be created from existing data in storage systems (like HDFS), and they can undergo various transformations and actions to perform operations like filtering, mapping, and aggregating. The "resilient" aspect refers to RDDs' ability