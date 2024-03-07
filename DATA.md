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

