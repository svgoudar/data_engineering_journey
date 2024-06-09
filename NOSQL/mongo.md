# MongoDB Overview



Welcome to an overview of MongoDB. After watching this video, you will be able to:
- Explain what MongoDB is
- List the different components of MongoDB
- Describe why and where to use MongoDB

## What is MongoDB?

MongoDB is a document and NoSQL database. Instead of storing data in tables of rows or columns like SQL databases, each record in a MongoDB database is a document. You store the data in a non-relational way. Documents are associative arrays like JSON objects or Python dictionaries.

### Example Document

A student document might represent a student's first name, last name, email address, and ID.

### Collections

MongoDB documents of similar type are grouped into a collection. For example:
- The Campus Management system stores all student records or documents in the `students` collection.
- All staff documents are stored in the `employees` collection.

### Database

Following our example, the Campus Management system stores all different types of data related to it in a MongoDB database called `CampusManagementDB`.

### Document Structure

In the document below, `first name`, `last name`, `email`, and `student ID` are fields or properties with values representing a student named John Doe. Each field name is unique within that document.

## Data Types

MongoDB supports a variety of data types, allowing you to use the correct data type to store your information. For example:
- Dates should be stored as `ISODate` or Unix-style epoch dates, which helps with queries like "give me all students born between 15th January to 15th February".
- Numbers can be stored as whole numbers or decimals.

### Subdocuments and Lists

Being a document database, MongoDB allows you to store subdocuments to group secondary information together. It also supports lists of values, including mixed types.

## Working with MongoDB

Working with MongoDB is easy because you can focus on the data you are writing and how you are going to read it. Traditional relational databases required you to:
1. Create the schema first.
2. Create table structures to hold your data.
3. Alter tables if you need to store an additional field.

In MongoDB, you can change as you go along.

## Data Flexibility

MongoDB allows you to bring in any structured or unstructured data. It provides high availability by keeping multiple copies of your data. You can design complex data structures easily in MongoDB without worrying about the complexity of how it is stored and linked. For example, your Campus Management application is also launched in the USA, where they use zip codes instead of postcodes.

## Scalability

MongoDB provides scalability as your data needs grow:
- **Vertically** by introducing bigger, faster, better hardware.
- **Horizontally** by partitioning your data.

This can be done whether you are running a self-managed on-premises MongoDB or using hybrid or cloud-hosted fully managed services such as:
- IBM Cloud databases for MongoDB
- MongoDB Atlas on AWS, Azure, and Google Cloud

## Summary

In this video, you have learned that:
- MongoDB is a document and NoSQL database.
- MongoDB supports various data types.
- Documents provide a flexible way of storing data.
- MongoDB documents of a similar type are grouped into collections.
- MongoDB models data as you read and write.
- MongoDB brings structured or unstructured data and provides high availability.
- MongoDB can be used for a variety of purposes due to its flexibility in storing structured or unstructured data.


# Advantages of MongoDB

Welcome to **Advantages of MongoDB**. After watching this video, you will be able to:
- Identify the key benefits of using MongoDB
- Explain why it suits your evolving data needs

## Key Benefits of MongoDB

### 1. Flexible Schema

MongoDB allows for a flexible schema, accommodating different data formats effortlessly.

#### Example
- UK addresses have no zip code.
- US addresses have no postcode.
  
In relational databases, this would lead to either many empty fields or complex, overarching fields. In MongoDB, this flexibility is inherent, allowing for easy storage of unstructured data from various sources.

### 2. Code-First Approach

MongoDB's document-based nature means you can start writing data immediately without the need for complex table definitions. This eliminates the need for third-party frameworks for read and write operations.

### 3. Evolving Schema

MongoDB supports schema evolution with minimal disruption. For example, if you run a courier company and need to store additional information for contactless delivery, you can easily add this new data to your existing documents.

### 4. Handling Unstructured Data

MongoDB excels in handling unstructured data, making it ideal for applications like stock market aggregators that collect diverse data from different sources.

### 5. Querying and Analytics

Mongo Query Language (MQL) offers robust querying capabilities. For more complex queries, MongoDB's aggregation pipelines allow for sophisticated data analysis.

#### Example
- Grouping student results by year and finding top-scoring students by semester.

### 6. High Availability

MongoDB supports high availability through redundancy. Typical setups involve three-node replica sets:
- One primary member
- Two secondary members

If the primary node fails, a secondary node takes over, ensuring no downtime. This setup also facilitates maintenance tasks like software updates or security patches without disrupting the system.

## Summary

In this video, you learned that:
- MongoDB offers a flexible schema, allowing for dynamic data changes.
- MongoDB uses a code-first approach, simplifying the development process.
- MongoDB supports evolving schemas, accommodating new data requirements easily.
- Complex data analysis is facilitated through aggregation pipelines.
- MongoDB ensures high availability through replica sets and redundancy.


# Use Cases for MongoDB

Welcome to **Use Cases for MongoDB**. After watching this video, you will be able to:
- List the most common use cases for MongoDB
- Describe the Many Sources – One View use case
- Describe the IoT use case
- Describe the E-commerce use case
- Describe the Real-time Analytics use case
- Describe the Gaming use case
- Describe the Finance use case

## Common Use Cases for MongoDB

### 1. Many Sources – One View

MongoDB allows you to bring data from different sources into a single view. Instead of each part of your data living in silos, you can ingest multiple shapes and formats of data into MongoDB. This unified view is facilitated by MongoDB's flexible schema.

### 2. IoT (Internet of Things)

MongoDB can be used with IoT devices, which generate vast amounts of data. Examples include:
- Autonomous car components
- Internet-connected light bulbs
- Weather stations sending temperature and wind speed readings every minute

MongoDB's scaling capabilities allow it to store this data globally. Using MongoDB's expressive querying capabilities, this data can be utilized in complex analysis and decision-making.

### 3. E-commerce

E-commerce products have diverse attributes. For example:
- A phone has storage, network, and color attributes.
- A book has publisher, writer, and number of pages attributes.

MongoDB supports dynamic schemas, allowing for the storage of products with varying attributes using documents, sub-documents, and lists. This optimizes data for reads and is ideal for e-commerce solutions.

### 4. Real-time Analytics

MongoDB is well-suited for real-time analytics. Most organizations aim to make better decisions based on data, but often struggle with complex ETL (Extract, Transform, Load) processes. MongoDB enables real-time analysis of semi-structured or unstructured data where it is stored, facilitating immediate response to changes.

### 5. Gaming

MongoDB supports the gaming industry, especially for multiplayer games played globally. With native scalability (sharding), MongoDB helps distribute data efficiently. Its flexible schema supports ever-changing data needs, making it ideal for dynamic gaming environments.

### 6. Finance

In the finance industry, MongoDB supports:
- High-speed transactions, performing thousands of operations per second
- Secure data handling with encryption during transfer and on disk
- Additional field-level encryption to prevent data incidents

MongoDB ensures high reliability and availability, critical for banking, trading, and financial services, ensuring no downtime and secure, fast transactions.

## Summary

In this video, you learned that MongoDB can be used in a variety of use cases:
- The scalability provided by MongoDB makes it easier to work globally.
- MongoDB enables real-time analysis of your data.
- MongoDB's flexible schema and robust security features make it suitable for diverse industries, including IoT, e-commerce, gaming, and finance.


```markdown
# CRUD Operations

Welcome to **CRUD Operations**. After watching this video, you will be able to use Mongo shell to connect to your MongoDB database and perform basic CRUD operations. 

## Mongo Shell

Mongo shell is a command line tool provided by MongoDB to interact with your databases. It is an interactive JavaScript interface used for performing data and administrative operations on MongoDB.

### Connecting to the Database

First, connect to your cluster by providing a connection string. Once connected, you can view the list of all your databases. For simplicity, we assume the shell is already connected to our MongoDB instance. To start working on the Campus Management database, run the following command:

```sh
use campus_management
```

Then, to see what collections are present in the Campus Management database, use this command:

```sh
show collections
```

It shows two collections: `staff` and `students`.

## CRUD Operations

CRUD operations are Create, Read, Update, and Delete operations.

### Create Operation

To insert a new document into the `students` collection:

```javascript
db.students.insertOne({
    firstName: "John",
    lastName: "Doe",
    email: "john.doe@example.com"
})
```

This operation returns an acknowledgment of success and shows the `insertedId`. The `_id` field is required in every MongoDB document. If not provided, MongoDB generates it automatically.

You can also insert multiple documents:

```javascript
let students_list = [
    { firstName: "Jane", lastName: "Doe", email: "jane.doe@example.com" },
    { firstName: "Jim", lastName: "Beam", email: "jim.beam@example.com" }
];

db.students.insertMany(students_list);
```

### Read Operations

To find the first document in the collection:

```javascript
db.students.findOne();
```

To find a specific student by email:

```javascript
db.students.findOne({ email: "john.doe@example.com" });
```

To retrieve all students with the last name "Doe":

```javascript
db.students.find({ lastName: "Doe" });
```

To count how many students have the last name "Doe":

```javascript
db.students.countDocuments({ lastName: "Doe" });
```

### Update Operations

#### Replace Operation

To replace a student's document:

1. Retrieve and modify the document:

    ```javascript
    let student = db.students.findOne({ lastName: "Doe" });
    student.onlineStatus = "on campus";
    student.email = "john.doe@campus.edu";
    ```

2. Replace the document:

    ```javascript
    db.students.replaceOne({ lastName: "Doe" }, student);
    ```

#### In-place Update

For small changes, use in-place updates:

```javascript
db.students.updateOne(
    { lastName: "Doe" },
    { $set: { onlineStatus: "online only", email: "john.doe@campus.edu" } }
);
```

To update multiple documents:

```javascript
db.students.updateMany(
    {},
    { $set: { onlineStatus: "online only" } }
);
```

### Delete Operations

To delete a specific document:

```javascript
db.students.deleteOne({ email: "john.doe@example.com" });
```

To delete multiple documents:

```javascript
db.students.deleteMany({ lastName: "Doe" });
```

## Summary

In this video, you learned that the Mongo shell is an interactive command line tool provided by MongoDB to interact with your databases. To use the Mongo shell:
- Connect to your cluster via a connection string.
- Use `show dbs` to list databases.
- Use `use <database_name>` to select a database.
- Use `show collections` to list collections in a database.

CRUD operations consist of:
- **Create**: `insertOne`, `insertMany`
- **Read**: `findOne`, `find`, `countDocuments`
- **Update**: `replaceOne`, `updateOne`, `updateMany`
- **Delete**: `deleteOne`, `deleteMany`

Different kinds of acknowledgments are returned based on the operation being run.
