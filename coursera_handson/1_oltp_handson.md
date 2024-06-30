```sql


create database sales;
create table sales.sales_data (
    product_id int primary key not null,
    customer_id int,
    price int,
    quantity int, 
    timestamp datetime)

COPY sales.sales_data from 'C:\Users\TEST\Downloads\oltpdata.csv' DELIMITER ',' CSV HEADER;
truncate table sales.sales_data;
select * from sales.sales_data;
alter table sales.sales_data drop primary key;
alter table sales.sales_data add constraint pk_customer primary key (product_id);
describe sales.sales_data;

truncate table sales.sales_data;
commit
select count(*) from sales.sales_data;

show tables from sales;

create index ts on sales.sales_data(timestamp);

```
