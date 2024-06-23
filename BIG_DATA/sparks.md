
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

### Key Characteristics of Functional Programming

- **Declarative Nature**: Emphasis on the "what" of the solution rather than the "how to."
- **Expressions**: Use expressions like f(x).

### Historical Background

- **LISP**: The first functional programming language, starting in the 1950s.
- **Modern Languages**: Scala, Python, R, and Java are some of the modern options.

## Functional Programming in Scala

![alt text](image-33.png)
![alt text](image-34.png)

- **Scala**: The most recent representative in the family of functional programming languages.
- **First-Class Functions**: Functions can be passed as arguments, returned by other functions, and used as variables.

### Example

![alt text](image-32.png)

```scala
val increment = (x: Int) => x + 1
val numbers = List(1, 2, 3, 4)
val incrementedNumbers = numbers.map(increment)
```

This program increments each element in the list by one.

## Imperative vs. Functional Programming

### Imperative Paradigm

- Uses explicit steps to perform tasks.
- Example: Using a "for-loop" to increment each element in an array.

### Functional Paradigm

- Emphasizes the "what" part of the solution.
- Directly applies functions to entire lists or arrays.

## Benefits of Functional Programming

### Parallelization

- Functional programming allows tasks to be split into multiple computing chunks (nodes) and run in parallel.
- No need to change function definitions or code to parallelize.

### Example

- Incrementing a large array from 1 to 9 by splitting the task into three nodes running in parallel.

## Lambda Calculus

- **Lambda Calculus**: A mathematical concept where every computation is expressed as an anonymous function applied to a data set.
- **Lambda Functions**: Anonymous functions used to write functional programming code.

### Example in Scala and Python

#### Scala

```scala
val add = (a: Int, b: Int) => a + b
```

#### Python

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

### Key Features of RDDs

- **Fault Tolerant**: RDDs can recover from node failures.
- **Partitioned**: Data is split across multiple nodes for parallel processing.
- **Immutable**: Data cannot be altered once created.

### Spark Applications

Every Spark application consists of a driver program that runs the user's main functions and executes multiple parallel operations on a cluster.

### Supported File Types

RDDs support various file types, including:

- Text
- Sequence files
- Avro
- Parquet
- Hadoop input formats

### Supported Storage Systems

RDDs can work with:

- Local file systems
- Cassandra
- HBase
- HDFS
- Amazon S3
- Many relational and NoSQL databases

## Creating RDDs

![alt text](image-36.png)

### Methods to Create RDDs

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

### Definition

Parallel programming is the simultaneous use of multiple compute resources to solve a computational task. It involves:

- Parsing tasks into discrete parts.
- Solving these parts concurrently using multiple processors.
- Processors accessing a shared pool of memory.

### RDDs and Parallel Programming

RDDs enable parallel programming by distributing partitions across nodes. Spark runs one task per partition, allowing RDDs to be operated on in parallel.

## Resilience in Spark

### How RDDs Provide Resilience

- **Immutability**: Data is always recoverable because RDDs are immutable.
- **Caching**:
  - Persisting or caching data in memory makes future actions much faster.
  - Each node stores the partitions it computes, allowing for reuse in future actions.

### Benefits of Caching

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

### Components

1. **Driver Program**:
   - Manages the Spark jobs and splits them into tasks.
   - Communicates with executors and receives task results.

2. **Executor Programs**:
   - Run on worker nodes.
   - Perform tasks assigned by the driver.
   - Can start additional processes if there is enough memory and cores available.
   - Can use multiple cores for multithreaded calculations.

### Communication

- **Driver and Executors**: The driver submits tasks to executors and receives results upon completion.

### Organizational Analogy

- **Driver Code**: Executive management making decisions and allocating work.
- **Executors**: Junior employees executing tasks.
- **Worker Nodes**: Physical office space where tasks are performed.

### Scaling

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

### Benefits of DataFrames

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

# Resilient Distributed Datasets in Parallel Programming and Spark

Welcome to "Resilient Distributed Datasets in Parallel Programming and Spark." After watching this video, you will be able to:

- Describe Resilient Distributed Datasets.
- Explain how to use Resilient Distributed Datasets in Spark.
- Explain RDD transformations and actions.
- List fundamental transformations and actions.

## What are Resilient Distributed Datasets (RDDs)?

Resilient Distributed Datasets, known as RDDs, are Spark's primary data abstraction and are partitioned across a cluster's nodes.
![alt text](image-43.png)

## Transformations

An RDD transformation creates a new RDD from an existing RDD. Transformations in Spark are considered lazy because Spark does not compute transformation results immediately. Instead, the results are only computed when evaluated by "actions."

### Example of a Transformation

The `map` transformation passes each element of a dataset through a function, resulting in a new RDD.

## Actions

To evaluate a transformation in Spark, you use an action. The action returns a value to the driver program after running a computation.

### Example of an Action

The `reduce` action aggregates all the elements of an RDD and returns the result to the driver program.

## Directed Acyclic Graph (DAG)

Spark uses a unique data structure called a Directed Acyclic Graph (DAG) and an associated DAG Scheduler to perform RDD operations.

### What is a DAG?

- A DAG is a graphical structure composed of edges and vertices.
- The term "acyclic" means that new edges only originate from an existing vertex.
- Vertices represent RDDs, and edges represent transformations or actions.

### Why does Spark use DAGs?

DAGs help enable fault tolerance. When a node goes down, Spark replicates the DAG and restores the node.

## Process Overview

1. Spark creates a DAG when creating an RDD.
2. The DAG Scheduler performs a transformation and updates the DAG.
3. The DAG now points to the new RDD.
4. If there is an action, the driver program evaluates the DAG after Spark completes the action.

## Examples of RDD Transformations and Actions

### Transformations

- `map`: Applies a function to each element of the dataset.
- `filter`: Filters elements based on a function.
- `distinct`: Finds the number of distinct elements in a dataset.
- `flatmap`: Similar to `map`, but can return multiple items for each input item.

### Actions

- `reduce`: Aggregates dataset elements using a function.
- `take`: Returns an array with the first `n` elements.
- `collect`: Returns all the elements of the dataset as an array.
- `takeOrdered`: Returns elements ordered in ascending order or as specified by an optional function argument.

For more details about transformations and actions, visit the [Spark Apache website](https://spark.apache.org).

## Example

![alt text](image-44.png)
Consider a function `f(x)` that decrements `x` by 1. Applying this function as a transformation to a dataset using the `map` transformation:

1. Each task makes a new partition by calling `f(e)` on each entry `e` in the original partition.
2. The `collect` action gathers the entries from all the partitions into the driver, which receives the results.

## Summary

- RDDs are Spark's primary data abstraction partitioned across the nodes of the cluster.
- Spark uses DAGs to enable fault tolerance. When a node goes down, Spark replicates the DAG and restores the node.
- Transformations create new RDDs based on the transformation function and are evaluated lazily.
- Actions are necessary to get the computed values to the driver program.

# Datasets and DataFrames in Spark

Welcome to “Datasets and DataFrames in Spark.” After watching this video, you will be able to:

- Describe dataset features and benefits within Apache Spark.
- Explain three ways you can create datasets for use in Spark.
- Summarize the differences between datasets and DataFrames.

## What are Datasets?

Datasets are the newest Spark data abstraction. Like RDDs and DataFrames, datasets provide an API to access a distributed data collection. Datasets are a collection of strongly typed Java Virtual Machine (JVM) objects. Strongly typed means that datasets are typesafe, and the dataset’s datatype is made explicit during its creation.

## Benefits of Datasets

Datasets provide the benefits of both RDDs and DataFrames:

- **Type-safety:** Datasets are strongly typed.
- **Lambda Functions:** Datasets support lambda functions.
- **SQL Optimizations:** Datasets benefit from SparkSQL optimizations.

### Additional Features of Datasets

- **Immutability:** Datasets, like RDDs, cannot be deleted or lost.
- **Encoders:** Convert type-specified JVM objects to a tabular representation.
- **Extension of DataFrame API:** A dataset of a generic untyped “Row” is a JVM object seen as a column of a DataFrame.
- **Statically Typed Languages:** APIs are available in Scala and Java, which are statically typed languages. Dynamically typed languages like Python and R do not support dataset APIs.

## Advantages of Datasets Over DataFrames and RDDs

- **Compile-time Type Safety:** Detects syntax and semantic errors before deployment, saving time and costs.
- **Faster Computation:** Especially for aggregate queries.
- **Query Optimization:** Enhanced by Catalyst and Tungsten.
- **Improved Memory Usage and Caching:** Spark optimizes the layout within memory based on the data structure.

## High-level Operations

The dataset API offers functions for convenient high-level aggregate operations, including:

- `sum`
- `average`
- `join`
- `group-by`

## Creating Datasets in Spark

### 1. Using `toDS` Function (Scala)

```scala
val data = Seq(1, 2, 3, 4, 5)
val ds = data.toDS()
```

### 2. From a Text File

```scala
val textFile = spark.read.textFile("path/to/file.txt").toDS()
```

### 3. Using a JSON File with a Custom Class

```scala
case class Customer(name: String, id: Long)
val customerDS = spark.read.json("path/to/file.json").as[Customer]
```

## Datasets vs. DataFrames

- **Strongly Typed:** Datasets are strongly typed, while DataFrames are not typesafe.
- **APIs:** Datasets use unified Java and Scala APIs. DataFrames have APIs in Java, Scala, Python, and R.
- **Foundation:** Datasets are built on top of DataFrames, which are built on RDDs.

## Summary

- A dataset is a distributed collection of data that provides the combined benefits of both RDDs and SparkSQL.
- Datasets consist of strongly typed JVM objects.
- Datasets use DataFrame typesafe capabilities and extend object-oriented API capabilities.
- Datasets work with both Scala and Java APIs.

# Spark SQL Memory Optimization using Catalyst and Tungsten

Welcome to “Spark SQL Memory Optimization using Catalyst and Tungsten.” After watching this video, you will be able to:

- Describe the goals of Apache Spark SQL Optimization.
- Explain how Catalyst and Tungsten benefit Spark SQL.
- Explain how Spark performs SQL and memory optimization using Catalyst and Tungsten.

## Goals of Spark SQL Optimization

The primary goal of Spark SQL Optimization is to improve SQL query run-time performance by reducing the query’s time and memory consumption, thereby saving organizations time and money. Spark SQL supports both rule-based and cost-based query optimization.

## Catalyst Optimizer

Catalyst, also known as the Catalyst Optimizer, is the built-in rule-based query optimizer for Spark SQL. It is based on Scala functional programming constructs and is designed to easily add new optimization techniques and features to Spark SQL. Developers can extend the optimizer by adding data-source-specific rules and support for new data types.

### Rule-based Optimization

During rule-based optimization, the SQL optimizer follows predefined rules to determine how to run the SQL query. Examples of predefined rules include:

- Validating that a table is indexed.
- Checking that a query contains only the required columns.

### Cost-based Optimization

With the query itself optimized, cost-based optimization measures and calculates cost based on the time and memory that the query consumes. The Catalyst optimizer selects the query path that results in the lowest time and memory consumption. This process can become complex with large datasets.

## Catalyst Optimization Phases

Catalyst uses a tree data structure and follows four high-level tasks or phases to optimize a query:

1. **Analysis**: Catalyst analyzes the query, the DataFrame, the unresolved logical plan, and the Catalog to create a logical plan.
2. **Logical Optimization**: The logical plan evolves into an optimized logical plan. This is the rule-based optimization step, where rules like folding, pushdown, and pruning are applied.
3. **Physical Planning**: Catalyst generates multiple physical plans based on the logical plan. A cost model then chooses the physical plan with the least cost, which is the cost-based optimization step.
4. **Code Generation**: Catalyst applies the selected physical plan and generates Java bytecode to run on each node.

## Tungsten Optimization

Tungsten optimizes the performance of underlying hardware by focusing on CPU performance instead of IO. It improves CPU and memory performance using methods more suited to data processing for the JVM.

### Tungsten Capabilities

- **Memory Management**: Manages memory explicitly without relying on the JVM object model or garbage collection.
- **Cache-friendly Data Structures**: Uses STRIDE-based memory access for better arrangement and security.
- **JVM Bytecode**: Supports on-demand JVM bytecode.
- **Reduced CPU Calls**: Eliminates virtual function dispatches.
- **Efficient CPU Usage**: Places intermediate data in CPU registers and enables loop unrolling.

## Summary

- **Catalyst**: The built-in rule-based query optimizer for Spark SQL. It performs analysis, logical optimization, physical planning, and code generation.
- **Tungsten**: The built-in cost-based optimizer for CPU and memory usage in Spark. It enables cache-friendly computation of algorithms and data structures.

# User-Defined Schema (UDS) for DSL and SQL

## Estimated time needed: 10 minutes

In this reading, you will learn how to define and enforce a user-defined schema in PySpark.

Spark provides a structured data processing framework that can define and enforce schemas for various data sources, including CSV files. Let's look at the steps to define and use a user-defined schema for a CSV file in PySpark:

## Step 1: Import the Required Libraries

```python
from pyspark.sql.types import StructType, IntegerType, FloatType, StringType, StructField
```

## Step 2: Define the Schema

Understanding the data before defining a schema is an important step. Let's take a look at the step-by-step approach to understanding the data and defining an appropriate schema for a given input file:

### Explore the Data

Understand the different data types present in each column.

### Column Data Types

Determine the appropriate data types for each column based on your observed values.

### Define the Schema

Use the `StructType` class in Spark and create a `StructField` for each column, mentioning the column name, data type, and other properties.

### Example

```python
schema = StructType([
    StructField("Emp_Id", StringType(), False),
    StructField("Emp_Name", StringType(), False),
    StructField("Department", StringType(), False),
    StructField("Salary", IntegerType(), False),
    StructField("Phone", IntegerType(), True),
])
```

'False' indicates null values are NOT allowed for the column.

### Example Data: `employee.csv`

```csv
emp_id,emp_name,dept,salary,phone
A101,jhon,computer science,1000,+1 (701) 846 958
A102,Peter,Electronics,2000,
A103,Micheal,IT,2500,
```

## Step 3: Read the Input File with User-Defined Schema

```python
#create a dataframe on top of a csv file
df = (spark.read
  .format("csv")
  .schema(schema)
  .option("header", "true")
  .load("employee.csv")
)
# display the dataframe content
df.show()
```

## Step 4: Display the Schema

Use the `printSchema()` method in Spark to display the schema of a DataFrame and ensure that the schema is applied correctly to the data.

```python
df.printSchema()
```

Through these four steps, you've acquired the ability to establish a schema for a CSV file. Additionally, you've employed this user-defined schema (UDF) to read the CSV file, exhibit its contents, and showcase the schema itself.

# Using DataFrames with Real World Data

Welcome to "Using DataFrames with Real World Data." After watching this video, you will be able to:

- Identify the basic DataFrame operational steps
- Apply basic DataFrame operations on real-world data
- Apply Spark DataFrames to real-world data

## Basic DataFrame Operations

DataFrame operations can be summarized in the following steps:

1. **Reading**
2. **Analysis**
3. **Transformation**
4. **Loading**
5. **Writing**

### Step 1: Reading Data

Spark reads in the data and loads it into a DataFrame. For example, you can load a dataset into a Pandas DataFrame in Python and then load that same dataset into a Spark DataFrame object.

### Step 2: Analyzing Data

Analyze the dataset by examining:

- Columns
- Data types
- Number of rows

You can also perform aggregated stats, trend analysis, and other operations.

#### Example Analysis

- **Print Schema**: Examine the DataFrame column data types.
  
  ```python
  df.printSchema()
  ```
  
- **Show Function**: View a specified number of DataFrame rows.
  
  ```python
  df.show(5)
  ```
  
- **Select Function**: Examine data from a specific column.

  ```python
  df.select("mpg").show(5)
  ```

### Step 3: Transforming Data

Transform the data to retain only relevant information. Common transformation techniques include:

- **Filtering**: Locate specific values.
  
  ```python
  df.filter(df["mpg"] < 18).show()
  ```
  
- **Sorting**: Sort the dataset based on specific criteria.
- **Joining**: Join this dataset with another dataset.
- **Columnar Operations**: Multiply each column by a specific number, convert units, etc.
- **Grouping/Aggregating**: Aggregate data, such as grouping by a column and calculating sums or averages.

#### Example Transformation

- **Filter Function**: Filter the dataset for cars with mileage less than 18 miles per gallon.
  
  ```python
  df.filter(df["mpg"] < 18).show()
  ```

- **Aggregation**: Aggregate records with the same number of cylinders and count the vehicles.

  ```python
  df.groupBy("cyl").count().orderBy("cyl").show()
  ```

### Step 4: Loading Data

Load your transformed dataset back to a database or a file system.

### Step 5: Writing Data

Write the data back to disk, save it into another database, or export it using an API.

```python
# Example: Save the DataFrame to a JSON file
df.write.format("json").save("output.json")
```

## ETL and ELT Processes

### ETL: Extract, Transform, Load

- **Extract**: Read data from various sources.
- **Transform**: Process and transform data as needed.
- **Load**: Load transformed data into a data warehouse or database.

ETL is essential for making data accessible to data warehouses, machine learning models, and other downstream applications.

### ELT: Extract, Load, Transform

- **Extract**: Read data and load it into a data lake.
- **Load**: Store all data in its raw form.
- **Transform**: Transform data as needed for specific projects.

ELT is beneficial for big data processing, where transformations are applied individually for each project.

## Summary

In this video, you learned that:

- Basic DataFrame operations are reading, analysis, transformation, loading, and writing.
- You can use a Pandas DataFrame in Python to load a dataset.
- You can apply the `printSchema`, `select`, and `show` functions for data analysis.
- For transform tasks, keep only relevant data and apply functions such as filters, joins, column operations, grouping, and aggregations.

# Welcome to "Apache Spark SQL"

After watching this video, you will be able to:

- Define Spark SQL
- Create a table view in Spark SQL
- Explain how to aggregate data using Spark SQL
- Explain the various data sources Spark SQL supports

## Quick Recap of Spark SQL

### What is Spark SQL?

Spark SQL is a Spark module for structured data processing. It is used to run SQL queries on Spark DataFrames and has available APIs in Java, Scala, Python, and R.

### Creating a Table View in Spark SQL

The first step to running SQL queries in Spark SQL is to create a table view. A table view is a temporary table used to run SQL queries. Spark SQL supports both temporary and global temporary table views.

- **Temporary View**: Has local scope, meaning it exists only within the current Spark session on the current node.
- **Global Temporary View**: Exists within the general Spark application and is shareable across different Spark sessions.

#### Example: Creating a Temporary View in Python using PySpark

First, create the DataFrame from the JSON file, then create a temporary view called "people." You can then run a SQL query using this view.

![alt text](image-45.png)

#### Example: Creating a Global Temporary View

![alt text](image-46.png)
Note the minor syntax change, including the "Global" prefix to the function name and the "global_temp" prefix to the view name.

### Aggregating Data Using Spark SQL

Aggregation, a standard Spark SQL process, is generally used to present grouped statistics. DataFrames come inbuilt with commonly used aggregation functions such as count, average, max, and others. You can also perform aggregation programmatically using SQL queries and table views.

1. **Import Your Data into a DataFrame**: Use pandas on Python to read the CSV file and create a DataFrame.
2. **Examine Data**: Apply the Select function to view the first five rows of the "mpg" column.

#### Example: Aggregating and Grouping Cars by Cylinders

![alt text](image-47.png)
You can perform this action using two methods:

1. **Inbuilt Functions of the DataFrame**: Use DataFrame functions to group and aggregate data.
2. **SQL Query with Table View**: Create a temp view for the DataFrame and run a SQL query to group by cylinders and view the data in descending order.

Both approaches produce the same results.

### Data Sources Supported by Spark SQL

1. **Parquet**: A columnar format supported by many data processing systems. Spark SQL supports reading and writing data from Parquet files and preserves the data schema.
2. **JSON**: Spark SQL can load and write to JSON datasets by inferring the schema.
3. **Hive**: Spark SQL supports reading and writing data stored in Hive.

## Summary

In this video, you learned that:

- Spark modules for structured data processing can run SQL queries on Spark DataFrames and are usable in Java, Scala, Python, and R.
- Spark SQL supports both temporary views and global temporary views.
- You can use a DataFrame function or a SQL Query plus Table View for data aggregation.
- Spark SQL supports Parquet files, JSON datasets, and Hive tables.

# Common Transformations and Optimization Techniques in Spark

**Estimated time needed:** 30 minutes

When working with PySpark DataFrames for data processing, it's important to understand the two types of transformations: narrow and wide.

## Narrow Transformations

Narrow transformations in Spark work within partitions without shuffling data between them. They're applied locally to each partition, avoiding data exchange.

**Examples of Narrow Transformations:**

- **Map:** Applying a function to each element in the data set.

    ```python
    from pyspark import SparkContext
    sc = SparkContext("local", "MapExample")
    data = [1, 2, 3, 4, 5]
    rdd = sc.parallelize(data)
    mapped_rdd = rdd.map(lambda x: x * 2)
    mapped_rdd.collect() # Output: [2, 4, 6, 8, 10]
    ```

- **Filter:** Selecting elements based on a specified condition.

    ```python
    from pyspark import SparkContext
    sc = SparkContext("local", "FilterExample")
    data = [1, 2, 3, 4, 5]
    rdd = sc.parallelize(data)
    filtered_rdd = rdd.filter(lambda x: x % 2 == 0)
    filtered_rdd.collect() # Output: [2, 4]
    ```

- **Union:** Combining two data sets with the same schema.

    ```python
    from pyspark import SparkContext
    sc = SparkContext("local", "UnionExample")
    rdd1 = sc.parallelize([1, 2, 3])
    rdd2 = sc.parallelize([4, 5, 6])
    union_rdd = rdd1.union(rdd2)
    union_rdd.collect() # Output: [1, 2, 3, 4, 5, 6]
    ```

## Wide Transformations

Wide transformations in Spark involve redistributing and shuffling data between partitions, leading to more resource-intensive and complex operations.

**Examples of Wide Transformations:**

- **GroupBy:** Aggregating data based on a specific key.

    ```python
    from pyspark import SparkContext
    sc = SparkContext("local", "GroupByExample")
    data = [("apple", 2), ("banana", 3), ("apple", 5), ("banana", 1)]
    rdd = sc.parallelize(data)
    grouped_rdd = rdd.groupBy(lambda x: x[0])
    sum_rdd = grouped_rdd.mapValues(lambda values: sum([v[1] for v in values]))
    sum_rdd.collect() # Output: [('apple', 7), ('banana', 4)]
    ```

- **Join:** Combining two data sets based on a common key.

    ```python
    from pyspark import SparkContext
    sc = SparkContext("local", "JoinExample")
    rdd1 = sc.parallelize([("apple", 2), ("banana", 3)])
    rdd2 = sc.parallelize([("apple", 5), ("banana", 1)])
    joined_rdd = rdd1.join(rdd2)
    joined_rdd.collect() # Output: [('apple', (2, 5)), ('banana', (3, 1))]
    ```

- **Sort:** Rearranging data based on a specific criterion.

    ```python
    from pyspark import SparkContext
    sc = SparkContext("local", "SortExample")
    data = [4, 2, 1, 3, 5]
    rdd = sc.parallelize(data)
    sorted_rdd = rdd.sortBy(lambda x: x, ascending=True)
    sorted_rdd.collect() # Output: [1, 2, 3, 4, 5]
    ```

## PySpark DataFrame: Rule-Based Common Transformations

The DataFrame API in PySpark offers various transformations based on predefined rules designed to improve query execution and boost overall performance.

**Common Rule-Based Transformations:**

- **Predicate Pushdown:** Pushing filtering conditions closer to the data source to minimize data movement.
- **Constant Folding:** Evaluating constant expressions during query compilation to reduce computation during runtime.
- **Column Pruning:** Eliminating unnecessary columns from the query plan to enhance processing efficiency.
- **Join Reordering:** Rearranging join operations to minimize intermediate data size and enhance performance.

**Example Code:**

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a Spark session
spark = SparkSession.builder.appName("RuleBasedTransformations").getOrCreate()

# Sample input data for DataFrame 1
data1 = [("Alice", 25, "F"), ("Bob", 30, "M"), ("Charlie", 22, "M"), ("Diana", 28, "F")]

# Sample input data for DataFrame 2
data2 = [("Alice", "New York"), ("Bob", "San Francisco"), ("Charlie", "Los Angeles"), ("Eve", "Chicago")]

# Create DataFrames
columns1 = ["name", "age", "gender"]
df1 = spark.createDataFrame(data1, columns1)
columns2 = ["name", "city"]
df2 = spark.createDataFrame(data2, columns2)

# Applying Predicate Pushdown (Filtering)
filtered_df = df1.filter(col("age") > 25)

# Applying Constant Folding
folded_df = filtered_df.select(col("name"), col("age") + 2)

# Applying Column Pruning
pruned_df = folded_df.select(col("name"))

# Join Reordering
reordered_join = df1.join(df2, on="name")

# Show the final results
print("Filtered DataFrame:")
filtered_df.show()
print("Folded DataFrame:")
folded_df.show()
print("Pruned DataFrame:")
pruned_df.show()
print("Reordered Join DataFrame:")
reordered_join.show()

# Stop the Spark session
spark.stop()
```

## Optimization Techniques Used in Spark SQL

**Predicate Pushdown:** Apply a filter to DataFrame `df1` to only select rows where the "age" column is greater than 25.

**Constant Folding:** Perform an arithmetic operation on the "age" column in `folded_df`, adding a constant value of 2.

**Column Pruning:** Select only the "name" column in `pruned_df`, eliminating unnecessary columns from the query plan.

**Join Reordering:** Perform a join between `df1` and `df2` on the "name" column, allowing Spark to potentially reorder the join for better performance.

## Cost-Based Optimization Techniques in Spark

Spark employs cost-based optimization techniques to enhance the efficiency of query execution. These methods involve estimating and analyzing the costs associated with queries, leading to more informed decisions that result in improved performance.

**Cost-Based Techniques:**

- **Adaptive Query Execution:** Dynamically adjusts the query plan during execution based on runtime statistics to optimize performance.
- **Cost-Based Join Reordering:** Optimizes join order based on estimated costs of different join paths.
- **Broadcast Hash Join:** Optimizes small-table joins by broadcasting one table to all nodes, reducing data shuffling.
- **Shuffle Partitioning and Memory Management:** Efficiently manages data shuffling during operations like `groupBy` and aggregation, optimizing memory usage.

**Example Code:**

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a Spark session
spark = SparkSession.builder.appName("CostBasedOptimization").getOrCreate()

# Sample input data for DataFrame 1
data1 = [("Alice", 25), ("Bob", 30), ("Charlie", 22), ("Diana", 28)]

# Sample input data for DataFrame 2
data2 = [("Alice", "New York"), ("Bob", "San Francisco"), ("Charlie", "Los Angeles"), ("Eve", "Chicago")]

# Create DataFrames
columns1 = ["name", "age"]
df1 = spark.createDataFrame(data1, columns1)
columns2 = ["name", "city"]
df2 = spark.createDataFrame(data2, columns2)

# Enable adaptive query execution
spark.conf.set("spark.sql.adaptive.enabled", "true")

# Applying Adaptive Query Execution (Runtime adaptive optimization)
optimized_join = df1.join(df2, on="name")

# Show the optimized join result
print("Optimized Join DataFrame:")
optimized_join.show()

# Stop the Spark session
spark.stop()
```

In this example, we created two DataFrames (`df1` and `df2`) with sample input data. Then, we enabled the adaptive query execution feature by setting the configuration parameter `"spark.sql.adaptive.enabled"` to `"true"`. Adaptive Query Execution allows Spark to adjust the query plan during execution based on runtime statistics.

The code performs a join between `df1` and `df2` on the "name" column. Spark's adaptive query execution dynamically adjusts the query plan based on runtime statistics, which can result in improved performance.

# Common Transformations and Optimization Techniques in Spark

**Estimated time needed:** 30 minutes

When working with PySpark DataFrames for data processing, it's important to understand the two types of transformations: narrow and wide.

## Narrow Transformations

Narrow transformations in Spark work within partitions without shuffling data between them. They're applied locally to each partition, avoiding data exchange.

**Examples of Narrow Transformations:**

- **Map:** Applying a function to each element in the data set.

    ```python
    from pyspark import SparkContext
    sc = SparkContext("local", "MapExample")
    data = [1, 2, 3, 4, 5]
    rdd = sc.parallelize(data)
    mapped_rdd = rdd.map(lambda x: x * 2)
    mapped_rdd.collect() # Output: [2, 4, 6, 8, 10]
    ```

- **Filter:** Selecting elements based on a specified condition.

    ```python
    from pyspark import SparkContext
    sc = SparkContext("local", "FilterExample")
    data = [1, 2, 3, 4, 5]
    rdd = sc.parallelize(data)
    filtered_rdd = rdd.filter(lambda x: x % 2 == 0)
    filtered_rdd.collect() # Output: [2, 4]
    ```

- **Union:** Combining two data sets with the same schema.

    ```python
    from pyspark import SparkContext
    sc = SparkContext("local", "UnionExample")
    rdd1 = sc.parallelize([1, 2, 3])
    rdd2 = sc.parallelize([4, 5, 6])
    union_rdd = rdd1.union(rdd2)
    union_rdd.collect() # Output: [1, 2, 3, 4, 5, 6]
    ```

## Wide Transformations

Wide transformations in Spark involve redistributing and shuffling data between partitions, leading to more resource-intensive and complex operations.

**Examples of Wide Transformations:**

- **GroupBy:** Aggregating data based on a specific key.

    ```python
    from pyspark import SparkContext
    sc = SparkContext("local", "GroupByExample")
    data = [("apple", 2), ("banana", 3), ("apple", 5), ("banana", 1)]
    rdd = sc.parallelize(data)
    grouped_rdd = rdd.groupBy(lambda x: x[0])
    sum_rdd = grouped_rdd.mapValues(lambda values: sum([v[1] for v in values]))
    sum_rdd.collect() # Output: [('apple', 7), ('banana', 4)]
    ```

- **Join:** Combining two data sets based on a common key.

    ```python
    from pyspark import SparkContext
    sc = SparkContext("local", "JoinExample")
    rdd1 = sc.parallelize([("apple", 2), ("banana", 3)])
    rdd2 = sc.parallelize([("apple", 5), ("banana", 1)])
    joined_rdd = rdd1.join(rdd2)
    joined_rdd.collect() # Output: [('apple', (2, 5)), ('banana', (3, 1))]
    ```

- **Sort:** Rearranging data based on a specific criterion.

    ```python
    from pyspark import SparkContext
    sc = SparkContext("local", "SortExample")
    data = [4, 2, 1, 3, 5]
    rdd = sc.parallelize(data)
    sorted_rdd = rdd.sortBy(lambda x: x, ascending=True)
    sorted_rdd.collect() # Output: [1, 2, 3, 4, 5]
    ```

## PySpark DataFrame: Rule-Based Common Transformations

The DataFrame API in PySpark offers various transformations based on predefined rules designed to improve query execution and boost overall performance.

**Common Rule-Based Transformations:**

- **Predicate Pushdown:** Pushing filtering conditions closer to the data source to minimize data movement.
- **Constant Folding:** Evaluating constant expressions during query compilation to reduce computation during runtime.
- **Column Pruning:** Eliminating unnecessary columns from the query plan to enhance processing efficiency.
- **Join Reordering:** Rearranging join operations to minimize intermediate data size and enhance performance.

**Example Code:**

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a Spark session
spark = SparkSession.builder.appName("RuleBasedTransformations").getOrCreate()

# Sample input data for DataFrame 1
data1 = [("Alice", 25, "F"), ("Bob", 30, "M"), ("Charlie", 22, "M"), ("Diana", 28, "F")]

# Sample input data for DataFrame 2
data2 = [("Alice", "New York"), ("Bob", "San Francisco"), ("Charlie", "Los Angeles"), ("Eve", "Chicago")]

# Create DataFrames
columns1 = ["name", "age", "gender"]
df1 = spark.createDataFrame(data1, columns1)
columns2 = ["name", "city"]
df2 = spark.createDataFrame(data2, columns2)

# Applying Predicate Pushdown (Filtering)
filtered_df = df1.filter(col("age") > 25)

# Applying Constant Folding
folded_df = filtered_df.select(col("name"), col("age") + 2)

# Applying Column Pruning
pruned_df = folded_df.select(col("name"))

# Join Reordering
reordered_join = df1.join(df2, on="name")

# Show the final results
print("Filtered DataFrame:")
filtered_df.show()
print("Folded DataFrame:")
folded_df.show()
print("Pruned DataFrame:")
pruned_df.show()
print("Reordered Join DataFrame:")
reordered_join.show()

# Stop the Spark session
spark.stop()
```

## Optimization Techniques Used in Spark SQL

**Predicate Pushdown:** Apply a filter to DataFrame `df1` to only select rows where the "age" column is greater than 25.

**Constant Folding:** Perform an arithmetic operation on the "age" column in `folded_df`, adding a constant value of 2.

**Column Pruning:** Select only the "name" column in `pruned_df`, eliminating unnecessary columns from the query plan.

**Join Reordering:** Perform a join between `df1` and `df2` on the "name" column, allowing Spark to potentially reorder the join for better performance.

## Cost-Based Optimization Techniques in Spark

Spark employs cost-based optimization techniques to enhance the efficiency of query execution. These methods involve estimating and analyzing the costs associated with queries, leading to more informed decisions that result in improved performance.

**Cost-Based Techniques:**

- **Adaptive Query Execution:** Dynamically adjusts the query plan during execution based on runtime statistics to optimize performance.
- **Cost-Based Join Reordering:** Optimizes join order based on estimated costs of different join paths.
- **Broadcast Hash Join:** Optimizes small-table joins by broadcasting one table to all nodes, reducing data shuffling.
- **Shuffle Partitioning and Memory Management:** Efficiently manages data shuffling during operations like `groupBy` and aggregation, optimizing memory usage.

**Example Code:**

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a Spark session
spark = SparkSession.builder.appName("CostBasedOptimization").getOrCreate()

# Sample input data for DataFrame 1
data1 = [("Alice", 25), ("Bob", 30), ("Charlie", 22), ("Diana", 28)]

# Sample input data for DataFrame 2
data2 = [("Alice", "New York"), ("Bob", "San Francisco"), ("Charlie", "Los Angeles"), ("Eve", "Chicago")]

# Create DataFrames
columns1 = ["name", "age"]
df1 = spark.createDataFrame(data1, columns1)
columns2 = ["name", "city"]
df2 = spark.createDataFrame(data2, columns2)

# Enable adaptive query execution
spark.conf.set("spark.sql.adaptive.enabled", "true")

# Applying Adaptive Query Execution (Runtime adaptive optimization)
optimized_join = df1.join(df2, on="name")

# Show the optimized join result
print("Optimized Join DataFrame:")
optimized_join.show()

# Stop the Spark session
spark.stop()
```

In this example, we created two DataFrames (`df1` and `df2`) with sample input data. Then, we enabled the adaptive query execution feature by setting the configuration parameter `"spark.sql.adaptive.enabled"` to `"true"`. Adaptive Query Execution allows Spark to adjust the query plan during execution based on runtime statistics.

The code performs a join between `df1` and `df2` on the "name" column. Spark's adaptive query execution dynamically adjusts the query plan based on runtime statistics, which can result in improved performance.

Here is the requested table in markdown format:

| Package/Method           | Description                                                                                                                                            | Code Example                                                                                                        |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| appName()                | A name for your job to display on the cluster web UI.                                                                                                  | ```python\nfrom pyspark.sql import SparkSession\nspark = SparkSession.builder.appName("MyApp").getOrCreate()\n```    |
| createDataFrame()        | Used to load the data into a Spark DataFrame.                                                                                                          | ```python\nfrom pyspark.sql import SparkSession\nspark = SparkSession.builder.appName("MyApp").getOrCreate()\ndata = [("Jhon", 30), ("Peter", 25), ("Bob", 35)]\ncolumns = ["name", "age"]\n```\nCreating a DataFrame\n```python\ndf = spark.createDataFrame(data, columns)\n``` |
| createTempView()         | Create a temporary view that can later be used to query the data. The only required parameter is the name of the view.                                  | ```python\ndf.createOrReplaceTempView("cust_tbl")\n```                                                              |
| fillna()                 | Used to replace NULL/None values on all or selected multiple DataFrame columns with either zero (0), empty string, space, or any constant literal values. | Replace NULL/None values in a DataFrame\n```python\nfilled_df = df.fillna(0)\n```\nReplace with zero                |
| filter()                 | Returns an iterator where the items are filtered through a function to test if the item is accepted or not.                                              | ```python\nfiltered_df = df.filter(df['age'] > 30)\n```                                                             |
| getOrCreate()            | Get or instantiate a SparkContext and register it as a singleton object.                                                                                | ```python\nspark = SparkSession.builder.getOrCreate()\n```                                                          |
| groupby()                | Used to collect the identical data into groups on DataFrame and perform count, sum, avg, min, max functions on the grouped data.                        | Grouping data and performing aggregation\n```python\ngrouped_df = df.groupBy("age").agg({"age": "count"})\n```      |
| head()                   | Returns the first n rows for the object based on position.                                                                                             | Returning the first 5 rows\n```python\nfirst_5_rows = df.head(5)\n```                                               |
| import                   | Used to make code from one module accessible in another. Python imports are crucial for a successful code structure.                                    | ```python\nfrom pyspark.sql import SparkSession\n```                                                                |
| pd.read_csv()            | Required to access data from the CSV file from Pandas that retrieves data in the form of the data frame.                                                | ```python\nimport pandas as pd\n```\nReading data from a CSV file into a DataFrame\n```python\ndf_from_csv = pd.read_csv("data.csv")\n``` |
| pip                      | To ensure that requests will function, the pip program searches for the package in the Python Package Index (PyPI), resolves any dependencies, and installs everything in your current Python environment. | ```python\npip list\n```                                                                                          |
| pip install              | The pip install <package> command looks for the latest version of the package and installs it.                                                          | ```python\npip install pyspark\n```                                                                                 |
| printSchema()            | Used to print or display the schema of the DataFrame or data set in tree format along with the column name and data type. If you have a DataFrame or data set with a nested structure, it displays the schema in a nested tree format. | ```python\ndf.printSchema()\n```                                                                                   |
| rename()                 | Used to change the row indexes and the column labels.                                                                                                  | ```python\nimport pandas as pd\n```\nCreate a sample DataFrame\n```python\ndata = {'A': [1, 2, 3], 'B': [4, 5, 6]}\ndf = pd.DataFrame(data)\n```\nRename columns\n```python\ndf = df.rename(columns={'A': 'X', 'B': 'Y'})\n```\nThe columns 'A' and 'B' are now renamed to 'X' and 'Y'\n```python\nprint(df)\n``` |
| select()                 | Used to select one or multiple columns, nested columns, column by index, all columns from the list, by regular expression from a DataFrame. select() is a transformation function in Spark and returns a new DataFrame with the selected columns. | ```python\nselected_df = df.select('name', 'age')\n```                                                             |
| show()                   | Spark DataFrame show() is used to display the contents of the DataFrame in a table row and column format. By default, it shows only twenty rows, and the column values are truncated at twenty characters. | ```python\ndf.show()\n```                                                                                           |
| sort()                   | Used to sort DataFrame by ascending or descending order based on single or multiple columns.                                                           | Sorting DataFrame by a column in ascending order\n```python\nsorted_df = df.sort("age")\n```\nSorting DataFrame by multiple columns in descending order\n```python\nsorted_df_desc = df.sort(["age", "name"], ascending=[False, True])\n``` |
| SparkContext()           | It is an entry point to Spark and is defined in org.apache.spark package since version 1.x and used to programmatically create Spark RDD, accumulators, and broadcast variables on the cluster. | ```python\nfrom pyspark import SparkContext\n```\nCreating a SparkContext\n```python\nsc = SparkContext("local", "MyApp")\n``` |
| SparkSession             | It is an entry point to Spark, and creating a SparkSession instance would be the first statement you would write to the program with RDD, DataFrame, and dataset. | ```python\nfrom pyspark.sql import SparkSession\n```\nCreating a SparkSession\n```python\nspark = SparkSession.builder.appName("MyApp").getOrCreate()\n``` |
| spark.read.json()        | Spark SQL can automatically infer the schema of a JSON data set and load it as a DataFrame. The read.json() function loads data from a directory of JSON files where each line of the files is a JSON object. Note that the file offered as a JSON file is not a typical JSON file. | ```python\njson_df = spark.read.json("customer.json")\n```                                                         |
| spark.sql()              | To issue any SQL query, use the sql() method on the SparkSession instance. All spark.sql queries executed in this manner return a DataFrame on which you may perform further Spark operations if required. | ```python\nresult = spark.sql("SELECT name, age FROM cust_tbl WHERE age > 30")\nresult.show()\n```                  |
| spark.udf.register()     | In PySpark DataFrame, it is used to register a user-defined function (UDF) with Spark, making it accessible for use in Spark SQL queries. This allows you to apply custom logic or operations to DataFrame columns using SQL expressions. | Registering a UDF (User-defined Function)\n```python\nfrom pyspark.sql.functions import udf\nfrom pyspark.sql.types import StringType\ndef my_udf(value):\nreturn value.upper()\nspark.udf.register("my_udf", my_udf, StringType())\n``` |
| where()                  | Used to filter the rows from DataFrame based on the given condition. Both filter() and where() functions are used for the same purpose.                 | Filtering rows based on a condition\n```python\nfiltered_df = df.where(df['age'] > 30)\n```                         |
| withColumn()             | Transformation function of DataFrame used to change the value, convert the data type of an existing column, create a new column, and many more.         | Adding a new column and performing transformations\n```python\nfrom pyspark.sql.functions import col\nnew_df = df.withColumn("age_squared", col("age") ** 2)\n``` |
| withColumnRenamed()      | Returns a new DataFrame by renaming an existing column.                                                                                                | Renaming an existing column\n```python\nrenamed_df = df.withColumnRenamed("age", "years_old")\n```                  |

| Term                                 | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aggregating data                     | Aggregation is a Spark SQL process frequently used to present aggregated statistics. Commonly used aggregation functions such as count(), avg(), max(), and others are built into DataFrames. Users can also perform aggregation programmatically using SQL queries and table views.                                                                                                                                                                                                                                                                                                                                                                                               |
| Analyze data using printSchema       | In this phase, users examine the schema or the DataFrame column data types using the print schema method. It is imperative to note the data types in each column. Users can apply the select() function to examine data from a specific column in detail.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Apache Spark                         | An in-memory and open-source application framework for distributed data processing and iterative analysis of enormous data volumes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Catalyst phases                      | Catalyst analyzes the query, DataFrame, unresolved logical plan, and Catalog to create a logical plan in the Analysis phase. The logical plan evolves into an optimized logical plan in the logical optimization phase. It is the rule-based optimization step of Spark SQL. Rules such as folding, pushdown, and pruning are applicable here. Catalyst generates multiple physical plans based on the logical plan in the physical planning phase. A physical plan describes computation on datasets with specific definitions explaining how to conduct the computation. A cost model then selects the physical plan with the least cost. This explains the cost-based optimization step. Code generation is the final phase. In this phase, the Catalyst applies the selected physical plan and generates Java bytecode to run on the nodes. |
| Catalyst query optimization          | Catalyst Optimizer uses a tree data structure and provides the data tree rule sets in the background. Catalyst performs the following four high-level tasks to optimize a query: analysis, logical optimization, physical planning, and code generation.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Catalyst                             | Within Spark's operational framework, it employs a pair of engines, namely Catalyst and Tungsten, in a sequential manner for query enhancement and execution. Catalyst's primary function involves deriving an optimized physical query plan from the initial logical query plan. This optimization process entails implementing a range of transformations such as predicate pushdown, column pruning, and constant folding onto the logical plan.                                                                                                                                                                                                               |
| Cost-based optimization              | Cost is measured and calculated based on the time and memory that a query consumes. Catalyst optimizer selects a query path that results in minimal time and memory consumption. As queries can use multiple paths, these calculations can become quite complex when large datasets are part of the calculation.                                                                                                                                                                                                                                                                                                                                                          |
| Creating a view in Spark SQL         | It is the first step in running SQL queries in Spark SQL. It is a temporary table used to run SQL queries. Both temporary and global temporary views are supported by Spark SQL. A temporary view has a local scope. Local scope implies that the view exists within the current Spark session on the current node. A global temporary view exists within the general Spark application. This view is shareable across different Spark sessions.                                                                                                                                                                                                                                     |
| DAGScheduler                         | As Spark acts and transforms data in the task execution processes, the DAGScheduler facilitates efficiency by orchestrating the worker nodes across the cluster. This task-tracking makes fault tolerance possible, as it reapplies the recorded operations to the data from a previous state.                                                                                                                                                                                                                                                                                                                                                                         |
| DataFrame operations                 | Refer to a set of actions and transformations that can be applied to a DataFrame, which is a two-dimensional data structure in Spark. Data within a DataFrame is organized in a tabular format with rows and columns, similar to a table in a relational database. These operations encompass a wide range of tasks, including reading data into a DataFrame, performing data analysis, executing data transformations (such as filtering, grouping, and aggregating), loading data from external sources, and writing data to various output formats. DataFrame operations are fundamental for working with structured data efficiently in Spark.                                        |
| DataFrames                           | Data collection is categorically organized into named columns. DataFrames are conceptually equivalent to a table in a relational database and similar to a data frame in R or Python, but with greater optimizations. They are built on top of the SparkSQL RDD API. They use RDDs to perform relational queries. Also, they are highly scalable and support many data formats and storage systems. They are developer-friendly, offering integration with most big data tooling via Spark and APIs for Python, Java, Scala, and R.                                                                                                                                                        |
| Dataset                              | The newest Spark data abstraction, like RDDs and DataFrames, provide APIs to access a distributed data collection. They are a collection of strongly typed Java Virtual Machine, or JVM, objects. Strongly typed implies that datasets are typesafe, and the data set's datatype is made explicit during its creation. They offer benefits of both RDDs, such as lambda functions, type-safety, and SQL Optimizations from SparkSQL.                                                                                                                                                                                                                                        |
| Directed acyclic graph (DAG)         | Spark uses a DAG and an associated DAGScheduler to perform RDD operations. It is a graphical structure composed of edges and vertices. Acyclic implies new edges can originate only from an existing vertex. The vertices and edges are sequential. The edges represent transformations or actions. The vertices represent RDDs. The DAGScheduler applies a graphical structure to run tasks using the RDD, performing transformation processes. DAG enables fault tolerance. Spark replicates the DAG and restores the node when a node goes down.                                                                                                                                         |
| distinct ([numTasks]))               | It helps in finding the number of varied elements in a dataset. It returns a new dataset containing distinct elements from the source dataset.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Extract, load, and transform (ELT)   | It emerged because of big data processing. All the data resides in a data lake. A data lake is a pool of raw data for which the data purpose is not predefined. In a data lake, each project forms individual transformation tasks as required. It does not anticipate all the transformation requirements usage scenarios as in the case of ETL and a data warehouse. Organizations opt to use a mixture of ETL and ELT.                                                                                                                                                                                                                                               |
| Extract, transform, load (ETL)       | It is an important process in any data processing pipeline as the first step that provides data to warehouses for downstream applications, machine learning models, and other services.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| filter (func)                        | It helps in filtering the elements of a data set basis its function. The filter operation is used to selectively retain elements from a data set or DataFrame based on a provided function (func). It allows you to filter and extract specific elements that meet certain criteria, making it a valuable tool for data transformation and analysis.                                                                                                                                                                                                                                                                                                                 |
| flatmap (func)                       | Similar to map (func) can map each input item to zero or more output items. Its function should return a Seq rather than a single item.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Hive tables                          | Spark supports reading and writing data stored in Apache Hive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Java virtual machines (JVMs)         | The platform-specific component that runs a Java program. At run time, the VM interprets the Java bytecode compiled by the Java Compiler. The VM is a translator between the language and the underlying operating system and hardware.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| JavaScript Object Notation (JSON)    | A simplified data-interchange format based on a subset of the JavaScript programming language. IBM® Integration Bus provides support for a JSON domain. The JSON parser and serializer process messages in the JSON domain.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| JSON data sets                       | Spark infers the schema and loads the data set as a DataFrame.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Loading or exporting the data        | In the ETL pipeline's last step, data is exported to disk or loaded into another database. Also, users can write the data to the disk as a JSON file or save the data into another database, such as a Postgres (PostgresSQL) database. Users can also use an API to export data to a database, such as a Postgres database.                                                                                                                                                                                                                                                                                                                                             |
| map (func)                           | It is an essential operation capable of expressing all transformations needed in data science. It passes each element of the source through a function func, thereby returning a newly formed distributed dataset.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Parquet                              | Columnar format that is supported by multiple data processing systems. Spark SQL allows reading and writing data from Parquet files, and Spark SQL preserves the data schema.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Python                               | High-level, easy-to-comprehend, interpreted, and general-purpose dynamic programming language used in code readability. It offers a robust framework that helps build quick and scalable applications for z/OS, with an ecosystem of modules to develop new applications on any platform.                                                                                                                                                                                                                                                                                                                                                                          |
| RDD actions                          | It is used to evaluate a transformation in Spark. It returns a value to the driver program after running a computation. An example is the reduce action that aggregates the elements of an RDD and returns the result to the driver program.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| RDD transformations                  | It helps in creating a new RDD from an existing RDD. Transformations in Spark are deemed lazy as results are not computed immediately. The results are computed after evaluation by actions. For example, map transformation passes each element of a dataset through a function. This results in a new RDD.                                                                                                                                                                                                                                                                                                                                                      |
| Read the data                        | When reading the data, users can load data directly into DataFrames or create a new Spark DataFrame from an existing DataFrame.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Resilient Distributed Datasets (RDDs) | A fundamental abstraction in Apache Spark that represents distributed collections of data. RDDs

# Welcome to Apache Spark Architecture

After watching this video, you will be able to:

- Describe the architecture of Apache Spark
- Identify processes in a Spark Application
- Explain how Spark Jobs and Tasks are related
- Define Stages and describe when a Data Shuffle occurs
- Describe the cluster deploy modes the driver program can be run in

## Apache Spark Architecture

![alt text](image-48.png)
A Spark application has two main processes:

1. **Driver Program**: Runs as one process per application. The driver process can be run on a cluster node or another machine as a client to the cluster. The driver runs the application’s user code, creates work, and sends it to the cluster.

2. **Executor**: A process running multiple threads to perform work concurrently for the cluster. Executors work independently and there can be many throughout a cluster, with one or more per node depending on the configuration.

## Spark Context

![alt text](image-50.png)

- The Spark Context starts when the application launches and must be created in the driver before DataFrames or RDDs.
- Any DataFrames or RDDs created under the context are tied to it and the context must remain active for the life of them.

## Jobs and Tasks

![alt text](image-51.png)

- The driver program creates work from the user code called “Jobs” (computations that can be performed in parallel).
- The Spark Context in the driver divides the jobs into tasks to be executed on the cluster.
- Tasks from a given job operate on different data subsets, called Partitions, allowing them to run in parallel in the Executors.

## Spark Worker and Executor

- A Spark Worker is a cluster node that performs work.
- A Spark Executor utilizes a set portion of local resources as memory and compute cores, running one task per available core.
- Each executor manages its data caching as dictated by the driver. Increasing executors and available cores increases the cluster’s parallelism.
- Tasks run in separate threads until all cores are used. When a task finishes, the executor puts the results in a new RDD partition or transfers them back to the driver.

## Stages and Data Shuffle

![alt text](image-52.png)

- A “stage” in a Spark job represents a set of tasks an executor can complete on the current data partition.
- When a task requires other data partitions, Spark must perform a “shuffle,” marking the boundary between stages.
- Shuffles are costly as they require data serialization, disk, and network I/O. They enable tasks to access other dataset partitions outside the current partition.

## Example of a Shuffle

![alt text](image-53.png)

- In Stage 1, a transformation (e.g., map) is applied on dataset “a” which has 2 partitions (“1a” and “2b”), creating dataset “b”.
- The next operation requires a shuffle (e.g., groupby). To group keys of equal value together, tasks must scan each partition to pick out the matching records.
- Transformation results are placed in Stage 2. The results have the same number of partitions, but this depends on the operation.
- Final results are sent to the driver program as an action, such as collect.

> **NOTE**: It is not advised to perform a collection to the driver on a large data set as it could easily use up the driver process memory. If the data set is large, apply a reduction before collection.

## Recap

- Spark Architecture consists of the driver and the executor processes.
- The cluster comprises the Cluster Manager and worker nodes.
- The Spark Context schedules tasks to the cluster and the Cluster Manager manages the cluster’s resources.
- The driver program can be run in either client or cluster mode:
  - **Client Mode**: The application submitter (such as a user machine terminal) launches the driver outside the cluster.
  - **Cluster Mode**: The driver program is sent to and run on an available Worker node inside the cluster.
- The driver must be able to communicate with the cluster while it is running, whether it is in client or cluster mode.

In this video, you learned that:

- Spark Architecture has driver and executor processes, coordinated by the Spark Context in the driver.
- The driver creates jobs and splits them into tasks which can be run in parallel in the executors.
- Stages are a set of tasks that are separated by a data shuffle.
- Shuffles are costly, as they require data serialization, disk, and network I/O.
- The Driver can be run in either Client or Cluster mode. Client Mode connects the driver outside the cluster while Cluster Mode runs the driver in the cluster.
![alt text](image-54.png)

# Welcome to Overview of Apache Spark Cluster Modes

After watching this video, you will be able to:

- Identify the different modes of running Apache Spark on a cluster.
- Describe the components and benefits of each cluster mode.
- Describe how to run Spark to connect with each cluster mode.
- Describe how and when to setup a local Spark instance.

## Spark Cluster Manager

The Spark Cluster Manager communicates with a cluster to acquire resources for an application to run. It runs as a service outside the application and abstracts the cluster type. While an application is running, the Spark Context creates tasks and communicates to the cluster manager what resources are needed. Then the cluster manager reserves executor cores and memory resources. Once the resources are reserved, tasks can be transferred to the executor processes to run.

Spark has built-in support for several cluster managers:

- **Standalone**: Included with the Spark installation, best for setting up a simple cluster.
- **Apache Hadoop YARN**: A cluster manager from the Hadoop project.
- **Apache Mesos**: A general-purpose cluster manager that Spark can run with additional benefits.
- **Kubernetes**: An open-source system for running containerized applications.

## Spark Standalone Cluster

Spark Standalone comes packaged with the Spark installation, so there are no additional dependencies required to configure and deploy. Spark Standalone is specifically designed to run Spark and is often the fastest way to get a cluster up and running applications.

A Spark Standalone cluster has two main components:

- **Workers**: Run on cluster nodes and start an executor process with one or more reserved cores.
- **Master**: There must be one master available, which can run on any cluster node. It connects workers to the cluster and keeps track of them with heartbeat polling.

> **Note**: If the master is together with a worker, do not reserve all the node’s cores and memory for the worker.

### Setting up a Spark Standalone Cluster

1. **Start the Master**: The Master is assigned a URL with a hostname and port number.
2. **Start Workers**: Use the Master URL to start workers on any node using bi-directional communication with the master.

Once the master and the workers are running, you can launch a Spark application on the cluster by specifying the master URL as an argument to connect them.

For additional configuration options, refer to the Apache Spark documentation on the [spark.apache.org](https://spark.apache.org) website.
![alt text](image-55.png)
![alt text](image-56.png)

## Apache Hadoop YARN

Apache Hadoop YARN is a general-purpose cluster manager. It’s popular in the big data ecosystem and supports many other frameworks besides Spark. YARN clusters have their own dependencies, set-up, and configuration requirements, so deploying them is more complex than Spark Standalone.

To run Spark on an existing YARN cluster, use the `--master` option with the keyword YARN. Spark will look for the standard Hadoop configuration files to decide how to connect with the YARN cluster. No other configuration from Spark is needed.

## Apache Mesos

Apache Mesos is another general-purpose cluster manager supported by Spark. Using Mesos has some advantages, such as providing dynamic partitioning between Spark and other big data frameworks and scalable partitioning between multiple Spark instances. However, running Spark on Apache Mesos might require some additional setup depending on your configuration requirements. More details are provided on the [spark.apache.org](https://spark.apache.org) website.

## Kubernetes

![alt text](image-57.png)
A Kubernetes cluster runs containerized applications. This makes Spark applications more portable and helps automate deployment, simplify dependency management, and scale the cluster as needed. Spark uses a built-in native Kubernetes scheduler. To run Spark on Kubernetes, use the example call shown.

## Local Mode

![alt text](image-58.png)
Local mode runs a Spark application as a single process locally on the machine. Executors are run as separate threads in the main process that calls `spark-submit`. Local mode does not connect to any cluster or require configuration outside a basic Spark installation.

Local mode can be run on a laptop. It is useful for testing or debugging a Spark application, such as testing a small data subset to verify correctness before running the application on a cluster. However, being constrained by a single process means local mode is not designed for optimal performance.

To run in local mode, use the `--master` option with the keyword `local` followed by a number to indicate how many cores the Spark application can use for the executor. To use all available cores, replace the number with an asterisk wildcard. Keep in mind not all configuration for a cluster will be valid in local mode.

## Summary

In this video, you learned that:

- Cluster managers acquire resources and run as an abstracted service outside the application.
- Spark can run on Spark Standalone, Apache Hadoop YARN, Apache Mesos, or Kubernetes cluster managers, with specific setup requirements.
- Choosing a cluster manager depends on your data ecosystem and factors such as ease of configuration, portability, deployment, or data partitioning needs.
- Spark can run in local mode, useful for testing or debugging an application.

# Welcome to “How to Run an Apache Spark Application”

After watching this video, you will be able to:

- Describe how to submit an Apache Spark application.
- Explain the characteristics of Spark’s unified interface, ‘spark-submit.’
- Describe and apply the options you can use to submit applications.
- Describe ways of managing external application dependencies.
- Describe the benefits of using Spark Shell to run applications.

## Submitting an Apache Spark Application

Spark comes with a unified interface for submitting applications – it is the ‘spark-submit’ script found in the ‘bin/’ directory. ‘spark-submit’ can be used for all supported cluster types and accepts many configuration options for the application or cluster. The “unified interface” means you can switch from running Spark in local mode to a cluster by changing a single argument. ‘spark-submit’ works the same way, no matter the application language. For example, a cluster can run Python and Java applications simultaneously by passing in the required files.

### Using ‘spark-submit’

1. The ‘spark-submit’ script first parses any command line arguments or options.
2. It reads any additional configuration specified in the ‘spark-defaults’ folder.
3. The ‘--master’ argument tells the application how to connect to the cluster or run locally.
4. Specify any application files (including JARs or Python files) so they can start the driver program and distribute files to run in the cluster.
![alt text](image-59.png)
Some ‘spark-submit’ options are mandatory, such as specifying the master option to tell Spark which cluster manager to connect to. If the application is written in Java or Scala and packaged in a JAR, you must specify the full class name of the program entry point. Other options include:

- Driver deploy mode (run as a client or in the cluster).
- Executor resource settings (such as reserving memory or cores).

Driver deploy mode defaults to client mode. Some options relate to specific cluster managers. Additional Spark configuration can be specified on the command line using the ‘--conf’ argument followed by key=value. For Java or Scala and Python, final arguments will be the path to the application JAR or Python script. Next are optional application-specific arguments. These will automatically be passed in. You can add Python files with ‘.py,’ ‘.egg’, or ‘.zip’ using the ‘--py-files’ argument. These files will be distributed to the cluster and available in the Python environment.

### Examples of ‘spark-submit’

1. **Launching SparkPi (Scala version) on YARN**:

    ```sh
    ./bin/spark-submit --class org.apache.spark.examples.SparkPi \
      --master yarn \
      examples/jars/spark-examples_2.11-2.4.5.jar 10
    ```

2. **Launching SparkPi (Python version) on a Standalone cluster**:

    ```sh
    ./bin/spark-submit \
      --master spark://your_spark_master:7077 \
      examples/src/main/python/pi.py 1000
    ```

## Managing Spark Dependencies

For a Java or Scala-based application, it’s best to create an uber-JAR. This is a single JAR file with all dependencies (including transitive ones) so the application is portable throughout the cluster. For Python applications, ensure that:

1. The cluster nodes access required dependencies with the same version.
2. The same Python version is used.

Solutions for Python dependencies may involve creating virtual environments so that applications can run in separate, isolated environments. Python dependencies can be included in the spark-submit script using the ‘--py-files’ argument: this will accept ‘.py’, ‘.zip’ or ‘.egg’ files.

## Using Spark Shell

![alt text](image-60.png)
Spark Shell is available for Scala and Python, giving you access to Spark APIs for working with data as Spark jobs. Spark Shell can be used in local or cluster mode, with all options available. When Spark Shell starts, the environment automatically initializes the SparkContext and SparkSession variables. This means you can start working with data immediately.

Expressions are entered in the shell and evaluated in the driver. Entering an action on a shell DataFrame generates Spark jobs that are sent to the cluster to be scheduled as tasks.

### Example: Spark Scala Shell

Starting up in local mode:

```sh
./bin/spark-shell --master local[2]
```

Output:

- Spark’s load log in the log4j-defaults.properties file.
- Spark’s Web UI address, displaying running jobs in the shell.
- Variable names for the initialized SparkContext and SparkSession.
- Version information for important libraries like JDK and Scala.

Running code in the Scala shell:

```scala
val df = spark.range(0, 10)
val df2 = df.withColumn("mod2", $"id" % 2)
df2.show(4)
```

In this video, you learned that:

- ‘spark-submit’ is a unified interface to submit the Spark Application, no matter the cluster manager or application language.
- Mandatory options include telling Spark which cluster manager to connect to; other options set driver deploy mode or executor resourcing.
- To manage dependencies, application projects or libraries must be accessible for driver and executor processes, for example by creating a Java or Scala uber-JAR.
- Spark Shell simplifies working with data by automatically initializing the SparkContext and SparkSession variables and providing Spark API access.

# Welcome to Setting Apache Spark Configuration

After watching this video, you will be able to:

- Describe the configuration types of an Apache Spark Application.
- Explain the purpose and common options for each configuration type.
- Describe when to use static or dynamic configuration.

## Configuring a Spark Application

You can configure a Spark Application using three different methods: properties, environment variables, or logging configuration.

### Spark Properties

You can set Spark properties to adjust and control most application behaviors, including setting properties with the driver and sharing them with the cluster. Spark properties can be configured in the following ways:

- **Programmatically**: Set configuration in the driver program when creating the `SparkSession` or by using a separate `SparkConf` object passed into the session constructor.
- **Configuration File**: Set properties in a configuration file found at `conf/spark-defaults.conf`.
- **spark-submit**: Set properties when launching the application with `spark-submit`, either by using provided options such as `--master` or using the `--conf` option with a key-value pair.

### Environment Variables

Environment variables are loaded on each machine, allowing for adjustments on a per-machine basis if hardware or installed software differs between the cluster nodes. These are set in the `conf/spark-env.sh` file and can be used to configure specifics such as ensuring each machine uses the same Python executable by setting the `PYSPARK_PYTHON` environment variable.

### Logging Configuration

Spark logging is controlled by the log4j configuration file located at `conf/log4j.properties`. This file dictates what level of messages, such as info or errors, are logged to file or output to the driver during application execution. Log4j allows configuring where the logs are sent to and adjusting specific components of Spark or third-party libraries.

## Configuration Files

Spark configuration files are located under the `conf` directory in the installation. By default, there are no preexisting files after installation, but Spark provides templates for each configuration type with the filenames shown below. You can create the appropriate file by removing the ‘.template’ extension. Inside the template files, there are sample configurations for common settings which can be enabled by uncommenting.

## Precedence Order of Configuration Settings

Because Spark properties can be set in different ways, it’s important to understand how they are merged to build the final configuration for the application:

1. **Programmatically**: Configuration set programmatically takes the highest precedence and will overwrite any previous settings.
2. **spark-submit**: Configuration provided with the `spark-submit` script has the next highest precedence.
3. **Configuration File**: Configuration set in the `spark-defaults.conf` file has the lowest precedence.

## Static vs Dynamic Configuration

### Static Configuration

Static configuration refers to settings that are written programmatically into the application itself. These settings are not usually changed because modifying them requires changing the application. Use static configuration for settings unlikely to change between application runs, such as application name or properties related to the application only.

Example:

```scala
val spark = SparkSession.builder()
  .appName("ExampleApp")
  .config("spark.driver.maxResultSize", "2g")
  .getOrCreate()
```

### Dynamic Configuration

Dynamic configuration is useful to avoid hardcoding specific values in the application itself. This is usually done for configurations such as the master location, allowing the application to be launched on different clusters by simply changing the master location. Examples include setting how many cores are used or how much memory is reserved by each executor to properly tune the application for the cluster it runs on.

## Summary

In this video, you learned that:

- You can set Spark configuration using properties (to control application behavior), environment variables (to adjust settings on a per-machine basis), or logging properties (to control logging outputs).
- Spark property configuration follows a precedence order, with the highest being configuration set programmatically, then `spark-submit` configuration, and lastly configuration set in the `spark-defaults.conf` file.
- Static configuration should be used for values that don’t change from run to run or properties related to the application, such as application name.
- Dynamic configuration should be used for values that change or need tuning when deployed, such as master location, executor memory, or core settings.
