
**An index is a schema object. It is used by the server to speed up the retrieval of rows by using a pointer. It can reduce disk I/O(input/output) by using a rapid path access method to locate data quickly.**

```sql
create index movie_index on movie(movie_name); -- Error Code: 1170. BLOB/TEXT column 'movie_name' used in key specification without a key length



create index movie_index on movie(release_date);
create index movie_index_1 on movie(release_date, release_year);


```



**When Should Indexes be Created?**

- A column contains a wide range of values.
- A column does not contain a large number of null values.
- One or more columns are frequently used together in a where clause or a join condition.

**When Should Indexes be Avoided?**
- The table is small
- The columns are not often used as a condition in the query
- The column is updated frequently

- ### Delete Index

    ```sql
    drop index movie_index;
    ```

- ### Clustered Index 
  - A clustered index is created only when both the following conditions are satisfied:
  - The data or file, that you are moving into secondary memory should be in sequential or sorted order.
  - There should be a key value, meaning it can not have repeated values.
  - In a clustered index, the index contains a pointer to block but not direct data. 

    ```sql
    insert into movie values ('The new movie', 2024,181,7.7,100,30000,'Action','New director','New cast','$100M',null,500),
 						 ('The new movie1', 2024,181,7.7,100,30000,'Action','New director 2','New cast','$101M',null,501);
    -- In this example, sl_id is a primary key, it will automatically act as a clustered index. The output of this code will produce in increasing order of sl_id. 
    ```


- ### Non Clustered Index
  - The non-Clustered Index is similar to the index of a book. The index of a book consists of a chapter name and page number, if you want to read any topic or chapter then you can directly go to that page by using the index of that book. No need to go through each and every page of a book.
  - The data is stored in one place, and the index is stored in another place. Since the data and non-clustered index is stored separately, then you can have multiple non-clustered indexes in a table. 

  - In a non-clustered index, the index contains the pointer to data. 