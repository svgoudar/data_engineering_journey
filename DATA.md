## Types of Data

### Structured Data:

* Well-defined structure adhering to specified data models.
* Typically stored in databases and represented in tabular formats.
* Sources include SQL databases, spreadsheets (e.g., Excel), online forms, sensors (e.g., GPS, RFID), and network/web server logs.
* Can be easily examined with standard data analysis methods and tools.

### Semi-structured Data:

* Has some organizational properties but lacks a fixed schema.
* Cannot be stored in traditional rows and columns.
* Contains tags, elements, or metadata for grouping and hierarchy.
* Sources include emails, XML, binary executables, TCP/IP packets, zipped files, and integration of data from different sources.
* XML and JSON are commonly used to store and exchange semi-structured data.

## Unstructured Data:

* Lacks an identifiable structure and cannot be organized in traditional databases.
* Does not follow a specific format, sequence, semantics, or rules.
* Sources include web pages, social media feeds, images, video/audio files, documents/PDFs, presentations, media logs, and surveys.
* Can be stored in files/documents for manual analysis or in NoSQL databases with specialized analysis tools.

## Tupes of File formats


### Delimited Text File Formats:

* Store data as text with values separated by delimiters like comma or tab.
* Common formats include CSV (comma-separated values) and TSV (tab-separated values).
* Each row represents a record with values separated by delimiters.
* Suitable for providing straightforward information schema and can be processed by various applications.

### Microsoft Excel Open XML Spreadsheet (XLSX):
* XML-based file format created by Microsoft for Excel.
* Contains multiple worksheets organized into rows and columns.
* Each cell contains data.
* Open file format accessible to most applications, known for security.

### Extensible Markup Language (XML):

* Markup language for encoding data.
* Readable by humans and machines.
* Self-descriptive language for sending information over the internet.
* Platform and programming language independent, simplifying data sharing.
### Portable Document Format (PDF):

* Developed by Adobe for presenting documents independent of software, hardware, and operating systems.
* Frequently used in legal, financial documents, and form filling.

### JavaScript Object Notation (JSON):

* Text-based open standard for transmitting structured data over the web.
* Language-independent data format readable in any programming language.
* Easy to use, compatible with a wide range of browsers.
* Commonly used in APIs and web services for sharing data.

## Sources of Data

### Relational Databases:

* Utilized in internal applications for managing business activities and transactions.
* Examples include SQL Server, Oracle, MySQL, and IBM DB2.
* Data from databases can be analyzed for insights such as sales analysis or customer projections.

### Flatfiles and XML Datasets:
* External datasets available in formats like flat files (CSV), spreadsheet files, or XML documents.
* Flat files store data in plain text format with delimiters like commas or tabs.
* XML files support complex data structures and are used for hierarchical data.

### APIs and Web Services:

* Offer data access for multiple users or applications in various formats like plain text, XML, HTML, JSON, or media files.
* Examples include Twitter and Facebook APIs for sentiment analysis, stock market APIs, and data lookup/validation APIs.

### Web Scraping:
* Extracts specific data from unstructured sources on web pages based on defined parameters.
* Common uses include collecting product details, generating sales leads, and gathering training datasets for machine learning.
* Popular tools include BeautifulSoup, Scrapy, Pandas, and Selenium.

### Data Streams and Feeds:

* Aggregate constant streams of data from various sources like IoT devices, social media, and web clicks.
* Used for tasks such as financial trading, supply chain management, threat detection, and sentiment analysis.
* Popular applications for processing data streams include Apache Kafka, Apache Spark Streaming, and Apache Storm.

### RSS Feeds:

* Capture updated data from online forums and news sites.
Updates are streamed to user devices through feed readers.


## Languages of Data professionals


### Query Languages

- Query languages are designed for accessing and manipulating data in a database, such as SQL.

### Programming Languages

- Programming languages are designed for developing applications and controlling application behavior. Examples include Python, R, and Java.

### Shell and Scripting Languages

- Shell and scripting languages, such as Unix/Linux Shell and PowerShell, are ideal for repetitive and time-consuming operational tasks.


### SQL

SQL (Structured Query Language) is a querying language designed for accessing and manipulating information from relational databases. Using SQL, we can:

- Insert, update, and delete records
- Create new databases, tables, and views
- Write stored procedures

Advantages of using SQL include:

- Portability across platforms
- Simple syntax similar to English
- Efficiency in retrieving large amounts of data
- Quick prototyping due to its interpreter system

### Python

- Python is a widely-used open-source, general-purpose, high-level programming language. Advantages of Python include:
- Expressiveness and readability
- Large developer community
- Ease of learning
- Performance in handling vast amounts of data
- Support for multiple programming paradigms

### R

- R is an open-source programming language and environment for data analysis, visualization, machine learning, and statistics. Key benefits of R include:
- Platform independence
- Extensibility
- Comprehensive data capabilities
- Compelling visualizations with libraries like Ggplot2 and Plotly

### Java

- Java is an object-oriented, platform-independent programming language used in data analytics processes such as cleaning, importing/exporting data, and statistical analysis.
- Java is also prominent in big data frameworks like Hadoop, Hive, and Spark.

### Unix/Linux Shell

- A Unix/Linux Shell is a series of commands written in a plain text file to accomplish specific tasks, useful for repetitive and time-consuming operations such as file manipulation, system administration, and backups.

### PowerShell

- PowerShell is a cross-platform automation tool and configuration framework by Microsoft. It's optimized for working with structured data formats, and it's object-based, making it suitable for tasks like data mining, GUI building, and report creation.



## Metadata in Data Management

Metadata is data that provides information about other data. In the context of databases, data warehousing, business intelligence systems, and various data repositories, metadata can be categorized into three main types:

### 1. Technical Metadata

Technical metadata defines data structures primarily from a technical perspective. Examples include:

- Tables recording information about tables in a database (e.g., name, number of columns and rows)
- Data catalog inventorying tables and their attributes (e.g., database names, column names, data types)
- Typically stored in specialized tables in the database's System Catalog.

### 2. Process Metadata

Process metadata describes the processes operating behind business systems, tracking things like:

- Process start and end times
- Disk usage
- Data movement between sources
- User access patterns
- Vital for troubleshooting and optimizing workflows.

### 3. Business Metadata

Business metadata is information about data described in readily interpretable ways for business users, including:

- How data is acquired
- What data measures or describes
- Connections between data sources
- Serves as documentation for the data warehouse system.

### Managing Metadata

Managing metadata involves developing policies and processes to ensure information can be accessed, integrated, and shared across the enterprise. Key components include:

- Reliable, user-friendly data catalog
- Web-based user interface for easy search and access
- Central to any Data Governance initiative.

### Importance of Metadata Management

Good metadata management offers numerous benefits, including:

- Enhanced data discovery and repeatability
- Improved data governance and lineage tracing
- Better understanding of business context associated with data.

### Popular Tools for Metadata Management

Some popular metadata management tools include:

- IBM InfoSphere Information Server
- CA Erwin Data Modeler
- Oracle Warehouse Builder
- SAS Data Integration Server
- Talend Data Fabric
- Alation Data Catalog
- SAP Information Steward
- Microsoft Azure Data Catalog
- IBM Watson Knowledge Catalog
- Oracle Enterprise Metadata Management (OEMM)
- Adaptive Metadata Manager
- Unifi Data Catalog
- data.world
- Informatica Enterprise Data Catalog


### Data Repositories
A data repository is a general term used to refer to data that has been collected, organized, and isolated so that it can be used for business operations or mined for reporting and data analysis. It can be a small or large database infrastructure with one or more databases that collect, manage, and store data sets. In this video, we will provide an overview of the different types of repositories your data might reside in, such as databases, data warehouses, and big data stores, and examine them in greater detail in further videos. Let’s begin with databases.

### Databases

A database is a collection of data, or information, designed for the input, storage, search and retrieval, and modification of data. And a Database Management System, or DBMS, is a set of programs that creates and maintains the database. It allows you to store, modify, and extract information from the database using a function called querying. For example, if you want to find customers who have been inactive for six months or more, using the query function, the database management system will retrieve data of all customers from the database that have been inactive for six months and more. Even though a database and DBMS mean different things, the terms are often used interchangeably.

There are different types of databases. Several factors influence the choice of database, such as the data type and structure, querying mechanisms, latency requirements, transaction speeds, and intended use of the data. It’s important to mention two main types of databases here—relational and non-relational databases.

#### Relational Databases

Relational databases, also referred to as RDBMSes, build on the organizational principles of flat files, with data organized into a tabular format with rows and columns following a well-defined structure and schema. However, unlike flat files, RDBMSes are optimized for data operations and querying involving many tables and much larger data volumes. Structured Query Language, or SQL, is the standard querying language for relational databases.

#### Non-relational Databases

Then we have non-relational databases, also known as NoSQL, or “Not Only SQL”. Non-relational databases emerged in response to the volume, diversity, and speed at which data is being generated today, mainly influenced by advances in cloud computing, the Internet of Things, and social media proliferation. Built for speed, flexibility, and scale, non-relational databases made it possible to store data in a schema-less or free-form fashion. NoSQL is widely used for processing big data.

### Data Warehouses

A data warehouse works as a central repository that merges information coming from disparate sources and consolidates it through the extract, transform, and load process, also known as the ETL process, into one comprehensive database for analytics and business intelligence. At a very high-level, the ETL process helps you to extract data from different data sources, transform the data into a clean and usable state, and load the data into the enterprise’s data repository. Related to Data Warehouses are the concepts of Data Marts and Data Lakes, which we will cover later. Data Marts and Data Warehouses have historically been relational since much of the traditional enterprise data has resided in RDBMSes. However, with the emergence of NoSQL technologies and new sources of data, non-relational data repositories are also now being used for Data Warehousing.

### Big Data Stores

Another category of data repositories are Big Data Stores, that include distributed computational and storage infrastructure to store, scale, and process very large data sets. Overall, data repositories help to isolate data and make reporting and analytics more efficient and credible while also serving as a data archive.


### RDMS
- **Relational Database Structure**: 
  - Organized into tables.
  - Tables can be linked based on common data.
  - Rows represent records, and columns represent attributes.
  
- **Querying with SQL**:
  - Uses Structured Query Language (SQL) for data querying.
  - Allows for retrieving data from multiple tables with a single query.
  
- **Optimized Storage and Processing**:
  - Ideal for large volumes of data.
  - Minimizes data redundancy.
  
- **Data Integrity and Consistency**:
  - Ensures consistency and integrity through data types and constraints.
  
- **Security and Access Control**:
  - Provides controlled access to data.
  - Enforces standards and policies for data governance.
  
- **Scalability**:
  - Ranges from small desktop systems to massive cloud-based systems.
  
- **Popular Relational Databases**:
  - IBM DB2, Microsoft SQL Server, MySQL, Oracle Database, PostgreSQL.
  
- **Cloud Relational Databases**:
  - Offered as Database-as-a-Service (DBaaS).
  - Examples include Amazon RDS, Google Cloud SQL, IBM DB2 on Cloud, Oracle Cloud, SQL Azure.
  
- **Advantages**:
  - Flexibility in schema modifications.
  - Reduced data redundancy.
  - Ease of backup and disaster recovery.
  - ACID-compliance for data reliability.
  
- **Use Cases**:
  - Online Transaction Processing (OLTP).
  - Data Warehousing and Online Analytical Processing (OLAP).
  - IoT Solutions.
  
- **Limitations**:
  - Not suitable for semi-structured and unstructured data.
  - Schema and data type matching required for migration.
  - Limits on data field lengths.
  
- **Continued Relevance**:
  - Despite limitations, remains predominant for structured data management.

### NoSQL

- **NoSQL Overview**:
  - Stands for “not only SQL” or sometimes “non SQL”.
  - Provides flexible schemas for data storage and retrieval.
  - Gained popularity in the era of cloud, big data, and high-volume web and mobile applications.
  - Chosen for attributes such as scale, performance, and ease of use.

- **NoSQL Characteristics**:
  - Built for specific data models.
  - Flexible schemas, not based on fixed row/column/table design.
  - Typically do not use SQL for querying.
  - Allows for schema-less or free-form data storage.

- **Types of NoSQL Databases**:
  1. **Key-value store**:
     - Data stored as key-value pairs.
     - Great for user session data, real-time recommendations, and caching.
     - Examples: Redis, Memcached, DynamoDB.
     
  2. **Document-based**:
     - Stores each record and associated data within a single document.
     - Suitable for eCommerce, CRM, and analytics platforms.
     - Examples: MongoDB, DocumentDB, CouchDB.
     
  3. **Column-based**:
     - Stores data in columns rather than rows.
     - Ideal for heavy write requests, time-series data, and IoT data.
     - Examples: Cassandra, HBase.
     
  4. **Graph-based**:
     - Uses graphical model to represent and store data.
     - Useful for analyzing interconnected relationships.
     - Examples: Neo4J, CosmosDB.

- **Advantages of NoSQL**:
  - Handles large volumes of structured, semi-structured, and unstructured data.
  - Can run as distributed systems scaled across multiple data centers.
  - Provides efficient and cost-effective scale-out architecture.
  - Offers simpler design, better control over availability, and improved scalability.
  
- **Key Differences with Relational Databases**:
  - NoSQL databases are schema-agnostic, allowing unstructured and semi-structured data.
  - Relational databases support ACID-compliance, ensuring reliability of transactions.
  - RDBMS is mature and well-documented, while NoSQL is relatively newer.
  
- **Continued Relevance**:
  - NoSQL databases are increasingly used for mission-critical applications.



- **NoSQL Overview**:
  - Stands for “not only SQL” or sometimes “non SQL”.
  - Provides flexible schemas for data storage and retrieval.
  - Popular in the era of cloud, big data, and high-volume applications.

- **Flexibility and Data Models**:
  - Built for specific data models with flexible schemas.
  - Does not strictly adhere to traditional row/column/table designs.
  - May not use SQL for querying data.

- **Common Types of NoSQL Databases**:
  - **Key-value store**: Redis, Memcached, DynamoDB.
  - **Document-based**: MongoDB, DocumentDB, CouchDB.
  - **Column-based**: Cassandra, HBase.
  - **Graph-based**: Neo4J, CosmosDB.

- **Advantages of NoSQL**:
  - Handles large volumes of structured, semi-structured, and unstructured data.
  - Runs as distributed systems scaled across multiple data centers.
  - Cost-effective scale-out architecture.
  - Simpler design and improved scalability.

- **Key Differences from Relational Databases**:
  - NoSQL databases are schema-agnostic, allowing for unstructured and semi-structured data.
  - Designed for low-cost commodity hardware.
  - ACID-compliance may not be supported.
  - Less mature compared to relational databases.

- **Use Cases**:
  - Key-value stores for user session data, real-time recommendations.
  - Document databases for flexible indexing, powerful ad hoc queries.
  - Column databases for heavy write requests, time-series data.
  - Graph databases for visualizing and analyzing interconnected data.

- **Continued Relevance**:
  - Increasingly used for mission-critical applications despite being a relatively newer technology.

### Data Warehouses, Data Marts, and Data Lakes

- **Data Mining Repositories Overview**:
  - Goal: House data for reporting, analysis, and deriving insights.
  - Characteristics and applications of data warehouses, data marts, and data lakes discussed.

- **Data Warehouse**:
   ![](snaps/data_warehouse.png)
  - Central repository of integrated data from multiple sources.
  - Single source of truth storing cleansed, conformed, and categorized current and historical data.
  - Three-tier architecture: Database servers, OLAP Server, Client front-end layer.
  - Moving to the cloud for benefits like lower costs and faster disaster recovery.
  - Popular examples include Teradata, Oracle Exadata, Amazon RedShift.

- **Data Mart**:
  - Sub-section of a data warehouse for specific business functions or user communities.
  - Types: Dependent, independent, hybrid data marts.
  - Purpose: Provide relevant data, accelerate processes, facilitate data-driven decisions.

- **Data Lake**:
  - Stores structured, semi-structured, and unstructured data in native format.
  - No need to define structure/schema before loading data.
  - Governance ensures data classification, protection, and governance.
  - Reference architecture independent of technology.
  - Benefits: Stores all types of data, scales based on capacity, saves time in defining structures.

- **Technologies and Vendors**:
  - Deployed using Cloud Object Storage (e.g., Amazon S3) or distributed systems (e.g., Apache Hadoop).
  - Vendors include Amazon, Cloudera, Google, IBM, Microsoft, Oracle, SAS, Snowflake, Teradata, Zaloni.

- **Evaluation**:
  - Need to be evaluated within the context of use case and technology infrastructure.
  
### Considerations for Choice of Data Repository

- Factors to consider when choosing a data repository:
  - Use case:
    - Structured, semi-structured, or unstructured data
    - Knowledge of data schema
  - Performance requirements:
    - Data at rest, streaming data, or data in motion
    - Encryption needs
  - Volume and storage requirements:
    - Big data system necessity
    - Storage and update frequency
  - Organizational standards:
    - Database preferences set by the organization
  - Capacity and access needs:
    - Short intervals or long-running queries
    - Transaction processing, analytics, archival, or warehousing purposes
  - Compatibility:
    - Integration with existing programming languages, tools, and processes
  - Security features:
    - Ensuring data security
  - Scalability:
    - Ability to scale along with the organization's growth

- Preferred solutions and considerations:
  - Enterprise relational database (e.g., Db2)
  - Open-source relational database for smaller projects and microservices
  - Preferred unstructured data source
  - Consideration of organizational skills and cost implications

- Hosting platform considerations:
  - Choice of hosting platform (e.g., AWS RDS, Amazon Aurora, Google's relational offerings)
  - Impact on decision-making regarding database selection

- Questions to consider:
  - Data storage decisions
  - Data retrieval methods
  - Hosting platform decisions

- Factors determining the choice of data source:
  - Structure, application nature, and data ingestion volume
  - Relational databases (e.g., IBM Db2, Oracle, Postgres) for most cases
  - Edge cases may require alternative solutions:
    - Document stores (e.g., MongoDB) for large data ingestion
    - Wide column stores (e.g., Cassandra) for certain use cases
    - Graph data structures (e.g., Neo4J, Apache TinkerPop) for network analysis
    - Hadoop with MapReduce for big data analytics



- In this video, we will learn about some of the different tools and processes that work to move data from source to destination systems, such as:
  - ETL, or the Extract, Transform, and Load Process
  - ELT, or the Extract, Load, and Transform Process
  - Data Pipelines

- **Extract, Transform, and Load (ETL) Process**:
  ![](snaps/etl.png)
  - Purpose: Converts raw data into analysis-ready data.
  - Extract:
    - Batch processing: Moves data in large chunks at scheduled intervals (e.g., Stitch, Blendo).
    - Stream processing: Pulls real-time data and transforms it in transit (e.g., Apache Samza, Apache Kafka).
  - Transform: Executes rules and functions to convert raw data (e.g., standardizing date formats, removing duplicates).
  - Load: Transports processed data to a destination system or repository (e.g., initial loading, incremental loading, full refresh).
  - Tools: IBM Infosphere Information Server, AWS Glue, Improvado, Skyvia, HEVO, Informatica PowerCenter.

- **Extract, Load, and Transform (ELT) Process**:
  ![](snaps/elt.png)
  - Extracted data is first loaded into the target system, and transformations are applied in the target system.
  - Ideal for processing large sets of unstructured and non-relational data.
  - Destination: Data lake or data warehouse.
  - Advantages: Shorter cycle between extraction and delivery, flexibility for analysts, leverages raw data for multiple use cases.

- **Data Pipelines**:
  - Encompasses the entire journey of moving data from one system to another.
  - Can be architected for batch processing, streaming data, or a combination of both.
  - Supports long-running batch queries and smaller interactive queries.
  - Destination: Typically a data lake, but may include other target destinations.
  - Solutions: Apache Beam, AirFlow, DataFlow.

- In this video, we learned about some of the different data movement approaches—the ETL (or Extract, Transfer, and Load process) and ELT (or the Extract, Load, and Transform process). We also learned about Data Pipelines, encompassing the complete journey of data from one system to another.


- **Definition of Data Integration**:
  - Discipline comprising practices, architectural techniques, and tools for ingesting, transforming, combining, and provisioning data across various types.

- **Usage Scenarios**:
  - Ensuring data consistency across applications.
  - Master data management.
  - Data sharing between enterprises.
  - Data migration and consolidation.

- **In Analytics and Data Science**:
  - Accessing, queuing, or extracting data from operational systems.
  - Transforming and merging extracted data.
  - Ensuring data quality and governance.
  - Delivering data through integrated approach for analytics.

- **Relation to ETL and Data Pipelines**:
  - Data integration combines disparate data into unified view, while data pipeline covers entire data movement journey.
  - ETL is a process within data integration.

- **Capabilities of Modern Data Integration Solutions**:
  - Extensive catalog of pre-built connectors.
  - Open-source architecture.
  - Optimization for batch processing and continuous data streams.
  - Integration with Big Data sources.
  - Additional functionalities like data quality, governance, compliance, and security.
  - Portability across cloud environments.

- **Data Integration Platforms and Tools**:
  - Offerings from various vendors: IBM, Talend, SAP, Oracle, Denodo, SAS, Microsoft, Qlik, TIBCO.
  - Examples of open-source frameworks: Dell Boomi, Jitterbit, SnapLogic.
  - Cloud-based Integration Platform as a Service (iPaaS) offerings.

- **Evolution of Data Integration**:
  - Continues to evolve with businesses embracing newer technologies and increasing data variety and use in decision-making.


## Big Data

- **Definition of Big Data**:
  - Refers to dynamic, large, and disparate volumes of data created by people, tools, and machines.
  - Requires innovative and scalable technology for collection, hosting, and analytical processing to derive real-time business insights.

- **V's of Big Data**:
  - **Velocity**: Speed at which data accumulates, facilitated by near or real-time streaming and processing technologies.
  - **Volume**: Scale of data increase, driven by more data sources, higher resolution sensors, and scalable infrastructure.
  - **Variety**: Diversity of data sources and formats, including structured and unstructured data from various sources.
  - **Veracity**: Quality and origin of data, including attributes like consistency, completeness, integrity, and ambiguity.
  - **Value**: Ability to derive value from data beyond profit, including medical, social, and personal benefits.

- **Examples of V's in Action**:
  - **Velocity**: Every 60 seconds, hours of footage uploaded to YouTube, demonstrating rapid data accumulation.
  - **Volume**: Approximately 2.5 quintillion bytes of data generated daily by digital devices used by the world population.
  - **Variety**: Various types of data including text, pictures, sound, health data from wearables, and IoT device data.
  - **Veracity**: Challenges in dealing with 80% unstructured data, requiring reliable methods for analysis and visualization.

- **Handling Big Data**:
  - Requires alternative tools leveraging distributed computing power like Apache Spark and Hadoop ecosystem.
  - Enables extraction, loading, analysis, and processing of data across distributed compute resources.
  - Provides organizations with more ways to connect with customers and enrich services.

- **Impact of Big Data**:
  - Demonstrates the journey of personal data through big data analysis, leading to insights and services that may benefit individuals.

  
- **Big Data Processing Technologies**:
  - Provide ways to work with large sets of structured, semi-structured, and unstructured data to derive value from big data.

- **Open Source Technologies for Big Data Analytics**:
  - **Apache Hadoop**:
    - Collection of tools for distributed storage and processing of big data.
    - Scales from single node to clusters, offering reliable and cost-effective storage solution.
    - Incorporates emerging data formats and provides real-time access for stakeholders.
  
  - **Apache Hive**:
    - Data warehouse for query and analysis built on top of Hadoop.
    - Read-based, less suitable for transaction processing, but suitable for ETL, reporting, and data analysis tasks.
    - Enables easy access to data via SQL.

  - **Apache Spark**:
    - Distributed data analytics framework for complex analytics in real-time.
    - General-purpose engine for various applications including Interactive Analytics, Streams Processing, Machine Learning, etc.
    - Utilizes in-memory processing to increase computation speed, with support for multiple programming languages and data sources.



## Layers of a Data Platform Architecture
  ![](snaps/layers_of_data_platform.png)
  - **Data Ingestion or Data Collection Layer**:
    - Connects to source systems and brings data into the platform.
    - Tasks include connecting to data sources, transferring data, and maintaining metadata.
    - Tools: Google Cloud DataFlow, IBM Streams, Amazon Kinesis, Apache Kafka.

  - **Data Storage and Integration Layer**:
    - Stores and integrates ingested data.
    - Tasks include storing data, transforming, and making it available for processing.
    - Tools: IBM DB2, Microsoft SQL Server, MySQL, MongoDB, Apache HBase, IBM Cloudant, Talend.

  - **Data Processing Layer**:
    - Processes ingested and integrated data.
    - Tasks include data validations, transformations, and applying business logic.
    - Tools: Apache Spark, Python, R, spreadsheets, Watson Studio Refinery, Google DataPrep.

  - **Analysis and User Interface Layer**:
    - Delivers processed data to data consumers.
    - Data consumers include BI analysts, data scientists, and other applications.
    - Tools: Tableau, Jupyter Notebooks, IBM Cognos Analytics, Microsoft Power BI.

  - **Data Pipeline Layer**:
    - Implements and maintains continuously flowing data pipelines.
    - Responsible for Extract, Transform, and Load (ETL) operations.
    - Tools: Apache Airflow, DataFlow.

- **Integration Platforms and Tools**:
  - Offer various integration solutions including iPaaS.
  - Tools: Adeptia Integration Suite, Google Cloud's Cooperation 534, IBM's Application Integration Suite on Cloud, Informatica's Integration Cloud.

## Factors for Selecting and Designing Data Stores


- **Design Considerations for Data Store**:
  - **Type of   Data**:
    - Can be relational or non-relational, structured or unstructured.
    - Requires selecting appropriate database types.

  - **Volume of Data**:
    - Consider scale of data and need for raw storage or structured processing.
    - Options include data lakes or big data repositories.

  - **Intended Use of Data**:
    - Consider transactional vs. analytical needs.
    - Determine response time, backup, and recovery requirements.

  - **Scalability**:
    - Capability to handle growth in data, workloads, and users.
    - Normalization vs. denormalization considerations.

  - **Performance, Availability, Integrity, and Recoverability**:
    - Performance: Throughput and latency.
    - Availability: Ensure data access without downtime.
    - Integrity: Protect data from corruption, loss, and attack.
    - Recoverability: Ability to recover data after failures or disasters.

  - **Data Privacy, Security, and Governance**:
    - Follow layered security approach with access control and encryption.
    - Comply with regulations like GDPR, CCPA, HIPAA.
    - Implement data privacy and governance strategies from the start.

- **Key Database Types**:
  - **Relational Databases**:
    - Suitable for structured data with defined schema.
    - Examples: IBM DB2, Microsoft SQL Server, MySQL.
  - **Non-Relational Databases (NoSQL)**:
    - Suitable for semi-structured and unstructured data.
    - Types include key-value, document, column, and graph-based.
    - Examples: MongoDB, Cassandra, Neo4J.


## Security 


- **Security in Enterprise Data Platforms**:
  - Security is addressed at multiple levels in enterprise data platforms.
  - Facets of security include:
    - Physical infrastructure security
    - Network security
    - Application security
    - Data security

- **Key Components of Information Security**:
  - **CIA Triad**:
    - **Confidentiality**: Control unauthorized access.
    - **Integrity**: Validate resources are trustworthy.
    - **Availability**: Ensure authorized access when needed.

- **Levels of Security**:
  1. **Physical Infrastructure Security**:
     - Measures include authentication, surveillance, power redundancy, environmental protections.
  2. **Network Security**:
     - Utilizes firewalls, network access control, segmentation, security protocols, intrusion detection.
  3. **Application Security**:
     - Built-in security through threat modeling, secure design, coding practices, and security testing.
  4. **Data Security**:
     - Involves encryption for data at rest and in transit, authentication, and authorization.

- **Data Security Measures**:
  - Authentication and authorization control access to data.
  - Encryption protects data at rest and in transit (e.g., HTTPS, SSL, TLS).
  - Monitoring and intelligence systems provide audit history and alerts for security violations.

- **Enterprise Security Policy**:
  - Essential for aligning business, IT, and stakeholders towards security goals.
  - Involves people, policy, processes, systems, and tools.

- **End-to-End Security Monitoring**:
  - Vital for proactive identification and reaction to security violations.
  - Provides complete audit history, compliance reports, and alerts for timely response.





- **Data Gathering Methods and Tools**:
  - **SQL (Structured Query Language)**:
    - Used for querying relational databases.
    - Offers commands for retrieving, grouping, sorting, and limiting results.

  - **Non-relational Databases**:
    - Can be queried using SQL or SQL-like tools.
    - Examples: CQL for Cassandra, GraphQL for Neo4J.

  - **Application Programming Interfaces (APIs)**:
    - Invoked from applications to access data endpoints.
    - Used for data extraction and validation.

  - **Web Scraping**:
    - Extracts specific data from web pages based on defined parameters.
    - Used for extracting text, contact information, images, videos, etc.

  - **RSS Feeds**:
    - Captures updated data from online forums and news sites.

  - **Data Streams**:
    - Aggregates constant streams of data from instruments, IoT devices, social media, etc.

  - **Data Exchange Platforms**:
    - Facilitate exchange of data between providers and consumers.
    - Examples: AWS Data Exchange, Crunchbase, Lotame.

- **Data Importing Methods**:
  - **Relational Databases**:
    - Suitable for structured data with a defined schema.
    - Stores data from OLTP systems, spreadsheets, etc.

  - **NoSQL**:
    - Stores semi-structured and unstructured data.
    - Supports JSON for web services and semi-structured data.

  - **Data Lakes**:
    - Store and manipulate large volumes of unstructured data.
    - Accommodate all data types and schema.

- **Tools and Methods for Importing Data**:
  - **ETL Tools and Data Pipelines**:
    - Provide automated functions for importing data.
    - Examples: Talend, Informatica, Python, R libraries.



- **Data Wrangling and Transformation**:
  - **Structuring**:
    - Change the form and schema of data.
    - Combine data from different formats.
    - Examples: Joins, Unions, Normalization, Denormalization.

  - **Cleaning**:
    - Fix irregularities in data.
    - Detect issues and errors.
    - Examples: Handling missing values, duplicate data, irrelevant data.
  
  - **Data Profiling and Visualization**:
    - Inspect data structure, content, and anomalies.
    - Visualize data to spot outliers.
    - Examples: Identifying blank/null values, duplicate data, outliers.

- **Common Data Cleaning Tasks**:
  - **Missing Values**:
    - Filter out or impute missing values.
  
  - **Duplicate Data**:
    - Remove repeated data points.

  - **Irrelevant Data**:
    - Exclude data not relevant to the analysis.

  - **Data Type Conversion**:
    - Ensure values are stored in appropriate data types.

  - **Standardization**:
    - Standardize strings, date formats, units of measurement.

  - **Syntax Errors**:
    - Rectify syntax errors like white spaces, typos, format inconsistencies.

  - **Outliers**:
    - Identify and handle values vastly different from other observations.

- **Summary**:
  - Data wrangling involves transforming and cleaning raw data for analysis.
  - Techniques include structuring, cleaning, and handling data anomalies.
  - Data profiling and visualization aid in identifying issues.


- **Popular Data Wrangling Software and Tools**:
  - **Excel Power Query / Spreadsheets and Add-ins**:
    - Features and formulae for identifying issues, cleaning, and transforming data.
    - Add-ins like Microsoft Power Query and Google Sheets Query function enhance data manipulation capabilities.

  - **OpenRefine**:
    - Open-source tool for importing and exporting data in various formats.
    - Cleans, transforms, and extends data with web services.

  - **Google DataPrep**:
    - Intelligent cloud data service for visually exploring, cleaning, and preparing structured and unstructured data.
    - Fully managed service with automatic detection of schemas, data types, and anomalies.

  - **Watson Studio Refinery (IBM Data Refinery)**:
    - Discovers, cleanses, and transforms data with built-in operations.
    - Flexibility to explore data from different sources and automatic enforcement of data governance policies.

  - **Trifacta Wrangler**:
    - Interactive cloud-based service for cleaning and transforming messy, real-world data.
    - Known for collaboration features allowing simultaneous work by multiple team members.

  - **Python**:
    - **Libraries and Packages**:
      - **Jupyter Notebook**: Open-source web application for data cleaning, transformation, statistical modeling, and visualization.
      - **Numpy**: Basic package for fast, versatile, and easy-to-use numerical operations on arrays and matrices.
      - **Pandas**: Designed for fast and easy data analysis operations, including merging, joining, and transformation of large data sets.
      - **Other Libraries in Python**: Dplyr, Data.table, Jsonlite for specific data wrangling tasks.

- **Considerations for Choosing Data Wrangling Tools**:
  - Supported data size and structures.
  - Cleaning and transformation capabilities.
  - Infrastructure needs.
  - Ease of use and learnability.



- **Performance Tuning for Data Pipelines**:
  - **Performance Areas**:
    - Scalability
    - Application failures
    - Scheduled job issues
    - Tool incompatibilities

  - **Performance Metrics**:
    - Latency : Time it takes for a service to fulfill a request
    - Failures : Rate at which service fails
    - Resource utilization : 
    - Traffic : No of user request received in a given period

  - **Troubleshooting Steps**:
    1. Collect information about the incident.
    2. Verify software and source code versions.
    3. Check recent deployments for changes.
    4. Analyze logs and metrics.
    5. Reproduce the issue in a test environment.

- **Database Optimization**:
  - **Performance Metrics**:
    - System outages
    - Capacity utilization 
    - Application slowdown
    - Query performance
    - Conflicting activities

  - **Best Practices**:
    - Capacity planning : Determining the optimal hardware and s/w resources required for performance
    - Database indexing : Quickly locate data without searching each row in a database
    - Database partitioning : It's a process whereby very large tables are divided into smaller, individual tables
    - Database normalization : design technique to reduce inconsistencies arising out of data redundancy and anomalies arising out of update, delete, and insert operations on databases 

- **Monitoring and Alerting Systems**:
  - **Database Monitoring Tools**:
    - Provide snapshots of database performance.

  - **Application Performance Management Tools**:
    - Measure application performance and resource utilization.

  - **Query Performance Monitoring Tools**:
    - Gather statistics about query throughput and execution performance.

  - **Job-level Runtime Monitoring**:
    - Monitor logical steps in long-running processes.

  - **Maintenance Routines**:
    - Time-based or condition-based routines to identify faults and low availability.


# Data Governance and Compliance

Data Governance is a collection of principles, practices, and processes to maintain the security, privacy, and integrity of data through its lifecycle. A data governance framework encompasses every part of an organization's data management process—including the technologies, databases, and data models.

## Types of Data Protected

- **Personal and Sensitive Data:**
  - Data that can be traced back to an individual.
  - Data used to identify an individual.
  - Information potentially harmful to individuals (e.g., race, sexual orientation, genetic information).

## Regulations

- **GDPR (General Data Protection Regulation):**
  - Protects personal data and privacy of EU citizens.
- **CCPA (California Consumer Privacy Act):**
  - Protects customer data in California.
- **Industry-Specific Regulations:**
  - HIPAA (Healthcare): Protects health information.
  - PCI DSS (Retail): Governs credit card data.
  - SOX (Finance): Governs financial information handling and reporting.

## Compliance

- **Definition:**
  - Adhering to regulations and conducting operations legally and ethically.
- **Processes:**
  - Establishing controls and checks.
  - Maintaining verifiable audit trails.
- **Consequences of Non-Compliance:**
  - Financial penalties.
  - Damage to public perception and trust.

## Data Lifecycle Considerations

- **Data Acquisition:**
    - establish What data needs to be collected and the contracts
and consent that give you a legal basis for procuring this data. The intended use of this data, published as
a privacy policy and communicated internally and with individuals whose data is being collected. The amount of data you need to meet your defined
purposes. For example, does the email address meet your
purpose, or do you also need to have the phone numbers and pin codes?  
    - Legal basis for data collection.
    - Intended use communicated internally and externally.
- **Data Processing:**
  - you will be
required to establish The details of how you are going to process
personal data. And your legal basis for the processing of
personal data, such as a contract or consent 
  - Legal basis for data processing.
- **Data Storage:**
  - you will be required
to establish Where the data will be stored, including specific
measures that will be taken to prevent internal and external security breaches
  - Security measures to prevent breaches.
- **Data Sharing:**
  - you will establish Which third-party vendors in your supply chain
may have access to the data you are collecting. as well how will you hold them contractually
accountable to the same regulations you are liable for
  - Accountability of third-party vendors.
- **Data Retention and Disposal:**
  - you will be required to establish What policies and processes you will follow
for the retention and deletion of personal data after a designated time. And how will you ensure that in the case of
data deletion, it will be removed from all locations, including third-party systems?
  - Policies for data retention and deletion.

## Tools for Compliance

- **Authentication and Access Control:**
  - are designed to verify
that you are who you say you are. Access control systems ensure that authorized
users have access to resources, both systems and data, based on their user group and role. Databases, for example, have the concept of
roles and privileges so only authorized users and applications can access specific objects,
such as tables or rows or columns, in a database
  - Layered authentication.
  - Role-based access control.
- **Encryption and Data Masking:**
  - data is converted to an
encoded format that can only be legible once it is decrypted via a secure key. Encryption of data is available both for data at rest, as it resides in the storage
systems, and data in transit, as it moves through browsers,
services, applications, and storage systems.
  - Data masking provides anonymization of data
for downstream processing and pseudonymization of data. Using Anonymization, the presentation layer
is abstracted without changing the data in the database itself. For example, replacing characters with symbols
when they are displayed on the screen.
  - Data encryption at rest and in transit.
  - Anonymization and pseudonymization.
    - Pseudonymization of data is a de-identification
process where personally identifiable information is replaced with artificial identifiers so
that a data set cannot be traced back to an individual's identity—for example, replacing
the name with a random value from the names dictionary
- **Hosting Options:**
  - Hosting options in on-premise and cloud systems
that comply with the requirements and restrictions for international data transfers. Monitoring and Alerting functionalities Security monitoring helps to proactively monitor,
track, and react to security violations across infrastructure, applications, and platforms.
  - Compliant on-premise and cloud systems.
- **Monitoring and Alerting:**
  - Proactive security monitoring.
  - Detailed audit reports.
  - Immediate breach alerts.
- **Data Erasure:**
  - Permanent data clearing to prevent retrieval.
  -  is a software-based method of
permanently clearing data from a system by overwriting. This is different from a simple deletion of
data since deleted data can still be retrieved

In summary, data governance and compliance are critical throughout the data lifecycle. Tools and technologies play a crucial role in implementing governance frameworks.

## API


- In this video we will discuss Application Program Interfaces (API) for short. Specifically, we will discuss:
  - What is an API
  - API Libraries
  - REST API, including:
    - Request and Response
    - An Example with PyCoinGecko
- An API lets two pieces of software talk to each other. For example, you have your program, you have some data, and you have other software components. You use the API to communicate with the other software components via inputs and outputs. Just like a function, you don’t have to know how the API works, but just its inputs and outputs.
- Pandas is actually a set of software components, much of which are not even written in Python. You have some data and a set of software components. We use the pandas API to process the data by communicating with the other software components.
- Let’s clean up the diagram. When you create a dictionary, and then create a pandas object with the Dataframe constructor, in API lingo, this is an “instance.” The data in the dictionary is passed along to the pandas API. You then use the dataframe to communicate with the API. When you call the method head, the dataframe communicates with the API displaying the first few rows of the dataframe. When you call the method mean, the API will calculate the mean and return the values.
- REST APIs are another popular type of API; they allow you to communicate through the internet, allowing you to take advantage of resources like storage, access more data, artificial intelligent algorithms, and much more. The RE stands for Representational, the S stands for State, the T stands for Transfer. In REST APIs, your program is called the client. The API communicates with a web service you call through the internet. There is a set of rules regarding Communication, Input or Request, and Output or Response. Here are some common terms:
  - You or your code can be thought of as a client.
  - The web service is referred to as a resource.
  - The client finds the service via an endpoint.
  - The client sends requests to the resource, and the resource (web service) sends a response to the client.
- HTTP methods are a way of transmitting data over the internet. We tell the REST APIs what to do by sending a request. The request is usually communicated via an HTTP message. The HTTP message usually contains a JSON file. This contains instructions for what operation we would like the service to perform. This operation is transmitted to the web service via the internet. The service performs the operation. In the similar manner, the web service returns a response via an HTTP message, where the information is usually returned via a JSON file. This information is transmitted back to the client.
- Cryptocurrency data is excellent to be used in an API because it is constantly updated and is vital to cryptocurrency trading. We will use the Py-Coin-Gecko Python Client/Wrapper for the Coin Gecko API, updated every minute by Coin-Gecko. We use the Wrapper/Client because it is easy to use so you can focus on the task of collecting data. We will also introduce pandas time series functions for dealing with time series data.
- Using Py-Coin-Gecko to collect data is quite simple. All we need is to install and import the library, create a client object, and finally use a function to request our data. In this function, we are getting data on bitcoin, in U.S. Dollars, for the past 30 days. In this case, our response is a JSON expressed as a python dictionary of nested lists including price, market cap, and total volumes which contain the unix timestamp and the price at that time. We are only interested in price so that is what we will select using the key price.
- To make things simple, we can convert our nested list to a DataFrame, with the columns timestamp and price. It's difficult to understand the column timestamp. We will convert it to a more readable format using the pandas Function to_datetime. Using the to_datetime function, we create readable time data, the input is the timestamp column unit of time is set to milliseconds. We append the output to the new column date.
- We would like to create a candlestick plot. To get the data for the daily candlesticks we will group by the date to find the minimum, maximum, first, and last price of each day. Finally, we will use plotly to create the candlestick chart and plot it. Now we can view the candlestick chart by opening the HTML file and clicking trust HTML in the top left of the tab. It should look something like this.



## ETL 

- Define the Extract, Transform, Load process or ETL process
- Explain the correct order of ETL functions
- Write a simple ETL program

Have you ever wondered how data was collected from multiple sources and combined to become a single source of information? This type of data collection is called Batch processing, and today we will be exploring a type of batch processing called Extract, Transform and Load.

Extract, Transform and Load or (ETL) does exactly what the name implies. It is the process of extracting large amounts of data from multiple sources and formats and transforming it into one specific format before loading it into a database or target file.

Let’s use the following block diagram to represent the ETL pipeline:


For example, let’s say you are the owner of a start-up that has built an AI to predict if someone is at Risk for diabetes using height and body weight. Some of your data is in CSV format, the other data is JSON files. You need to Extract all this data into one file so the AI can read it. Your data is in imperial but the AI uses metric units so you must transform it. The AI only reads CSV data in one big file, so you need to load the data as CSV.

Let’s implement the following ETL with Python.

### Extraction Step

- Discuss the `glob` function from the `glob` module.
  - Input: File extension
  - Output: List of files with that particular extension
- Write a function to extract CSV files of names, height, and weight.
  - Input: File name of the `.csv` file
  - Output: Dataframe
- Write a function to extract JSON files.
  - Input: Name of the `.json` file
  - Output: Dataframe

The `extract` function will extract large amounts of data from multiple sources in batches. We create an empty dataframe with the column names assigned.

#### Process to Extract the `.csv` File:

1. Find all CSV files using the `glob` function.
2. Append CSV files to the dataframe in each iteration of the loop.
3. Review the parameter `ignore_index="True"`.

This section of code appends the JSON files to the dataframe. The parameter `ignore_index` sets the index in the order each column was appended to the dataframe.

### Transformation Step

This function will convert the column height from inches to millimeters, and the column weight from pounds to kilograms.

### Loading and Logging

Now that we have collected and defined the data, it is time to load it into the target file. We save the pandas dataframe as a CSV. Before completing our task, we create a logging entry to attach a timestamp to each part of the process.

### Conclusion

Now that we have defined all of the code necessary to run the ETL process on the selected data, the last thing we need to do is call all of the functions. We first start by calling the `extract_data` function. The data received from this step will then be transferred to the second step of transforming the data. After this has completed the data is then loaded into the target file. Also, note that before and after every step the time and date for start and completion has been added.

In this video, you learned:

- How to write a simple Extract function.
- How to write a simple Transform function.
- How to write a simple Load function.
- How to write a simple Logging function.

Check out the labs for more.

