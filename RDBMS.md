- Welcome to Review of Data Fundamentals. After watching this video, you will be able to:
  - Describe three important data structures with examples for each.
  - Identify common file formats for transferring data between systems.
  - Describe relational and non-relational databases.

- **Definition of Data:**
  - Data refers to unorganized information that undergoes processing to make it meaningful. It includes facts, observations, perceptions, numbers, characters, symbols, images, or a combination of these elements.

- **Types of Data Structures:**
  - **Structured Data:**
    - Highly organized and follows a predefined format.
    - Examples:
      - Excel spreadsheets
      - SQL databases
      - Online forms
  - **Unstructured Data:**
    - Lacks a specific format or organization.
    - Examples:
      - Text files
      - Media files (images, audio, video)
      - Web pages
      - Social media content
  - **Semi-Structured Data:**
    - Possesses some organizational properties but does not adhere to a strict tabular structure.
    - Examples:
      - JSON files
      - XML documents
      - Emails

- **Common File Formats for Data Transfer:**
  - Delimited text files (e.g., CSV, TSV)
  - Spreadsheets
  - Language files (e.g., XML, JSON)

- **Data Repositories:**
  - Actively store, manage, and organize data in a centralized manner.
  - Two major categories:
    - Relational databases
    - Non-relational databases

- **Relational Databases:**
  - Consist of structured data stored in related tables.
  - Examples: IBM DB2, Microsoft SQL Server, Oracle, MySQL
  - Used primarily for OLTP (Online Transaction Processing).

- **OLAP Systems:**
  - Focus on querying and analyzing large datasets for meaningful insights.
  - Include relational and non-relational databases, data warehouses, data lakes, and big data stores.

- **Non-Relational Databases:**
  - Offer flexibility in handling diverse and unstructured data.
  - Examples: MongoDB, Cassandra, Redis
  - MongoDB is suitable for storing semi-structured or unstructured data.

- **Conclusion:**
  - Different types and structures of data demand appropriate storage solutions.
  - Relational databases serve OLTP needs, OLAP systems enable complex analytics, and non-relational databases provide flexibility for diverse data.

### Data Models


- Welcome to Information and Data Models. After watching this video, you will be able to:
  - Describe the difference between an information model and a data model.
  - Explain the advantage of the relational model.
  - Describe the difference between an entity and an attribute.

- **Information Model vs Data Model:**
  - **Information Model:**
    - Abstract, formal representation of entities including properties, relationships, and operations.
    - Serves conceptual level, defining relationships between objects.
  - **Data Model:**
    - Concrete level, specific, includes details.
    - Blueprint of a database system.

- **Hierarchical Information Model:**
  - Organizes data using a tree structure.
  - Root is parent node, followed by child nodes.
  - First hierarchical database management system: IBM's Information Management System (1968).

- **Relational Model:**
  - Most used data model for databases.
  - Allows for data independence.
  - Data stored in tables providing logical, physical, and storage independence.

- **Entity-Relationship Data Model (ER Model):**
  - Alternative to relational model.
  - Used as a tool to design relational databases.
  - Entities are objects that exist independently in the database.
  - Entities have attributes characterizing them.
  - Entities represented as rectangles, attributes as ovals in ER Diagrams.
  - Entities become tables in the database, attributes become columns.

- **Example of ER Model:**
  - **Entity: Book**
    - Attributes: Title, edition, year written, etc.
  - **Entity: Author**
    - Attributes: Last name, first name, email, city, country, author ID.

- **Process of Entity Identification:**
  - Progress through identifying entities and their attributes.
  - Each entity becomes a table in the database.

- **In Conclusion:**
  - Information Models are abstract representations, while Data Models are more concrete and specific.
  - Relational Model offers advantages of logical, physical, and storage independence.
  - Entities represent objects independently in the database, with attributes characterizing them.


### Types of Relationships

- Welcome to Types of Relationships. After watching this video, you will be able to:
  - Describe the building blocks of a relationship.
  - Explain the symbols used in a relationship set.
  - Describe the difference between the one-to-one and many-to-many relationship.

- **Building Blocks of a Relationship:**
  - Entities
  - Relationship sets
  - Crows foot notations

- **Representation of Entities and Relationships:**
  - Entity sets: represented by rectangles
  - Relationship sets: represented by diamonds, with lines connecting associated entities
  - Crows foot notations: utilize symbols such as greater-than, less-than, and vertical lines for relationships

- **Entity-Relationship Diagram (ER Diagram):**
  - Represents entities (e.g., Book, Author) and their attributes (e.g., title, edition, author ID)
  - Attributes are connected to exactly one entity
  - Attributes omitted in relationship diagrams for clarity

- **Types of Relationships:**
  - **One-to-One Relationship:**
    - One entity associated with one and only one instance of another entity.
    - Example: One book has only one author.
    ![](snaps/onetoone.png)
  - **One-to-Many Relationship:**
    - One entity associated with one or more instances of another entity.
    - Example: One book has many authors.
    ![](snaps/onetomany.png)
  - **Many-to-Many Relationship:**
    - Many instances of an entity associated with many instances of another entity.
    - Example: Many authors write many different books.
    ![](snaps/manytomany.png)

- **Representation of Relationships:**
  - **One-to-One Relationship:**
    - Thick lines indicate each entity in the entity set is involved in exactly one relationship.
  - **One-to-Many Relationship:**
    - Represented by a less-than symbol, indicating one entity participating in more than one relationship.
  - **Many-to-Many Relationship:**
    - Represented by greater-than and less-than symbols on either side of the relationship set.

- **Conclusion:**
  - Building blocks of a relationship include entities, relationship sets, and crows foot notations.
  - One-to-one, one-to-many, and many-to-many relationships differ in the association between entities.
  - Understanding these relationships helps in modeling data effectively.


### Data Types


- Welcome to Data Types. After watching this video, you will be able to:
  - Explain what data types are.
  - Explain how data types are used in a database.
  - Identify some common data types.
  - Describe the advantages of using appropriate data types.

- **Database Table Representation:**
  - Represents a single entity with columns as attributes.
  - Each column should contain data of the same type.

- **Defining Data Types:**
  - Data type controls the type of data a column can store.
  - Different database management systems may have variations but generally support a standard set.

- **Common Data Types in RDBMS:**
  - **Character String Data Types:**
    - Fixed-length (e.g., CHAR(10)) and variable-length (e.g., VARCHAR).
  - **Numeric Data Types:**
    - Integer types (e.g., INT, SMALLINT, BIGINT) and decimal types (e.g., DECIMAL, NUMERIC).
  - **Date/Time Data Types:**
    - Dates, times, timestamps (e.g., DATE, TIME, DATETIME).
  - **Other Common Data Types:**
    - Boolean (e.g., BOOLEAN), binary string, large object (LOB), XML.

- **Advantages of Using Appropriate Data Types:**
  - Prevents incorrect data insertion.
  - Facilitates accurate sorting and selection of data.
  - Enables numeric calculations and standard function usage.

- **Custom Data Types:**
  - Relational databases allow creating custom or user-defined data types (UDTs) derived from built-in types.

- **Conclusion:**
  - Data types define the type of data stored in a column.
  - Choosing the correct data type offers several advantages.

### Relation Models

- **Welcome to Relational Model Concepts.** After watching this video, you will be able to:
  - Identify various set operations.
  - Describe the properties and aspects of relations.
  - Explain the difference between a relational schema and a relational instance.
  - Define relational terms such as degree and cardinality.

- **Sets and Relations:**
  - **Sets:**
    - Collections of unique elements without a specified order.
    - Basic operations include membership, subsets, union, intersection, and difference.
    ![](snaps/set_operations_1.png)
    ![](snaps/set_operations_2.png)
    ![](snaps/set_operations_3.png)
    
  - **Relations:**
    - Describe connections between elements of sets.
    - Common types include binary relations and ordered pairs.
    - Properties: reflexivity, symmetry, transitivity, and antisymmetry.
    ![](snaps/property_relations_1.png)
    ![](snaps/property_relarions_2.png)

- **Relational Concepts:**
 ![](snaps/relation_components.png)
  - **Relation Schema:**
    - Specifies the structure of a relation including column names and types (attributes).
    ![](snaps/relation_schema.png)
  - **Relation Instance:**
    - Represents the actual data stored in the table, consisting of rows (tuples) and columns.
    ![](snaps/relation_instance.png)
  - **Degree and Cardinality:**
    - Degree: Number of attributes or columns in a relation.
    - Cardinality: Number of tuples or rows in a relation.

- **Conclusion:**
  - Sets and relations are fundamental concepts in the relational model.
  - Understanding key set operations and relation properties is crucial.
  - Relational schema and instance delineate the structure and data of relations.
  - Degree and cardinality are essential measures in analyzing relations.



# Database Architectures

Welcome to Database Architectures. After watching this video, you will be able to:

- Describe deployment topologies for DBs
- Explain 2-Tier and 3-Tier architectures, including their layers such as database drivers, interfaces, and APIs

The deployment topology you use for your database is determined by how it will be used and accessed. For example, you can deploy a small database which requires limited user access on a local desktop. The database resides on the user's system and access is often limited to a single user. This deployment topology is sometimes known as single-tier architecture. It is useful for development and testing or when the database is embedded in a local application.


You can deploy a larger database that many users must access in a client-server architecture. In this scenario, the database resides on a remote server and users access it from client systems, often through a web page or local application. Some scenarios employ a middle-tier (or an application server layer) between the application client and the remote database server. These client/server deployments are commonly used for multi-user scenarios and typical of production environments.

Deploying a database in the Cloud is an increasingly popular option. In a Cloud deployment, the database resides in a Cloud environment and has all the advantages of a cloud-based service. You don’t have to download or install the database software, you don’t have to maintain the supporting infrastructure, and it is easy for users to access from wherever they are, whatever they are doing, so long as they have an internet connection. In Cloud deployments, client apps and users typically access the database through an application server layer or interface in the cloud. Cloud deployments are very flexible; you can use them for development, testing, and full production environments.

## 2-Tier Architecture

Let’s look more closely at the client-server topology. It is also referred to as a 2-Tier architecture. In a 2-Tier database architecture, the database server and the application run in 2 separate tiers. The application in the client tier connects to the database server through some sort of database interface such as an API or Framework, which can be dependent on the programming language the application is written in. The database interface communicates with the database server through a Database Client or API that is installed on client system. The database management system software (DBMS) on the server includes multiple layers which on a high level can be categorized as:

- Data Access layer
- Database Engine layer
- Database Storage layer

The Data Access layer server includes interfaces for different types of clients which can include data industry standard APIs such as JDBC and ODBC, Command Line Processor (CLP) interfaces as well vendor specific or proprietary interfaces. The database server also contains an Engine which compiles queries, and retrieves and processes the data and returns the result set. The database storage or persistence layer is where the data is stored, which may be on local storage on the same device, or reside physically on network storage or specialized storage appliances.

## 3-Tier Architecture

In most production environments, especially in the last 20-25 years, the database server is typically not accessed directly (except by administrators). The client applications and users typically go through a middle tier such as a web application server, a BI server, etc, and hence referred to as 3-tier architecture. In this architecture, the application presentation layer and the business logic layer reside in different tiers. The presentation layer is the interface with which end-users interact, which could be a traditional desktop application, a web browser or a mobile application. The client application communicates with an application server over the network. The application server encapsulates the application and business logic and communicates with the database server through a database API or driver.

## Summary

In this video, you learned that databases are deployed in different topologies, depending on which best suits the processing and access requirements. 

- A single-tier topology is one where the database is installed on a user’s local desktop. It is useful for small databases that only require single user access.
- In 2-tier database topologies, the database resides on a remote server and users access it from client systems.
- In 3-tier database topologies, the database resides on a remote server and users access it through an application server or a middle-tier.
- In Cloud deployments, the database resides in the cloud, and users access it through an application server layer or another interface that also resides in the cloud.


# Distributed Architecture and Clustered Databases

Welcome to Distributed Architecture and Clustered Databases. After watching this video, you will be able to:

- Describe common types of database architecture along with their benefits.
- Describe some techniques for managing data and optimizing performance.

In our exploration of database architectures, we've primarily focused on single-server configurations. However, for critical or large-scale workloads where high availability or scalability is important, relational database management systems, RDBMSs, offer distributed architectures. These distributed database architectures involve clusters of machines interconnected through a network, distributing data processing and storage tasks. The approach brings about notable benefits including enhanced scalability, fault tolerance, and overall performance improvements.

## Types of Database Architecture

Let's now discuss the types of database architecture. The common types of database architecture include:

- Shared disk architecture
- Shared nothing architecture
- Combination and specialized architectures

### Shared Disk Architecture

Shared disk architecture involves multiple database servers processing workloads in parallel. Each server establishes a connection to shared storage and communications with other servers using high-speed interconnection. The shared disk architecture also facilitates the effective distribution of workloads, ensuring scalability as the demand for processing power grows. In the event of a server failure, a mechanism is in place to reroute clients seamlessly to other servers, maintaining high availability and minimizing service disruptions.

### Shared Nothing Architecture

Shared nothing architecture utilizes either replication or partitioning techniques. The approach allows for the effective distribution of client workloads across multiple nodes, promoting parallel processing and efficient resource utilization. One of the key advantages lies in enhanced fault tolerance achieved by rerouting clients to alternative nodes in the event of a server failure.

### Combination and Specialized Architectures

Certain distributed database architectures employ a combination of shared disk, shared nothing, replication, or partitioning techniques. Additionally, they integrate specialized hardware components to achieve specific goals related to availability and scalability.

## Techniques for Managing Data and Optimizing Performance

Now that you know different types of database architectures, let's explore some techniques for managing data and optimizing performance. Some of the common techniques include:

- Database replication
- Database partitioning and sharding

### Database Replication

Database replication involves copying changes from one database server to one or more replicas. This process distributes the client workload across servers, leading to improved performance. Replicas can be established for high availability within the same location or for disaster recovery across geographically distributed locations.

### Database Partitioning and Sharding

An alternative strategy involves partitioning tables with substantial data into logical segments, each containing a subset of the overall data, e.g., sales records for different quarters. This technique, known as sharding, places these partitions on separate nodes in a cluster. Each shard possesses its compute resources, processing, memory, and storage to operate on its specific subset of data. When a client issues a query, it is processed in parallel across multiple nodes or shards, and the results from different nodes are synthesized and returned to the client. Database partitioning and sharding are particularly prevalent in handling data warehousing and business intelligence workloads that involve extensive volumes of data.

In this video, you learned that RDBMSs offer distributed architectures for critical or large-scale workloads. Shared disk allows parallel processing with mechanisms for high availability during server failures. Shared nothing employs replication or partitioning for optimized performance. Database replication involves copying changes from one database server to one or more replicas. Sharding involves placing partitions on separate nodes, facilitating increased parallel processing and improved overall performance.



# Welcome to Db2

After watching this video, you will be able to:

- Describe Db2 and its history and features
- List various Db2 products and deployment options
- Describe Db2 on Cloud and its Plans
- Explain how you can work with Db2 on Cloud
- Describe Db2 high availability options
- Describe Db2 scalability with partitioning

## History and Features

Database 2, or DB2, was first released by IBM in 1983 and was an early example of a relational database management system. This first release ran on IBM mainframe computers, but over the years different versions were developed to run on many other platforms, including OS/2, UNIX, Linux, and Windows. After some time, the product was rewritten to use the same codebase across the multiple operating systems so that you can easily port applications accessing Db2 data from one operating system to another. After many iterations of the offering across many platforms and with enhanced functionality, today Db2 is a whole suite of database management products including Db2 Database, Db2 Warehouse, Db2 on Cloud, Db2 Warehouse on Cloud, Db2 Big SQL, Db2 Event Store, and Db2 for z/OS.

## Db2 Products and Deployment Options

- **Db2 Database**: Powerful enterprise-ready RDBMS optimized for OLTP.
- **Db2 Warehouse**: On-premises data warehouse for advanced data analytics and massively parallel processing.
- **Db2 on Cloud**: Fully managed, cloud-based SQL database with performance, high availability, scalability, and resilience.
- **Db2 Warehouse on Cloud**: Fully managed, elastic, cloud-based data warehouse with features similar to on-premises Db2 Warehouse.
- **Db2 Big SQL**: SQL-on-Hadoop engine for massively parallel processing and advanced querying functionality.
- **Db2 Event Store**: Memory-optimized database for analyzing streamed data for event-driven applications.
- **Db2 for z/OS**: Enterprise data server for IBM Z.

## Db2 on Cloud Plans

- **Lite Plan**: Free and time unlimited, limited to 200 MB of data and 15 simultaneous connections.
- **Standard Plan**: Provides flexible scaling of compute capability and storage, with built-in three-node high availability clustering.
- **Enterprise Plan**: Provides a dedicated database instance with flexible scaling of compute capability and storage, with built-in three-node high availability clustering.

## Working with Db2 on Cloud

- Access databases using CLPPlus command line interface, Db2 on Cloud GUI console, or standard APIs such as ODBC, JDBC, and REST.
- Load data from Excel, CSV, and text files, or from Amazon S3 object storage.
- Programmatically load data from IBM Cloud Object Storage.

## High Availability Options

- **HADR (High Availability Disaster Recovery)**: Replicates changes made at a primary database to up to three standby servers, supporting automatic promotion and failover.

## Scalability with Partitioning

- **Database Partitioning Feature**: Transparently splits data across partitions and servers for massively parallel processing.

In this video, you learned that Db2 is a family of products that you can use to work with and manage your data in whatever way you need. You can deploy Db2 across many platforms, both on premises and in the cloud. Cloud Pak for Data includes Db2 and many IBM tools for data. Db2 on Cloud is a fully managed, cloud-based SQL database that can run on IBM Cloud or AWS. Db2 provides high availability, disaster recovery, and scalability functionality.



# Welcome to MySQL

After watching this video, you will be able to:

- Describe MySQL
- Explain how you can work with MySQL
- List some of the MySQL storage engines
- Understand MySQL high availability and scalability options

## Description of MySQL

MySQL was first developed by a Swedish company MySQL AB and named after My, the daughter of one of the co-founders of MySQL AB, Monty Widenius. The company was later acquired by Sun Microsystems, which in turn was acquired by Oracle Corporation. MySQL soared in popularity in the late 1990s and early 2000s, partly because it was a key component in the LAMP (Linux operating system, Apache web server, MySQL database, and PHP scripting language) stack which was being used to build many popular websites at the time. MySQL is available under dual license: the open source GNU GPL and a commercial license for applications and solutions that embed MySQL. Because the GNU GPL is open source, there have been various forks of MySQL, the most prominent being MariaDB which is led by some of the original developers of MySQL. MySQL is an object-relational database management system.

## Working with MySQL

- MySQL is available in various flavors and editions, including a clustered version for demanding workloads.
- You can run MySQL on many versions of UNIX, as well as Microsoft Windows and Linux.
- Client applications for MySQL can be written using most modern programming languages.
- MySQL uses standard SQL syntax, as well as its own extensions for additional functionality.

## MySQL Storage Engines

- MySQL supports multiple storage engines, including:
  - **InnoDB**: Default engine providing a balance of high performance and reliability.
  - **MyISAM**: Suitable for mainly read operations with few updates.
  - **NDB**: Supports multiple instances of MySQL servers running in a cluster for high availability and redundancy.

## MySQL High Availability and Scalability

- **Replication**: Create copies of your data on one or more replicas to improve scalability and availability.
- **Clustering Options**:
  - **InnoDB with Group Replication**: Allows one read-write primary server and multiple secondary servers, with MySQL Router for load balancing and failover.
  - **MySQL Cluster Edition**: Uses the NDB storage engine for highly available and scalable solutions with multiple MySQL server nodes and data nodes.

In this video, you learned that MySQL is an object-relational database available in various editions, supports many operating systems and languages for client application development, supports relational and JSON data, provides multiple storage engines for differing workloads, and offers high availability and scalability options.


# Welcome to PostgreSQL

After watching this video, you will be able to:

- Describe PostgreSQL
- Explain how you can work with PostgreSQL
- Describe replication functionality in PostgreSQL

## Description of PostgreSQL

PostgreSQL originates from the POSTGRES project at the University of California more than 30 years ago. POSTGRES was used for many research and production applications across a range of industries, including financial services, aviation, and medicine. In 1994, the open-source Postgres95 was released which included an SQL language interpreter. This was soon renamed PostgreSQL and is today generally pronounced as simply Postgres. You can use it as part of the LAPP (Linux, Apache, PostgreSQL, and PHP) stack for web applications and websites. And you can also use independently developed extensions for additional functionality, such as PostGIS for geographic and spatial data handling. PostgreSQL is a free open-source object-relational database management system.

## Working with PostgreSQL

- PostgreSQL is compatible with most commonly used operating systems and supports many programming languages, enabling integration with web applications.
- It supports ANSI SQL standards and offers both relational database constructs and some NoSQL functionality.
- You can use standard relational database constructs such as keys, transactions, views, functions, and stored procedures.

## Replication Functionality in PostgreSQL

- PostgreSQL supports replication for high availability.
- It supports two-node synchronous replication where changes made to Node 1 are applied to Node 2, enabling shared read loads and failover.
- It also supports multi-node asynchronous replication for scalability, where changes from a master node are distributed to read-only replicas.
- Commercial editions like EDB PostgreSQL Replication Server provide multi-master read/write replication for greater flexibility in scaling applications.
- PostgreSQL also includes technologies like partitioning and sharding to enhance scalability and work with larger datasets.

In this video, you learned that PostgreSQL is an open-source, object-relational database that supports a range of languages for client application development, supports relational, structured, and non-structured data, and supports replication and partitioning for high availability and scalability.


## Data Movement Utilities

- Data engineers and database administrators often need to move data into and out of databases for various reasons, including:
  - Initially populating the entire database with objects such as tables.
  - Creating a working copy of the database for development and testing purposes.
  - Creating a snapshot of the database for disaster recovery.
  - Creating new tables from data extracted from external sources or files.
  - Adding or appending data into existing tables.
- Tools and utilities used for data movement in relational databases can be broadly classified into three categories:
  - Backup and Restore
  - Import and Export
  - Load
- Backup and Restore:
  - Backup creates files encapsulating all database objects and data, allowing restoration of an exact copy of the original database.
  - Useful for disaster recovery, development/test environments, and periodic backups of production databases.
- Import and Export:
  - Import reads data from a file and performs INSERT statements into the target table.
  - Export selects data from a table and saves it into a file.
  - Supported through various interfaces, including command-line utilities, management APIs, and graphical/web tools.
  - Common file formats include DEL (Delimited ASCII), ASC (Non-delimited ASCII), PC/IXF, and JSON.
- Example of Export in DB2:
  - In the DB2 console, select the table to export.
  - View data and click Export to CSV, specifying the file name and location.
- Load:
  - A faster alternative to Import, writes formatted pages directly into the database.
  - May bypass database logging for higher performance.
  - Useful for large volumes of data where referential or table constraints checking is not necessary.



## Database Objects and Hierarchy

Welcome to Database Objects and Hierarchy. After watching this video, you will be able to:

- Recall the hierarchy of database objects
- Describe an instance of a database
- Define the term relational database
- Explain when to create a new database
- Define the term schema
- Compare user schemas and system schemas
- Describe a database partition
- List commonly used database objects

Relational Database Management Systems (RDBMSes) contain many objects that Database Engineers and Database Administrators must organize. Storing tables, constraints, indexes, and other database objects in a hierarchical structure allows database administrators to manage security, maintenance, and accessibility. This example hierarchy gives you an overview of how RDBMSes are structured, although slight variations may occur between products. 

- Instance:
  - A logical boundary for organizing the database and its objects.
  - Can contain multiple databases.
  ![](snaps/db_instances.png)
- Schema:
  - A logical grouping of objects within a database.
  - Prevents ambiguous references and defines object naming conventions.
  ![](snaps/schemas.png)
- Database Objects:
  - Tables, constraints, and indexes reside within a schema.
  ![](snaps/db_objects.png)
  
An instance is a logical boundary for a database or set of databases where you organize database objects and set configuration parameters. A relational database is a set of objects used to store, manage, and access data. Relationships between tables reduce redundant data and improve data integrity. 

- Schema:
  - Provides a way to logically group tables, views, triggers, functions, etc.
  - Helps distinguish between objects with the same name.
- User Schema:
  - Contains database objects like tables, views, functions.
- System Schema:
  - Contains configuration information and metadata for the database.

You can split very large tables across multiple partitions to improve performance. Database objects are items that exist within the database, such as tables, constraints, indexes, views, and aliases.
![](snaps/partitions.png)

In this video, you learned that:
- An instance is a logical boundary for organizing a database.
- A relational database stores, manages, and accesses data.
- Schemas logically group database objects.
- User schemas contain database objects, while system schemas contain configuration information.
- Large tables can be split across multiple partitions for performance.
- Database objects include tables, constraints, indexes, views, and aliases.




## Primary Keys and Foreign Keys


You can use a primary key to uniquely identify every row in a table. In some tables, the choice of primary key is easy because it is a naturally occurring unique attribute of an entity. For example, the book ID of a book or the employee ID number of a staff member. If your table doesn’t have an existing unique attribute, you can add a column to the table to serve as the primary key. Or if a combination of two attributes uniquely identifies each row, you can create a primary key across the two columns. For example, where employees have a unique identifier within their work site, you can use the combination of their site ID and employee ID. Each table can only have one primary key. 
![](snaps/foreign_keys_1.png)
![](snaps/fk_syntax.png)
![](snaps/fk_syntax_2.png)

You can create a primary key when you create the table by using the `PRIMARY KEY` clause of the `CREATE TABLE` statement. In the parenthesis for the `PRIMARY KEY` clause, state the name of the column or columns that will be the primary key. Alternatively, you can create a primary key on an existing table by using the `ADD PRIMARY KEY` clause of the `ALTER TABLE` statement. And again in the parenthesis, state the name of the column or columns that will be the primary key. 

You use primary and foreign keys to define the relationships between your tables. A foreign key is a column in a table which contains the same information as the primary key in another table. For example, the `Copy` table might list all books that the library owns. Therefore, the `book_id` of a copy of an individual book must exist in the `Book` table as a valid book. Where the library owns multiple copies of a popular book, the `book_id` of that particular book will appear multiple times in the `Copy` table. You can also specify that whenever you add a row to the `Copy` table, the `book_id` you use must already exist in the `Book` table.

Similar to primary keys, you can create a foreign key when you create the table by using the `CONSTRAINT <constraint_name> FOREIGN KEY` clause of the `CREATE TABLE` statement. In the parenthesis for the `FOREIGN KEY` clause, state the name of the column or columns that will be the foreign key and then reference the table and primary key column that the foreign key links to. You can also use the `RULE` clause to define what action to take if a row in the parent table, that is the table with the primary key, is updated or deleted. 


## Indexes



Usually, when you add data to a table it is appended to the end of the table, however, there is no guarantee of this and there is no inherent order to the data. So when you select a particular row from that table, the processor must check each row in turn until it finds the one that you want. On a large table, this can become a very slow way of locating a row. Also when you select multiple rows, unless you specify a sort order in your SELECT statement they may be returned in an unordered state. Because you often want to return the rows in a particular order or select a subset of sequential rows, you can create an index on a table to easily locate the specific row or set of rows you require. An index works by storing pointers to each row in the table so when you request a particular row, the SQL processor can use the index to quickly locate the row. This is similar to how you use the index in a book to quickly find a particular section of the book. The index is ordered by values within the unique key upon which it is based. By default, when you create a primary key on a table an index is automatically created on that key, but you can also create your own indexes on regularly searched columns. Use the CREATE INDEX statement to define the index, specifying the index name, its uniqueness, and the table and column on which to base it.

![](snaps/index.png)
Indexes provide the database user with many benefits, including:
- Improved performance of SELECT queries when searching on an indexed column. Because the index provides a quick route to locate rows matching the search term, the results are returned quicker than when it has to check every row in the table.
- Reduce need to sort data. If you regularly require rows in a specific order, using an index can eliminate the need for sorting the rows after they are located.
- Guaranteed uniqueness of rows. If you use the UNIQUE clause when you create the index, you can be sure that updates and insertions will not create duplicate entries in that column while not bearing the overhead of having to check this against each row in the table.

They do however have a few disadvantages:
- Each index that you create uses disk space, in the same way that adding indexes increases the number of pages in a book.
- Decreased performance of INSERT, UPDATE, and DELETE queries. Because the rows in an indexed table are sorted according to the index, adding or removing rows can take longer than in a non-indexed table.

You should only create an index when you will gain more from the advantages that you lose from the disadvantages. For example, on a table that rarely has rows inserted or updated, but is regularly used in SELECT queries and WHERE clauses. If you create many indexes on a table, you can actually negate the performance benefits in the same way that indexing every word in a book would result in an unhelpful index.

![](snaps/index_benefits.png)



## Normalization

When you keep records of data, such as books in a bookshop, you will inevitably have some inconsistencies and duplicate information. Such duplication can cause extra work and inconsistencies if the data is updated because you must change it in more than one place. Normalization is the process of organizing your data to reduce redundant data, often by dividing larger tables into multiple related tables. Normalization helps speed up transactions because you perform updates, additions, and deletes only once on a normalized database. It also improves data integrity because it reduces the chance of a change being made in one place but not in another.
![](snaps/normalization.png)
As you begin the normalization process, it’s important to recognize that you focus on normalizing each table until you reach the required normal form level. Normalization usually results in creating more tables, and once all the tables are normalized, you will have a normalized database.

There are several forms of normalization, and most data engineers will need to be familiar with first normal form, second normal form, and third normal form.

- First Normal Form (1NF):
  - Each row must be unique, and each cell must contain only a single value.
    ![](snaps/1_NF.png)
    ![](snaps/1_NF_1.png)
    ![](snaps/1_NF_2.png)
- Second Normal Form (2NF):
  - Specifies that you should separate groups of values that apply to multiple rows by creating new tables.
    ![](snaps/2NF_1.png)
    ![](snaps/2NF_2.png)
    ![](snaps/22_NF.png)
- Third Normal Form (3NF):
  - Eliminate any columns that do not depend on the key.
  ![](snaps/3_NF.png)
  ![](snaps/3NF_1.png)
  ![](snaps/3NF_3.png)
In transactional systems (OLTP), where data is both read and written frequently, you typically normalize the data to 3NF. OLTP systems need to efficiently process and store transactions, as well as query transactional data, and normalizing the data to 3NF helps the database to efficiently process and store individual transactions.

In analytical (OLAP) systems, where the usage is mostly read only, databases are optimized for read performance rather than write integrity, hence the data may have undergone some de-normalization to a lower normal form before being loaded into the analytical system such as a data warehouse. In data warehousing, Data Engineers are focused on performance, which can benefit from having fewer tables to process.
  ![](snaps/Norm_OLPT_OLAP.png)



Relational Model Constraints



- Entity Integrity Constraint:
  - Identifies each tuple in a relation with a primary key, ensuring uniqueness.
  - No attribute participating in the primary key can accept NULL values.
  - Prevents duplicate values in a table.
![img.png](snaps/Entity.png)
  ![img.png](snaps/entiy_1.png)
- Referential Integrity Constraint:
  - Defines relationships between tables and ensures their validity using Primary Keys and Foreign Keys.
  - Ensures that relationships between tables remain valid.
  ![img.png](snaps/Refer.png)
- Semantic Integrity Constraint:
  - Ensures the correctness of the meaning of the data.
  - Guarantees that data has meaningful interpretations.
  ![img.png](snaps/Semantic.png)
- Domain Constraint:
  - Specifies permissible values for a given attribute.
  - Ensures that attribute values adhere to defined rules or formats.
![img.png](snaps/Domain.png)
- Null Constraint:
  - Specifies that attribute values cannot be null.
  - Ensures that required attributes have values assigned to them.
  ![img.png](snaps/null.png)
- Check Constraint:
  - Enforces domain integrity by limiting accepted values for an attribute.
  - Restricts the range of values that can be assigned to an attribute.
  ![img.png](snaps/Check.png)
In this video, you learned that:
  - Entity Integrity Constraint ensures the primary key is a unique value that identifies each tuple (or row).
  - Referential integrity constraint defines relationships between tables.
  - Semantic Integrity Constraint refers to the correctness of the meaning of the data.
  - Domain Constraint specifies the permissible values for a given attribute.
  - Null Constraint specifies that attribute values cannot be null.
  - Check Constraint limits the values that are accepted by an attribute.

## Database Design

![](snaps/Database_design.png)
- Welcome to Approach to Database Design
After watching this video, you will be able to:
  - Describe the importance of good database design
  - Explain the database design process
  - Describe the purpose of an ERD tool
  
A well-designed database is crucial to the success of any data-driven project. The design of the database contributes to the integrity of data, the reduction of redundant data, application performance, and user satisfaction, which are all key markers of a successful project. As such, it is essential that you spend the time up-front designing your database to avoid costly problems at a later date.

There are three key steps in the database design process:
- Requirements analysis – where you analyse the data you are working with and the requirements for the use of that data
- Logical design – where you plan how to organise your data
- Physical design – where you plan how to implement your logical design in the database management system you will be using

During the first stage, you gather and analyze real-world business information and policies. You need to identify the base objects in the data and the relationships between these objects. For example, in a library scenario, a person borrows a book. You also need to identify the information associated with these objects that you will use to interact with them. For a book, this could be the title, description, ISBN, and authors. And for a person, it could be their name, address, and contact details. How you obtain this information can vary from project to project, but is likely to include:
- Reviewing any existing stores of this data, be that in a database, other electronic format, or even a paper-based system.
- Interviewing users to determine how the business currently uses this data.
- Interviewing users and potential users to determine how the business could make better use of this data.

If the data currently resides in a database, when reviewing the existing structure, be sure to use it as a source of information about the data rather than a starting template for your own database design. The output from your requirements analysis could be a report, a data diagram, or a presentation that you can share with stakeholders to validate your understanding of the system.

In the logical design phase, you take the requirements you identified in the analysis stage and map them to entities, attributes, and relationships. However, logical models should not specify any technical requirements, so you should not be thinking about any implementation considerations at this stage.

The objects that you identified in the previous stage become entities. Generally, entities are people, events, locations, or things, and if you find you have an object that doesn’t fit into one of these categories, you should double-check that it really is an object rather than a characteristic of another object. The characteristics of the objects will become attributes. So the book object becomes a book entity and the person object becomes a person entity. At this stage, you should also think about the attributes of your entities. You may think of a person having a name, but in database terms it is better to think of them having a first name and a last name. This makes it easier to search on and sort by either first or last name. And although the requirements analysis identified that a person has an address, when you think about storing that address, you should divide it up into its constituent parts.

When analyzing the requirements, you identified that a person borrows a book. However, a person may borrow many books and a book may be borrowed by many people, so this is a many-to-many relationship which can lead to ambiguity in a database. The easiest way to solve this is by creating two separate one-to-many relationships by introducing an associative entity in between the existing ones. In the book-to-person scenario, you can add in a loan entity. One person can have many loans and one book can be loaned many times. The loan entity will contain attributes from the book table and the person table, as well as some loan-specific ones. You could relate these entities by their matching attributes; however, none of those are guaranteed to be unique. In the Book entity, the ISBN will be unique, so you could use that as the primary key. You can then use the ISBN instead of the book title in the Loan entity to identify the borrowed book. There are no unique attributes in the person entity, so you can add an identifier attribute to that entity and use that to link the loan to the person. And you can add a loan id to the Loan entity to uniquely identify each loan.

Now that you have a view of your entities and attributes, you can consider normalization. Most OLTP systems are normalized to the third normal form for optimal transactional performance. Whereas OLAP systems are generally denormalized to enhance read performance. To adhere to the 1st normal form, you need to remove the potential of two (or more) authors' names being listed in the authors attribute for an individual book. One option is to split this into author 1 and author 2 attributes; however, there’s no guarantee of a maximum number of authors for a book and this would not adhere to 2nd normal form. So a better way is to create a separate authors entity with a many-to-one relationship to the Book entity. When you have finished normalizing your entities, you can move on to the physical design stage – how your database will actually look. At this stage, you can start to consider the impact that your choice of database management system will have on your design. For example, the data types it supports, the naming rules it implements, and the indexes and constraints it supports. When you are thinking about naming rules, you should also consider implementing your own convention so that anyone working with your data will understand your schema. So the Person entity from your logical design will become a person table in your physical design with each attribute becoming a typed column and keys being defined. You can use an ERD designer to create your entity relationship diagrams. pgAdmin includes the ERD Tool in which you can design your ERD and then generate an SQL script that will create your database and objects based on your design.

After watching this video, you will be able to:
- It is important to spend time designing your database before you start the implementation
- There are three stages of database design: requirements analysis, logical design, and physical design
- Using an ERD designer can simplify the design process

