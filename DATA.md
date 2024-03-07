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