## My SQL

- Welcome to Getting Started with MySQL
- After watching this video, you will be able to:
  - Explain the ways you can use MySQL
  - Describe some of the popular MySQL tools

MySQL is a popular open source relational database management system, or RDBMS. MariaDB is a fork of the MySQL database by some of the original developers of MySQL. It’s available to use in a range of ways to suit your needs. 

- You can download and install the free Community Edition under a GNU General Public License and you can embed this in your own applications.
- Alternatively, you can purchase, download, and install commercial editions, such as Standard, Enterprise, and Cluster versions, which include additional functionality.

MySQL is also available in the cloud. You can self-manage in virtual machine images or containers or you can use a managed service such as:
- IBM Cloud
- Amazon RDS for MySQL
- Azure Database for MySQL
- Google Cloud SQL for MySQL

And there is a range of tools that you can use to work with your databases, including:
- The mysql command line interface
- The mysqladmin command line program for administering your RDBMS, along with other mysql utilities for specific tasks
- The MySQL Workbench desktop application for Windows, Linux, and Mac OS versions of MySQL
- The popular third-party web interface, phpMyAdmin

The mysql command line interface enables you to issue commands to interact with your MySQL server and data. These commands can be typed directly at the prompt for interactive use or run from a text file that you invoke from the command prompt. This screenshot shows running the `show databases` command interactively to list the databases currently available. When running in batch mode, you can specify a file to store any output messages in for later use.

MySQL Workbench is a visual database design tool that integrates SQL development, administration, database design, creation, and maintenance into a single development environment for the MySQL database system. From the Administration page, you can view connection details and server features as well as performing administration tasks such as importing and exporting data and reviewing server logs and performance reports. The Schemas page enables you to access the objects in your database, work with your data, and it provides direct access to the Help documentation.

phpMyAdmin is a graphical user interface, or GUI, that you can use to interact with your MySQL databases. When you first connect to the server, you see the server information and the system databases. You can then create your own user databases and use the different tabs to interact with them. You can create databases and tables, load and query data, and import and export data using phpMyAdmin.

In this video, you learned that:
- You can download and install MySQL on your own desktop servers
- You can self-manage or use managed services for MySQL in the cloud
- mysql and mysqladmin are command line interfaces for database management
- MySQL Workbench is a desktop application for designing, developing and administering MySQL databases
- phpMyAdmin is a web interface for working with MySQL databases


## Import and Export 


- Welcome to Populating MySQL Databases and Tables
- After watching this video, you will be able to:
  - Describe MySQL backup and restore functionality
  - Explain how to load small and large amounts of data into MySQL
  - Describe how to export MySQL data to a CSV file

As a data engineer or database administrator, you will often need to populate databases and tables. One method of doing this is to backup an existing database containing your data and restore it to your new destination. You can use `mysqldump` to backup a database to a `.sql` file containing all of the statements needed to recreate the contents of the database. The simplest use of this is shown here. The `--u` parameter specifies the username of root, `employees` is the name of the database, and `employeesbackup.sql` is the name of the file in which to create the backup. If you want to just back up specific tables, you can list their names after the name of the database. And to restore a backed up file, you can use `mysql` in a similar fashion. This runs all of the SQL statements in the backup file to recreate the objects and restore the data in the destination database. Note that the greater than sign signifies output to the `.sql` file, or backup, and the less than sign signifies input to the database, or restore. If you’re already at the mysql command prompt, you can restore a dump file by using the `source` command with the name of the dump file. This method can also be used execute SQL scripts from file.

You can also back up databases using phpMyAdmin. Select a database in the tree view, then on the Export tab, click Go. By default, this Quick export method generates an SQL file that contains all of the script necessary to completely recreate the contents of your database. You can then use the Import tab to restore this database to this or another instance of MySQL. Select your destination database, locate the backup file and then click Go. Again, this runs all of the SQL statements in the backup file to recreate the objects and restore the data in the destination database.

Alternatively, if you only want to populate a small number of rows in an individual table instead of populating an entire database, you can use the phpMyAdmin tool to manually enter rows or run SQL INSERT statements To manually enter rows in phpMyAdmin, on the Insert tab, enter the data, and then click Go. By default, you can enter two rows at a time, but you can increase or decrease this as required. After you have entered data into a table, you can view that data on the Browse tab. Manually entering rows and running individual SQL statements is fine for small amounts of data, but if you are loading a large number of rows, you’ll find the import functionality is easier and quicker to use. You can use the `mysql load data infile` statement to import the contents of a CSV file into an existing MySQL table or you can use the `mysqlimport` utility passing the name of the database that the table resides in and the name of the CSV file. The table name is inferred from the name of the CSV file, so you must ensure that your file name matches your table name exactly. Alternatively, phpMyAdmin provides a visual interface for importing data into tables. On the Import tab, click Browse to select your file, check that the format and options have been correctly determined from the data file, and then click Go. Using this method, you can import up to 2 megabytes of data at a time. You can also use phpMyAdmin to export data from a table to CSV format. On the Export tab, change the Format to CSV, optionally specify which rows to export, and then click GO.


## Keys and Constraints

- Welcome to Using Keys and Constraints in MySQL
- After watching this video, you will be able to:
  - Create keys
  - Use constraints

Similarly to other relational databases, MySQL supports keys and constraints, including primary keys, foreign keys, unique constraints, and null constraints. You can create these constraints either when creating your table or at a later time. 

In this video, you will see how to create and use keys and constraints in phpMyAdmin web interface, a popular visual tool for interacting with MySQL.

- You can create a primary key on one column or a combination of columns. Primary key columns cannot contain nulls and the key definition enforces uniqueness on the column or combination of columns in the key. Creating a primary key automatically creates an index on the column or columns that make up the primary key. To create a primary key on a column when creating a table in phpMyAdmin, add an index of type PRIMARY and then confirm this by clicking Go. If you want to include another column in the key, just add a PRIMARY index to that column too. You’ll then find a primary key icon next to the column name and an index named PRIMARY on the table.

- Often your table will have an existing column that fits the requirements of a primary key, such as the employee ID for the employees table. However, in other scenarios, you may want to automatically generate an id number for each row as it’s added to the table. The auto increment property of a column enables this functionality and, as with keys, can be set when you create the table or at a later time. On the Create table or the Structure tab, select the A_I checkbox for your primary key row and then click Save. Now when you add data to the table, the database engine automatically generates incrementing entries for the empid column.

- You can also create foreign keys to relate data across tables. For example, you can use the empid column in the employee_details table to link to the empid column in the employee_contact_info table by creating a foreign key. To create a foreign key, on the Relation view of the Structure tab, enter the name for your key and identify the columns that define it. You can also specify what action to take when a related row is deleted or updated. And as with primary keys, the underlying index now also shows on the Structure tab.

- By default, when you create a MySQL table in phpMyAdmin the columns are defined as not null. You can change this either when you create the table or by changing the column definition. For example, to enable null values to be entered in the startdate and salary columns, select the Null checkbox. Leaving the empid, firstname, and lastname null checkboxes blank ensures that those columns require data. To ensure that the email address for each employee is unique, you can use the unique constraint. On the Structure tab, click the More link for the relevant column, and then click Unique.

