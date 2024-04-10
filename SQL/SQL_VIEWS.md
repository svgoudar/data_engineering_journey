- Views in SQL are a kind of virtual table. A view also has rows and columns like tables, but a view doesn’t store data on the disk like a table. View defines a customized query that retrieves data from one or more tables, and represents the data as if it was coming from a single source.

- ### Creating views
    ```sql
    create view movie_view as select movie.movie_name, movie_copy.release_date from movie, movie_copy where movie.movie_name = movie_copy.movie_name;
    select * from movie_view;
    show full tables where table_type = 'VIEW';
    ```
  
- ### Deleting views

    ```sql
    DROP VIEW view_name;
    ```

- ### Updating views
- Rules for updating view
  - The SELECT statement which is used to create the view should not include GROUP BY clause or ORDER BY clause.
  - The SELECT statement should not have the DISTINCT keyword. 
  - The View should have all NOT NULL values.
  - The view should not be created using nested queries or complex queries.
  - The view should be created from a single table. If the view is created using multiple tables then we will not be allowed to update the view.
  - 
  - Views is not updateable as long as it is based on more than one tables , 
      ```sql
      update movie_view set movie_name="God movie" where movie_name="The godfather"; -- sonce it is created from multiple tables we cannot update the view
    
      ```

- ### Inserting the views

- using with check option 
  - The WITH CHECK OPTION clause in SQL is a very useful clause for views. It applies to an updatable view. 

  - The WITH CHECK OPTION clause is used to prevent data modification (using INSERT or UPDATE) if the condition in the WHERE clause in the CREATE VIEW statement is not satisfied.
  
      ```sql
          create view check_option_view as select * from movie where movie_name like 'S%' with check option;
          select * from check_option_view ;
          insert into check_option_view(movie_name) values ("Fun"); -- Error Code: 1369. CHECK OPTION failed 'learn_sql.check_option_view'
          update check_option_view set movie_name='GGGG'; -- Error Code: 1369. CHECK OPTION failed 'learn_sql.check_option_view'
      ```

- ### Uses of a View
  - A good database should contain views for the given reasons:

  - **Restricting data access** – Views provide an additional level of table security by restricting access to a predetermined set of rows and columns of a table.
  - **Hiding data complexity** – A view can hide the complexity that exists in multiple joined tables.
  - **Simplify commands for the user** – Views allow the user to select information from multiple tables without requiring the users to actually know how to perform a join.
  - **Store complex queries** – Views can be used to store complex queries.
  - **Rename Columns** – Views can also be used to rename the columns without affecting the base tables provided the number of columns in view must match the number of columns specified in a select statement. Thus, renaming helps to hide the names of the columns of the base tables.
  - **Multiple view facility** – Different views can be created on the same table for different users.
  ### Key Takeaways About SQL Views
  - Views in SQL are a kind of virtual table.
  - The fields in a view can be from one or multiple tables.
  - We can create a view using the CREATE VIEW statement and delete a view using the DROP VIEW statement.
  - We can update a view using the CREATE OR REPLACE VIEW statement.
  - WITH CHECK OPTION clause is used to prevent inserting new rows that do not satisfy the view’s filtering condition.